import pandas as pd
import numpy as np

print("=" * 60)
print("EduVision DV - KPI Engineering")
print("=" * 60)

# Load cleaned dataset
df = pd.read_csv("university_cleaned.csv")

print("\nDataset Loaded Successfully!")
print("Rows :", df.shape[0])
print("Columns :", df.shape[1])

print("\nCalculating KPIs...")

# -------------------------------------------------
# Convert numeric columns
# -------------------------------------------------

numeric_columns = [
    "2026 Rank",
    "AR SCORE",
    "FSR SCORE",
    "ISR SCORE",
    "CPF SCORE",
    "IRN SCORE"
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# -------------------------------------------------
# KPI 1: Global Ranking Score
# Higher score = Better ranking
# -------------------------------------------------

if "2026 Rank" in df.columns:
    max_rank = df["2026 Rank"].max()
    df["Global Ranking Score"] = max_rank - df["2026 Rank"] + 1

# -------------------------------------------------
# KPI 2: Academic Reputation Score
# -------------------------------------------------

if "AR SCORE" in df.columns:
    df["Academic Reputation Score"] = df["AR SCORE"]

# -------------------------------------------------
# KPI 3: Faculty-to-Student Ratio
# -------------------------------------------------

if "FSR SCORE" in df.columns:
    df["Faculty-to-Student Ratio"] = df["FSR SCORE"]

# -------------------------------------------------
# KPI 4: International Student Percentage
# -------------------------------------------------

if "ISR SCORE" in df.columns:
    df["International Student Percentage"] = df["ISR SCORE"]

# -------------------------------------------------
# KPI 5: Research Impact Score
# -------------------------------------------------

if "CPF SCORE" in df.columns:
    df["Research Impact Score"] = df["CPF SCORE"]

# -------------------------------------------------
# KPI 6: Research Productivity Index
# -------------------------------------------------

if "IRN SCORE" in df.columns:
    df["Research Productivity Index"] = df["IRN SCORE"]

print("All KPIs generated successfully!")

# -------------------------------------------------
# Display KPI Preview
# -------------------------------------------------

kpi_columns = [
    "Institution Name",
    "Global Ranking Score",
    "Academic Reputation Score",
    "Faculty-to-Student Ratio",
    "International Student Percentage",
    "Research Impact Score",
    "Research Productivity Index"
]

available_columns = [col for col in kpi_columns if col in df.columns]

print("\nKPI Preview:")
print(df[available_columns].head())

# -------------------------------------------------
# Save Final Dataset
# -------------------------------------------------

output_file = "university_final_dataset.xlsx"

df.to_excel(output_file, index=False)

print("\nFinal dataset saved successfully!")
print("Output File :", output_file)
print("Final Shape :", df.shape)

print("\n========== MODULE 3 COMPLETED ==========")