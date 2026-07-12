import re
from pathlib import Path

import pandas as pd  # type: ignore[import]

# ==========================================
# QS Master Dataset Creation (2017–2026)
# ==========================================

SCRIPT_DIR = Path(__file__).resolve().parent
RAW_PATH = SCRIPT_DIR.parent / "datasets" / "raw" / "qs"
OUTPUT_PATH = SCRIPT_DIR.parent / "datasets" / "final"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# ------------------------------------------
# Common Column Mapping
# ------------------------------------------

COLUMN_MAPPING = {

    # University
    "Institution": "University",
    "Institution Name": "University",
    "Institution_Name": "University",
    "institution": "University",

    # Country
    "Location": "Country",
    "location": "Country",
    "Country/Territory": "Country",

    # Rank
    "rank_display": "Rank",
    "rank display": "Rank",
    "rank_dispaly": "Rank",

    # Overall Score
    "Overall SCORE": "Overall Score",
    "overall score": "Overall Score",

    # Country Code
    "LocationCode": "Country Code",
    "location_code": "Country Code",

    # Employment Outcomes Score
    "GerScore": "Employment Outcomes Score",
    "Gerscore": "Employment Outcomes Score",

    # Employment Outcomes Rank
    "GerRank": "Employment Outcomes Rank",
    "Gerrank": "Employment Outcomes Rank",

    # Year
    "year": "Year",

    # University Size
    "Size": "University Size",
    "size": "University Size",

    # University Focus
    "Focus": "University Focus",
    "focus": "University Focus",

    # Research
    "Research": "Research",
    "research": "Research",

    # University Status
    "Status": "University Status",
    "status": "University Status",

    # University Age Band
    "Age Band": "University Age Band",
    "age band": "University Age Band",
}

YEAR_PATTERN = re.compile(r"20\d{2}")

all_data = []

# ==========================================
# Read every QS csv
# ==========================================

for file in sorted(RAW_PATH.glob("*.csv")):

    print(f"Reading : {file.name}")

    try:
        df = pd.read_csv(file, low_memory=False)

    except UnicodeDecodeError:

        df = pd.read_csv(
            file,
            encoding="latin1",
            low_memory=False
        )

    # --------------------------------------
    # Rename common columns
    # --------------------------------------

    df.rename(columns=COLUMN_MAPPING, inplace=True)

    # --------------------------------------
    # Remove duplicate column names
    # --------------------------------------

    df = df.loc[:, ~df.columns.duplicated()]

    # --------------------------------------
    # Add Year automatically
    # --------------------------------------

    if "Year" not in df.columns:

        match = YEAR_PATTERN.search(file.name)

        if match:
            df["Year"] = int(match.group())

    # --------------------------------------
    # Track source
    # --------------------------------------

    df["Source File"] = file.stem

    all_data.append(df)

# ==========================================
# Merge
# ==========================================

qs_master = pd.concat(
    all_data,
    ignore_index=True,
    sort=False
)

# ==========================================
# Merge duplicate columns
# ==========================================

def merge_duplicate_columns(df, primary, duplicates):
    """
    Merge duplicate columns into one anchor column.
    """

    if primary not in df.columns:
        df[primary] = pd.NA

    for col in duplicates:

        if col in df.columns:

            df[primary] = df[primary].combine_first(df[col])

            df.drop(columns=col, inplace=True)

    return df

# ==========================================
# Normalize Duplicate Columns
# ==========================================

