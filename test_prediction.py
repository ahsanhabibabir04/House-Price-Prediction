import joblib
import pandas as pd

model = joblib.load("models/random_forest.pkl")

sample = pd.DataFrame([{
    "MedInc": 5.0,
    "HouseAge": 25.0,
    "AveRooms": 5.5,
    "AveBedrms": 1.1,
    "Population": 1000.0,
    "AveOccup": 3.0,
    "Latitude": 34.05,
    "Longitude": -118.25
}])

prediction = model.predict(sample)[0]

print("Sample prediction successful!")
print(f"Predicted median house value: ${prediction * 100000:,.0f}")
print(f"Raw model output: {prediction:.4f}")
