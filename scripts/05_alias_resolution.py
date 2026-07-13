"""
Project : EduVision - Higher Education Analytics Dashboard
Script  : 05_alias_resolution.py

Description:
Create possible aliases for universities to improve
matching between QS, THE and OpenAlex.

Input:
data/interim/registry/university_registry.csv

Output:
data/interim/matching/university_aliases.csv

Author:
Ishita Tiwari
"""

import logging
import re
from pathlib import Path

import pandas as pd

INPUT_PATH = Path("data/interim/registry/university_registry.csv")

OUTPUT_PATH = Path(
    "data/interim/matching/university_aliases.csv"
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)
def create_aliases(name):
    """
    Generate possible aliases for one university.
    """

    aliases = set()

    aliases.add(name)

    # Remove text inside brackets
    cleaned = re.sub(r"\(.*?\)", "", name).strip()

    aliases.add(cleaned)

    # Replace common separators
    aliases.add(cleaned.replace(",", " "))
    aliases.add(cleaned.replace("-", " "))

    # Remove multiple spaces
    aliases = {
        " ".join(alias.split())
        for alias in aliases
        if alias.strip()
    }

    return sorted(aliases)
def main():

    logger.info("Loading registry...")

    registry = pd.read_csv(INPUT_PATH)

    rows = []

    for _, row in registry.iterrows():

        aliases = create_aliases(
            row["university_name"]
        )

        for alias in aliases:

            rows.append({

                "university_id": row["university_id"],
                "university_name": row["university_name"],
                "country": row["country"],
                "alias": alias,

            })

    alias_df = pd.DataFrame(rows)

    alias_df["normalized_alias"] = (

        alias_df["alias"]

        .str.lower()

        .str.replace(
            r"[^a-z0-9 ]",
            "",
            regex=True,
        )

        .str.replace(
            r"\s+",
            " ",
            regex=True,
        )

        .str.strip()

    )

    alias_df = alias_df.drop_duplicates()

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    alias_df.to_csv(
        OUTPUT_PATH,
        index=False,
        encoding="utf-8-sig",
    )

    logger.info(f"Aliases Created : {len(alias_df):,}")

    logger.info(f"Universities : {registry.shape[0]:,}")

    logger.info(f"Saved : {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
