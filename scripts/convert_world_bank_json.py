"""
World Bank JSON to CSV Converter
Converts World Bank API JSON responses to clean CSV files containing only project-required fields.

Required fields (per project requirements):
  - country_name:     Country name for joining with university data
  - country_iso3code: Standardized ISO3 country code
  - year:             Analysis period (2020-2024)
  - indicator_value:  The actual metric value

NOT needed (metadata/always empty in these files):
  - indicator.id, indicator.value (redundant - each file = one indicator)
  - unit (always empty)
  - obs_status (always empty)
  - decimal (display formatting only)
"""

import json
import csv
import os

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
YEARS = ["2020", "2021", "2022", "2023", "2024"]

# Map filenames to their output CSV names and indicator descriptions
INDICATORS = {
    "world_bank_gdp_per_capita.json": {
        "csv": "world_bank_gdp_per_capita.csv",
        "description": "GDP per capita (current US$)"
    },
    "world_bank_education_expenditure.json": {
        "csv": "world_bank_education_expenditure.csv",
        "description": "Government expenditure on education, total (% of GDP)"
    },
    "world_bank_literacy_rate.json": {
        "csv": "world_bank_literacy_rate.csv",
        "description": "Literacy rate, adult total (% of people ages 15 and above)"
    },
    "world_bank_population.json": {
        "csv": "world_bank_population.csv",
        "description": "Population, total"
    },
    "world_bank_tertiary_enrollment.json": {
        "csv": "world_bank_tertiary_enrollment.csv",
        "description": "School enrollment, tertiary (% gross)"
    }
}


def convert_json_to_csv(json_filename, config):
    """Convert a single World Bank JSON file to a project-required CSV."""
    json_path = os.path.join(RAW_DIR, json_filename)
    csv_path = os.path.join(RAW_DIR, config["csv"])

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # World Bank API returns [metadata, [records]]
    records = data[1]

    converted = 0
    skipped_year = 0
    skipped_null = 0

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["country_name", "country_iso3code", "year", "indicator_value"])

        for record in records:
            year = record["date"]
            value = record["value"]

            # Filter to project analysis period (2020-2024)
            if year not in YEARS:
                skipped_year += 1
                continue

            # Skip records with null values
            if value is None:
                skipped_null += 1
                continue

            writer.writerow([
                record["country"]["value"],   # country_name
                record["countryiso3code"],    # country_iso3code
                year,                         # year
                value                         # indicator_value
            ])
            converted += 1

    print(f"  {config['csv']}")
    print(f"    Records written:  {converted}")
    print(f"    Skipped (year):   {skipped_year}")
    print(f"    Skipped (null):   {skipped_null}")
    return converted


def main():
    print("=" * 60)
    print("World Bank JSON to CSV Conversion")
    print("=" * 60)
    print(f"Analysis period: {YEARS[0]}–{YEARS[-1]}")
    print(f"Source: {RAW_DIR}")
    print()

    total = 0
    for json_file, config in INDICATORS.items():
        print(f"Converting: {json_file}")
        count = convert_json_to_csv(json_file, config)
        total += count
        print()

    print("=" * 60)
    print(f"Total records across all indicators: {total}")
    print("=" * 60)


if __name__ == "__main__":
    main()
