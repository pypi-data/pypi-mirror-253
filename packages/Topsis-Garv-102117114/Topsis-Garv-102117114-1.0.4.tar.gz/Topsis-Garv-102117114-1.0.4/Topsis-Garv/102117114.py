import sys
import pandas as pd
import numpy as np
import logging


def preprocess_input(input_file):
    try:
        data = pd.read_csv(input_file)
        roll_number = input_file.split('-')[0]
        output_file = f"{roll_number}-data.csv"
        data.to_csv(output_file, index=False)
        return output_file
    except FileNotFoundError:
        logging.warning('Error: File not found - {input_file}')
        # print(f"Error: File not found - {input_file}")
        sys.exit(1)

def validate_input(weights, impacts, data):
    try:
        # weights = list(map(float, weights.split(',')))
        # impacts = impacts.split(',')
        if len(weights) != len(data.columns) - 1 or len(impacts) != len(data.columns) - 1:
            raise ValueError("Number of weights or impacts does not match the number of columns.")
        if not all(isinstance(w, (int, float)) for w in weights):
            raise ValueError("Weights must be numeric.")
        if not all(impact in ['+', '-'] for impact in impacts):
            raise ValueError("Impacts must be either '+' or '-'.")
    except ValueError as e:
        logging.warning('Error: {e}')
        # print(f"Error: {e}")
        sys.exit(1)

def topsis(input_file, weights, impacts, result_file):
    data = pd.read_csv(input_file)
    impacts = impacts.replace(",", "")
    weights  = weights.replace(",","")
    weights = [int(element) for element in weights]
    impacts=list(impacts)
    
    validate_input(weights, impacts, data)
    for i in range(1, len(data.columns)):
        data.iloc[:, i] = data.iloc[:, i]*(-1 if impacts[i-1]=='-' else 1)
        
    norm_data = data.iloc[:, 1:].apply(lambda x: x / np.linalg.norm(x), axis=0)

    weighted_data = norm_data * weights

    ideal_best = weighted_data.max()
    ideal_worst = weighted_data.min()

    dist_best = np.linalg.norm(weighted_data - ideal_best, axis=1)
    dist_worst = np.linalg.norm(weighted_data - ideal_worst, axis=1)

    topsis_score = dist_worst / (dist_best + dist_worst)

    rank = np.argsort(topsis_score)[::-1] + 1

    data['Topsis Score'] = topsis_score
    data['Rank'] = rank

    data.to_csv(result_file, index=False)

def main():
    if len(sys.argv) != 5:
        logging.warning("Usage: python topsis.py <inputFile> <weights> <impacts> <resultFile>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result_file = sys.argv[4]
    
    input_file = preprocess_input(input_file)
    topsis(input_file, weights, impacts, result_file)

if __name__=="__main__":
    main()