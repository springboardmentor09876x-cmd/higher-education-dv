import pandas as pd

# Read Reference 2 dataset
ref2 = pd.read_csv("data/raw/reference2.csv")

print("=" * 80)
print("REFERENCE 2 INFORMATION")
print("=" * 80)

print("\nShape:")
print(ref2.shape)

print("\nColumns:")
print(ref2.columns.tolist())

print("\nData Types:")
print(ref2.dtypes)

print("\nMissing Values:")
print(ref2.isnull().sum())

print("\nFirst 5 Rows:")
print(ref2.head())