"""Module for loading stock return data and integrating it with ticker pairs"""

import pandas as pd

def add_stock_info(pairs, returns_file, nyse_returns_file):
    """Add stock information from returns files to a DataFrame of ticker pairs"""
    # Read stock data from returns file
    stock_data = pd.read_csv(returns_file, usecols=["TICKER", "date", "VOL", "RET"])

    # Read NYSE returns data
    nyse_data = pd.read_csv(nyse_returns_file, usecols=["TICKER", "date", "RET"])
    nyse_data.rename(columns={"RET": "NYSE_RET"}, inplace=True)

    # Merge stock data for T1
    data_t1 = pairs.merge(stock_data, left_on="T1", right_on="TICKER")
    data_t1.rename(columns={"VOL": "T1_VOL", "RET": "T1_RET"}, inplace=True)
    data_t1.drop(columns="TICKER", inplace=True)

    # Merge stock data for T2
    data_t2 = pairs.merge(stock_data, left_on="T2", right_on="TICKER")
    data_t2.rename(columns={"VOL": "T2_VOL", "RET": "T2_RET"}, inplace=True)
    data_t2.drop(columns="TICKER", inplace=True)

    # Merge T1 and T2 data
    data = pd.merge(data_t1, data_t2, on=["T1", "T2", "date"])

    # Merge with NYSE returns
    final_data = data.merge(nyse_data, on=["TICKER", "date"], how="left")

    return final_data
