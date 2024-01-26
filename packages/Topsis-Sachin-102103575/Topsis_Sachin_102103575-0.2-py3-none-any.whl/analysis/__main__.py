import pandas as pd
import numpy as np
import sys

def read_input_file(inputcsv):
    try:
        data=pd.read_csv(inputcsv)
        return data
    except FileNotFoundError:
        print(f"file '{inputcsv}' not found")
        sys.exit()

def validate_input(data, weights, userimpacts):
    if len(data.columns)<3:
        print("Input file must have more than two columns")
        sys.exit()

    for col in data.columns[1:]:
        if not pd.to_numeric(data[col], errors='coerce').notnull().all():
            print(f"Non-numeric values found in column '{col}'")
            sys.exit()

    num_weights=len(weights.split(','))
    num_impacts=len(userimpacts.split(','))

    if num_weights!= len(data.columns)-1 or num_impacts!= len(data.columns)-1:
        print("Number of weights, impacts, and columns must be the same")
        sys.exit()

    impacts=[]
    for i, char in enumerate(userimpacts):
        if char == ',':
            continue
        elif char != '+' and char != '-':
            print("Impacts must be either '+' or '-'")
        else:

            impacts.append(i // 2) 


    
    return impacts

def topsis(data, weights, impacts, userimpacts):
    mtx1 = data.iloc[:, 1:].apply(lambda x: x / np.sqrt((x**2).sum()), axis=0)
    mtx2 = mtx1 * np.array(list(map(float, weights.split(','))))

    impact_counter = 0
    for i in impacts:
        
        impact = userimpacts[impact_counter]
        if impact == '-':
            mtx2.iloc[:, i] = 1 / mtx2.iloc[:, i]
        impact_counter += 2  
    
    ibest = mtx2.max()
    iworst = mtx2.min()
    bestdist = np.sqrt(((mtx2 - ibest)**2).sum(axis=1))
    worstdist = np.sqrt(((mtx2 - iworst)**2).sum(axis=1))
    score = worstdist / (worstdist + bestdist)
    
    rank = np.argsort(score, kind='mergesort')+1
    data['Topsis Score']=score

    data['Rank']=rank

    return data



def main():
    if len(sys.argv)!= 5:
        print("Usages: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit()

    inputcsv = sys.argv[1]
    weights = sys.argv[2]
    userimpacts = sys.argv[3]
    finalcsv = sys.argv[4]

    data=read_input_file(inputcsv)
    impacts=validate_input(data, weights, userimpacts)


    finaldata = topsis(data, weights, impacts, userimpacts)
    finaldata.to_csv(finalcsv, index=False)
    print(f"TOPSIS analysis completed. Results saved to {finalcsv}")

if __name__ == "__main__":
    main()
