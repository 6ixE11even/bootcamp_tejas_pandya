from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd
import numpy as np

def numeric_cols(df):
    numeric_columns = df.select_dtypes(include='number').columns
    print("\nNumeric columns:", list(numeric_columns))
    return numeric_columns

def fill_missing_median(df, columns=None):
    df_copy = df.copy()
    if columns is None:
        columns = df.select_dtypes(include=np.number).columns
    for col in columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].median())
    return df_copy

def drop_missing(df, columns=None, threshold=None):
    df_copy = df.copy()
    if columns is not None:
        return df_copy.dropna(subset=columns)
    if threshold is not None:
        return df_copy.dropna(thresh=int(threshold*df_copy.shape[1]))
    return df_copy.dropna()

def normalize_data(df,columns='age', method='minmax'):
    df_copy = df.copy()
    if method=='minmax':
        scaler = MinMaxScaler()
    else:
        scaler = StandardScaler()
    df_copy['scaled'] = scaler.fit_transform(df_copy[['age']])
    return df_copy