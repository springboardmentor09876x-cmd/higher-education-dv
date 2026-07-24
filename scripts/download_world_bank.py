"""
World Bank API Data Downloader
Downloads maximum historical data for all 5 required indicators.
Saves raw JSON and converts to CSV.
"""

import json
import csv
import os
import time
import urllib.request
import urllib.error

BASE_URL = "https://api.worldbank.org/v2/country/all/indicator"
JSON_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "world_bank", "json")
CSV_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "world_bank", "csv")

INDICATORS = {
    "NY.GDP.PCAP.CD": {
        "name": "GDP per Capita",
        "csv_name": "world_bank_gdp_per_capita",
        "description": "GDP per capita (current US$)"
    },
    "SP.POP.TOTL": {
        "name": "Population",
        "csv_name": "world_bank_population",
        "description": "Population, total"
    },
    "SE.ADT.LITR.ZS": {
        "name": "Literacy Rate",
        "csv_name": "world_bank_literacy_rate",
        "description": "Literacy rate, adult total (% of people ages 15 and above)"
    },
    "SE.XPD.TOTL.GD.ZS": {
        "name": "Education Expenditure",
        "csv_name": "world_bank_education_expenditure",
        "description": "Government expenditure on education, total (% of GDP)"
    },
    "SE.TER.ENRR": {
        "name": "Tertiary Enrollment",
        "csv_name": "world_bank_tertiary_enrollment",
        "description": "School enrollment, tertiary (% gross)"
    }
}


def fetch_page(indicator_code, page, per_page=1000):
    """Fetch a single page from the World Bank API."""
    url = f"{BASE_URL}/{indicator_code}?format=json&per_page={per_page}&page={page}"
    req = urllib.request.Request(url, headers={"User-Agent": "EduVision-DV/1.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def download_indicator(indicator_code, config):
    """Download all pages for a single indicator."""
    print(f"  Downloading: {config['name']} ({indicator_code})")

    all_records = []
    page = 1
    total_pages = 1

    while page <= total_pages:
        try:
            data = fetch_page(indicator_code, page)
        except urllib.error.URLError as e:
            print(f"    ERROR on page {page}: {e}")
            break
        except Exception as e:
            print(f"    ERROR on page {page}: {e}")
            break

        if not isinstance(data, list) or len(data) < 2:
            print(f"    Unexpected response on page {page}")
            break

        metadata = data[0]
        records = data[1]

        total_pages = metadata.get("pages", 1)
        total_records = metadata.get("total", 0)

        if page == 1:
            print(f"    Total records in API: {total_records}, Pages: {total_pages}")

        if records:
            all_records.extend(records)

        print(f"    Page {page}/{total_pages} fetched ({len(records)} records)")
        page += 1
        time.sleep(0.3)

    print(f"    Total records collected: {len(all_records)}")
    return all_records


def save_json(indicator_code, config, records):
    """Save raw API records as JSON."""
    filepath = os.path.join(JSON_DIR, f"{config['csv_name']}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    print(f"    Saved JSON: {filepath}")
    return filepath


def convert_to_csv(indicator_code, config, records):
    """Convert records to CSV with project-required fields only."""
    filepath = os.path.join(CSV_DIR, f"{config['csv_name']}.csv")

    years_set = set()
    countries_set = set()
    null_count = 0
    row_count = 0

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["country_name", "country_iso3code", "year", "indicator_value"])

        for record in records:
            year = record.get("date", "")
            value = record.get("value")
            country_name = record.get("country", {}).get("value", "")
            country_iso3 = record.get("countryiso3code", "")

            if value is None:
                null_count += 1
                continue

            writer.writerow([country_name, country_iso3, year, value])
            years_set.add(year)
            countries_set.add(country_name)
            row_count += 1

    return {
        "filepath": filepath,
        "rows": row_count,
        "countries": len(countries_set),
        "year_range": f"{min(years_set)} - {max(years_set)}" if years_set else "N/A",
        "nulls": null_count
    }


def main():
    os.makedirs(JSON_DIR, exist_ok=True)
    os.makedirs(CSV_DIR, exist_ok=True)

    print("=" * 70)
    print("World Bank API Data Downloader")
    print("=" * 70)
    print(f"Indicators: {len(INDICATORS)}")
    print(f"JSON output: {JSON_DIR}")
    print(f"CSV output:  {CSV_DIR}")
    print()

    results = []

    for code, config in INDICATORS.items():
        print(f"[{config['name']}]")
        records = download_indicator(code, config)

        if records:
            save_json(code, config, records)
            csv_info = convert_to_csv(code, config, records)
            results.append({
                "name": config["name"],
                "code": code,
                **csv_info
            })
        else:
            print(f"    WARNING: No records downloaded for {config['name']}")
            results.append({
                "name": config["name"],
                "code": code,
                "rows": 0,
                "countries": 0,
                "year_range": "N/A",
                "nulls": 0
            })
        print()

    print("=" * 70)
    print("VALIDATION REPORT")
    print("=" * 70)
    print()
    print(f"{'Indicator':<25} {'Code':<18} {'Countries':<12} {'Year Range':<20} {'Rows':<8} {'Nulls':<8}")
    print("-" * 95)
    for r in results:
        print(f"{r['name']:<25} {r['code']:<18} {r['countries']:<12} {r['year_range']:<20} {r['rows']:<8} {r['nulls']:<8}")
    print()

    total_rows = sum(r["rows"] for r in results)
    print(f"Total data rows across all indicators: {total_rows}")
    print("=" * 70)


if __name__ == "__main__":
    main()
