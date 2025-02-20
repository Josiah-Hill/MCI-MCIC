"""This module tests the correlation between the volume of trading in the pairs"""

import pandas as pd


# Calculate the correlation coefficient between the volume of trading in the pairs
# Uses Pearson product-moment correlation coefficient
# Function to calculate Pearson correlation for each ticker pair
def calculate_correlations(data):
    """Calculate correlations between T1 and T2, T1 and NYSE, and T2 and NYSE"""
    # Drop non-numeric returns (usually first row in pair)
    data["T1_RET"] = pd.to_numeric(data["T1_RET"], errors="coerce")
    data["T2_RET"] = pd.to_numeric(data["T2_RET"], errors="coerce")
    data = data.dropna(subset=["T1_RET", "T2_RET"])

    # Calculate correlation between T1 and T2 returns
    t1_t2_corr = (
        data.groupby(["T1", "T2"])[["T1_RET", "T2_RET"]]
        .corr()
        .iloc[0::2, -1]
        .reset_index()
    )
    t1_t2_corr = t1_t2_corr.rename(columns={"T2_RET": "T1 vs T2"}).drop(
        columns="level_2"
    )

    # Calculate correlation between T1 and NYSE returns
    t1_nyse_corr = (
        data.groupby(["T1"])[["T1_RET", "NYSE_RET"]].corr().iloc[0::2, -1].reset_index()
    )
    t1_nyse_corr = t1_nyse_corr.rename(columns={"NYSE_RET": "T1 vs NYSE"}).drop(
        columns="level_1"
    )

    # Calculate correlation between T2 and NYSE returns
    t2_nyse_corr = (
        data.groupby(["T2"])[["T2_RET", "NYSE_RET"]].corr().iloc[0::2, -1].reset_index()
    )
    t2_nyse_corr = t2_nyse_corr.rename(columns={"NYSE_RET": "T2 vs NYSE"}).drop(
        columns="level_1"
    )

    # Merge the correlation data into a single DataFrame
    corr_data = pd.merge(t1_t2_corr, t1_nyse_corr, on="T1", how="left")
    corr_data = pd.merge(corr_data, t2_nyse_corr, on="T2", how="left")

    # Select and rename columns for the final output
    corr_data = corr_data[["T1", "T2", "T1 vs T2", "T1 vs NYSE", "T2 vs NYSE"]]

    return corr_data
