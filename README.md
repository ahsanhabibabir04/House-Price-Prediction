# California House Price Prediction

## Live Demo

[Launch the California House Price Prediction App](https://house-price-prediction-byabir.streamlit.app/)

## Overview

A machine learning project that predicts California district-level median house values using the California Housing dataset. The project implements and compares Linear Regression and Random Forest regression models, with an interactive Streamlit web application powered by the trained Random Forest model.

## Project Objectives

- Explore and preprocess the California Housing dataset.
- Train and evaluate multiple regression models.
- Compare model performance using standard regression metrics.
- Select a suitable model for house value prediction.
- Deploy an interactive application using Streamlit.

## Dataset

This project uses the California Housing dataset available through scikit-learn.

- **Number of samples:** 20,640
- **Input features:** 8
- **Target variable:** Median house value
- **Target unit:** Hundreds of thousands of US dollars
- **Source:** scikit-learn California Housing dataset

The target value is capped at approximately $500,000 in the dataset.

## Machine Learning Models

Two regression algorithms were trained and evaluated:

1. **Linear Regression** — a baseline model for estimating the relationship between input features and median house values.
2. **Random Forest Regressor** — an ensemble learning model that combines multiple decision trees to capture more complex relationships in the data.

The Random Forest model is used in the Streamlit application because it achieved better evaluation results in this project.

## Model Evaluation

The models were compared using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and the coefficient of determination (R²).

| Metric | Linear Regression | Random Forest |
|---|---:|---:|
| MAE | 0.5332 | 0.3277 |
| RMSE | 0.7456 | 0.5060 |
| R² Score | 0.5758 | 0.8046 |

### Results

The Random Forest Regressor outperformed Linear Regression across all three reported metrics.

- **Lower MAE:** The Random Forest model produced smaller average absolute prediction errors.
- **Lower RMSE:** Its predictions had a lower root mean squared error.
- **Higher R²:** The model explained approximately 80.46% of the variance in the target values on the evaluation data.

These results indicate that Random Forest was the stronger model for this project.

## Features

- Interactive house value prediction interface.
- California Housing dataset integration.
- Linear Regression and Random Forest model comparison.
- Evaluation using MAE, RMSE, and R².
- Trained model persistence with Joblib.
- Automated unit tests using Python's `unittest` framework.
- Web deployment using Streamlit.

## Technologies Used

- Python
- pandas
- NumPy
- scikit-learn
- Streamlit
- Joblib
- unittest

## Project Structure

```text
California-House-Price-Prediction/
├── app.py
├── requirements.txt
├── README.md
├── models/
├── data/
└── tests/
```

*Note: Update this structure if your actual repository contains a different set of files or folders.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ahsanhabibabir04/house-price-prediction.git
cd house-price-prediction
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser. If it does not open automatically, use the local URL displayed in the terminal.

## Running Tests

Run the project's automated tests with:

```bash
python -m unittest discover -s tests -v
```

## Limitations

- Predictions are estimates based on historical dataset patterns and are not professional property valuations.
- The dataset's target values are capped, which limits the model's ability to distinguish properties above that threshold.
- Model performance depends on the dataset, preprocessing, train-test split, and evaluation methodology.
- Predictions should not be used as the sole basis for real estate investment or purchasing decisions.

## Future Improvements

- Add visualizations for feature distributions and model performance.
- Perform hyperparameter tuning for the Random Forest model.
- Add cross-validation for more robust model evaluation.
- Improve the user interface and input validation.
- Explore additional regression algorithms and compare their performance.

## Author

**M.A. Ahsan Habib Abir**

Computer Science Student | Aspiring AI/ML Engineer

- GitHub: [ahsanhabibabir04](https://github.com/ahsanhabibabir04)

## License

This project is intended for educational and portfolio purposes. Add a `LICENSE` file if you want to distribute the project under a specific open-source license.
