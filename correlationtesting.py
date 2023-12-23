"""This module tests the correlation between the volume of trading in the pairs"""

# import pandas as pd
import returnsintegration
import pairgeneration


# Calculate the correlation coefficient between the volume of trading in the pairs
# Uses Pearson product-moment correlation coefficient
# Function to calculate Pearson correlation for each ticker pair
def calculate_pearson_correlation(df):
    """Calculate the Pearson correlation coefficient for each ticker pair"""
    # Group by T1 and T2 pairs and calculate correlation
    correlation_data = df.groupby(["T1", "T2"]).apply(
        lambda group: group["T1_VOL"].corr(group["T2_VOL"])
    )
    return correlation_data.reset_index(name="Pearson Correlation")


# Calculate the correlation coefficient between each stock and the NYSE or NASDAQ
# How do we know which index to choose?

# In another file, plot kdes of correlations

# Identify pairs with high correlation to each other but
# low correlation to the index


def main(returns_file):
    """Main function for correlation testing"""
    pairs = pairgeneration.pairgeneration("data\\tickers.csv", "data\\sic_table.csv")
    data = returnsintegration.add_stock_info(pairs, returns_file)
    pearson_correlation = calculate_pearson_correlation(data)
    return pearson_correlation


main("data\\MonthlyTickerConfusion.csv")

# Need to save this data to results folder
