import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="California House Price Predictor",
    page_icon="🏡",
    layout="wide"
)

MODEL_PATH = Path("models/random_forest.pkl")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

st.title("🏡 California House Price Predictor")
st.write(
    "Estimate a California area's median house value "
    "using a trained Random Forest machine learning model."
)

st.info(
    "This educational demo predicts area-level median house values, "
    "not the market price of an individual property."
)

if not MODEL_PATH.exists():
    st.error("Model file not found. Please run `python train.py` first.")
    st.stop()

model = load_model()

st.subheader("Enter Housing Information")

with st.form("house_prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        med_inc = st.number_input(
            "Median income (in $10,000s)",
            min_value=0.5, max_value=15.0, value=5.0, step=0.1
        )
        house_age = st.number_input(
            "Median house age (years)",
            min_value=1.0, max_value=52.0, value=25.0, step=1.0
        )
        ave_rooms = st.number_input(
            "Average rooms per household",
            min_value=0.5, max_value=150.0, value=5.5, step=0.1
        )
        ave_bedrms = st.number_input(
            "Average bedrooms per household",
            min_value=0.3, max_value=35.0, value=1.1, step=0.1
        )

    with col2:
        population = st.number_input(
            "Area population",
            min_value=1.0, max_value=40000.0, value=1000.0, step=100.0
        )
        ave_occup = st.number_input(
            "Average household occupancy",
            min_value=0.5, max_value=1250.0, value=3.0, step=0.1
        )
        latitude = st.number_input(
            "Latitude",
            min_value=32.54, max_value=41.95, value=34.05, step=0.01,
            format="%.2f"
        )
        longitude = st.number_input(
            "Longitude",
            min_value=-124.35, max_value=-114.31, value=-118.25, step=0.01,
            format="%.2f"
        )

    submitted = st.form_submit_button(
        "Predict Median House Value",
        type="primary",
        use_container_width=True
    )

if submitted:
    input_data = pd.DataFrame([{
        "MedInc": med_inc,
        "HouseAge": house_age,
        "AveRooms": ave_rooms,
        "AveBedrms": ave_bedrms,
        "Population": population,
        "AveOccup": ave_occup,
        "Latitude": latitude,
        "Longitude": longitude
    }])

    prediction = float(model.predict(input_data)[0])
    predicted_usd = prediction * 100000

    st.subheader("Prediction Result")
    st.metric(
        "Estimated Median House Value",
        f"${predicted_usd:,.0f}"
    )
    st.caption(
        "The model output is expressed in $100,000 units. "
        "The dataset caps target values near $500,000, and predictions "
        "are estimates rather than guaranteed market prices."
    )

with st.expander("About this project"):
    st.write(
        "Dataset: California Housing. "
        "Model: Random Forest Regressor. "
        "Test R² score: 0.8046. "
        "Evaluation used a held-out test split."
    )
