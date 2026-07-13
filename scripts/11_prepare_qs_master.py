"""
Project : EduVision - Higher Education Analytics Dashboard
Script  : 11_prepare_qs_master.py

Description:
Prepare one clean QS dataset by standardizing
QS History and QS 2024 into a common schema.

Input:
data/processed/qs_master.csv

Output:
data/processed/qs_master_clean.csv

Author:
Ishita Tiwari
"""

import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

BASE = Path(__file__).resolve().parents[1]

INPUT = BASE / "data" / "processed" / "qs_master.csv"

OUTPUT = BASE / "data" / "processed" / "qs_master_clean.csv"
logger.info("Loading QS dataset...")

qs = pd.read_csv(INPUT)

logger.info(f"Rows : {len(qs):,}")


# Standardize ranking columns

qs["qs_rank"] = qs["rank_display"]

mask = qs["qs_rank"].isna()

qs.loc[mask, "qs_rank"] = qs.loc[
    mask,
    "2024 RANK",
]

 
# Standardize score
qs["qs_score"] = qs["score"].astype("object")

# QS 2024 records do not contain a year column, so assign 2024
qs.loc[qs["year"].isna(), "year"] = 2024

# Standardize year
qs["year"] = qs["year"].astype(int)

# Fill QS scores from the 2024 dataset where required
mask = qs["qs_score"].isna()

qs.loc[mask, "qs_score"] = (
    qs.loc[mask, "Overall SCORE"]
    .replace("-", pd.NA)
)

# Standardize university name


qs["university"] = qs["university"].fillna(
    qs["Institution Name"]
)


# Standardize country


qs["country"] = qs["country"].fillna(
    qs["Country"]
)

# Keep only required columns

columns = [

    "university_id",

    "university",

    "country",

    "year",

    "qs_rank",

    "qs_score",

    "Academic Reputation Score",

    "Employer Reputation Score",

    "Faculty Student Score",

    "Citations per Faculty Score",

    "International Faculty Score",

    "International Students Score",

    "International Research Network Score",

    "Employment Outcomes Score",

    "Sustainability Score",

]

qs = qs[columns]

qs.to_csv(
    OUTPUT,
    index=False,
)

logger.info("=" * 60)
logger.info(f"Rows Saved : {len(qs):,}")
logger.info(f"Saved : {OUTPUT}")
logger.info("=" * 60)