COLUMN_GROUPS = {

    "University": [
        "Institution",
        "Institution Name",
        "Institution_Name",
        "institution"
    ],

    "Country": [
        "Location",
        "location",
        "Country/Territory"
    ],

    "Country Code": [
        "LocationCode",
        "location_code",
        "location code"
    ],

    "Rank": [
        "rank_display",
        "rank display",
        "rank_dispaly"
    ],

    "Overall Score": [
        "Overall SCORE",
        "overall score"
    ],

    "Academic Reputation Score": [
        "ArScore",
        "Arscore"
    ],

    "Academic Reputation Rank": [
        "ArRank",
        "Arrank"
    ],

    "Employer Reputation Score": [
        "ErScore",
        "Erscore"
    ],

    "Employer Reputation Rank": [
        "ErRank",
        "Errank"
    ],

    "Faculty Student Score": [
        "FsrScore",
        "Fsrscore"
    ],

    "Faculty Student Rank": [
        "FsrRank",
        "Fsrrank"
    ],

    "Citations per Faculty Score": [
        "CpfScore",
        "Cpfscore"
    ],

    "Citations per Faculty Rank": [
        "CpfRank",
        "Cpfrank"
    ],

    "International Faculty Score": [
        "IfrScore",
        "Ifrscore"
    ],

    "International Faculty Rank": [
        "IfrRank",
        "Ifrrank"
    ],

    "International Students Score": [
        "IsrScore",
        "Isrscore"
    ],

    "International Students Rank": [
        "IsrRank",
        "Isrrank"
    ],

    "International Research Network Score": [
        "IrnScore",
        "Irnscore"
    ],

    "International Research Network Rank": [
        "IrnRank",
        "Irnrank"
    ],

    "Employment Outcomes Score": [
        "GerScore",
        "Gerscore",
        "EO SCORE",
        "EO Score"
    ],

    "Employment Outcomes Rank": [
        "GerRank",
        "Gerrank",
        "EO RANK",
        "EO Rank"
],

    "Region": [
        "region"
    ],

    "University Size": [
        "size"
    ],

    "University Focus": [
        "focus"
    ],

    "Research": [
        "research"
    ],

    "University Status": [
        "status"
    ],

    "City": [
        "city"
    ],

    "University Type": [
        "type"
    ],

    "Research Output": [
        "research_output"
    ],

    "Students to Staff Ratio": [
        "student_faculty_ratio"
    ],

    "International Students": [
        "international_students"
    ],

    "Faculty Count": [
        "faculty_count"
    ],

    "University Age Band": [
        "age band"
    ],

    "Sustainability Score": [
        "SUS SCORE"
    ],

    "Sustainability Rank": [
        "SUS RANK"
    ],
}

for primary, duplicates in COLUMN_GROUPS.items():

    qs_master = merge_duplicate_columns(
        qs_master,
        primary,
        duplicates
    )

# ==========================================
# Validation
# ==========================================

print("\n" + "=" * 60)
print("QS MASTER DATASET")
print("=" * 60)

print("Rows :", qs_master.shape[0])
print("Columns :", qs_master.shape[1])

print("\nYear Distribution")
print(qs_master["Year"].value_counts().sort_index())

print("\nDuplicate Rows :", qs_master.duplicated().sum())

# ==========================================
# Arrange Columns
# ==========================================

priority_columns = [

    "University",
    "Country",
    "Country Code",
    "City",
    "Region",
    "University Type",
    "University Size",
    "University Focus",
    "Research",
    "University Status",
    "University Age Band",

    "Rank",
    "Overall Score",

    "Academic Reputation Score",
    "Academic Reputation Rank",

    "Employer Reputation Score",
    "Employer Reputation Rank",

    "Faculty Student Score",
    "Faculty Student Rank",

    "Citations per Faculty Score",
    "Citations per Faculty Rank",

    "International Faculty Score",
    "International Faculty Rank",

    "International Students Score",
    "International Students Rank",

    "International Research Network Score",
    "International Research Network Rank",

    "Employment Outcomes Score",
    "Employment Outcomes Rank",

    "Sustainability Score",
    "Sustainability Rank",

    "Faculty Count",
    "Students to Staff Ratio",
    "International Students",
    "Research Output",

    "Year",
    "Source File"
]

remaining_columns = [
    col for col in qs_master.columns
    if col not in priority_columns
]

qs_master = qs_master[
    priority_columns + sorted(remaining_columns)
]

print("\nFinal Columns")

for col in sorted(qs_master.columns):

    print(col)

# ==========================================
# Save
# ==========================================

output_file = OUTPUT_PATH / "qs_master.csv"

qs_master.to_csv(
    output_file,
    index=False
)

print(f"\nSaved Successfully : {output_file}")