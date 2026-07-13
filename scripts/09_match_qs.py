"""
09_match_qs.py

Match QS rankings with University Registry
Creates:
    processed/qs_master.csv
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

qs2024 = pd.read_csv(
    NORMALIZED / "qs_rankings_2024_raw_normalized.csv"
)

qshistory = pd.read_csv(
    NORMALIZED / "qs_rankings_2017_2022_raw_normalized.csv"
)

# normalized_name -> university_id

lookup = dict(
    zip(
        registry["normalized_name"],
        registry["university_id"],
    )
)
def assign_university_id(df):
    """
    Match normalized university names
    with the registry.
    """

    df = df.copy()

    df["university_id"] = (
        df["normalized_name"]
        .map(lookup)
    )

    return df
logger.info("Matching QS datasets...")

qs2024 = assign_university_id(qs2024)

qshistory = assign_university_id(qshistory)
# ============================================================
# Match Statistics
# ============================================================

matched_2024 = qs2024["university_id"].notna().sum()
matched_history = qshistory["university_id"].notna().sum()

logger.info("=" * 60)

logger.info(
    f"QS 2024 Matched : {matched_2024:,} / {len(qs2024):,}"
)

logger.info(
    f"QS History Matched : {matched_history:,} / {len(qshistory):,}"
)

logger.info(
    f"Overall Match Rate : "
    f"{(matched_2024 + matched_history) / (len(qs2024) + len(qshistory) ) * 100:.2f}%"
)

logger.info("=" * 60)
# ============================================================
# Combine QS datasets
# ============================================================

logger.info("Combining QS datasets...")

qs_master = pd.concat(
    [
        qshistory,
        qs2024,
    ],
    ignore_index=True,
)
# ============================================================
# Save
# ============================================================

output = PROCESSED / "qs_master.csv"

qs_master.to_csv(
    output,
    index=False,
)

logger.info(f"Rows Saved : {len(qs_master):,}")
logger.info(f"Saved : {output}")