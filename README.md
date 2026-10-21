# California House Price Prediction

A machine learning project that predicts California area-level median house values using regression models, including Linear Regression and Random Forest Regressor.

## Live Demo

Try the deployed application: [California House Price Prediction — Live Demo](https://california-house-price-prediction-byabir.streamlit.app/)

## GitHub Repository

Source code: [California House Price Prediction on GitHub](https://github.com/ahsanhabibabir04/house-price-prediction)

## Overview

This project uses the California Housing dataset to train and compare two regression models: Linear Regression and Random Forest Regressor.

The project includes data exploration, validation, model training, performance evaluation, and an interactive Streamlit web application that predicts area-level median house values based on housing-related features.

The goal is to demonstrate a practical machine learning workflow, from dataset preparation to model deployment.

## Features

- Housing dataset exploration and validation
- Data preprocessing and feature analysis
- Training and comparison of regression models
- Linear Regression and Random Forest Regressor
- Model evaluation using MAE, RMSE, and R² score
- Interactive house value prediction through Streamlit
- Automated unit tests
- Model serialization using Joblib

## Dataset

This project uses the California Housing dataset provided by scikit-learn.

- **Number of samples:** 20,640
- **Number of input features:** 8
- **Target variable:** Median house value
- **Target units:** $100,000

The dataset contains aggregated information about California housing districts, including median income, housing age, average rooms, population, and geographic coordinates.

Target values are capped near $500,000. Therefore, predictions should be interpreted as estimates of area-level median house values rather than exact prices for individual properties.

## Model Performance

The models were evaluated on a held-out test set.

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 0.5332 | 0.7456 | 0.5758 |
| Random Forest Regressor | 0.3277 | 0.5060 | 0.8046 |

### Model Comparison

Random Forest Regressor performed better than Linear Regression across all three reported metrics on this test set.

- **MAE (Mean Absolute Error):** Measures the average absolute difference between predicted and actual values. Lower is better.
- **RMSE (Root Mean Squared Error):** Measures prediction error while penalizing larger errors more heavily. Lower is better.
- **R² Score:** Measures how well the model explains variation in the target variable. Higher is generally better.

The target is measured in units of $100,000. For example, an MAE of 0.3277 corresponds to an average absolute error of approximately $32,770 in the dataset's target units.

Based on these results, the Random Forest Regressor is used in the Streamlit application.

**Note:** These results represent one held-out test set and do not guarantee the same performance on other datasets or future housing markets.

## Technologies Used

- **Python** — Programming language
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical computing
- **Scikit-learn** — Data processing and machine learning
- **Streamlit** — Interactive web application
- **Joblib** — Model serialization
- **unittest** — Automated testing
- **Git and GitHub** — Version control and source code hosting

## Requirements

- Python 3.10 or newer, compatible with the project's dependencies
- pip
- Git (optional, for cloning the repository)
- An internet connection for installing dependencies

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ahsanhabibabir04/house-price-prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd house-price-prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

## Run the Streamlit Application

Start the application with:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal to access the application.

Enter the required housing information to generate a predicted median house value.

## Run Automated Tests

Run the project's test suite with:

```bash
python -m unittest discover -s tests -v
```

The test suite checks the implemented project functionality and helps detect regressions.

## Limitations

- The dataset represents California housing districts, not individual property listings.
- Target values are capped near $500,000.
- Predictions are educational estimates and may not reflect current market prices.
- The model may not generalize well to locations outside California.
- Housing market conditions can change over time, affecting prediction accuracy.
- Model performance depends on the dataset, selected features, and training configuration.

## Future Improvements

Potential improvements include:

- Hyperparameter tuning for the Random Forest model
- Cross-validation for more robust model evaluation
- Feature importance analysis and model explainability
- Improved visualizations of housing data and prediction errors
- Testing additional regression algorithms
- Retraining with more recent housing data
- Deploying additional model evaluation metrics in the web application

## Learning Outcomes

Through this project, I practiced:

- Exploring and validating a real-world dataset
- Preparing data for regression tasks
- Training and comparing machine learning models
- Evaluating regression performance using MAE, RMSE, and R²
- Understanding prediction errors and model limitations
- Saving and loading trained models with Joblib
- Building an interactive application with Streamlit
- Writing automated tests with Python's `unittest`
- Organizing and documenting a machine learning project
- Managing source code using Git and GitHub

## Author

**M.A. Ahsan Habib Abir**

Computer Science Student | Aspiring AI/ML Engineer

## Repository Links

- **Live Demo:** [California House Price Prediction](https://california-house-price-prediction-byabir.streamlit.app/)
- **GitHub Repository:** [house-price-prediction](https://github.com/ahsanhabibabir04/house-price-prediction)
- **GitHub Profile:** [ahsanhabibabir04](https://github.com/ahsanhabibabir04)

---

If you find this project useful, consider giving the repository a star.
