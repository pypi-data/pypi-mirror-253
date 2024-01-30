import sys
import pandas as pd
import numpy as np

def check_inputs(argv):
    # Check correct number of parameters
    if len(argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

def load_data(input_file):
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: File not found - {input_file}")
        sys.exit(1)

    # Check if the input file contains three or more columns
    if data.shape[1] < 3:
        print("Error: Input file must contain three or more columns.")
        sys.exit(1)

    # Check if the columns from 2nd to last contain numeric values only
    if not data.iloc[:, 1:].applymap(np.isreal).all().all():
        print("Error: Columns from 2nd to last must contain numeric values only.")
        sys.exit(1)

    return data

def check_weights_impacts(weights, impacts, num_columns):
    # Check if the number of weights, impacts, and columns match
    num_weights = len(weights.split(","))
    num_impacts = len(impacts.split(","))

    if num_weights != num_impacts or num_weights != num_columns - 1:
        print("Error: Number of weights, impacts, and columns must match.")
        sys.exit(1)

    # Check if impacts are either +ve or -ve
    if any(impact not in ['+', '-'] for impact in impacts.split(",")):
        print("Error: Impacts must be either +ve or -ve.")
        sys.exit(1)

def topsis(input_file, weights, impacts, result_file):
    data = load_data(input_file)

    # Extracting weights and impacts
    weights = np.array(list(map(float, weights.split(","))))
    impacts = np.array(list(map(lambda x: 1 if x == '+' else -1, impacts.split(","))))

    # Normalize the data
    normalized_data = data.iloc[:, 1:].apply(lambda x: x / np.linalg.norm(x))

    # Weighted normalized decision matrix
    weighted_normalized_data = normalized_data * weights

    # Ideal and Negative-Ideal solutions
    ideal_best = weighted_normalized_data.max()
    ideal_worst = weighted_normalized_data.min()

    # Calculate separation measures
    separation_positive = np.linalg.norm(weighted_normalized_data - ideal_best, axis=1)
    separation_negative = np.linalg.norm(weighted_normalized_data - ideal_worst, axis=1)

    # Topsis Score
    topsis_score = separation_negative / (separation_negative + separation_positive)

    # Rank the alternatives
    rank = np.argsort(topsis_score)[::-1] + 1

    # Add Topsis Score and Rank columns to the result
    result = pd.concat([data, pd.DataFrame({'Topsis Score': topsis_score, 'Rank': rank})], axis=1)

    # Save the result to the specified output file
    result.to_csv(result_file, index=False)
    print(f"Result saved to {result_file}")

if __name__ == "__main__":
    try:
        check_inputs(sys.argv)
        input_file, weights, impacts, result_file = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

        # Check and validate inputs
        data = load_data(input_file)
        num_columns = data.shape[1]

        check_weights_impacts(weights, impacts, num_columns)

        # Run Topsis algorithm and save the result
        topsis(input_file, weights, impacts, result_file)
    except Exception as e:
        print(f"Error: {e}")
