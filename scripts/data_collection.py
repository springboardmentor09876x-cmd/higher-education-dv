"""
EduVision - Higher Education Dashboard
Module 1 : Data Collection & Integration

Author : Chandana P
"""

from pathlib import Path
import pandas as pd
import numpy as np
import uuid

# ==========================================================
# PROJECT PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[1]

RAW_DIR = BASE_DIR / "data" / "raw"

PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = PROCESSED_DIR / "university_raw_data.csv"

# ==========================================================
# MASTER SCHEMA
# ==========================================================

MASTER_COLUMNS = [

    # ---------- Identification ----------
    "university_id",
    "university_name",
    "country",
    "region",

    # ---------- Ranking ----------
    "world_rank",
    "national_rank",
    "overall_score",
    "year",
    "source",

    # ---------- QS ----------
    "academic_reputation_score",
    "employer_reputation_score",
    "faculty_student_score",
    "citations_per_faculty_score",
    "international_faculty_score",
    "international_students_score",
    "international_research_network_score",
    "employment_outcomes_score",
    "sustainability_score",

    # ---------- THE ----------
    "teaching_score",
    "research_score",
    "research_quality",
    "industry_impact",
    "international_outlook",

    # ---------- CWUR ----------
    "quality_of_education",
    "quality_of_faculty",
    "alumni_employment",
    "publications",
    "influence",
    "citations",
    "broad_impact",
    "patents",

    # ---------- Student ----------
    "student_population",
    "student_staff_ratio",
    "international_students",
    "female_male_ratio",

    # ---------- Shanghai ----------
    "alumni",
    "award",
    "hici",
    "ns",
    "pub",
    "pcp"

]

# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def read_dataset(filepath):
    """
    Reads CSV using multiple encodings.
    """

    encodings = [
        "utf-8",
        "latin1",
        "cp1252"
    ]

    for encoding in encodings:

        try:

            print(f"Reading {filepath.name} ({encoding})")

            return pd.read_csv(filepath, encoding=encoding)

        except UnicodeDecodeError:

            continue

    raise Exception(f"Unable to read {filepath.name}")


def clean_columns(df):
    """
    Standardize column names.
    """

    df.columns = (

        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        .str.replace("/", "_")

    )

    return df


def create_master_dataframe():

    """
    Creates empty dataframe with master schema.
    """

    return pd.DataFrame(columns=MASTER_COLUMNS)


def generate_ids(df):
    """
    Generate unique university IDs.
    """

    df["university_id"] = [

        str(uuid.uuid4())[:8]

        for _ in range(len(df))

    ]

    return df


def ensure_master_schema(df):
    """
    Adds missing columns from master schema.
    """

    for column in MASTER_COLUMNS:

        if column not in df.columns:

            df[column] = np.nan

    return df[MASTER_COLUMNS]


# ==========================================================
# DATASET MAPPING FUNCTIONS
# (Part 2 onwards)
# ==========================================================
def map_qs():
    """
    Maps QS Rankings dataset to the master schema.
    """

    print("\nProcessing QS Rankings...")

    qs = read_dataset(RAW_DIR / "qs_rankings_2025.csv")
    qs = clean_columns(qs)

    qs = qs.rename(columns={
        "institution_name": "university_name",
        "location": "country",
        "rank_2025": "world_rank",
        "overall_score": "overall_score",
        "academic_reputation_score": "academic_reputation_score",
        "employer_reputation_score": "employer_reputation_score",
        "faculty_student_score": "faculty_student_score",
        "citations_per_faculty_score": "citations_per_faculty_score",
        "international_faculty_score": "international_faculty_score",
        "international_students_score": "international_students_score",
        "international_research_network_score": "international_research_network_score",
        "employment_outcomes_score": "employment_outcomes_score",
        "sustainability_score": "sustainability_score"
    })

    qs["year"] = 2025
    qs["source"] = "QS"

    # QS doesn't have national rank
    qs["national_rank"] = np.nan

    # Keep region if available
    if "region" not in qs.columns:
        qs["region"] = np.nan

    qs = ensure_master_schema(qs)

    print(f"QS Records : {len(qs)}")

    return qs
def map_the():
    """
    Maps Times Higher Education dataset to the master schema.
    """

    print("\nProcessing THE Rankings...")

    the = read_dataset(RAW_DIR / "THE World University Rankings 2016-2026.csv")
    the = clean_columns(the)

    the = the.rename(columns={
        "name": "university_name",
        "country": "country",
        "rank": "world_rank",
        "overall_score": "overall_score",
        "teaching": "teaching_score",
        "research_environment": "research_score",
        "research_quality": "research_quality",
        "industry_impact": "industry_impact",
        "international_outlook": "international_outlook",
        "student_population": "student_population",
        "students_to_staff_ratio": "student_staff_ratio",
        "international_students": "international_students",
        "female_to_male_ratio": "female_male_ratio",
        "year": "year"
    })

    the["source"] = "THE"
    the["national_rank"] = np.nan
    the["region"] = np.nan

    the = ensure_master_schema(the)

    print(f"THE Records : {len(the)}")

    return the

def map_times():
    """
    Maps Times World University Rankings dataset to the master schema.
    """

    print("\nProcessing Times Rankings...")

    times = read_dataset(RAW_DIR / "timesData.csv")
    times = clean_columns(times)

    times = times.rename(columns={
        "university_name": "university_name",
        "country": "country",
        "world_rank": "world_rank",
        "total_score": "overall_score",
        "teaching": "teaching_score",
        "research": "research_score",
        "international": "international_outlook",
        "citations": "citations",
        "num_students": "student_population",
        "student_staff_ratio": "student_staff_ratio",
        "international_students": "international_students",
        "female_male_ratio": "female_male_ratio",
        "year": "year"
    })

    times["source"] = "Times"
    times["national_rank"] = np.nan
    times["region"] = np.nan

    times = ensure_master_schema(times)

    print(f"Times Records : {len(times)}")

    return times

