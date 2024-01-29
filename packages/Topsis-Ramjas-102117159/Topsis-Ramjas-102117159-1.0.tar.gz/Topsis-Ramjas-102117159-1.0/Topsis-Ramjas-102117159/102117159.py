import sys
import pandas as pd

def get_input(ipfile, weights, impacts, opfile):
    
    try:
        data = pd.read_excel(ipfile, engine='openpyxl')
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)


    data.to_csv(opfile, index=False)

    
    if len(data.columns) < 3:
        print("Error: Input file must contain three or more columns.")
        sys.exit(1)

 
    if (len(weights)!=(len(data.columns)-1)) or (len(impacts)!=(len(data.columns)-1)):
        print("Error: Number of weights, impacts & columns must be same.")
        sys.exit(1)

 
    for i in impacts:
        if i not in ['+', '-']:
            print("Error: Impacts must either be '+' or '-'.")
            sys.exit(1)

    return opfile

def normalise(data,ncol,weights):
    for i in range(1, ncol):
        temp = 0
        for j in range(len(data)):
            temp = temp + data.iloc[j, i]**2
        temp = temp**0.5
        for j in range(len(data)):
            data.iat[j, i] = (data.iloc[j, i] / temp)*weights[i-1]

def topsis(ipfile, weights, impacts, opfile):

    ipfile = get_input(ipfile, weights, impacts, opfile)
    data = pd.read_csv(ipfile)
    
    if not data.iloc[:,1:].apply(pd.to_numeric,errors='coerce').notnull().all().all():
        print("Error: 2nd to last columns must contain numeric values only.")
        sys.exit(1)


    normalise(data,len(weights),weights)
    

    s_plus = (data.max().values)[1:]
    s_minus = (data.min().values)[1:]
    for i in range(1, len(weights)):
        if impacts[i-1] == '-':
            s_plus[i-1], s_minus[i-1] = s_minus[i-1], s_plus[i-1]

    score = []
    pos_dist = [] 
    neg_dist = [] 
 
    for i in range(len(data)):
        temp_p, temp_n = 0, 0
        for j in range(1, len(weights)):
            temp_p = temp_p + (s_plus[j-1] - data.iloc[i, j])**2
            temp_n = temp_n + (s_minus[j-1] - data.iloc[i, j])**2
        temp_p, temp_n = temp_p*0.5, temp_n*0.5
        score.append(temp_n/(temp_p + temp_n))
        neg_dist.append(temp_n)
        pos_dist.append(temp_p)
    

    data['Topsis Score'] = score
 

    data['Rank'] = (data['Topsis Score'].rank(method='max', ascending=False))
    data = data.astype({"Rank": int})
  

    data.to_csv(opfile, index=False)

    print("Result saved in file ", opfile)

if name == "main":
    if len(sys.argv) != 5:
        print("Please Check format: python topsis.py <inputFile> <Weights> <Impacts> <resultFile>")
        sys.exit(1)

    ipfile = sys.argv[1]
    weights = [float(w) for w in sys.argv[2].split(',')]
    impacts = sys.argv[3].split(',')
    opfile = sys.argv[4]
    if ',' not in sys.argv[2]:
        print("Error: Weights must be separated by ',' (comma).")
        sys.exit(1)      

    topsis(ipfile, weights, impacts, opfile)