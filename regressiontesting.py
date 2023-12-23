# We want to recreate Rashes' regression calculation
# Predict the small stock based on the large stock, average large stocks,
# average small stocks, and bond prices

# Average large stock was S&P 500
# Average small stock was S&P small cap index
# Bond prices were Lehman Brothers Long Term Bond Index

# The small stocks were included because MCI was an index fund, so don't include
# them in the regression calculation

# Return is calculated as log(price(t) + dividend(t)) - log(price(t-1))
