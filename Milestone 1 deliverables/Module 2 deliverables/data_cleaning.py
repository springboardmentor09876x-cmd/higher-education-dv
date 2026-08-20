"""
EduVision - Higher Education Dashboard
Module 2 : Data Cleaning & Transformation

Reads data/university_raw_data.csv (Module 1 output) and produces a
fully populated, analysis-ready dataset: standardized names/countries,
a real country->region lookup, parsed ratio/percentage fields, derived
KPIs, and no missing values anywhere in the output.

Author : Chandana P
"""

import re
from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

INPUT_FILE = DATA_DIR / "university_raw_data.csv"
OUTPUT_FILE = DATA_DIR / "university_cleaned.csv"

# Columns that come from sources we don't have raw files for yet
# (CWUR / Shanghai). They're 100% empty right now, so they're dropped
# instead of being carried around (and re-added automatically once
# those sources are ingested, since ensure_master_schema in
# data_collection.py will populate them).
EMPTY_SOURCE_COLUMNS = [
    "national_rank", "quality_of_education", "quality_of_faculty",
    "alumni_employment", "publications", "influence", "citations",
    "broad_impact", "patents", "alumni", "award", "hici", "ns", "pub", "pcp",
]

# Country name variants -> one canonical name
COUNTRY_ALIASES = {
    "china (mainland)": "China",
    "hong kong sar": "Hong Kong",
    "macau sar": "Macao",
    "czechia": "Czech Republic",
    "russian federation": "Russia",
    "iran, islamic republic of": "Iran",
    "syrian arab republic": "Syria",
    "brunei darussalam": "Brunei",
    "palestinian territory, occupied": "Palestine",
}

# Country -> region (continent-level grouping used across the plan's
# "Country Comparison" dashboard). Covers every country present in the
# QS / THE source files.
COUNTRY_REGION = {
    "Algeria": "Africa", "Egypt": "Africa", "Ethiopia": "Africa", "Ghana": "Africa",
    "Kenya": "Africa", "Libya": "Africa", "Mauritius": "Africa", "Morocco": "Africa",
    "Mozambique": "Africa", "Namibia": "Africa", "Nigeria": "Africa", "Rwanda": "Africa",
    "Senegal": "Africa", "South Africa": "Africa", "Sudan": "Africa", "Tanzania": "Africa",
    "Tunisia": "Africa", "Uganda": "Africa", "Zambia": "Africa", "Zimbabwe": "Africa",
    "Democratic Republic of the Congo": "Africa", "Botswana": "Africa",

    "Argentina": "Americas", "Bolivia": "Americas", "Brazil": "Americas", "Canada": "Americas",
    "Chile": "Americas", "Colombia": "Americas", "Costa Rica": "Americas", "Cuba": "Americas",
    "Dominican Republic": "Americas", "Ecuador": "Americas", "Guatemala": "Americas",
    "Honduras": "Americas", "Jamaica": "Americas", "Mexico": "Americas", "Panama": "Americas",
    "Paraguay": "Americas", "Peru": "Americas", "Puerto Rico": "Americas",
    "United States": "Americas", "Uruguay": "Americas", "Venezuela": "Americas",

    "Armenia": "Asia", "Azerbaijan": "Asia", "Bahrain": "Asia", "Bangladesh": "Asia",
    "Brunei": "Asia", "China": "Asia", "Georgia": "Asia", "Hong Kong": "Asia", "India": "Asia",
    "Indonesia": "Asia", "Iran": "Asia", "Iraq": "Asia", "Israel": "Asia", "Japan": "Asia",
    "Jordan": "Asia", "Kazakhstan": "Asia", "Kuwait": "Asia", "Kyrgyzstan": "Asia",
    "Lebanon": "Asia", "Macao": "Asia", "Malaysia": "Asia", "Mongolia": "Asia", "Nepal": "Asia",
    "Oman": "Asia", "Pakistan": "Asia", "Palestine": "Asia", "Philippines": "Asia",
    "Qatar": "Asia", "Saudi Arabia": "Asia", "Singapore": "Asia", "South Korea": "Asia",
    "Sri Lanka": "Asia", "Syria": "Asia", "Taiwan": "Asia", "Thailand": "Asia",
    "Turkey": "Asia", "United Arab Emirates": "Asia", "Uzbekistan": "Asia", "Vietnam": "Asia",
    "Yemen": "Asia",

    "Austria": "Europe", "Belarus": "Europe", "Belgium": "Europe",
    "Bosnia and Herzegovina": "Europe", "Bulgaria": "Europe", "Croatia": "Europe",
    "Cyprus": "Europe", "Czech Republic": "Europe", "Denmark": "Europe", "Estonia": "Europe",
    "Finland": "Europe", "France": "Europe", "Germany": "Europe", "Greece": "Europe",
    "Hungary": "Europe", "Iceland": "Europe", "Ireland": "Europe", "Italy": "Europe",
    "Kosovo": "Europe", "Latvia": "Europe", "Lithuania": "Europe", "Luxembourg": "Europe",
    "Malta": "Europe", "Montenegro": "Europe", "Netherlands": "Europe",
    "North Macedonia": "Europe", "Northern Cyprus": "Europe", "Norway": "Europe",
    "Poland": "Europe", "Portugal": "Europe", "Romania": "Europe", "Russia": "Europe",
    "Serbia": "Europe", "Slovakia": "Europe", "Slovenia": "Europe", "Spain": "Europe",
    "Sweden": "Europe", "Switzerland": "Europe", "Ukraine": "Europe",
    "United Kingdom": "Europe",

    "Australia": "Oceania", "Fiji": "Oceania", "New Zealand": "Oceania",
}


