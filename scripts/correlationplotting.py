"""Module for plotting correlation coefficients"""
import matplotlib.pyplot as plt
import seaborn as sns

def kde_plots(corr_data):
    """Plot the correlations"""
    # KDE plot of Pearson correlation coefficients for each comparison
    plt.figure(figsize=(12, 8))

    # KDE for T1 vs T2 correlations
    sns.kdeplot(corr_data["T1 vs T2"], shade=True, label="T1 vs T2")

    # KDE for T1 vs NYSE correlations
    sns.kdeplot(corr_data["T1 vs NYSE"], shade=True, label="T1 vs NYSE")

    # KDE for T2 vs NYSE correlations
    sns.kdeplot(corr_data["T2 vs NYSE"], shade=True, label="T2 vs NYSE")

    plt.title("KDE of Pearson Correlation Coefficients")
    plt.xlabel("Pearson Correlation")
    plt.ylabel("Density")
    plt.legend()
    plt.show()

    # Export image to results folder - specify the path where you want to save
    plt.savefig('/path/to/results/folder/correlation_kde.png')
