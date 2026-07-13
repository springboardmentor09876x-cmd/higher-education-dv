"""
Project : EduVision - Higher Education Analytics Dashboard
Script  : 06_match_openalex.py

Description:
Match university aliases with OpenAlex institutions.

Input
-----
data/interim/matching/university_aliases.csv
data/raw/openalex_bulk_raw.csv

Output
------
data/processed/openalex_matches.csv
data/processed/openalex_unmatched.csv
data/processed/openalex_match_summary.csv

Author:
Ishita Tiwari
"""

import logging
import re
from pathlib import Path

import pandas as pd

ALIAS_PATH = Path(
    "data/interim/matching/university_aliases.csv"
)

OPENALEX_PATH = Path(
    "data/raw/openalex_bulk_raw.csv"
)

OUTPUT_FOLDER = Path(
    "data/processed"
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)
def normalize(text):

    if pd.isna(text):
        return ""

    text = str(text).lower()

    text = re.sub(
        r"[^a-z0-9 ]",
        " ",
        text,
    )

    text = re.sub(
        r"\s+",
        " ",
        text,
    )

    return text.strip()


def main():

    logger.info("Loading datasets...")

    aliases = pd.read_csv(ALIAS_PATH)

    openalex = pd.read_csv(OPENALEX_PATH)

    logger.info(f"Aliases : {len(aliases):,}")
    logger.info(f"OpenAlex : {len(openalex):,}")

    openalex["normalized_name"] = (
        openalex["openalex_display_name"]
        .apply(normalize)
    )

    alias_lookup = (
        openalex
        .drop_duplicates("normalized_name")
        .set_index("normalized_name")
    )
    matches = []
    matched_ids = set()

    for _, row in aliases.iterrows():

        key = normalize(row["alias"])

        if key in alias_lookup.index:

            oa = alias_lookup.loc[key]
            matched_ids.add(row["university_id"])

            matches.append({

                "university_id": row["university_id"],
                "university_name": row["university_name"],
                "country": row["country"],

                "openalex_name":
                oa["openalex_display_name"],

                "institution_id":
                oa["institution_id"],

                "works_count":
                oa["works_count"],

                "cited_by_count":
                oa["cited_by_count"],

                "h_index":
                oa["h_index"],

                "i10_index":
                oa["i10_index"],

                "2yr_mean_citedness":
                oa["2yr_mean_citedness"],

            })


    matches = (
    pd.DataFrame(matches)
    .drop_duplicates("university_id")
    )

    registry = pd.read_csv(
    "data/interim/registry/university_registry.csv"
    )
    unmatched = registry[
    ~registry["university_id"].isin(matched_ids)
    ].copy()

    summary = pd.DataFrame({

        "Metric": [

            "Total Universities",
            "Matched",
            "Unmatched",
            "Coverage (%)",

        ],

        "Value": [

            len(registry),

            len(matches),

            len(unmatched),

            round(
                len(matches)
                /
                (len(matches)+len(unmatched))
                *100,
                2,
            ),

        ],

    })

    OUTPUT_FOLDER.mkdir(
        parents=True,
        exist_ok=True,
    )

    matches.to_csv(
        OUTPUT_FOLDER /
        "openalex_matches.csv",
        index=False,
        encoding="utf-8-sig",
    )

    unmatched.to_csv(
        OUTPUT_FOLDER /
        "openalex_unmatched.csv",
        index=False,
        encoding="utf-8-sig",
    )

    summary.to_csv(
        OUTPUT_FOLDER /
        "openalex_match_summary.csv",
        index=False,
        encoding="utf-8-sig",
    )

    logger.info(f"Matched : {len(matches):,}")
    logger.info(f"Unmatched : {len(unmatched):,}")
    logger.info("Completed Successfully.")


if __name__ == "__main__":
    main()