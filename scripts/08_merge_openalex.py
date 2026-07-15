"""
08_merge_openalex.py

Merge Exact + Fuzzy OpenAlex Matches
Creates one clean OpenAlex dataset.
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

PROCESSED = BASE / "data" / "processed"

OUTPUT = PROCESSED / "openalex_master.csv"
logger.info("Loading files...")

exact = pd.read_csv(
    PROCESSED / "openalex_matches.csv"
)

fuzzy = pd.read_csv(
    PROCESSED / "openalex_fuzzy_matches.csv"
)
logger.info("Combining datasets...")

master = pd.concat(
    [exact, fuzzy],
    ignore_index=True,
)

master = (
    master
    .drop_duplicates(subset="university_id")
    .sort_values("university_name")
    .reset_index(drop=True)
)
logger.info("Saving...")

master.to_csv(
    OUTPUT,
    index=False,
)

logger.info("=" * 60)
logger.info(f"Rows : {len(master):,}")
logger.info(f"Saved : {OUTPUT}")
logger.info("=" * 60)