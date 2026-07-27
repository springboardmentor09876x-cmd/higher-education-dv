from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

RAW = BASE_DIR / "data" / "raw"
OUT = BASE_DIR / "data" / "processed"
OUT.mkdir(exist_ok=True)

def read_csv(file):
    """Read CSV with automatic encoding detection."""
    for enc in ["utf-8", "latin1", "cp1252"]:
        try:
            return pd.read_csv(file, encoding=enc)
        except UnicodeDecodeError:
            continue
    raise Exception(f"Cannot read {file}")


frames = []

# ---------------------------------------------------
# QS Rankings
# ---------------------------------------------------

qs = read_csv(RAW / "qs_rankings_2025.csv")

qs = qs.rename(columns={
    "Institution_Name": "university_name",
    "Location": "country",
    "RANK_2025": "world_rank",
    "Overall_Score": "overall_score"
})

qs["year"] = 2025
qs["national_rank"] = None
qs["source"] = "QS"

frames.append(
    qs[[
        "university_name",
        "country",
        "world_rank",
        "national_rank",
        "overall_score",
        "year",
        "source"
    ]]
)

# ---------------------------------------------------
# THE
# ---------------------------------------------------

the = read_csv(RAW / "THE World University Rankings 2016-2026.csv")

the = the.rename(columns={
    "Name": "university_name",
    "Country": "country",
    "Rank": "world_rank",
    "Overall Score": "overall_score"
})

the["national_rank"] = None
the["source"] = "THE"

frames.append(
    the[[
        "university_name",
        "country",
        "world_rank",
        "national_rank",
        "overall_score",
        "Year",
        "source"
    ]].rename(columns={"Year": "year"})
)

# ---------------------------------------------------
# CWUR
# ---------------------------------------------------

cwur = read_csv(RAW / "cwurData.csv")

cwur = cwur.rename(columns={
    "institution": "university_name",
    "country": "country",
    "world_rank": "world_rank",
    "national_rank": "national_rank",
    "score": "overall_score"
})

cwur["source"] = "CWUR"

frames.append(
    cwur[[
        "university_name",
        "country",
        "world_rank",
        "national_rank",
        "overall_score",
        "year",
        "source"
    ]]
)

# ---------------------------------------------------
# Times
# ---------------------------------------------------

times = read_csv(RAW / "timesData.csv")

times = times.rename(columns={
    "university_name": "university_name",
    "country": "country",
    "world_rank": "world_rank",
    "total_score": "overall_score"
})

times["national_rank"] = None
times["source"] = "Times"

frames.append(
    times[[
        "university_name",
        "country",
        "world_rank",
        "national_rank",
        "overall_score",
        "year",
        "source"
    ]]
)

# ---------------------------------------------------
# Shanghai
# ---------------------------------------------------

shanghai = read_csv(RAW / "shanghaiData.csv")

shanghai = shanghai.rename(columns={
    "university_name": "university_name",
    "world_rank": "world_rank",
    "national_rank": "national_rank",
    "total_score": "overall_score"
})

# No country in this dataset
shanghai["country"] = None
shanghai["source"] = "Shanghai"

frames.append(
    shanghai[[
        "university_name",
        "country",
        "world_rank",
        "national_rank",
        "overall_score",
        "year",
        "source"
    ]]
)

# ---------------------------------------------------
# School-Country mapping
# ---------------------------------------------------

mapping = read_csv(RAW / "school_and_country_table.csv")

mapping = mapping.rename(columns={
    "school_name": "university_name"
})

# Merge country into Shanghai
frames[-1] = frames[-1].merge(
    mapping,
    on="university_name",
    how="left",
    suffixes=("", "_map")
)

frames[-1]["country"] = frames[-1]["country"].fillna(frames[-1]["country_map"])

frames[-1] = frames[-1].drop(columns=["country_map"])

# ---------------------------------------------------
# Merge everything
# ---------------------------------------------------

raw = pd.concat(frames, ignore_index=True)

raw.to_csv(
    OUT / "university_raw_data.csv",
    index=False
)

print("="*50)
print("MERGE SUCCESSFUL")
print("="*50)
print(raw.head())
print()
print(f"Rows : {len(raw)}")
print(f"Columns : {len(raw.columns)}")
print(f"Saved : {OUT/'university_raw_data.csv'}")