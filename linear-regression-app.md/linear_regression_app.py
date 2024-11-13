import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Title of the app
st.title("Linear Regression Model with Streamlit")

# Step 1: Uploading the Dataset
st.sidebar.header("Step 1: Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Dataset:")
    st.write(data)

    # Step 2: Select Features and Target Variable
    st.sidebar.header("Step 2: Select Features and Target")
    feature_columns = st.sidebar.multiselect("Select Feature Column(s)", data.columns)
    target_column = st.sidebar.selectbox("Select Target Column", data.columns)

    if feature_columns and target_column:
        X = data[feature_columns]
        y = data[target_column]
        
        # Splitting data into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Step 3: Train the Model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Making predictions
        predictions = model.predict(X_test)
        
        # Calculating Mean Squared Error
        mse = mean_squared_error(y_test, predictions)
        
        # Display the results
        st.header("Results")
        st.write(f"Mean Squared Error: {mse}")
        st.write("Predictions vs Actual:")
        result_df = pd.DataFrame({"Actual": y_test, "Predicted": predictions})
        st.write(result_df)

        # Visualize the predictions vs. actual values
        st.line_chart(result_df)
    else:
        st.warning("Please select both feature(s) and target column.")
else:
    st.info("Please upload a CSV file to proceed.")
