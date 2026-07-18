import pandas as pd
import numpy as np

# ===============================
# Load Dataset
# ===============================

df = pd.read_csv("university_cleaned.csv", header=1)

# ===============================
# Clean Column Names
# ===============================

df.columns = (
    df.columns.astype(str)
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

print("Columns in Dataset:\n")
print(df.columns.tolist())

# ===============================
# Convert Numeric Columns
# ===============================

numeric_cols = [
    "world_rank",
    "national_rank",
    "overall_score",
    "academic_reputation_score",
    "employer_reputation_score",
    "citations_score",
    "publications_count",
    "citations_count",
    "citations_per_faculty",
    "h_index",
    "research_output_score",
    "research_productivity_index",
    "total_students",
    "international_students_count",
    "international_student_ratio",
    "faculty_count",
    "faculty_to_student_ratio"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# ===============================
# KPI 1 - Global Ranking Score
# ===============================

if "world_rank" in df.columns:

    max_rank = df["world_rank"].max()

    df["global_ranking_score"] = (
        100 * (1 - (df["world_rank"] - 1) / (max_rank - 1))
    )

# ===============================
# KPI 2 - Research Impact Score
# ===============================

if {"citations_score", "citations_per_faculty"}.issubset(df.columns):

    df["research_impact_score"] = (
        df["citations_score"] +
        df["citations_per_faculty"]
    ) / 2

# ===============================
# KPI 3 - Faculty to Student Ratio
# ===============================

if {"faculty_count", "total_students"}.issubset(df.columns):

    df["faculty_to_student_ratio_kpi"] = (
        df["faculty_count"] /
        df["total_students"]
    )

# ===============================
# KPI 4 - International Student %
# ===============================

if {"international_students_count", "total_students"}.issubset(df.columns):

    df["international_student_percentage"] = (
        df["international_students_count"] /
        df["total_students"]
    ) * 100

elif "international_student_ratio" in df.columns:

    df["international_student_percentage"] = (
        df["international_student_ratio"] * 100
    )

# ===============================
# KPI 5 - Academic Reputation Score
# ===============================

if "academic_reputation_score" in df.columns:

    df["academic_reputation_kpi"] = (
        df["academic_reputation_score"]
    )

# ===============================
# KPI 6 - Research Productivity Index
# ===============================

if {"publications_count", "faculty_count"}.issubset(df.columns):

    df["research_productivity_index_kpi"] = (
        df["publications_count"] /
        df["faculty_count"]
    )

elif "research_productivity_index" in df.columns:

    df["research_productivity_index_kpi"] = (
        df["research_productivity_index"]
    )

# ===============================
# Remove Infinite Values
# ===============================

df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill Missing Values
df.fillna(0, inplace=True)

# ===============================
# Save Final Dataset
# ===============================

df.to_excel(
    "university_final_dataset.xlsx",
    index=False
)

print("\nKPI Engineering Completed Successfully!")
print("Output File: university_final_dataset.xlsx")