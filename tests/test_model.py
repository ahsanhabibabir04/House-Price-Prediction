import unittest
import joblib
import pandas as pd
from pathlib import Path

class TestHousePriceProject(unittest.TestCase):

    def test_dataset_shape(self):
        df = pd.read_csv("data/california_housing.csv")
        self.assertEqual(df.shape, (20640, 9))

    def test_no_missing_values(self):
        df = pd.read_csv("data/california_housing.csv")
        self.assertEqual(df.isnull().sum().sum(), 0)

    def test_model_file_exists(self):
        self.assertTrue(Path("models/random_forest.pkl").exists())

    def test_model_loads(self):
        model = joblib.load("models/random_forest.pkl")
        self.assertIsNotNone(model)

    def test_model_predicts(self):
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
        prediction = model.predict(sample)
        self.assertEqual(len(prediction), 1)
        self.assertTrue(0 <= prediction[0] <= 5.1)

    def test_model_comparison_exists(self):
        self.assertTrue(Path("models/model_comparison.csv").exists())

if __name__ == "__main__":
    unittest.main()