# ==========================================================
# HELPERS
# ==========================================================

def standardize_country(country):
    if pd.isna(country):
        return np.nan
    key = str(country).strip().lower()
    canonical = COUNTRY_ALIASES.get(key, str(country).strip())
    return canonical


def parse_ratio(value):
    """
    'female_male_ratio' arrives corrupted from the raw THE export
    (e.g. '46:54:00' instead of '46:54'). Extract the first two
    numeric parts and return (female_pct, male_pct) normalized to
    sum to 100.
    """

    if pd.isna(value):
        return np.nan, np.nan

    nums = re.findall(r"\d+(?:\.\d+)?", str(value))

    if len(nums) < 2:
        return np.nan, np.nan

    f, m = float(nums[0]), float(nums[1])
    total = f + m

    if total == 0:
        return np.nan, np.nan

    return round(f / total * 100, 1), round(m / total * 100, 1)


def parse_percentage(value):
    if pd.isna(value):
        return np.nan
    match = re.search(r"[\d.]+", str(value))
    return float(match.group()) if match else np.nan


def group_fillna(df, column, group_cols):
    """
    Fill missing numeric values with the median for their
    (source, region) group, falling back to the overall column
    median, falling back to 0.
    """

    overall_median = df[column].median()

    df[column] = df.groupby(group_cols)[column].transform(
        lambda s: s.fillna(s.median())
    )

    df[column] = df[column].fillna(overall_median)
    df[column] = df[column].fillna(0)

    return df[column]


# ==========================================================
# PIPELINE
# ==========================================================

def load_raw():
    print(f"Reading {INPUT_FILE.name}")
    return pd.read_csv(INPUT_FILE, low_memory=False)


def drop_empty_columns(df):
    print("Dropping columns with no data from any current source...")
    return df.drop(columns=[c for c in EMPTY_SOURCE_COLUMNS if c in df.columns])


def clean_identity_fields(df):
    print("Cleaning names, countries, removing duplicates...")

    df["university_name"] = df["university_name"].astype(str).str.strip()
    df["country"] = df["country"].apply(standardize_country)
    df["overall_score"] = pd.to_numeric(df["overall_score"], errors="coerce")

    # Drop rows with no usable identity or headline score
    df = df.dropna(subset=["university_name", "country", "overall_score"])
    df = df[df["university_name"].str.lower() != "nan"]

    # Remove exact duplicate (university, year, source) rows
    df = df.drop_duplicates(subset=["university_name", "country", "year", "source"])

    return df.reset_index(drop=True)


def fill_region(df):
    print("Filling region from country lookup table...")
    df["region"] = df["country"].map(COUNTRY_REGION).fillna("Other")
    return df


def parse_ratios_and_percentages(df):
    print("Parsing gender ratio and international-student percentages...")

    ratios = df["female_male_ratio"].apply(parse_ratio)
    df["female_percentage"] = [r[0] for r in ratios]
    df["male_percentage"] = [r[1] for r in ratios]

    df["international_students_pct"] = df["international_students"].apply(parse_percentage)

    # QS doesn't publish a literal international-student percentage,
    # but it does publish an International Students Score (0-100)
    # from the same underlying concept - use it for QS rows so the
    # column is populated for every source rather than mixing two
    # different units silently.
    qs_mask = df["source"] == "QS"
    df.loc[qs_mask, "international_students_pct"] = df.loc[qs_mask, "international_students_pct"].fillna(
        df.loc[qs_mask, "international_students_score"]
    )

    return df


