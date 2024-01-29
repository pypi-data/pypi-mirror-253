import pandas as pd
import numpy as np 
import argparse
import os



def normalize_data(df):
    squared_sums = np.zeros(df.shape[1])

    for column in df.columns:
        squared_sums[df.columns.get_loc(column)] = np.sum(df[column]**2)

    normalized_df = df.copy()

    for column in df.columns:
        col_loc = df.columns.get_loc(column)
        normalized_df[column] = df[column] / np.sqrt(squared_sums[col_loc] if squared_sums[col_loc] != 0 else 1e-10)

    return normalized_df



def multiply_weights(df, weights):
    df_array = df.values
    weights_array = np.array(weights, dtype = np.float64)
    weights_array = weights_array/sum(weights_array)

    result = df_array * weights_array
    result_df = pd.DataFrame(result, columns=df.columns, index=df.index)

    return result_df

def SplusSminus(df, impacts):
    num_columns = df.shape[1]
    Splus = np.zeros(num_columns)
    Sminus = np.zeros(num_columns)

    for i in range(num_columns):
        column_values = df.iloc[:, i]
        if impacts[i] == '+':
            Splus[i] = max(column_values)
            Sminus[i] = min(column_values)
        elif impacts[i] == '-':
            Splus[i] = min(column_values)
            Sminus[i] = max(column_values)

    return Splus, Sminus
    
def PerformanceScore(df, Splus, Sminus):
    EDPlus = ((df-Splus)**2).sum(axis = 1).apply(np.sqrt)
    EDMinus = ((df-Sminus)**2).sum(axis = 1).apply(np.sqrt)
    

    df['Topsis Score'] = EDPlus / (EDPlus + EDMinus)
    df['Rank'] = df['Topsis Score'].rank(ascending=False)

    return df

def validate(values):
    for value in values:
        if ' ' in value:
            return False
    return True
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'InputDataFile',
        type=str,
        help='Path to the input data file'
    )
    parser.add_argument(
        'Weights',
        type=str,
        help='Comma-separated list of weights'
    )
    parser.add_argument(
        'Impacts', 
        type=str,
        help='Comma-separated list of impacts (+ or -)'
    )
    parser.add_argument(
        'ResultFileName',
        type=str,
        help='Output result file name'
    )
    args = parser.parse_args()
    
    if len(vars(args))!=4:
        parser.error(f'Incorrect number of parameters - 4 needed, provided: {len(vars(args))}')
    

    weights = args.Weights.split(',')
    impacts = args.Impacts.split(',')

    assert(validate(weights) == True and validate(impacts) == True), "Weights and Impacts should be present in comma separated format"

    try:
        df = pd.read_csv(args.InputDataFile)
    except FileNotFoundError:
        print(f'Error: File {args.InputDataFile} not found')
        exit()
    except Exception as e:
        print(f'An unexpected error occured: {e}')
        exit()
    
    if(df.shape[1]<3):
        print('Invalid data for TOSIS')
        exit()
    
    assert (len(weights)==len(impacts) and (len(impacts)==df.shape[1]-1)), "Length of impacts, weights and columns must be equal"
    
    allowed_signs = ['+', '-']
    flag = all(value in allowed_signs for value in impacts)

    assert(flag == True), "Impacts can only be negative or positive"

    df_products = df.iloc[:, 0]
    df = df.drop(columns = df.columns[0])
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    df = normalize_data(df)
    df = multiply_weights(df, weights)
    Splus, Sminus = SplusSminus(df, impacts)

    df = PerformanceScore(df, Splus, Sminus)

    output_path = os.path.join(output_dir, args.ResultFileName)
    df = pd.concat([df_products, df], axis = 1)
    df.to_csv(output_path, index=False)

    print(f'Results saved to: {output_path}')
