import logging
from pathlib import Path

import pandas as pd

RAW_DATA = Path("data/interim")
OUTPUT_PATH = Path("data/interim/candidate_universities.csv")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

def load_qs_history():

    df = pd.read_csv(
        RAW_DATA / "qs_rankings_2017_2022_raw_normalized.csv"
    )

    return pd.DataFrame({
        "university_name": df["university"],
        "normalized_name": df["normalized_name"],
        "country": df["country"],
        "year": df["year"],
        "source": "QS"
    })


def load_qs_2024():

    df = pd.read_csv(
        RAW_DATA / "qs_rankings_2024_raw_normalized.csv"
    )

    return pd.DataFrame({
        "university_name": df["Institution Name"],
        "normalized_name": df["normalized_name"],
        "country": df["Country"],
        "year": 2024,
        "source": "QS"
    })


def load_the():

    frames = []

    for year in range(2020, 2025):

        df = pd.read_csv(
            RAW_DATA / f"{year}_rankings_normalized.csv"
        )

        frames.append(
            pd.DataFrame({
                "university_name": df["name"],
                "normalized_name": df["normalized_name"],
                "country": df["location"],
                "year": year,
                "source": "THE"
            })
        )

    return pd.concat(
        frames,
        ignore_index=True,
    )
def main():

    logger.info("Creating candidate university list...")

    candidate = pd.concat(
        [
            load_qs_history(),
            load_qs_2024(),
            load_the(),
        ],
        ignore_index=True,
    )

    candidate.to_csv(
        OUTPUT_PATH,
        index=False,
        encoding="utf-8-sig",
    )

    logger.info(f"Rows created : {len(candidate):,}")
    logger.info(f"Unique universities : {candidate['university_name'].nunique():,}")
    logger.info(f"Saved to : {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