def impute_missing_scores(df):
    print("Imputing missing metrics using source/region medians...")

    numeric_cols = [
        "academic_reputation_score", "employer_reputation_score", "faculty_student_score",
        "citations_per_faculty_score", "international_faculty_score",
        "international_students_score", "international_research_network_score",
        "employment_outcomes_score", "sustainability_score",
        "teaching_score", "research_score", "research_quality", "industry_impact",
        "international_outlook", "student_population", "student_staff_ratio",
        "international_students_pct", "female_percentage", "male_percentage",
        "overall_score",
    ]

    for col in numeric_cols:
        if col in df.columns:
            # Several of these arrive as text (e.g. "11074.0") because
            # the raw CSV mixes numeric and non-numeric rows; coerce
            # to proper floats before computing medians.
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df[col] = group_fillna(df, col, ["source", "region"])

    return df


def add_kpis(df):
    print("Engineering education KPIs...")

    # Global Ranking Score: normalize rank to 0-100 within each
    # source's own scale, since QS (~1500 institutions) and THE
    # (~2200 institutions) use different rank ranges.
    df["world_rank"] = pd.to_numeric(df["world_rank"], errors="coerce")
    max_rank = df.groupby("source")["world_rank"].transform("max")
    df["global_ranking_score"] = (100 * (1 - (df["world_rank"] - 1) / (max_rank - 1))).round(1)

    # Research Impact Score: blend of the research-related metrics
    # each source publishes (already imputed above so both sources
    # have values in every one of these columns).
    df["research_impact_score"] = df[
        ["research_score", "research_quality", "citations_per_faculty_score"]
    ].mean(axis=1).round(1)

    # Faculty-to-Student Score: QS publishes a 0-100 Faculty/Student
    # score directly; THE publishes a literal students-per-staff
    # ratio (lower is better). Convert the THE ratio onto the same
    # 0-100 scale (capped at a ratio of 30:1) so both sources are
    # comparable in one column.
    ratio_score = (100 * (1 - (df["student_staff_ratio"].clip(upper=30) / 30))).round(1)
    df["faculty_student_ratio_score"] = df["faculty_student_score"].where(
        df["source"] == "QS", ratio_score
    )

    # Academic Reputation Score: QS metric as-is; already imputed
    # for THE rows via the regional median in impute_missing_scores.
    df["academic_reputation_index"] = df["academic_reputation_score"].round(1)

    # Research Productivity Index: composite score combining research
    # impact, citation performance and overall standing.
    df["research_productivity_index"] = (
        0.5 * df["research_impact_score"]
        + 0.3 * df["citations_per_faculty_score"]
        + 0.2 * df["overall_score"]
    ).round(1)

    return df


def finalize(df):
    print("Final pass: guaranteeing no missing values remain...")

    for col in df.select_dtypes(include=["number"]).columns:
        df[col] = df[col].fillna(df[col].median())
        df[col] = df[col].fillna(0)

    for col in df.select_dtypes(exclude=["number"]).columns:
        df[col] = df[col].fillna("Unknown")

    df["year"] = df["year"].astype(int)
    df["world_rank"] = df["world_rank"].astype(int)

    ordered_cols = [c for c in df.columns if c != "university_id"]
    df = df[["university_id"] + ordered_cols]

    return df


def main():
    print("=" * 60)
    print("EduVision - Data Cleaning & KPI Engineering Pipeline")
    print("=" * 60)

    df = load_raw()
    df = drop_empty_columns(df)
    df = clean_identity_fields(df)
    df = fill_region(df)
    df = parse_ratios_and_percentages(df)
    df = impute_missing_scores(df)
    df = add_kpis(df)
    df = finalize(df)

    assert df.isna().sum().sum() == 0, "Missing values remain after cleaning!"

    df.to_csv(OUTPUT_FILE, index=False)

    print("\n" + "=" * 60)
    print("DATA CLEANING COMPLETED SUCCESSFULLY")
    print("=" * 60)
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")
    print(f"Missing values remaining : {df.isna().sum().sum()}")
    print(f"\nSaved To:\n{OUTPUT_FILE}")

    return df


if __name__ == "__main__":
    main()
