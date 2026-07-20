import pandas as pd

# STEP 1: Read cleaned dataset
df = pd.read_csv(
    "output/university_cleaned.csv"
)

# STEP 2: KPI Formulas
# KPI 1
df["global_ranking_score"] = (
    (1 - (df["world_rank"] / df["world_rank"].max())) * 50
) + (
    df["overall_score"] * 0.5
)

# KPI 2
df["research_impact_score"] = (
    df["citations_score"] * 0.4
    + df["citations_per_faculty"] * 0.3
    + df["h_index"] * 0.3
)

# KPI 3
df["faculty_student_ratio_kpi"] = (
    df["faculty_to_student_ratio"]
)

# KPI 4
df["international_student_percentage_kpi"] = (
    df["international_student_ratio"]
)

# KPI 5
df["academic_reputation_kpi"] = (
    df["academic_reputation_score"] * 0.7
    + df["employer_reputation_score"] * 0.3
)

# KPI 6
df["research_productivity_kpi"] = (
    df["research_productivity_index"]
)
print(
    df[
        [
            "global_ranking_score",
            "research_impact_score",
            "faculty_student_ratio_kpi",
            "international_student_percentage_kpi",
            "academic_reputation_kpi",
            "research_productivity_kpi"
        ]
    ].head()
)
df.to_excel(
    "output/university_final_dataset.xlsx",
    index=False
)

print(
    "\n✅ university_final_dataset.xlsx created successfully!"
)