"""To perform regression testing"""
# We want to recreate Rashes' regression calculation

#import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Assuming 'data' is your prepared DataFrame
def lin_analysis(data):
    """Shit function"""
    # Split the data into features and target
    x = data[['larger_stock_ret', 'sp500_ret', 'bond_index_ret']]  # replace with your column names
    y = data['smaller_stock_ret']  # replace with your column name

    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Create a linear regression model
    model = LinearRegression()

    # Train the model
    model.fit(x_train, y_train)

    # Predictions
    y_pred = model.predict(x_test)

    # Model Evaluation
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")
