\# California House Price Prediction



A machine learning project that predicts California area-level median house values using a Random Forest regression model.



\## Overview



This project uses the California Housing dataset to train and compare two regression models:



\- Linear Regression

\- Random Forest Regressor



The trained Random Forest model is integrated into an interactive Streamlit web application.



\## Features



\- Housing data exploration and validation

\- Regression model training and comparison

\- Evaluation using MAE, RMSE, and R²

\- Interactive house value prediction

\- Automated unit tests



\## Dataset



\- Samples: 20,640

\- Input features: 8

\- Target: Median house value, measured in units of $100,000



The dataset is provided by scikit-learn. Target values are capped near $500,000, so predictions should be treated as estimates rather than guaranteed market prices.



\## Model Performance



Results on the held-out test set:



| Model | MAE | RMSE | R² Score |

|---|---:|---:|---:|

| Linear Regression | 0.5332 | 0.7456 | 0.5758 |

| Random Forest | 0.3277 | 0.5060 | 0.8046 |



Random Forest performed better in this comparison.



\## Tech Stack



\- Python

\- pandas

\- NumPy

\- scikit-learn

\- Streamlit

\- joblib

\- unittest



\## How to Run



Install dependencies:



```bash

python -m pip install -r requirements.txt

```



Start the application:



```bash

python -m streamlit run app.py

```



\## Run Tests



```bash

python -m unittest discover -s tests -v

```



\## Limitations



\- This dataset represents California areas, not individual property listings.

\- Target values are capped near $500,000.

\- Predictions are educational estimates and may not reflect current market prices.



\## Author



M.A. Ahsan Habib Abir



Computer Science Student | Aspiring AI/ML Engineer



