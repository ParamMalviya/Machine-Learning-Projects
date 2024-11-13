# Machine Learning - Height and Weight Linear Regression

This project demonstrates a simple **Linear Regression** model to predict **Weight** based on **Height** using a sample dataset. The app provides an interactive way to visualize the relationship between height and weight and uses linear regression to predict the weight for any given height.

## 📝 Project Overview

The main goal of this project is to build a linear regression model that can predict a person's **Weight** based on their **Height**. This can serve as a basic example of supervised machine learning, specifically regression analysis.

### App Features:
- Visualize the relationship between Height and Weight.
- Get real-time predictions for Weight based on any given Height.
- View the Mean Squared Error of the model to evaluate its performance.

## 🚀 Live Demo

You can interact with the app here:

[**Streamlit App: Height-Weight Linear Regression**](https://machine-learning-height-weight-linear-regression-dsn2gouq3essp.streamlit.app/)

## 💻 Files in this Repository

- **`linear_regression_app.py`**: The main Streamlit app that runs the linear regression model.
- **`data/height_weight.csv`**: The CSV file containing the dataset with **Height** and **Weight** columns.
- **`requirements.txt`**: Lists the dependencies required to run the app, such as `streamlit`, `pandas`, and `scikit-learn`.
- **`README.md`**: Documentation for this project (you are here now!).

## 🛠️ Requirements

To run this project locally, you will need the following Python libraries:

- `streamlit` - For building and deploying the web app.
- `pandas` - For data manipulation.
- `scikit-learn` - For building the linear regression model.

You can install these dependencies by running:

```bash
pip install -r requirements.txt
```

## 📝 How to Run the Project Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/ParamMalviya/Machine-Learning-Projects.git
   cd Machine-Learning-Projects/height-weight-linear-regression
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run linear_regression_app.py
   ```

4. Open the app in your browser at `http://localhost:8501`.

## 🤖 Model Details

This project uses a **Linear Regression** model from the `scikit-learn` library to predict the weight based on height. It performs the following steps:

1. Loads the dataset containing height and weight values.
2. Splits the data into training and testing sets.
3. Fits a linear regression model to the training data.
4. Makes predictions on the test set and calculates the Mean Squared Error (MSE).

## 📊 Dataset

The dataset contains two columns:
- **Height** (in inches)
- **Weight** (in pounds)

Here's a preview of the data:

| Height (inches) | Weight (pounds) |
|-----------------|-----------------|
| 60              | 115             |
| 62              | 120             |
| 64              | 125             |
| 66              | 130             |
| 68              | 135             |
| 70              | 140             |
| 72              | 145             |
| 74              | 150             |
| 76              | 155             |
| 78              | 160             |

## 📈 Visualizations

The app provides a graphical representation of the relationship between **Height** and **Weight**. You can see how the linear regression model fits the data and how well it predicts new values.

## 🔧 Technologies Used

- **Python**: Programming language used for the app and model.
- **Streamlit**: For building the interactive web application.
- **Pandas**: For data handling and manipulation.
- **scikit-learn**: For building the linear regression model.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author

- [Param Malviya](https://github.com/ParamMalviya)

---

Feel free to reach out with questions, suggestions, or contributions!
```
