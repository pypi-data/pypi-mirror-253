import sys
import pandas as pd
import numpy as np


def check_input():
    if len(sys.argv) != 5:
        print("Command not in correct format: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)


def load_data(input_data):
    try:
        data = pd.read_csv(input_data)
        return data
    except FileNotFoundError:
        print(
            "Error: File not found. Please provide a valid input file.")
        sys.exit(1)


def check_no_of_columns(data):
    if len(data.columns) < 3:
        print("Error: Input file must contain three or more columns.")
        sys.exit(1)


def check_numeric_values(data):
    non_numeric_columns = data.iloc[:, 1:].select_dtypes(
        exclude='number').columns
    if non_numeric_columns.any():
        print("Error: Columns from 2nd to last must contain numeric values only.")
        sys.exit(1)


def check_weights_impacts(weights, impacts, num_cols):
    weights_list = [float(x) for x in weights.split(',')]
    impacts_list = impacts.split(',')

    if len(weights_list) != num_cols - 1 or len(impacts_list) != num_cols - 1:
        print("Error: Number of weights, impacts, and columns must be the same.")
        sys.exit(1)


def check_impact_format(impacts):
    impacts_list = impacts.split(',')
    if any(impact not in ['+', '-'] for impact in impacts_list):
        print("Error: Impacts must be either +ve or -ve.")
        sys.exit(1)


def normalization(data):
    normalized_data = data.iloc[:, 1:].apply(
        lambda x: x / np.sqrt(np.sum(x**2)), axis=0)
    return normalized_data


def calculate_score(data, weights, impacts):
    normalized_data = normalization(data)
    weighted_normalized = normalized_data * \
        list(map(float, weights.split(',')))
    ideal_best = weighted_normalized.max(
    ) if impacts[0] == '+' else weighted_normalized.min()
    ideal_worst = weighted_normalized.min(
    ) if impacts[0] == '+' else weighted_normalized.max()
    performance_score = np.sqrt(np.sum((weighted_normalized - ideal_worst)**2, axis=1)) / (
        np.sqrt(np.sum((weighted_normalized - ideal_best)**2, axis=1)) +
        np.sqrt(np.sum((weighted_normalized - ideal_worst)**2, axis=1))
    )
    return performance_score


def main():
    check_input()
    input = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result = sys.argv[4]

    data = load_data(input)
    check_no_of_columns(data)
    check_numeric_values(data)
    check_weights_impacts(
        weights, impacts, len(data.columns))
    check_impact_format(impacts)

    topsis_score = calculate_score(data, weights, impacts)
    data['Topsis Score'] = topsis_score
    data['Rank'] = data['Topsis Score'].rank(ascending=False)

    data.to_csv(result, index=False)
    print("Results saved to", result)


if __name__ == "__main__":
    main()