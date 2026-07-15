"""
Project : EduVision - Higher Education Analytics Dashboard
Script  : 07_fuzzy_match_openalex.py

Description:
Perform fuzzy matching between unmatched universities
and the OpenAlex institution dataset.

Author:
Ishita Tiwari
"""

import logging
import re
from pathlib import Path

import pandas as pd
from rapidfuzz import fuzz, process

UNMATCHED_PATH = Path("data/processed/openalex_unmatched.csv")
OPENALEX_PATH = Path("data/raw/openalex_bulk_raw.csv")
OUTPUT_PATH = Path("data/processed/openalex_fuzzy_matches.csv")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)
def normalize(text):

    if pd.isna(text):
        return ""

    text = str(text).lower()

    text = re.sub(r"[^a-z0-9 ]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


logger.info("Loading datasets...")

unmatched = pd.read_csv(UNMATCHED_PATH)

openalex = pd.read_csv(OPENALEX_PATH)

openalex["normalized_name"] = (
    openalex["openalex_display_name"]
    .apply(normalize)
)

choices = openalex["normalized_name"].tolist()
results = []

for _, row in unmatched.iterrows():

    query = normalize(row["university_name"])

    match = process.extractOne(
        query,
        choices,
        scorer=fuzz.token_sort_ratio,
    )

    if match is None:
        continue

    matched_name = match[0]
    score = match[1]

    if score < 90:
        continue

    oa = openalex[
        openalex["normalized_name"] == matched_name
    ].iloc[0]

    results.append({

        "university_id": row["university_id"],
        "university_name": row["university_name"],
        "country": row["country"],

        "matched_name": oa["openalex_display_name"],

        "score": score,

        "institution_id": oa["institution_id"],

        "works_count": oa["works_count"],

        "cited_by_count": oa["cited_by_count"],

        "h_index": oa["h_index"],

        "i10_index": oa["i10_index"],

        "2yr_mean_citedness": oa["2yr_mean_citedness"],

    })

matches = pd.DataFrame(results)

matches.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

logger.info("=" * 60)
logger.info(f"Recovered Matches : {len(matches):,}")
logger.info(f"Saved : {OUTPUT_PATH}")
logger.info("=" * 60)
