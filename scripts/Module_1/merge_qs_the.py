from pathlib import Path
import pandas as pd

# ==========================================
# Merge QS + THE Master Dataset
# ==========================================

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent.parent
FINAL_PATH = ROOT_DIR / "datasets" / "final" / "intermediate"
OUTPUT_PATH = FINAL_PATH

for path_name, path_obj in [
    ("qs_master.csv", FINAL_PATH / "qs_master.csv"),
    ("the_master.csv", FINAL_PATH / "the_master.csv"),
]:
    if not path_obj.exists():
        raise FileNotFoundError(
            f"Required input file '{path_name}' not found in {FINAL_PATH}."
        )

# ------------------------------------------
# Read Master Files
# ------------------------------------------

qs_master = pd.read_csv(
    FINAL_PATH / "qs_master.csv",
    low_memory=False
)

the_master = pd.read_csv(
    FINAL_PATH / "the_master.csv",
    low_memory=False
)

# ------------------------------------------
# Merge
# ------------------------------------------

education_master = pd.merge(
    qs_master,
    the_master,
    on=["University", "Country", "Year"],
    how="outer",
    suffixes=("_QS", "_THE")
)

# ------------------------------------------
# Validation
# ------------------------------------------

print("=" * 60)
print("QS + THE MASTER DATASET")
print("=" * 60)

print(f"Rows      : {education_master.shape[0]}")
print(f"Columns   : {education_master.shape[1]}")
print(f"Duplicates: {education_master.duplicated().sum()}")

print("\nYears")
print(education_master["Year"].value_counts().sort_index())

print("\nMissing Universities")
print(education_master["University"].isna().sum())

# ------------------------------------------
# Save
# ------------------------------------------

output_file = OUTPUT_PATH / "education_master.csv"

education_master.to_csv(
    output_file,
    index=False
)

print(f"\nSaved Successfully : {output_file}")