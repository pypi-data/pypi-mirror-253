import sys

try:
    import pandas as pd
    import numpy as np
except ImportError:
    print("Error: Required libraries 'pandas' and 'numpy' not found.")
    print("Please install them by running the following commands:")
    print("pip install pandas")
    print("pip install numpy")
    sys.exit(1)


def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

def validate_input_parameters(weights, impacts, result_file):
    try:
        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')
        if len(weights) != len(impacts):
            raise ValueError("Number of weights and impacts must be the same.")
        if not all(impact in ['+', '-'] for impact in impacts):
            raise ValueError("Impacts must be either + or -.")
        return weights, impacts
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def validate_numeric_columns(data):
    try:
        numeric_cols = data.iloc[:, 1:].apply(lambda col: pd.to_numeric(col, errors='raise'))
        return numeric_cols
    except ValueError:
        print("Error: Non-numeric values found in data columns.")
        sys.exit(1)

def topsis_method(data, weights, impacts):
    normalized_data = data.iloc[:, 1:] / np.linalg.norm(data.iloc[:, 1:], axis=0)
    weighted_data = normalized_data * weights
    ideal_best = np.where(np.array(impacts) == '+', weighted_data.max(), weighted_data.min())
    ideal_worst = np.where(np.array(impacts) == '+', weighted_data.min(), weighted_data.max())
    
    positive_distances = np.linalg.norm(weighted_data - ideal_best, axis=1)
    negative_distances = np.linalg.norm(weighted_data - ideal_worst, axis=1)
    
    topsis_scores = negative_distances / (negative_distances + positive_distances)
    ranks = np.argsort(topsis_scores) + 1
    
    return topsis_scores, ranks

def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result_file = sys.argv[4]

    data = load_data(input_file)
    weights, impacts = validate_input_parameters(weights, impacts, result_file)
    numeric_cols = validate_numeric_columns(data)

    topsis_scores, ranks = topsis_method(data, weights, impacts)

    result_df = pd.concat([data, pd.Series(topsis_scores, name='Topsis Score'), pd.Series(ranks, name='Rank')], axis=1)
    result_df.to_csv(result_file, index=False)

    print(f"Results saved to {result_file}")

if __name__ == "__main__":
    main()
