import requests
import pandas as pd
import time

# ---- SETTINGS -------------------------------------------------------------

# OpenAlex lets you add an email to a "polite pool" for faster, more reliable
# responses. Replace with your own email. This is NOT a login/API key.
MY_EMAIL = "ishitatiwari51"

BASE_URL = "https://api.openalex.org/institutions"


TARGET_COUNT = 2000

PER_PAGE = 200  # max allowed by OpenAlex per request

OUTPUT_PATH = "data/raw/openalex_institutions_raw.csv"

# ---- COLLECTION LOOP --------------------------------------------------------

def fetch_institutions():
    all_rows = []
    cursor = "*"  # OpenAlex uses "cursor paging" for large result sets

    while len(all_rows) < TARGET_COUNT:
        params = {
            "per-page": PER_PAGE,
            "cursor": cursor,
            "sort": "works_count:desc",  # start with the biggest/most active institutions
            "mailto": MY_EMAIL,
        }

        response = requests.get(BASE_URL, params=params, timeout=30)
        response.raise_for_status()  # will raise an error if the request failed
        data = response.json()

        for record in data["results"]:
            all_rows.append({
                "institution_id": record.get("id"),
                "display_name": record.get("display_name"),
                "country_code": record.get("country_code"),
                "type": record.get("type"),
                "homepage_url": record.get("homepage_url"),
                "works_count": record.get("works_count"),
                "cited_by_count": record.get("cited_by_count"),
                "h_index": record.get("summary_stats", {}).get("h_index"),
                "i10_index": record.get("summary_stats", {}).get("i10_index"),
                "2yr_mean_citedness": record.get("summary_stats", {}).get("2yr_mean_citedness"),
            })

        print(f"Collected {len(all_rows)} institutions so far...")

        # Move to the next page
        cursor = data["meta"].get("next_cursor")
        if not cursor:
            break  # no more pages available

        time.sleep(0.2)  # be polite to the API, don't hammer it with requests

    return all_rows


if __name__ == "__main__":
    rows = fetch_institutions()
    df = pd.DataFrame(rows)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"\nSaved {len(df)} rows to {OUTPUT_PATH}")
    print(df.head())
