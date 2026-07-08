import pandas as pd

# ----------------------------------------------------
# READ DATASETS
# ----------------------------------------------------

qs = pd.read_csv(
    "data/raw/QS 2025.csv",
    encoding="latin1"
)

the = pd.read_csv(
    "data/raw/THE 2025.csv"
)

# ----------------------------------------------------
# RENAME QS COLUMNS
# ----------------------------------------------------

qs = qs.rename(columns={
    "Institution_Name":"university_name",
    "Location":"country",
    "Region":"region",
    "RANK_2025":"world_rank",
    "Overall_Score":"overall_score",
    "Academic_Reputation_Score":"academic_reputation_score",
    "Employer_Reputation_Score":"employer_reputation_score",
    "Faculty_Student_Score":"faculty_student_ratio",
    "Citations_per_Faculty_Score":"citations_per_faculty",
    "International_Faculty_Score":"international_faculty_score",
    "International_Students_Score":"international_students_ratio",
    "International_Research_Network_Score":"international_research_network_score"
})

# ----------------------------------------------------
# RENAME THE COLUMNS
# ----------------------------------------------------

the = the.rename(columns={
    "university":"university_name",
    "country":"country",
    "rank":"world_rank",
    "overall_score":"overall_score",
    "student_pop":"total_students",
    "student_staff_ratio":"faculty_student_ratio",
    "intl_students_pct":"international_students_ratio",
    "female_pct":"female_percentage",
    "research_env":"research_environment",
    "research_qual":"research_quality",
    "intl_outlook":"international_outlook"
})

# Select required QS columns
qs = qs[
    [
        "university_name",
        "country",
        "region",
        "world_rank",
        "overall_score",
        "academic_reputation_score",
        "employer_reputation_score",
        "faculty_student_ratio",
        "citations_per_faculty",
        "international_faculty_score",
        "international_students_ratio",
        "international_research_network_score"
    ]
]

# Select required THE columns
the = the[
    [
        "university_name",
        "country",
        "world_rank",
        "overall_score",
        "total_students",
        "faculty_student_ratio",
        "international_students_ratio",
        "female_percentage",
        "teaching",
        "research_environment",
        "research_quality",
        "industry",
        "international_outlook",
        "year"
    ]
]

print(qs.head())

print(the.head())

# ---------------------------------
# Merge QS and THE datasets
# ---------------------------------

merged_data = pd.merge(
    qs,
    the,
    on="university_name",
    how="outer",
    suffixes=("_QS", "_THE")
)

# ---------------------------------------
# Rename merged columns to reference names
# ---------------------------------------

merged_data = merged_data.rename(columns={

    "world_rank_QS": "world_rank",
    "overall_score_QS": "overall_score",
    "country_QS": "country",

    "faculty_student_ratio_QS": "faculty_to_student_ratio",

    "international_students_ratio_QS": "international_student_ratio",

    "citations_per_faculty": "citations_per_faculty_score",

    "international_faculty_score": "international_faculty_score",

    "international_research_network_score": "international_research_network_score",

    "total_students": "total_students",

    "female_percentage": "female_percentage",

    "research_environment": "research_environment_score",

    "research_quality": "research_quality_score",

    "international_outlook": "international_outlook_score"

})

print("\nFinal Column Names:\n")

print(merged_data.columns.tolist())

print("\nMerged Dataset Preview")
print(merged_data.head())

print("\nMerged Dataset Shape")
print(merged_data.shape)

# Save the merged dataset
merged_data.to_csv(
    "output/university_raw_data.csv",
    index=False
)

print("\n✅ university_raw_data.csv has been created successfully!")