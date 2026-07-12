import pandas as pd

print("Loading datasets...")

# Load datasets
qs = pd.read_csv("raw_data/qs_2026.csv")
qs_ref = pd.read_csv("raw_data/qs_reference.csv")
world = pd.read_csv("raw_data/world_rankings_2026.csv")

# -----------------------------
# Data Cleaning
# -----------------------------

# Standardize university names
qs["Institution Name"] = qs["Institution Name"].str.strip().str.lower()
world["university"] = world["university"].str.strip().str.lower()

# Standardize country names
qs["Country/Territory"] = qs["Country/Territory"].str.strip().str.lower()
world["country"] = world["country"].str.strip().str.lower()

print("Cleaning completed...")

# -----------------------------
# Merge Datasets
# -----------------------------

merged = pd.merge(
    qs,
    world,
    left_on=["Institution Name", "Country/Territory"],
    right_on=["university", "country"],
    how="left"
)

print("Merge completed!")

# -----------------------------
# Remove duplicate rows
# -----------------------------
merged = merged.drop_duplicates()

# -----------------------------
# Handle missing values
# -----------------------------
merged = merged.fillna("Not Available")

# -----------------------------
# Save Final Dataset
# -----------------------------
merged.to_csv("university_raw_data.csv", index=False)

print("Final dataset saved as university_raw_data.csv")
print("Rows :", merged.shape[0])
print("Columns :", merged.shape[1])
print("\nDataset Preview:")
print(merged.head())

print("\nMissing Values:")
print(merged.isnull().sum())

print("\nDataset generated successfully!")