def map_shanghai():
    """
    Maps Shanghai Ranking dataset to the master schema.
    """

    print("\nProcessing Shanghai Rankings...")

    shanghai = read_dataset(RAW_DIR / "shanghaiData.csv")
    shanghai = clean_columns(shanghai)

    shanghai = shanghai.rename(columns={
        "university_name": "university_name",
        "world_rank": "world_rank",
        "national_rank": "national_rank",
        "total_score": "overall_score",
        "alumni": "alumni",
        "award": "award",
        "hici": "hici",
        "ns": "ns",
        "pub": "pub",
        "pcp": "pcp",
        "year": "year"
    })

    # Add country using mapping file
    mapping = read_dataset(RAW_DIR / "school_and_country_table.csv")
    mapping = clean_columns(mapping)

    mapping = mapping.rename(columns={
        "school_name": "university_name"
    })

    shanghai = shanghai.merge(
        mapping,
        on="university_name",
        how="left"
    )

    shanghai["source"] = "Shanghai"
    shanghai["region"] = np.nan

    shanghai = ensure_master_schema(shanghai)

    print(f"Shanghai Records : {len(shanghai)}")

    return shanghai

def map_cwur():
    """
    Maps CWUR dataset to the master schema.
    """

    print("\nProcessing CWUR Rankings...")

    cwur = read_dataset(RAW_DIR / "cwurData.csv")
    cwur = clean_columns(cwur)

    cwur = cwur.rename(columns={
        "institution": "university_name",
        "country": "country",
        "world_rank": "world_rank",
        "national_rank": "national_rank",
        "score": "overall_score",
        "quality_of_education": "quality_of_education",
        "alumni_employment": "alumni_employment",
        "quality_of_faculty": "quality_of_faculty",
        "publications": "publications",
        "influence": "influence",
        "citations": "citations",
        "broad_impact": "broad_impact",
        "patents": "patents",
        "year": "year"
    })

    cwur["source"] = "CWUR"
    cwur["region"] = np.nan

    cwur = ensure_master_schema(cwur)

    print(f"CWUR Records : {len(cwur)}")

    return cwur

def create_merge_key(df):

    df["merge_key"] = (

        df["university_name"]
        .astype(str)
        .str.lower()
        .str.strip()
        .str.replace("&", "and", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False)

    )

    if "country" in df.columns:

        df["merge_key"] = (
            df["merge_key"] + "_" +
            df["country"].fillna("").astype(str).str.lower()
        )

    return df

def consolidate_columns(df):
    """
    Combine duplicate columns created after merging.
    """

    base_columns = [
        "university_name",
        "country",
        "region",
        "world_rank",
        "national_rank",
        "overall_score",
        "year",
        "source",

        "academic_reputation_score",
        "employer_reputation_score",
        "faculty_student_score",
        "citations_per_faculty_score",
        "international_faculty_score",
        "international_students_score",
        "international_research_network_score",
        "employment_outcomes_score",
        "sustainability_score",

        "teaching_score",
        "research_score",
        "research_quality",
        "industry_impact",
        "international_outlook",

        "quality_of_education",
        "quality_of_faculty",
        "alumni_employment",
        "publications",
        "influence",
        "citations",
        "broad_impact",
        "patents",

        "student_population",
        "student_staff_ratio",
        "international_students",
        "female_male_ratio",

        "alumni",
        "award",
        "hici",
        "ns",
        "pub",
        "pcp"
    ]

    suffixes = [
        "_the",
        "_cwur",
        "_times",
        "_sh"
    ]

    for col in base_columns:

        for suf in suffixes:

            dup = col + suf

            if dup in df.columns:

                df[col] = df[col].combine_first(df[dup])

                df.drop(columns=dup, inplace=True)

    return df

# ==========================================================
# MAIN ETL PIPELINE
# ==========================================================

def main():

    print("\nLoading datasets...")

    qs = map_qs()
    the = map_the()
    cwur = map_cwur()
    times = map_times()
    shanghai = map_shanghai()
    qs = create_merge_key(qs)
    the = create_merge_key(the)
    cwur = create_merge_key(cwur)
    times = create_merge_key(times)
    shanghai = create_merge_key(shanghai)
    print("\nMerging QS + THE")

    master = qs.merge(
        the,
        on="merge_key",
        how="outer",
        suffixes=("", "_the")
    )
    print("Merging CWUR")

    master = master.merge(
        cwur,
        on="merge_key",
        how="outer",
        suffixes=("", "_cwur")
    )
    print("Merging Times")

    master = master.merge(
        times,
        on="merge_key",
        how="outer",
        suffixes=("", "_times")
    )
    print("Merging Shanghai")
    master = master.merge(
    shanghai,
    on="merge_key",
    how="outer",
    suffixes=("", "_sh")
    )
    print("\nConsolidating duplicate columns...")

    master = consolidate_columns(master)

    master.drop(columns=["merge_key"], inplace=True, errors="ignore")

    master = master.merge(
        shanghai,
        on="merge_key",
        how="outer",
        suffixes=("", "_sh")
    )

# ==========================================================
# DRIVER
# ==========================================================

if __name__ == "__main__":

    main()