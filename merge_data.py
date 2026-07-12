import pandas as pd

print("========== Higher Education Dataset Integration ==========")

# ----------------------------------------------------
# Load Datasets
# ----------------------------------------------------
print("Loading datasets...")

qs = pd.read_csv("raw_data/qs_2026.csv")
qs_ref = pd.read_csv("raw_data/qs_reference.csv")
world = pd.read_csv("raw_data/world_rankings_2026.csv")

# ----------------------------------------------------
# Remove unnecessary columns
# ----------------------------------------------------
qs_ref = qs_ref.loc[:, ~qs_ref.columns.str.contains("^Unnamed")]

# ----------------------------------------------------
# Standardize column values
# ----------------------------------------------------
qs["Institution Name"] = qs["Institution Name"].str.strip().str.lower()
qs["Country/Territory"] = qs["Country/Territory"].str.strip().str.lower()

qs_ref["Name"] = qs_ref["Name"].str.strip().str.lower()
qs_ref["Country/Territory"] = qs_ref["Country/Territory"].str.strip().str.lower()

world["university"] = world["university"].str.strip().str.lower()
world["country"] = world["country"].str.strip().str.lower()

print("Cleaning completed.")

# ----------------------------------------------------
# Merge QS Dataset with World Rankings
# ----------------------------------------------------
merged = pd.merge(
    qs,
    world,
    left_on=["Institution Name", "Country/Territory"],
    right_on=["university", "country"],
    how="left"
)

print("QS + World Rankings merged.")

# ----------------------------------------------------
# Merge with Reference Dataset
# ----------------------------------------------------
merged = pd.merge(
    merged,
    qs_ref,
    left_on=["Institution Name", "Country/Territory"],
    right_on=["Name", "Country/Territory"],
    how="left",
    suffixes=("", "_ref")
)

print("Reference dataset merged.")

# ----------------------------------------------------
# Remove duplicate rows
# ----------------------------------------------------
merged.drop_duplicates(inplace=True)

# ----------------------------------------------------
# Handle missing values
# ----------------------------------------------------
# Fill text columns
object_cols = merged.select_dtypes(include=["object"]).columns
merged[object_cols] = merged[object_cols].fillna("Not Available")

# Fill numeric columns
numeric_cols = merged.select_dtypes(include=["number"]).columns
merged[numeric_cols] = merged[numeric_cols].fillna(0)

# ----------------------------------------------------
# Save Final Dataset
# ----------------------------------------------------
merged.to_csv("university_raw_data.csv", index=False)

# ----------------------------------------------------
# Summary
# ----------------------------------------------------
print("\n========== SUMMARY ==========")
print("Rows    :", merged.shape[0])
print("Columns :", merged.shape[1])

print("\nFirst Five Records")
print(merged.head())

print("\nMissing Values")
print(merged.isnull().sum())

print("\nDataset generated successfully!")