import pandas as pd
import numpy as np

# ==========================================
# Load Dataset
# ==========================================
INPUT_FILE = "output/university_raw_data.csv"
OUTPUT_FILE = "data/processed/university_cleaned.csv"

df = pd.read_csv(INPUT_FILE)

print("="*60)
print("Original Shape:", df.shape)
print("="*60)

# ==========================================
# Clean Column Names
# ==========================================
df.columns = (
    df.columns.str.strip()
              .str.lower()
              .str.replace(" ", "_")
              .str.replace(r"[()]", "", regex=True)
)

# ==========================================
# Remove Exact Duplicate Rows
# ==========================================
df.drop_duplicates(inplace=True)

# ==========================================
# Remove Duplicate University-Year Records
# ==========================================
if "university_name" in df.columns and "year" in df.columns:
    df.drop_duplicates(
        subset=["university_name", "year"],
        inplace=True
    )

# ==========================================
# Standardize University Names
# ==========================================
name_map = {
    "Massachusetts Institute of Technology (MIT)":
        "Massachusetts Institute of Technology",
    "MIT":
        "Massachusetts Institute of Technology",

    "UC Berkeley":
        "University of California, Berkeley",

    "NUS":
        "National University of Singapore"
}

if "university_name" in df.columns:
    df["university_name"] = (
        df["university_name"]
        .replace(name_map)
        .str.strip()
    )

# ==========================================
# Standardize Country Names
# ==========================================
country_map = {
    "USA": "United States",
    "U.S.A.": "United States",
    "United States of America": "United States",

    "UK": "United Kingdom",

    "South Korea": "Korea, South",

    "Russian Federation": "Russia"
}

if "country" in df.columns:
    df["country"] = df["country"].replace(country_map)

if "country_the" in df.columns:

    df["country"] = df["country"].fillna(df["country_the"])

    df.drop(columns=["country_the"], inplace=True)

# ==========================================
# Clean Percentage Columns
# ==========================================
percentage_cols = [
    "female_percentage",
    "international_students_ratio_the",
    "international_student_ratio"
]

for col in percentage_cols:

    if col in df.columns:

        df[col] = (
            df[col]
            .astype(str)
            .str.replace("%", "", regex=False)
        )

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

# ==========================================
# Clean Ranking Columns
# ==========================================
rank_cols = [
    "world_rank",
    "world_rank_the"
]

for col in rank_cols:

    if col in df.columns:

        df[col] = (
            df[col]
            .astype(str)
            .str.replace("=", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.strip()
        )

        def convert_rank(x):

            if "-" in str(x):

                try:
                    a, b = x.split("-")
                    return (float(a) + float(b)) / 2
                except:
                    return np.nan

            if "+" in str(x):

                try:
                    return float(x.replace("+", ""))
                except:
                    return np.nan

            try:
                return float(x)
            except:
                return np.nan

        df[col] = df[col].apply(convert_rank)

# ==========================================
# Convert Numeric Columns
# ==========================================
numeric_cols = [
    "overall_score",
    "academic_reputation_score",
    "employer_reputation_score",
    "faculty_to_student_ratio",
    "citations_per_faculty_score",
    "international_faculty_score",
    "international_student_ratio",
    "international_research_network_score",
    "overall_score_the",
    "total_students",
    "faculty_student_ratio_the",
    "international_students_ratio_the",
    "female_percentage",
    "teaching",
    "research_environment_score",
    "research_quality_score",
    "industry",
    "international_outlook_score"
]

for col in numeric_cols:

    if col in df.columns:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

# ==========================================
# Fill Missing Values
# ==========================================

# Numeric -> Median
num_cols = df.select_dtypes(include=["number"]).columns

for col in num_cols:

    median = df[col].median()

    df[col] = df[col].fillna(median)

# Categorical -> Mode
cat_cols = df.select_dtypes(include=["object"]).columns

for col in cat_cols:

    mode = df[col].mode()

    if len(mode) > 0:
        df[col] = df[col].fillna(mode[0])
    else:
        df[col] = df[col].fillna("Unknown")

# ==========================================
# Remove Impossible Values
# ==========================================

if "world_rank" in df.columns:
    df = df[df["world_rank"] > 0]

if "world_rank_the" in df.columns:
    df = df[df["world_rank_the"] > 0]

# ==========================================
# Normalize Score Columns (0-100)
# ==========================================

score_cols = [
    "overall_score",
    "academic_reputation_score",
    "employer_reputation_score",
    "citations_per_faculty_score",
    "international_faculty_score",
    "international_student_ratio",
    "international_research_network_score",
    "overall_score_the",
    "teaching",
    "research_environment_score",
    "research_quality_score",
    "industry",
    "international_outlook_score"
]

for col in score_cols:

    if col in df.columns:

        mn = df[col].min()
        mx = df[col].max()

        if mx != mn:

            df[col] = (
                (df[col] - mn)
                / (mx - mn)
            ) * 100

# ==========================================
# Final Check
# ==========================================

print("\nFinal Shape :", df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicates :", df.duplicated().sum())

# ==========================================
# Save
# ==========================================

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nCleaning Completed Successfully!")
print("Saved :", OUTPUT_FILE)