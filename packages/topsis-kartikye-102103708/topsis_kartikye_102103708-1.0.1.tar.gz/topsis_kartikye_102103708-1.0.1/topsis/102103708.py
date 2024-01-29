import pandas as pd
import numpy as np
import sys

def topsis(input_file, weights_str, impacts_str, output_file):
    try:
        df = pd.read_csv(input_file)

        # check for more than three columns
        if df.shape[1] < 3:
            raise ValueError("Input file must contain three or more columns.")

        # Check if columns from 2nd to last contain numeric values only
        for col in df.columns[1:]:
            if not pd.to_numeric(df[col], errors='coerce').notna().all():
                raise ValueError("Columns from 2nd to last must contain numeric values only.")

        # Convert weights and impacts to numeric values
        weights = list(map(float, weights_str.split(',')))
        impacts = impacts_str.split(',')

        # Check if the number of weights, impacts, and columns match
        if len(weights) != len(impacts) or len(weights) != df.shape[1] - 1:
            raise ValueError("Number of weights, impacts, and columns must be the same.")

        # Check if the impacts are either + or -
        if not all(impact in ['+', '-'] for impact in impacts):
            raise ValueError("Impacts must be either + or -.")

        # Normalize the decision matrix using NumPy
        normalized_matrix = df.iloc[:, 1:].values / np.linalg.norm(df.iloc[:, 1:].values, axis=0)

        # Apply weights to the normalized matrix
        weighted_matrix = normalized_matrix * weights

        # Determine the ideal and negative-ideal solutions based on specified impacts
        ideal_best = np.where(np.array(impacts) == '+', weighted_matrix.max(axis=0), weighted_matrix.min(axis=0))
        ideal_worst = np.where(np.array(impacts) == '+', weighted_matrix.min(axis=0), weighted_matrix.max(axis=0))

        # Euclidean Distance
        distance_best = np.linalg.norm(weighted_matrix - ideal_best, axis=1)
        distance_worst = np.linalg.norm(weighted_matrix - ideal_worst, axis=1)

        topsis_score = distance_worst / (distance_best + distance_worst)

        df['TOPSIS Score'] = topsis_score
        df['Rank'] = df['TOPSIS Score'].rank(ascending=False)

        df.to_csv(output_file, index=False)

        print("TOPSIS completed successfully. Results saved to", output_file)

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError as e:
        print("Error:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py input_file.csv weights impacts output_file.csv")
        sys.exit(1)

    input_csv_file = sys.argv[1]
    weights_str = sys.argv[2]
    impacts_str = sys.argv[3].strip('"')
    output_csv_file = sys.argv[4]

    topsis(input_csv_file, weights_str, impacts_str, output_csv_file)