import re
from pathlib import Path

import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
RAW_DATA_PATH = SCRIPT_DIR.parent / "datasets" / "raw"
OUTPUT_PATH = SCRIPT_DIR.parent / "datasets" / "final"

REQUIRED_COLUMNS = [
    "University",
    "Country",
    "Country Code",
    "Rank",
    "Overall Score",
    "Academic Reputation Score",
    "Employer Reputation Score",
    "Faculty Student Score",
    "Citations per Faculty Score",
    "International Faculty Score",
    "International Students Score",
    "International Research Network Score",
    "Employment Outcomes Score",
    "Sustainability Score",
    "Student Population",
    "Students to Staff Ratio",
    "International Students",
    "Female to Male Ratio",
    "Teaching",
    "Research Environment",
    "Research Quality",
    "Industry Impact",
    "International Outlook",
    "Year",
    "Source File",
]

YEAR_PATTERN = re.compile(r"20\d{2}")

COLUMN_LOOKUPS = {
    "University": ["University", "Institution", "Institution Name", "University Name", "university", "Name"],
    "Country": ["Country", "Location", "location", "Country Name"],
    "Country Code": ["Country Code", "LocationCode", "location_code"],
    "Rank": ["Rank", "2026 Rank", "2025 Rank", "2024 RANK", "2023 RANK", "rank_display", "World Rank"],
    "Overall Score": ["Overall Score", "Overall SCORE", "Overall score", "overall score", "Score"],
    "Academic Reputation Score": ["Academic Reputation Score", "Ar Score", "ArScore"],
    "Employer Reputation Score": ["Employer Reputation Score", "Er Score", "ErScore"],
    "Faculty Student Score": ["Faculty Student Score", "Fsr Score", "FsrScore"],
    "Citations per Faculty Score": ["Citations per Faculty Score", "Cpf Score", "CpfScore"],
    "International Faculty Score": ["International Faculty Score", "IFR Score", "International Faculty"],
    "International Students Score": ["International Students Score", "ISR Score"],
    "International Research Network Score": ["International Research Network Score", "IRN Score"],
    "Employment Outcomes Score": ["Employment Outcomes Score", "EO Score"],
    "Sustainability Score": ["Sustainability Score", "SUS Score"],
    "Student Population": ["Student Population", "Students"],
    "Students to Staff Ratio": ["Students to Staff Ratio", "Student Staff Ratio"],
    "International Students": ["International Students"],
    "Female to Male Ratio": ["Female to Male Ratio", "Female:Male Ratio"],
    "Teaching": ["Teaching"],
    "Research Environment": ["Research Environment"],
    "Research Quality": ["Research Quality"],
    "Industry Impact": ["Industry Impact", "Industry Income"],
    "International Outlook": ["International Outlook"],
}


def get_first_existing_column(df: pd.DataFrame, candidates):
    for column in candidates:
        if column in df.columns:
            return df[column]
    return pd.Series(pd.NA, index=df.index)


def extract_year(file_name: str, df: pd.DataFrame):
    match = YEAR_PATTERN.search(file_name)
    if match:
        return int(match.group())

    if "2017-to-2022" in file_name.lower() and "year" in df.columns:
        return df["year"]

    return pd.NA


def normalize_dataframe(df: pd.DataFrame, source_file: Path) -> pd.DataFrame:
    df = df.copy()

    for target_column, candidates in COLUMN_LOOKUPS.items():
        df[target_column] = get_first_existing_column(df, candidates)

    df["Year"] = extract_year(source_file.name, df)
    df["Source File"] = source_file.stem

    for column in REQUIRED_COLUMNS:
        if column not in df.columns:
            df[column] = pd.NA

    return df[REQUIRED_COLUMNS]


def load_raw_datasets():
    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(f"Raw data folder not found: {RAW_DATA_PATH}")

    csv_files = sorted(RAW_DATA_PATH.rglob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in: {RAW_DATA_PATH}")

    datasets = []
    for file in csv_files:
        try:
            df = pd.read_csv(file, low_memory=False)
        except UnicodeDecodeError:
            df = pd.read_csv(file, encoding="latin1", low_memory=False)

        normalized_df = normalize_dataframe(df, file)
        datasets.append(normalized_df)

    return datasets


def main():
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    all_data = load_raw_datasets()

    if not all_data:
        raise ValueError("No dataframes were loaded from raw datasets.")

    master_df = pd.concat(all_data, ignore_index=True, sort=False)
    output_file = OUTPUT_PATH / "master_dataset.csv"
    master_df.to_csv(output_file, index=False)

    print("\n========================================")
    print("Master Dataset Created Successfully")
    print("========================================")
    print(f"Rows    : {master_df.shape[0]}")
    print(f"Columns : {master_df.shape[1]}")
    print(f"Saved Successfully : {output_file}")


if __name__ == "__main__":
    main()