import sys
import math as m
import csv
from os import path
from tabulate import tabulate
import pandas as pd

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        df.dropna(inplace=True)
        df = df.iloc[0:, 1:].values
        matrix = pd.DataFrame(df)
        return matrix
    except pd.errors.EmptyDataError:
        raise ValueError("Error: Input file is empty")

def check_numeric_columns(df):
    for col in df.columns[1:]:
        if not pd.to_numeric(df[col], errors='coerce').notna().all():
            raise ValueError("Error: All columns from the 2nd column onwards must be numeric")

def check_weights_impact_lengths(weights, impact, num_columns):
    print(weights)
    print(impact)
    print(num_columns)
    if len(weights) != num_columns or len(impact) != num_columns:
        raise ValueError("Error: Number of weights and impact must be equal to the number of numeric columns")

def check_impact_values(impact):
    valid_impact_values = ['+', '-']
    for imp in impact:
        if imp not in valid_impact_values:
            raise ValueError("Error: Impact must have only + or - values")

def check_output_file_format(output_file):
    if not output_file.endswith('.csv'):
        raise ValueError("Error: Output file should end with '.csv'")

def check_minimum_columns(df):
    if len(df.columns) < 3:
        raise ValueError("Error: File must contain at least 3 columns")

def check_file_existence(file_path):
    if not path.exists(file_path):
        raise FileNotFoundError("Error: Input file missing")

def calculate_sum_of_squares(matrix):
    # CALCULATING SUM OF SQUARES
    sumSquares = []
    for col in range(0, len(matrix.columns)):
        X = matrix.iloc[0:,[col]].values
        sum = 0
        for value in X:
            sum = sum + m.pow(value, 2)
        sumSquares.append(m.sqrt(sum))
    return sumSquares

def normalize_matrix(matrix, sum_squares):
    normalized_matrix = matrix.copy()
    for j in range(len(matrix.columns)):
        for i in range(len(matrix)):
            normalized_matrix.iloc[i, j] = matrix.iloc[i, j] / sum_squares[j]
    return normalized_matrix

def multiply_by_weights(matrix, weights):
    weighted_matrix = matrix.copy()
    for k in range(len(matrix.columns)):
        for i in range(len(matrix)):
            weighted_matrix.iloc[i, k] = matrix.iloc[i, k] * weights[k]
    return weighted_matrix

def calculate_ideal_values(matrix, imp):
    # CALCULATING IDEAL BEST AND IDEAL WORST
    # imp = ['+', '+', '-', '+']
    best_vals = []
    worst_vals = []

    for col in range(0, len(matrix.columns)):
        Y = matrix.iloc[0:,[col]].values
        
        if imp[col] == "-" :
            maxValue = max(Y)
            minValue = min(Y)
            best_vals.append(minValue[0])
            worst_vals.append(maxValue[0])
        if imp[col] == "+" :
            maxValue = max(Y)
            minValue = min(Y)
            best_vals.append(maxValue[0])
            worst_vals.append(minValue[0])
    return best_vals, worst_vals

def calculate_si_values(matrix, best_vals, worst_vals):
    # CALCULATING Si+ & Si-
    SiPlus = []
    SiMinus = []

    for row in range(0, len(matrix)):
        temp = 0
        temp2 = 0
        wholeRow = matrix.iloc[row, 0:].values
        for value in range(0, len(wholeRow)):
            temp = temp + (m.pow(wholeRow[value] - best_vals[value], 2))
            temp2 = temp2 + (m.pow(wholeRow[value] - worst_vals[value], 2))
        SiPlus.append(m.sqrt(temp))
        SiMinus.append(m.sqrt(temp2))
    return SiPlus, SiMinus

def calculate_performance_score(SiPlus, SiMinus):
    return [SiMinus[row] / (SiPlus[row] + SiMinus[row]) for row in range(len(SiPlus))]

def calculate_rank(performance_scores):
    sorted_scores = sorted(performance_scores, reverse=True)
    return [sorted_scores.index(score) + 1 for score in performance_scores]

def save_and_display_result(matrix, output_file):
    matrix.to_csv(output_file, index=False)
    print(tabulate(matrix, headers=matrix.columns))

def topsis(df, weights, impact, output_file, file_path):
    print(df)
    sum_squares = calculate_sum_of_squares(df)
    normalized_matrix = normalize_matrix(df, sum_squares)
    weighted_matrix = multiply_by_weights(normalized_matrix, weights)

    best_vals, worst_vals = calculate_ideal_values(weighted_matrix, impact)
    SiPlus, SiMinus = calculate_si_values(weighted_matrix, best_vals, worst_vals)

    performance_scores = calculate_performance_score(SiPlus, SiMinus)
    ranks = calculate_rank(performance_scores)

    new_df = pd.read_csv(file_path)
    new_df['Topsis Score'] = performance_scores
    new_df['Rank'] = ranks

    save_and_display_result(new_df, output_file)

def main():
    if len(sys.argv) == 5:
        file_path = sys.argv[1].lower()
        weights = list(map(int, sys.argv[2].split(',')))
        impact = sys.argv[3].split(',')
        output_file = sys.argv[-1].lower()
        

        try:
            check_file_existence(file_path)
            df = load_dataset(file_path)
            check_minimum_columns(df)
            check_numeric_columns(df)
            num_columns = len(df.columns)
            check_weights_impact_lengths(weights, impact, num_columns)
            check_impact_values(impact)
            check_output_file_format(output_file)
        except ValueError as v:
            print(v)
            return
        except FileNotFoundError as f:
            print(f)
            return

    else:
        print("Required number of arguments are not provided!")
        print("Sample Input: python <script_name> <input_data_file_name> <wt> <imp> <result_file_name>")
        return

    topsis(df, weights, impact, output_file, file_path)

if __name__ == '__main__':
    main()
