import sys
import pandas as pd
import numpy as np


# HANDLING EXCEPTIONS
def check_input_parameters():
    if len(sys.argv) != 5:
        print("Write the command in correct format: \npython <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)


def read_data(input_data):
    try:
        data = pd.read_csv(input_data)
        return data
    except FileNotFoundError:
        print(
            f"Error: File {input_data} not found. \nPlease provide a valid input file.")
        sys.exit(1)


def check_data_columns(data):
    if len(data.columns) < 3:
        print("Error: Input file must contain three or more columns.")
        sys.exit(1)


def check_numeric_values(data):
    non_numeric_columns = data.iloc[:, 1:].select_dtypes(
        exclude='number').columns
    if non_numeric_columns.any():
        print("Error: Columns from 2nd to last must contain numeric values only.")
        sys.exit(1)


def check_weights_impacts_separator(weights, impacts, num_cols):
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

# TOPSIS PROGRAM


def vector_normalization(data):
    normalized_data = data.iloc[:, 1:].apply(
        lambda x: x / np.sqrt(np.sum(x**2)), axis=0)
    return normalized_data


def calculate_performance_score(data, weights, impacts):
    normalized_data = vector_normalization(data)
    weighted_normalized_matrix = normalized_data * \
        list(map(float, weights.split(',')))
    ideal_best = weighted_normalized_matrix.max(
    ) if impacts[0] == '+' else weighted_normalized_matrix.min()
    ideal_worst = weighted_normalized_matrix.min(
    ) if impacts[0] == '+' else weighted_normalized_matrix.max()
    performance_score = np.sqrt(np.sum((weighted_normalized_matrix - ideal_worst)**2, axis=1)) / (
        np.sqrt(np.sum((weighted_normalized_matrix - ideal_best)**2, axis=1)) +
        np.sqrt(np.sum((weighted_normalized_matrix - ideal_worst)**2, axis=1))
    )
    return performance_score


def main():
    check_input_parameters()
    input_data = sys.argv[1]
    data_weights = sys.argv[2]
    data_impacts = sys.argv[3]
    result = sys.argv[4]

    Df = read_data(input_data)
    check_data_columns(Df)
    check_numeric_values(Df)
    check_weights_impacts_separator(
        data_weights, data_impacts, len(Df.columns))
    check_impact_format(data_impacts)

    topsis_score = calculate_performance_score(Df, data_weights, data_impacts)
    Df['Topsis Score'] = topsis_score
    Df['Rank'] = Df['Topsis Score'].rank(ascending=False)

    Df.to_csv(result, index=False)
    print("Jasmeet's Topsis Implementation")
    print("Roll Number: 102116124")
    print("Results saved to", result)


if __name__ == "__main__":
    main()
