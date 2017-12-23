#
#
#

# Import statements (standard)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from statsmodels.tsa.stattools import kpss
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf, pacf
from sklearn.preprocessing import StandardScaler

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def adf_stationarity_test(df, al=None, nl=1):
    """
    Performs augmented Dickey-Fuller test for stationarity. The null
    hypothesis is that the time series possesses a unit root (non-
    stationary), while the alternative hypothesis is there is no unit
    root (stationary). This function is written to be called one cryptocurrency
    at a time.

    Inputs:
        df: cryptocurrency prices (rows: times, column: prices)
        al: autolag (parameter for adfuller -> options: 'AIC', 'BIC', 't-stat')
        nl: number of lags (input manually)

    Returns:
        output: results from ADF test
    """
    if al is None:
        results = adfuller(df, maxlag=nl)
    else:
        results = adfuller(df, autolag=al)

    formatted_results = pd.Series({'Test Statistic': results[0], 'p-value':
                                   results[1], 'Number of Lags': results[2],
                                   'Number of Data Points': results[3]})

    return formatted_results

def difference_prices(df, order=1):
    """
    Difference cryptocurrency closing prices.

    Inputs:
        df: cryptocurrency prices (rows: times, columns: cryptocurrencies)
        order: order of differencing (default: 1)

    Returns:
        diff_df: differenced cryptocurrency prices (same as above)
    """
    diff_df = df.diff(periods=order)
    diff_df = diff_df.dropna()

    return diff_df

def normalize_prices(df):
    """
    Normalize cryptocurrency closing prices.

    Inputs:
        df: cryptocurrency prices (rows: times, columns: cryptocurrencies)

    Returns:
        std_df: standardized cryptocurrency prices (same as above)
    """
    scl = StandardScaler()

    std_vals = scl.fit_transform(df)
    std_df = pd.DataFrame(std_vals)
    std_df.set_index(df.index, inplace=True)
    std_df.columns = df.columns

    return std_df
"""
df = pd.read_csv('~/Desktop/Springboard/Cryptocurrency/cleaned_crypto_closing_prices.csv',
                 index_col='time')

#std_df = standardize_prices(df)
diff_df = difference_prices(df)


for i in range(len(diff_df.columns)):
    crypto_str = diff_df.columns[i]
    crypto_df = diff_df[crypto_str]
    print('%s:' % crypto_str)

    adf_test_results = adf_stationarity_test(crypto_df, al='AIC')

    #c_acf = pd.DataFrame(acf(crypto_df.values)[:500])
    #c_pacf = pd.DataFrame(pacf(crypto_df.values)[:500])

    #plot_acf(crypto_df.values)
    #plt.show()

    #plot_pacf(crypto_df.values)
    #plt.show()

y = None
print(y is None)
crypto_str = diff_df.columns[1]
crypto_df = diff_df[crypto_str]
print('%s:' % crypto_str)

#adf_test_results = adf_stationarity_test(crypto_df, j)

c_acf = pd.DataFrame(acf(crypto_df.values))
c_pacf = pd.DataFrame(pacf(crypto_df.values))

#plot_acf(crypto_df.values, lags=100)
#plt.show()

_ = plt.stem(range(0,len(c_acf)), c_acf)
_ = plt.stem(range(0,len(c_pacf)), c_pacf, linefmt='y-', markerfmt='yo')
plt.show()

#plot_pacf(crypto_df.values)
#plt.show()
"""
