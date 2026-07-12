from pathlib import Path
import pandas as pd

# ==========================================
# Module 1 - Final Master Dataset Creation
# ==========================================

SCRIPT_DIR = Path(__file__).resolve().parent

FINAL_PATH = SCRIPT_DIR.parent / "datasets" / "final"
RAW_RESEARCH_PATH = SCRIPT_DIR.parent / "datasets" / "raw" / "research"

OUTPUT_PATH = FINAL_PATH / "Module_1_Deliverables"
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# ==========================================
# Read Datasets
# ==========================================

education_master = pd.read_csv(
    FINAL_PATH / "education_master.csv",
    low_memory=False
)

research_master = pd.read_csv(
    RAW_RESEARCH_PATH / "research_enrichment.csv",
    low_memory=False
)

# ==========================================
# Standardize Research Columns
# ==========================================

COLUMN_MAPPING = {

    "university_name": "University",
    "year": "Year",

    "university_type": "University Type",

    "publications_count": "Publications",
    "citations_count": "Citation Count",
    "h_index": "h-index",
    "research_productivity_index": "Research Productivity Index",

    "subject_field": "Subject Area",

    "female_percentage": "Female Student Percentage",
    "male_percentage": "Male Student Percentage"
}

research_master.rename(columns=COLUMN_MAPPING, inplace=True)

# ==========================================
# Keep Required Columns
# ==========================================

research_master = research_master[[
    "University",
    "Year",
    "University Type",
    "Publications",
    "Citation Count",
    "h-index",
    "Research Productivity Index",
    "Subject Area",
    "Female Student Percentage",
    "Male Student Percentage"
]]

# ==========================================
# Merge
# ==========================================

master_dataset = pd.merge(
    education_master,
    research_master,
    on=["University", "Year"],
    how="left",
    suffixes=("", "_Research")
)

print(f"\nRows with Publications : {master_dataset['Publications'].notna().sum()}")
print(f"Rows with h-index      : {master_dataset['h-index'].notna().sum()}")
print(f"Rows with Subject Area : {master_dataset['Subject Area'].notna().sum()}")

# ==========================================
# Validation
# ==========================================

print("\n" + "=" * 60)
print("MASTER DATASET SUMMARY")
print("=" * 60)

print(f"Rows              : {master_dataset.shape[0]}")
print(f"Columns           : {master_dataset.shape[1]}")
print(f"Duplicate Rows    : {master_dataset.duplicated().sum()}")

print("\nYear Distribution")
print(master_dataset["Year"].value_counts().sort_index())

print("\nColumns")

for col in sorted(master_dataset.columns):
    print(f"• {col}")

# ==========================================
# Save
# ==========================================

output_file = OUTPUT_PATH / "master_dataset.csv"

master_dataset.to_csv(
    output_file,
    index=False
)

print(f"\nSaved Successfully : {output_file}")