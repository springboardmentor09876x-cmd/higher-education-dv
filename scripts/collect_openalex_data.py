"""
OpenAlex Research Data Collection Script
EduVision_DV - Phase 1 Data Acquisition

This script queries the OpenAlex API to collect institution-level research data
for universities in the QS and THE ranking datasets.

Output: data/raw/openalex_research_data.json
"""

import json
import time
import requests
import pandas as pd
from pathlib import Path
from typing import Dict, List, Optional


# Configuration
BASE_URL = "https://api.openalex.org"
HEADERS = {"Accept": "application/json"}
RATE_LIMIT_DELAY = 0.5  # 500ms between requests (respecting free tier)

# Output file
OUTPUT_FILE = Path("data/raw/openalex_research_data.json")


def load_university_names() -> List[str]:
    """Load unique university names from QS and THE datasets."""
    universities = set()
    
    # Load from QS datasets
    qs_files = [
        "data/raw/qs_rankings_2020.csv",
        "data/raw/qs_rankings_2021.csv",
        "data/raw/qs_rankings_2022.csv",
        "data/raw/qs_rankings_2023.csv",
        "data/raw/qs_rankings_2024.csv",
    ]
    
    # QS column names vary by year
    qs_name_columns = {
        "data/raw/qs_rankings_2020.csv": "Institution Name",
        "data/raw/qs_rankings_2021.csv": "institution name",
        "data/raw/qs_rankings_2022.csv": "University",
        "data/raw/qs_rankings_2023.csv": "institution",
        "data/raw/qs_rankings_2024.csv": "institution",
    }
    
    for file_path in qs_files:
        try:
            # Try different encodings
            for encoding in ['utf-8', 'latin-1', 'cp1252']:
                try:
                    # Handle QS 2024 semicolon delimiter and multiple headers
                    if '2024' in file_path:
                        df = pd.read_csv(file_path, encoding=encoding, sep=';', skiprows=3)
                    else:
                        df = pd.read_csv(file_path, encoding=encoding)
                    col_name = qs_name_columns.get(file_path)
                    if col_name and col_name in df.columns:
                        names = df[col_name].dropna().str.strip().tolist()
                        universities.update(names)
                    break
                except UnicodeDecodeError:
                    continue
        except Exception as e:
            print(f"Warning: Could not read {file_path}: {e}")
    
    # Load from THE datasets
    the_files = [
        "data/raw/the_rankings_2020.csv",
        "data/raw/the_rankings_2021.csv",
        "data/raw/the_rankings_2022.csv",
        "data/raw/the_rankings_2023.csv",
        "data/raw/the_rankings_2024.csv",
    ]
    
    for file_path in the_files:
        try:
            df = pd.read_csv(file_path)
            if "Name" in df.columns:
                names = df["Name"].dropna().str.strip().tolist()
                universities.update(names)
        except Exception as e:
            print(f"Warning: Could not read {file_path}: {e}")
    
    return sorted(list(universities))


def search_institution(name: str, max_retries: int = 3) -> Optional[Dict]:
    """Search for an institution in OpenAlex by name with retry logic."""
    url = f"{BASE_URL}/institutions"
    params = {"search": name, "per_page": 1}
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=HEADERS, params=params, timeout=10)
            
            # Handle rate limiting
            if response.status_code == 429:
                wait_time = (attempt + 1) * 2  # Exponential backoff: 2, 4, 6 seconds
                print(f"  Rate limited. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                continue
            
            response.raise_for_status()
            data = response.json()
            
            if data.get("results") and len(data["results"]) > 0:
                return data["results"][0]
            return None
            
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                time.sleep(1)
            else:
                try:
                    print(f"  Error searching: {e}")
                except UnicodeEncodeError:
                    print(f"  Error searching (unicode)")
    
    return None


def extract_research_data(institution: Dict, search_name: str) -> Dict:
    """Extract research metrics from OpenAlex institution data."""
    # Extract yearly counts
    counts_by_year = institution.get("counts_by_year", [])
    yearly_data = {}
    
    for year_data in counts_by_year:
        year = year_data.get("year")
        if year and 2020 <= year <= 2024:
            yearly_data[year] = {
                "works_count": year_data.get("works_count", 0),
                "cited_by_count": year_data.get("cited_by_count", 0),
                "oa_works_count": year_data.get("oa_works_count", 0),
            }
    
    # Extract summary stats
    summary_stats = institution.get("summary_stats", {})
    
    return {
        "search_name": search_name,
        "openalex_id": institution.get("id", ""),
        "display_name": institution.get("display_name", ""),
        "country_code": institution.get("country_code", ""),
        "type": institution.get("type", ""),
        "works_count_total": institution.get("works_count", 0),
        "cited_by_count_total": institution.get("cited_by_count", 0),
        "h_index": summary_stats.get("h_index", 0),
        "i10_index": summary_stats.get("i10_index", 0),
        "2yr_mean_citedness": summary_stats.get("2yr_mean_citedness", 0),
        "yearly_data": yearly_data,
    }


def collect_research_data(universities: List[str]) -> List[Dict]:
    """Collect research data for all universities from OpenAlex."""
    results = []
    total = len(universities)
    
    print(f"\nCollecting research data for {total} universities...")
    print("=" * 60)
    
    for idx, uni_name in enumerate(universities, 1):
        try:
            print(f"[{idx}/{total}] Searching: {uni_name[:50]}...")
        except UnicodeEncodeError:
            print(f"[{idx}/{total}] Searching: (unicode name)...")
        
        # Search OpenAlex
        institution = search_institution(uni_name)
        
        if institution:
            # Extract data
            research_data = extract_research_data(institution, uni_name)
            results.append(research_data)
            try:
                print(f"  [FOUND] {research_data['display_name']}")
            except UnicodeEncodeError:
                print(f"  [FOUND] (unicode name)")
        else:
            print(f"  [NOT FOUND]")
        
        # Rate limiting
        time.sleep(RATE_LIMIT_DELAY)
    
    print("=" * 60)
    print(f"\nCollection complete: {len(results)} institutions found")
    
    return results


def save_results(results: List[Dict]) -> None:
    """Save results to JSON file."""
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\nResults saved to: {OUTPUT_FILE}")


def main():
    """Main execution function."""
    print("=" * 60)
    print("OpenAlex Research Data Collection")
    print("EduVision_DV - Phase 1 Data Acquisition")
    print("=" * 60)
    
    # Load university names
    print("\nLoading university names from QS and THE datasets...")
    universities = load_university_names()
    print(f"Found {len(universities)} unique universities")
    
    # Collect research data
    results = collect_research_data(universities)
    
    # Save results
    save_results(results)
    
    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total universities searched: {len(universities)}")
    print(f"Institutions found in OpenAlex: {len(results)}")
    print(f"Success rate: {len(results)/len(universities)*100:.1f}%")
    
    # Show sample data
    if results:
        sample = results[0]
        print(f"\nSample data for: {sample['display_name']}")
        print(f"  Total works: {sample['works_count_total']:,}")
        print(f"  Total citations: {sample['cited_by_count_total']:,}")
        print(f"  h-index: {sample['h_index']}")
        if sample['yearly_data']:
            print("  Yearly breakdown:")
            for year in sorted(sample['yearly_data'].keys()):
                data = sample['yearly_data'][year]
                print(f"    {year}: {data['works_count']:,} works, {data['cited_by_count']:,} citations")


if __name__ == "__main__":
    main()
