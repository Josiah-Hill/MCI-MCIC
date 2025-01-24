"""Script for downloading S&P 500 returns from Yahoo Finance and saving them to CSV files."""

import os
import yfinance as yf


def main(ticker_dict, data_dir):
    """
    Downloads ticker returns and saves it to the data folder.

    Parameters
    ----------
    ticker_dict : dictionary
        key : relevant NYSE ticker
        value : colloquial name
    data_dir : directory location for data folder

    Returns
    -------
    None
    """
    for t, name in ticker_dict.items():
        data = yf.download(t, start="2003-01-01", end="2020-12-31")

        data["Daily Returns"] = data["Adj Close"].pct_change()

        # Rename column to monthly returns or something
        data_monthly_returns = (
            data["Daily Returns"].resample("M").agg(lambda x: (x + 1).prod() - 1)
        )

        data.to_csv(os.path.join(data_dir, f"{name}_daily_returns.csv"))
        data_monthly_returns.to_csv(
            os.path.join(data_dir, f"{name}_monthly_returns.csv")
        )


if __name__ == "__main__":
    # Get the parent directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)

    # Construct the path to the data folder
    data_folder = os.path.join(parent_dir, "data")

    # Ensure the data folder exists
    os.makedirs(data_folder, exist_ok=True)

    tickers = {"^GSPC": "sp500", "LQD": "bond", "^NYA": "nyse"}
    main(tickers, data_folder)
