#
#
#

# Import statements (standard)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import grangercausalitytests as gct

# Import statements (custom)
import helper_functions as hf

def granger_causality(df, a_idx, b_idx, max_lags=48):
    """
    Test for Granger causality between series identified by a_idx and b_idx.
    (b_idx "causes" a_idx -> Series B causes Series A in output generated).

    Inputs:
        df: input data frame (rows: observations, columns: variables)
            - For n observations, this will be an n x 2 matrix.
        a_idx: series "A" identifier (integer index)
        b_idx: series "B" identifier (integer index)
        max_lags: number of maximum lags to include in test; test is performed
                  with all lags up to/including max_lags

    Returns:
        results: dictionary containing results from test

    """
    a_str = df.columns[a_idx]
    b_str = df.columns[b_idx]
    ab_series = df[[a_str, b_str]].values
    results = gct(ab_series, maxlag=max_lags)

    return results
"""
df = pd.read_csv('~/Desktop/Springboard/Cryptocurrency/cleaned_crypto_closing_prices.csv',
                 index_col='time')

diff_df = hf.difference_prices(df)

#test = granger_causality(diff_df, 1, 2)

n_cols = 2
for i in range(n_cols):
    for j in range(n_cols):
        if i == j:
            continue
        else:
            print('Series A: ', diff_df.columns[i])
            print('Series B: ', diff_df.columns[j])
            gc_results = granger_causality(diff_df, i, j)
            print('\n')
"""
