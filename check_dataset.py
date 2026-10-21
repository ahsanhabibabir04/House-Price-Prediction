import pandas as pd

df = pd.read_csv("data/california_housing.csv")

print("Dataset shape:", df.shape)
print("\nColumn data types:")
print(df.dtypes)

print("\nStatistical summary:")
print(df.describe().round(2))

print("\nDuplicate rows:", df.duplicated().sum())
print("Missing values:", df.isnull().sum().sum())

print("\nTarget value range:")
print("Minimum:", df["MedHouseVal"].min())
print("Maximum:", df["MedHouseVal"].max())
