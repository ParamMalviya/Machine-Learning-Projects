import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Sample Data - Directly embedding the height-weight dataset
data = pd.DataFrame({
    'Height': [60, 62, 64, 66, 68, 70, 72, 74, 76, 78],
    'Weight': [115, 120, 125, 130, 135, 140, 145, 150, 155, 160]
})

# Title of the app
st.title("Simple Linear Regression Model")

# Displaying the dataset
st.write("### Dataset: Height vs Weight")
st.write(data)

# Feature and target setup
X = data[['Height']]  # Features (independent variable)
y = data['Weight']    # Target (dependent variable)

# Splitting the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions
predictions = model.predict(X_test)

# Calculating Mean Squared Error
mse = mean_squared_error(y_test, predictions)

# Displaying Results
st.write("### Model Performance")
st.write(f"Mean Squared Error: {mse}")

# Showing predictions vs actual values
st.write("### Predictions vs Actual Values")
result_df = pd.DataFrame({"Actual": y_test.values, "Predicted": predictions})
st.write(result_df)

# Plotting predictions vs actual values
st.line_chart(result_df)

# Optional: Displaying model's coefficient and intercept
st.write("### Model Coefficients")
st.write(f"Intercept: {model.intercept_}")
st.write(f"Coefficient: {model.coef_[0]}")
