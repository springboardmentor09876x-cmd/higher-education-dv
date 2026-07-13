# ==========================================
# Module 2: Data Cleaning & Transformation
# ==========================================

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load dataset
df = pd.read_csv("university_raw_data.csv")

print("Original Shape:", df.shape)

# -------------------------------
# 1. Remove Duplicate Records
# -------------------------------
df.drop_duplicates(inplace=True)

# -------------------------------
# 2. Standardize Column Names
# -------------------------------
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# -------------------------------
# 3. Standardize University Names
# -------------------------------
if "university_name" in df.columns:
    df["university_name"] = (
        df["university_name"]
        .str.strip()
        .str.title()
    )

# -------------------------------
# 4. Standardize Country Names
# -------------------------------
country_map = {
    "USA": "United States",
    "U.S.A": "United States",
    "US": "United States",
    "UK": "United Kingdom",
    "U.K": "United Kingdom"
}

if "country" in df.columns:
    df["country"] = (
        df["country"]
        .replace(country_map)
        .str.strip()
        .str.title()
    )

# -------------------------------
# 5. Handle Missing Values
# -------------------------------
for col in df.select_dtypes(include="number").columns:
    df[col].fillna(df[col].median(), inplace=True)

for col in df.select_dtypes(include="object").columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# -------------------------------
# 6. Normalize Ranking Metrics
# -------------------------------
ranking_columns = []

possible_columns = [
    "rank",
    "overall_score",
    "academic_reputation",
    "employer_reputation",
    "citations_per_faculty",
    "faculty_student_ratio"
]

for col in possible_columns:
    if col in df.columns:
        ranking_columns.append(col)

if ranking_columns:
    scaler = MinMaxScaler()
    df[ranking_columns] = scaler.fit_transform(df[ranking_columns])

# -------------------------------
# 7. Save Cleaned Dataset
# -------------------------------
df.to_csv("university_cleaned.csv", index=False)

print("\nCleaning Completed Successfully!")
print("Final Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

print("\nFirst 5 Rows:")
print(df.head())