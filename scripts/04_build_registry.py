import logging
from pathlib import Path

import pandas as pd

INPUT_PATH = Path("data/interim/matching/candidate_universities.csv")

REGISTRY_PATH = Path(
    "data/interim/registry/university_registry.csv"
)

MAPPING_PATH = Path(
    "data/interim/registry/university_source_mapping.csv"
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)
def create_registry(df):

    registry = (
        df[
            [
                "normalized_name",
                "university_name",
                "country",
            ]
        ]
        .drop_duplicates(
            subset=["normalized_name"]
        )
        .sort_values("normalized_name")
        .reset_index(drop=True)
    )

    registry.insert(
        0,
        "university_id",
        [
            f"U{i:06d}"
            for i in range(1, len(registry) + 1)
        ],
    )

    return registry
def create_mapping(df, registry):

    mapping = df.merge(
        registry[
            [
                "university_id",
                "normalized_name",
            ]
        ],
        on="normalized_name",
        how="left",
    )

    mapping = mapping[
        [
            "university_id",
            "university_name",
            "country",
            "source",
            "year",
        ]
    ]

    return mapping
def main():

    logger.info("Loading candidate universities...")

    candidate = pd.read_csv(INPUT_PATH)

    logger.info("Building university registry...")

    registry = create_registry(candidate)

    logger.info("Building source mapping...")

    mapping = create_mapping(
        candidate,
        registry,
    )

    registry.to_csv(
        REGISTRY_PATH,
        index=False,
        encoding="utf-8-sig",
    )

    mapping.to_csv(
        MAPPING_PATH,
        index=False,
        encoding="utf-8-sig",
    )

    logger.info(f"Registry rows : {len(registry):,}")
    logger.info(f"Mapping rows : {len(mapping):,}")

    logger.info("Completed.")


if __name__ == "__main__":
    main()