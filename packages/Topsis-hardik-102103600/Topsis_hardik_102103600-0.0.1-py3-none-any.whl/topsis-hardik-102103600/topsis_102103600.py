import numpy as np
import pandas as pd
import sys

def topsis(data, weight, impact):
    normData = data.copy()
    
    for i, col in enumerate(data.columns[0:]):
        normData[col] = data[col] / np.linalg.norm(data[col])
    normData = normData*weight
    # print(normData)

    ideal_best = np.max(normData, axis=0)
    ideal_worst = np.min(normData, axis=0)
    for idx, x in enumerate(impact):
        if(x=='-'):
            ideal_worst.iloc[idx], ideal_best.iloc[idx] = ideal_best.iloc[idx], ideal_worst.iloc[idx]
    # print(ideal_best)
    # print(ideal_worst)

    separation_best = np.linalg.norm(normData - ideal_best, axis=1)
    separation_worst = np.linalg.norm(normData - ideal_worst, axis=1)

    score = separation_worst / (separation_best + separation_worst)
    res = pd.DataFrame()
    res['TOPSIS Score'] = score
    res['Rank'] = res['TOPSIS Score'].rank(ascending=False)

    return res

# inputFile = "topsisData.csv"
# weightString = "0.25,0.25,0.25,0.25"
# impactString = "-,+,+,+"
# resultFile = "102103620-result.csv"

if len(sys.argv) != 5:
    print("Please Use Format: python topsis_102103620.py <inputFileName> <weights> <impacts> <resultFileName>")
    sys.exit()

inputFile = sys.argv[1] 
w=sys.argv[2]
i=sys.argv[3]
resultFile=sys.argv[4]
weight=np.array([float(x) for x in w.split(',')])
impact=np.array([str(x) for x in i.split(',')])

df = pd.read_csv(inputFile)
data = df.copy()
data.drop(data.columns[0], axis=1, inplace=True)
# print(impact)
# print(df)
# print(resultFile)

result = topsis(data,weight,impact)
result['Rank'] = result['Rank'].astype(int)
output = df.copy()
output['Topsis Score'] = result['TOPSIS Score']
output['Rank'] = result['Rank']
print(output)

output.to_csv(resultFile)