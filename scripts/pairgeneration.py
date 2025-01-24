"""Module for identifying ticker pairs in the style of MCI/MCIC"""

from itertools import combinations
import pandas as pd


def read_sic(sic_file):
    """Takes the file of SIC codes and extracts the intervals for major groups."""
    data = pd.read_csv(sic_file, skiprows=1)

    # Create a filtered version of the data with only relevant rows
    data["Title"] = data["Title"].shift(
        1
    )  # Move title in line with relevant division info
    pattern = r"^\d{2}-\d{2}$"  # Define how the division values are displayed
    clean_data = data[data["Division"].str.contains(pattern, na=False)].reset_index()

    # Expand the division column and remove unneccesarry columns
    clean_data[["Group Start", "Group End"]] = clean_data["Division"].str.split(
        "-", expand=True
    )
    clean_data = clean_data[["Title", "Group Start", "Group End"]]

    return clean_data


def sic_mapping(sic_data):
    """Create a mapping of SIC prefix to its corresponding division"""
    sic_prefix_to_division = {}
    for _, row in sic_data.iterrows():
        for prefix in range(int(row["Group Start"]), int(row["Group End"]) + 1):
            sic_prefix_to_division[f"{prefix:02d}"] = row["Title"]
    return sic_prefix_to_division


def ticker_match(t1, t2):
    """Returns true if two tickers match the comparison criteria"""

    return (t1 == t2[:-1] or t1[:-1] == t2 or t1[:-1] == t2[:-1]) and len(t1) + len(
        t2
    ) > 2


def sic_check(sic1, sic2, sic_dict):
    """Returns true if two SICs belong to different major groups"""

    sic1_prefix = str(int(sic1))[:2]
    sic2_prefix = str(int(sic2))[:2]

    division_sic1 = sic_dict.get(sic1_prefix)
    division_sic2 = sic_dict.get(sic2_prefix)

    return division_sic1 == division_sic2 if division_sic1 and division_sic2 else False


def detect_pairs(tick_lst, sic_dict):
    """Identifies ticker pairs with the MCI/MCIC naming convention.
    Eliminates ticker pairs in the same SIC major group.

    Keyword arguments:
    tick_lst -- A dataframe of ticker symbols and relevant SIC codes
    sic -- A dataframe of SIC major groups; the output of read_sic

    Return values:
    pairs -- A dataframe of identified ticker pairs
    """
    # X and A are being paired and they shouldn't be
    pairs_list = []  # Using a list to accumulate pairs
    for ticker1, ticker2 in combinations(tick_lst.itertuples(index=False), 2):
        if ticker_match(ticker1.TICKER, ticker2.TICKER):
            if sic_check(ticker1.SICCD, ticker2.SICCD, sic_dict):
                pairs_list.append({"T1": ticker1.TICKER, "T2": ticker2.TICKER})

    # Creating DataFrame from the list
    pairs = pd.DataFrame(pairs_list)
    return pairs


def pairgeneration(ticker_file, sic_file):
    """Return a DataFrame of ticker pairs matching the MCI/MCIC constraints"""
    sic_divisions = sic_mapping(read_sic(sic_file))

    tickers = pd.read_csv(ticker_file, usecols=["SICCD", "TICKER"]).dropna()
    return detect_pairs(tickers, sic_divisions)
