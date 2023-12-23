"""Module for plotting correlation coefficients"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample Pearson correlation data for demonstration
# In real scenario, use the pearson_correlation DataFrame
sample_pearson_correlation = pd.DataFrame(
    {
        "T1": ["ABC", "EFG", "HIJ", "KLM"],
        "T2": ["ABCD", "EFGH", "HIJK", "KLMN"],
        "Pearson Correlation": [1.0, 0.8, -0.5, 0.3],
    }
)

# KDE plot of Pearson correlation coefficients
plt.figure(figsize=(8, 6))
sns.kdeplot(sample_pearson_correlation["Pearson Correlation"], shade=True)
plt.title("KDE of Pearson Correlation Coefficients")
plt.xlabel("Pearson Correlation")
plt.ylabel("Density")
plt.show()

# Export image to results folder
