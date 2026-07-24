# ============================================================
# Module 3: Education KPI Engineering
# Higher Education Performance Dashboard
# ============================================================

import pandas as pd
import numpy as np

input_file = r"C:\Users\s sai vaishnavi\OneDrive\Desktop\Higher_Education_Project\datasets\processed_data\cleaned data\final_cleaned_university_dataset.xls"

df = pd.read_csv(input_file)

print("Dataset Loaded Successfully")
print("Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

df["world_rank_numeric"] = (
    df["world_rank"].astype(str)
      .str.replace("=", "", regex=False)
      .str.replace("+", "", regex=False)
      .str.extract(r"(\d+)", expand=False)
)
df["world_rank_numeric"] = pd.to_numeric(df["world_rank_numeric"], errors="coerce")

max_rank = df["world_rank_numeric"].max()
min_rank = df["world_rank_numeric"].min()

df["global_ranking_score"] = (
    (max_rank - df["world_rank_numeric"]) /
    (max_rank - min_rank)
) * 100
df["global_ranking_score"] = df["global_ranking_score"].round(2)

df["research_impact_score"] = (
    df["citations_score"] * 0.6 +
    df["research_output_score"] * 0.4
).round(2)

df["international_students_count"] = (
    df["international_students_count"]
      .astype(str)
      .str.replace("%","",regex=False)
      .astype(float)
)

df["overall_score"] = (
    df["overall_score"]
      .replace("-", np.nan)
      .fillna("Not Published")
)

output_file = r"C:\Users\s sai vaishnavi\OneDrive\Desktop\Higher_Education_Project\datasets\processed_data\cleaned data\university_final_dataset.xlsx"
df.to_excel(output_file, index=False)

print("KPI Engineering Completed Successfully!")
