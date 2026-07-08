import requests
import pandas as pd

# ---- SETTINGS ---------------------------------------------------------

# World Bank indicator codes we want.
# https://data.worldbank.org/indicator
INDICATORS = {
    "NY.GDP.PCAP.CD": "gdp_per_capita_usd",
    "SE.XPD.TOTL.GD.ZS": "education_expenditure_pct_gdp",
    "SE.TER.ENRR": "tertiary_enrollment_ratio",
    "SP.POP.TOTL": "population",
    "SE.ADT.LITR.ZS": "literacy_rate_pct",
}

START_YEAR = 2015
END_YEAR = 2024

OUTPUT_PATH = "data/raw/worldbank_indicators_raw.csv"


def fetch_indicator(indicator_code, column_name):
    """Fetches one indicator for all countries across our year range."""
    url = f"https://api.worldbank.org/v2/country/all/indicator/{indicator_code}"
    params = {
        "format": "json",
        "per_page": 20000,          # large enough to get everything in one call
        "date": f"{START_YEAR}:{END_YEAR}",
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    # World Bank responses are a list: [metadata, actual_records]
    # Sometimes there are zero records — guard against that.
    if len(data) < 2 or data[1] is None:
        print(f"WARNING: no data returned for {indicator_code}")
        return pd.DataFrame(columns=["country_code", "country_name", "year", column_name])

    records = data[1]
    rows = []
    for r in records:
        rows.append({
            "country_code": r["countryiso3code"],
            "country_name": r["country"]["value"],
            "year": r["date"],
            column_name: r["value"],
        })

    return pd.DataFrame(rows)


if __name__ == "__main__":
    dfs = []
    for code, name in INDICATORS.items():
        print(f"Fetching {name} ({code})...")
        df_ind = fetch_indicator(code, name)
        dfs.append(df_ind)

    # Merge all indicators together on country_code + year
    merged = dfs[0]
    for df_next in dfs[1:]:
        merged = merged.merge(
            df_next.drop(columns=["country_name"]),
            on=["country_code", "year"],
            how="outer",
        )

    # Drop rows where country_code is blank (World Bank includes some
    # aggregate "regions" like "World" or "Arab World" mixed in with real
    # countries — we don't want those in a country comparison dashboard)
    merged = merged[merged["country_code"].notna() & (merged["country_code"] != "")]

    merged.to_csv(OUTPUT_PATH, index=False)
    print(f"\nSaved {len(merged)} rows to {OUTPUT_PATH}")
    print(merged.head())
