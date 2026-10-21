from sklearn.datasets import fetch_california_housing
import pandas as pd

dataset = fetch_california_housing(data_home="data", download_if_missing=True)

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df["MedHouseVal"] = dataset.target

df.to_csv("data/california_housing.csv", index=False)

print("CSV saved successfully!")
print("Dataset shape:", df.shape)
print("Missing values:", df.isnull().sum().sum())
print("\nFirst 5 rows:")
print(df.head())
