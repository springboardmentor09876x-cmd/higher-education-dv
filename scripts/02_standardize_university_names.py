import logging
import re
import unicodedata
from pathlib import Path

import pandas as pd

RAW_DATA = Path("data/raw")
OUTPUT_DIR = Path("data/interim")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)
def normalize_name(name):

    if pd.isna(name):
        return None

    name = str(name)

    # Convert accented characters to ASCII
    name = unicodedata.normalize("NFKD", name)
    name = name.encode("ascii", "ignore").decode("utf-8")

    name = name.lower()

    # Replace "&" with "and"
    name = name.replace("&", " and ")

   # Remove text inside brackets (usually abbreviations)
    name = re.sub(r"\(.*?\)", "", name)

    # Remove punctuation
    name = re.sub(r"[^\w\s]", " ", name)

    # Remove extra spaces
    name = re.sub(r"\s+", " ", name).strip()

    return name
def process_file(file_path, university_column):

    logger.info(f"Processing {file_path.name}")

    df = pd.read_csv(file_path)

    df["normalized_name"] = (
        df[university_column]
        .apply(normalize_name)
    )

    output_name = file_path.stem + "_normalized.csv"

    df.to_csv(
        OUTPUT_DIR / output_name,
        index=False,
        encoding="utf-8-sig",
    )

    logger.info(f"Saved {output_name}")
def main():

    process_file(
        RAW_DATA / "qs_rankings_2017_2022_raw.csv",
        "university",
    )

    process_file(
        RAW_DATA / "qs_rankings_2024_raw.csv",
        "Institution Name",
    )

    for year in range(2020, 2025):

        process_file(
            RAW_DATA / f"{year}_rankings.csv",
            "name",
        )

    logger.info("University name standardization completed.")


if __name__ == "__main__":
    main()