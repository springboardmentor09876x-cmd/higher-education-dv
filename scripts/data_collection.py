"""
Project : Higher Education Data Visualization
Script  : data_collection.py

Description:
This script combines the cleaned QS, THE, OpenAlex and
World Bank datasets into one final analytical dataset.

Output:
data/university_cleaned.csv

Author:
Ishita Tiwari
"""

from pathlib import Path
import logging
import pandas as pd


# Project paths
BASE = Path(__file__).resolve().parents[1]

DATA = BASE / "data"
PROCESSED = DATA / "processed"
RAW = DATA / "university_raw_data"

OUTPUT = DATA / "university_cleaned.csv"


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def show_shape(name, df):
    logger.info(f"{name:<15}: {df.shape[0]:,} rows × {df.shape[1]} columns")


logger.info("Loading datasets...")


# Load datasets
qs = pd.read_csv(PROCESSED / "qs_master_clean.csv")
the = pd.read_csv(RAW / "the_master.csv")
openalex = pd.read_csv(RAW / "openalex_master.csv")
worldbank = pd.read_csv(RAW / "worldbank_indicators_raw.csv")


show_shape("QS", qs)
show_shape("THE", the)
show_shape("OpenAlex", openalex)
show_shape("World Bank", worldbank)


# Keep required THE columns
the = the[
    [
        "university_id",
        "year",
        "scores_overall",
        "scores_teaching",
        "scores_research",
        "scores_citations",
        "scores_industry_income",
        "scores_international_outlook",
        "stats_number_students",
        "stats_student_staff_ratio",
        "stats_pc_intl_students",
        "stats_female_male_ratio",
    ]
]


# Keep required OpenAlex columns
openalex = openalex[
    [
        "university_id",
        "institution_id",
        "works_count",
        "cited_by_count",
        "h_index",
        "i10_index",
        "2yr_mean_citedness",
    ]
]


# Keep required World Bank columns
worldbank = worldbank[
    [
        "country_name",
        "year",
        "gdp_per_capita_usd",
        "education_expenditure_pct_gdp",
        "tertiary_enrollment_ratio",
        "population",
        "literacy_rate_pct",
    ]
]


# Standardize country names before merging
country_map = {
    "China (Mainland)": "China",
    "Hong Kong SAR": "Hong Kong SAR, China",
    "Macau SAR": "Macao SAR, China",
    "South Korea": "Korea, Rep.",
    "Iran, Islamic Republic of": "Iran, Islamic Rep.",
    "Russia": "Russian Federation",
    "Turkey": "Turkiye",
    "Vietnam": "Viet Nam",
    "Slovakia": "Slovak Republic",
    "Czech Republic": "Czechia",
    "Egypt": "Egypt, Arab Rep.",
    "Brunei": "Brunei Darussalam",
    "Venezuela": "Venezuela, RB",
    "Kyrgyzstan": "Kyrgyz Republic",
    "Palestinian Territory, Occupied": "West Bank and Gaza",
    "Taiwan": "Taiwan, China",
}

qs["country"] = qs["country"].replace(country_map)


# Merge THE
logger.info("Merging THE dataset...")

master = qs.merge(
    the,
    on=["university_id", "year"],
    how="left",
)

show_shape("After THE", master)


# Merge OpenAlex
logger.info("Merging OpenAlex dataset...")

master = master.merge(
    openalex,
    on="university_id",
    how="left",
)

show_shape("After OpenAlex", master)


# Merge World Bank
logger.info("Merging World Bank dataset...")

master = master.merge(
    worldbank,
    left_on=["country", "year"],
    right_on=["country_name", "year"],
    how="left",
)

master.drop(columns=["country_name"], inplace=True)

show_shape("Final Dataset", master)


# Save final dataset
master.to_csv(
    OUTPUT,
    index=False,
)

logger.info("=" * 60)
logger.info("University cleaned dataset created successfully.")
logger.info(f"Rows    : {len(master):,}")
logger.info(f"Columns : {master.shape[1]}")
logger.info(f"Saved   : {OUTPUT}")
logger.info("=" * 60)