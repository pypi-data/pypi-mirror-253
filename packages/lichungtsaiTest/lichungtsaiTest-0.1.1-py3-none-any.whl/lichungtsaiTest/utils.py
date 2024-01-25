import pandas as pd

def find_all_empty_columns(df):
    """
    Identifies and returns a list of column names in the DataFrame where all values are NaN.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame to analyze.

    Returns:
    list: A list of column names that are 100% NaN.
    """
    # Using isna() to find NaNs and all() to check if all values in the column are NaN
    empty_columns = df.columns[df.isna().all()].tolist()
    return empty_columns


def find_all_constant_columns(df):
    """
    Identifies and returns a list of column names in the DataFrame where all values are constant.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame to analyze.

    Returns:
    list: A list of column names with constant values.
    """
    # Using nunique() to count unique values in each column
    constant_columns = [column for column in df.columns if df[column].nunique() == 1]
    return constant_columns

import pandas as pd


def find_perfect_correlation_columns(df):
    """
    Identifies pairs of columns in the DataFrame with a correlation coefficient of exactly 1 or -1.

    Parameters:
    df (pandas.DataFrame): The DataFrame to analyze.

    Returns:
    list: A list of tuples, each tuple containing a pair of column names with perfect correlation.
    """
    corr_matrix = df.corr()
    perfect_corr_pairs = []
    
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) == 1:
                perfect_corr_pairs.append((corr_matrix.columns[i], corr_matrix.columns[j]))

    return perfect_corr_pairs