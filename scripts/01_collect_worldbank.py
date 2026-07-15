"""
Project : EduVision - Higher Education Analytics Dashboard
Script  : 01_collect_worldbank.py

Description:
This script downloads official country-level indicators from the World Bank API.
The generated dataset will be used as the raw input for country comparison,
KPI engineering, and dashboard development.

Data Source:
https://api.worldbank.org/

Output:
data/raw/worldbank_indicators_raw.csv

Author:
Ishita Tiwari
"""


# IMPORT LIBRARIES


import logging
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry



# PROJECT CONFIGURATION


START_YEAR = 2020
END_YEAR = 2024

OUTPUT_PATH = Path("data/raw/worldbank_indicators_raw.csv")
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)


# World Bank indicators required for the project
INDICATORS = {
    "NY.GDP.PCAP.CD": "gdp_per_capita_usd",
    "SE.XPD.TOTL.GD.ZS": "education_expenditure_pct_gdp",
    "SE.TER.ENRR": "tertiary_enrollment_ratio",
    "SP.POP.TOTL": "population",
    "SE.ADT.LITR.ZS": "literacy_rate_pct",
}


# Regional aggregates are excluded because the dashboard compares countries,
# not groups of countries.
EXCLUDED_COUNTRIES = {
    "",
    "World",
    "High income",
    "Low income",
    "Lower middle income",
    "Upper middle income",
    "OECD members",
    "European Union",
    "Arab World",
    "East Asia & Pacific",
    "Europe & Central Asia",
    "Latin America & Caribbean",
    "Middle East & North Africa",
    "North America",
    "South Asia",
    "Sub-Saharan Africa",
}


# LOGGING

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


# API SESSION


# Reuse a single session for all requests. This improves performance and
# automatically retries temporary network failures.

session = requests.Session()

session.headers.update(
    {
        "User-Agent": "EduVision-Higher-Education-Analytics/1.0"
    }
)

retry_strategy = Retry(
    total=3,
    connect=3,
    read=3,
    backoff_factor=1.5,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"],
)

adapter = HTTPAdapter(max_retries=retry_strategy)

session.mount("https://", adapter)
session.mount("http://", adapter)

# FUNCTIONS

def fetch_indicator(indicator_code: str, column_name: str) -> pd.DataFrame:
    """
    Download a single indicator from the World Bank API and return it
    as a DataFrame.
    """

    url = f"https://api.worldbank.org/v2/country/all/indicator/{indicator_code}"

    params = {
        "format": "json",
        "per_page": 20000,
        "date": f"{START_YEAR}:{END_YEAR}",
    }

    logger.info(f"Downloading: {column_name}")

    try:
        response = session.get(
            url=url,
            params=params,
            timeout=120,
        )

        response.raise_for_status()

    except requests.exceptions.RequestException as error:
        logger.error(f"Failed to download {column_name}")
        logger.error(error)
        return pd.DataFrame(
            columns=[
                "country_code",
                "country_name",
                "year",
                column_name,
            ]
        )

    data = response.json()

    if len(data) < 2 or data[1] is None:
        logger.warning(f"No records found for {column_name}")

        return pd.DataFrame(
            columns=[
                "country_code",
                "country_name",
                "year",
                column_name,
            ]
        )

    rows = []

    for record in data[1]:

        rows.append(
            {
                "country_code": record.get("countryiso3code"),
                "country_name": record["country"]["value"],
                "year": int(record["date"]),
                column_name: record.get("value"),
            }
        )

    df = pd.DataFrame(rows)

    logger.info(f"{len(df):,} records collected.")

    return df


def merge_indicators(dataframes: list[pd.DataFrame]) -> pd.DataFrame:
    """
    Merge all indicator datasets into a single country-year dataset.
    """

    merged = dataframes[0]

    for df in dataframes[1:]:

        merged = merged.merge(
            df.drop(columns=["country_name"]),
            on=["country_code", "year"],
            how="outer",
        )

    return merged


def remove_aggregates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Keep only individual countries.
    """

    df = df[
        (~df["country_name"].isin(EXCLUDED_COUNTRIES))
        &
        (df["country_code"].notna())
        &
        (df["country_code"] != "")
    ]

    return df.reset_index(drop=True)


def add_metadata(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add metadata that helps track dataset provenance.
    """

    df["data_source"] = "World Bank API"

    df["download_timestamp_utc"] = (
        datetime.now(timezone.utc)
        .strftime("%Y-%m-%d %H:%M:%S UTC")
    )

    return df


def validate_dataset(df: pd.DataFrame) -> None:
    """
    Display a simple validation summary before saving.
    """

    duplicates = df.duplicated(
        subset=["country_code", "year"]
    ).sum()

    logger.info("=" * 60)
    logger.info("DATA VALIDATION SUMMARY")
    logger.info("=" * 60)

    logger.info(f"Countries           : {df['country_code'].nunique()}")
    logger.info(f"Years               : {START_YEAR}-{END_YEAR}")
    logger.info(f"Rows                : {len(df):,}")
    logger.info(f"Duplicate Records   : {duplicates}")

    logger.info("\nMissing Values")

    missing = df.isnull().sum()

    for column, value in missing.items():
        logger.info(f"{column:<35}: {value}")
# MAIN

def main():

    start_time = datetime.now()

    logger.info("=" * 60)
    logger.info("WORLD BANK DATA COLLECTION STARTED")
    logger.info("=" * 60)

    
    # Download all required indicators
    

    indicator_data = []

    for indicator_code, column_name in INDICATORS.items():

        df = fetch_indicator(indicator_code, column_name)
        indicator_data.append(df)

    
    # Merge all indicators


    logger.info("Merging indicator datasets...")

    merged = merge_indicators(indicator_data)


    # Keep only valid countries
    

    logger.info("Removing aggregate regions...")

    merged = remove_aggregates(merged)

    
    # Sort records for consistency
    

    merged = (
        merged
        .sort_values(["country_name", "year"])
        .reset_index(drop=True)
    )

    
    # Add metadata
    

    merged = add_metadata(merged)

    
    # Validate dataset
    

    validate_dataset(merged)

    
    # Save dataset


    merged.to_csv(
        OUTPUT_PATH,
        index=False,
        encoding="utf-8-sig",
    )

    logger.info("")
    logger.info("Dataset saved successfully.")
    logger.info(f"Location : {OUTPUT_PATH}")

    execution_time = datetime.now() - start_time

    logger.info(f"Execution Time : {execution_time}")

    logger.info("=" * 60)
    logger.info("WORLD BANK DATA COLLECTION COMPLETED")
    logger.info("=" * 60)


# RUN SCRIPT

if __name__ == "__main__":
    main()