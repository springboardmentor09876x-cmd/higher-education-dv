"""
10_match_the.py

Match THE Rankings with University Registry
Creates:
    processed/the_master.csv
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

NORMALIZED = BASE / "data" / "interim" / "normalized"
REGISTRY = BASE / "data" / "interim" / "registry"
PROCESSED = BASE / "data" / "processed"
logger.info("Loading datasets...")

registry = pd.read_csv(
    REGISTRY / "university_registry.csv"
)

lookup = dict(
    zip(
        registry["normalized_name"],
        registry["university_id"],
    )
)
the_frames = []

for year in range(2020, 2025):

    file = NORMALIZED / f"{year}_rankings_normalized.csv"

    df = pd.read_csv(file)

    df["year"] = year

    df["university_id"] = (
        df["normalized_name"]
        .map(lookup)
    )

    the_frames.append(df)
logger.info("Combining THE datasets...")

the_master = pd.concat(
    the_frames,
    ignore_index=True,
)
matched = the_master["university_id"].notna().sum()

logger.info("=" * 60)

logger.info(
    f"Matched : {matched:,} / {len(the_master):,}"
)

logger.info(
    f"Coverage : {matched / len(the_master) * 100:.2f}%"
)

logger.info("=" * 60)
output = PROCESSED / "the_master.csv"

the_master.to_csv(
    output,
    index=False,
)

logger.info(f"Rows Saved : {len(the_master):,}")
logger.info(f"Saved : {output}")