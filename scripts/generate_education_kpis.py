import pandas as pd
import numpy as np
path = r"C:\Users\yadav\higher-education-dv\datasets\processed_data\university_cleaned.csv"

df = pd.read_csv(path)
required_columns = [
    "world_rank",
    "academic_reputation_score",
    "citations_count",
    "Research_Output_x",
    "Student Population",
    "faculty_count",
    "international_students_count"
]

for col in required_columns:
    print(col, "->", col in df.columns)

# Global Ranking Score (Higher is Better)
df["global_ranking_score"] = 1000 - pd.to_numeric(df["world_rank"], errors="coerce")

# Research Impact Score
df["research_impact_score"] = (
    df["citations_count"] +
    df["Research_Output_x"] +
    df["research_productivity_index"]
) / 3

# Faculty to Student Ratio
df["faculty_student_ratio_kpi"] = df["faculty_to_student_ratio"]

# International Student Percentage
df["international_student_percentage"] = df["international_student_ratio"]

# Academic Reputation Score
df["academic_reputation_kpi"] = df["academic_reputation_score"]

# Research Productivity Index
df["research_productivity_kpi"] = df["research_productivity_index"]

print(df.shape)
output_path = r"C:\Users\yadav\higher-education-dv\datasets\processed_data\university_final_dataset.xlsx"

df.to_excel(output_path, index=False)

print("Final Dataset Saved Successfully!")

print("=" * 50)
print("University KPI Generation Completed Successfully")
print("Final Dataset Shape:", df.shape)
print("Dataset Saved Successfully!")
print("=" * 50)