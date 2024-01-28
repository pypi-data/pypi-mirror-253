import pandas as pd
import numpy as np
import os
import sys
def load_data(input_file):
    try:
        read_file = pd.read_excel(input_file)
        #read_file.to_csv("102103715-data.csv", index=None, header=True)
        #data = pd.DataFrame(pd.read_csv("102103715-data.csv"))
        return read_file
    except FileNotFoundError:
        print("Error: File not found. Please provide a valid input file.")
        sys.exit(1)

def read_weights(weights_str):
    try:
        weights = np.array([float(w) for w in weights_str.split(',')])
        return weights
    except Exception as e:
        print(f"Error parsing weights: {e}")
        sys.exit(1)

def read_impacts(impacts_str):
    try:
        impacts = np.array(list(impacts_str))
        # if not all(impact in ['+', '-'] for impact in impacts):
        #     print("Error: Impacts must be either +ve or -ve.")
        #     sys.exit(1)
        return impacts
    except Exception as e:
        print(f"Error parsing impacts: {e}")
        sys.exit(1)

def normalize_data(data):
    normalized_data = data.iloc[:, 1:].apply(lambda x: x / np.sqrt(np.sum(x**2)), axis=0)
    return normalized_data

def calculate_topsis_score(data, weights, impacts):
    normalized_data = normalize_data(data)
    weighted_normalized_data = normalized_data * weights
    ideal_best = weighted_normalized_data.max() if impacts[0] == '+' else weighted_normalized_data.min()
    ideal_worst = weighted_normalized_data.min() if impacts[0] == '+' else weighted_normalized_data.max()
    topsis_score = np.sqrt(np.sum((weighted_normalized_data - ideal_best)**2, axis=1)) / (
            np.sqrt(np.sum((weighted_normalized_data - ideal_best)**2, axis=1)) +
            np.sqrt(np.sum((weighted_normalized_data - ideal_worst)**2, axis=1))
    )
    return topsis_score


def main():
    if len(sys.argv) != 5:
        print("Usage: python Topsis.py <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_data_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result_file = sys.argv[4]

    dataset = load_data(input_data_file)
    if len(dataset.columns) < 3:
        print("Error: Input file must contain three or more columns.")
        sys.exit(1)
    non_numeric_columns = dataset.iloc[:, 1:].apply(lambda col: col.apply(lambda x: not np.isreal(x))).any()
    if non_numeric_columns.any():
        print("Error: Columns from 2nd to last must contain numeric values only.")
        sys.exit(1)
    weights = read_weights(weights)
    impacts_list = impacts.split(',')
    if not all(impact in ['+', '-'] for impact in impacts_list):
        print("Error: Impacts must be either +ve or -ve.")
        sys.exit(1)
    impacts = read_impacts(impacts)

    topsis_score = calculate_topsis_score(dataset, weights, impacts)
    dataset['Topsis Score'] = topsis_score
    dataset['Rank'] = dataset['Topsis Score'].rank(ascending=False)
    dataset.to_csv(result_file, index=False)

if __name__ == "__main__":
    main()



