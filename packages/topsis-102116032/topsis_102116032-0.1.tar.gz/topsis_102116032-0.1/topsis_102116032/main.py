import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def topsis(input_file, weights, impact):

    if len(sys.argv) != 3:
        print("Error: Number of arguments are not equal to 3")
        return
    
    if input_file[-4:] != '.csv':
        print("Error: Input file is not a csv file")
        return
    
    w = list(map(int, weights.split(',')))
    im = list(impact.split(','))
    
    if len(w) != len(im):
        print("Error: Number of weights and impacts are not equal")
        return
    
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Error: File not found")
        return
    
    le = LabelEncoder()
    for col in data.columns[1:]:
        if data[col].dtype == 'object':
            data[col] = le.fit_transform(data[col])
    
    data = data.values[:, 1:].astype(float)
    n, m = data.shape

    # Check if number of columns are greater than 3
    if m < 3:
        print("Error: Number of columns are less than 3")
        return
    
    if len(w) != m:
        print("Error: Number of weights and columns are not equal")
        return
    
    root = np.sqrt(np.sum(data ** 2, axis=0))
    data = data / root
    
    data *= w
    
    ideal_best = np.zeros(m)
    ideal_worst = np.zeros(m)
    for i in range(m):
        if im[i] == '+':
            ideal_best[i] = max(data[:, i])
            ideal_worst[i] = min(data[:, i])
        elif im[i] == '-':
            ideal_best[i] = min(data[:, i])
            ideal_worst[i] = max(data[:, i])
        else:
            print("Error: Impact should be either + or -")
            return
    
    euclidean_pos = np.sqrt(np.sum((data - ideal_best) ** 2, axis=1))
    euclidean_neg = np.sqrt(np.sum((data - ideal_worst) ** 2, axis=1))


    performance_score = (euclidean_neg / (euclidean_neg + euclidean_pos)) * 100
    
    result_df = pd.read_csv(input_file)
    result_df['Topsis Score'] = performance_score
    result_df['Rank'] = result_df['Topsis Score'].rank(ascending=False)
    result_df = result_df.sort_values(by=["Rank"])
    
    return result_df
