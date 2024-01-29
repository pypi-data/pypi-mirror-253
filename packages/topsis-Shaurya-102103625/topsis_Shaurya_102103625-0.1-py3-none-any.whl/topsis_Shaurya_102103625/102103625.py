#102103625
#Shaurya Chichra

import pandas as pd
import numpy as np
import sys

def topsis(df, weights, impacts):
    if weights is None:
        weights = [1] * (df.shape[1] - 1)
    if impacts is None:
        impacts = [1] * (df.shape[1] - 1)
    normalized_df = df.copy()
    for i, col in enumerate(df.columns[1:]):
        normalized_df[col] = df[col] / np.linalg.norm(df[col])
    weighted_df = normalized_df * weights

    ideal_best = np.max(weighted_df, axis=0)
    ideal_worst = np.min(weighted_df, axis=0)

    for index, value in enumerate(impacts):
        if(value==-1):
            ideal_best.iloc[index], ideal_worst.iloc[index] = ideal_worst.iloc[index], ideal_best.iloc[index]

    separation_best = np.linalg.norm(weighted_df - ideal_best, axis=1)
    separation_worst = np.linalg.norm(weighted_df - ideal_worst, axis=1)

    # Calculate the TOPSIS score
    topsis_score = separation_worst / (separation_best + separation_worst)
    df['TOPSIS Score'] = topsis_score
    df['Rank'] = df['TOPSIS Score'].rank(ascending=False)

    return df

""" if len(sys.argv) != 5:
    print(sys.argv)
    print("Usage: python topsis.py inputFileName weights_and_impacts resultFileName")
else:
    file_path = input() 
    w=input()
    i=input()
    weights=np.array([int(x) for x in w.split(',')])
    impacts=np.array([1 if x=='+' else -1 for x in i.split(',')])
    df = pd.read_csv(file_path, index_col=0) """

file_path = sys.argv[1]
w=sys.argv[2]
i=sys.argv[3]
x=sys.argv[4]
# file_path = "topsisData.csv"
# w = "1,1,1,1"
# i = "-,+,+,+"
weights=np.array([int(x) for x in w.split(',')])
impacts=np.array([1 if x=='+' else -1 for x in i.split(',')])
df = pd.read_csv(file_path, index_col=0)

result_df = topsis(df,weights,impacts)
result_df['Rank'] = result_df['Rank'].astype(int)
print(result_df)
result_df.to_csv(x)