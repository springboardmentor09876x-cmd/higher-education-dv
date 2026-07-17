"""
============================================================
EduVision_DV
Module 3 - Education KPI Engineering
============================================================

Description:
    Generates education KPIs from the cleaned university dataset
    and creates a Power BI-ready final dataset.

Input:
    datasets/final/Module_2_Deliverables/university_cleaned.csv

Outputs:
    datasets/final/Module_3_Deliverables/university_final_dataset.csv
    datasets/final/Module_3_Deliverables/university_final_dataset.xlsx

Author:
    Guru Sasank
============================================================
"""

from pathlib import Path

import numpy as np
import pandas as pd


# ============================================================
# Paths
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    PROJECT_ROOT
    / "datasets"
    / "final"
    / "Module_2_Deliverables"
    / "university_cleaned.csv"
)

OUTPUT_FOLDER = (
    PROJECT_ROOT
    / "datasets"
    / "final"
    / "Module_3_Deliverables"
)

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

CSV_OUTPUT = OUTPUT_FOLDER / "university_final_dataset.csv"
EXCEL_OUTPUT = OUTPUT_FOLDER / "university_final_dataset.xlsx"


# ============================================================
# Load Dataset
# ============================================================

def load_dataset() -> pd.DataFrame:
    """
    Load the cleaned university dataset.
    """

    print("=" * 60)
    print("MODULE 3 - KPI ENGINEERING")
    print("=" * 60)

    df = pd.read_csv(INPUT_FILE)

    print("Dataset Loaded Successfully")
    print(f"Rows    : {len(df):,}")
    print(f"Columns : {df.shape[1]}")

    return df


# ============================================================
# Required Columns Validation
# ============================================================

def validate_columns(df: pd.DataFrame) -> None:
    """
    Validate required columns.
    """

    required_columns = [
        "Overall Score",
        "Academic Reputation Score",
        "Faculty Count",
        "Student Population",
        "International Students",
        "Publications",
        "Citation Count",
        "h-index",
        "Citations per Faculty Score",
        "Research Quality",
    ]

    missing = [c for c in required_columns if c not in df.columns]

    if missing:
        raise ValueError(
            "Missing required columns:\n"
            + "\n".join(missing)
        )

    print("✓ Required columns verified.")


# ============================================================
# Utility Functions
# ============================================================

def min_max_scale(series: pd.Series) -> pd.Series:
    """
    Scale a numeric series to 0-100.
    """

    minimum = series.min()
    maximum = series.max()

    if minimum == maximum:
        return pd.Series(100.0, index=series.index)

    return ((series - minimum) / (maximum - minimum)) * 100

def log_min_max_scale(series: pd.Series) -> pd.Series:
    """
    Apply log transformation followed by Min-Max scaling.

    This reduces the effect of extremely large values while
    preserving the relative ranking of universities.
    """

    log_series = np.log1p(series)

    minimum = log_series.min()
    maximum = log_series.max()

    if minimum == maximum:
        return pd.Series(100.0, index=series.index)

    return ((log_series - minimum) / (maximum - minimum)) * 100


# ============================================================
# KPI Functions
# ============================================================

def calculate_global_ranking_score(df: pd.DataFrame) -> None:
    """
    Create Global Ranking Score.
    """

    df["Global Ranking Score"] = (
        df["Overall Score"]
        .round(2)
    )


def calculate_research_impact_score(df: pd.DataFrame) -> None:
    """
    Create Research Impact Score.

    Formula:
        50% Citation Count (log-scaled)
        30% h-index
        20% Citations per Faculty Score
    """

    citation_score = log_min_max_scale(df["Citation Count"])

    h_index_score = min_max_scale(df["h-index"])

    cpf_score = df["Citations per Faculty Score"]

    df["Research Impact Score"] = (
        0.50 * citation_score
        + 0.30 * h_index_score
        + 0.20 * cpf_score
    ).round(2)

def calculate_faculty_student_ratio(df: pd.DataFrame) -> None:
    """
    Create Faculty-to-Student Ratio.
    """

    ratio = (
        df["Faculty Count"]
        / df["Student Population"]
    )

    df["Faculty-to-Student Ratio"] = (
        ratio.replace([np.inf, -np.inf], np.nan).round(6)
    )


def calculate_international_student_percentage(
    df: pd.DataFrame
) -> None:
    """
    Create International Student Percentage.
    """

    percentage = (
        df["International Students"]
        / df["Student Population"]
        * 100
    )

    df["International Student Percentage"] = (
        percentage
        .replace([np.inf, -np.inf], np.nan)
        .round(2)
    )


def calculate_academic_reputation_kpi(
    df: pd.DataFrame
) -> None:
    """
    Create Academic Reputation KPI.
    """

    df["Academic Reputation KPI"] = (
        df["Academic Reputation Score"]
        .round(2)
    )


def calculate_research_productivity_index(df: pd.DataFrame) -> None:
    """
    Create Research Productivity Index.

    Formula:
        70% Publications per Faculty
        30% Citation Count per Faculty (log-scaled)

    This combines research volume and research impact.
    """

    publications_per_faculty = (
        df["Publications"] / df["Faculty Count"]
    ).replace([np.inf, -np.inf], np.nan)

    citations_per_faculty = (
        df["Citation Count"] / df["Faculty Count"]
    ).replace([np.inf, -np.inf], np.nan)

    publications_score = min_max_scale(publications_per_faculty)
    citations_score = log_min_max_scale(citations_per_faculty)

    df["Research Productivity Index"] = (
        0.70 * publications_score
        + 0.30 * citations_score
    ).round(2)


# ============================================================
# KPI Pipeline
# ============================================================

def generate_kpis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate all KPIs.
    """

    print("\nGenerating KPIs...")

    calculate_global_ranking_score(df)
    print("✓ Global Ranking Score")

    calculate_research_impact_score(df)
    print("✓ Research Impact Score")

    calculate_faculty_student_ratio(df)
    print("✓ Faculty-to-Student Ratio")

    calculate_international_student_percentage(df)
    print("✓ International Student Percentage")

    calculate_academic_reputation_kpi(df)
    print("✓ Academic Reputation KPI")

    calculate_research_productivity_index(df)
    print("✓ Research Productivity Index")

    print("\nAll KPIs generated successfully.")

    return df

# ============================================================
# Export Dataset
# ============================================================

def export_dataset(df: pd.DataFrame) -> None:
    """
    Export the final KPI dataset to CSV and Excel.
    """

    # Export CSV
    df.to_csv(CSV_OUTPUT, index=False)

    print("\n✓ CSV exported successfully.")
    print(f"Location : {CSV_OUTPUT}")

    # Export Excel
    try:
        df.to_excel(
            EXCEL_OUTPUT,
            index=False,
            engine="openpyxl"
        )

        print("✓ Excel exported successfully.")
        print(f"Location : {EXCEL_OUTPUT}")

    except ModuleNotFoundError:
        print("\n⚠ Excel export skipped.")
        print("Reason : openpyxl is not installed.")
        print("Install using:")
        print("    python -m pip install openpyxl")


# ============================================================
# Summary
# ============================================================

def print_summary(df: pd.DataFrame) -> None:
    """
    Print Module 3 summary.
    """

    print("\n" + "=" * 60)
    print("MODULE 3 SUMMARY")
    print("=" * 60)

    print(f"Rows                 : {len(df):,}")
    print(f"Columns              : {df.shape[1]}")
    print(f"Missing Values       : {df.isna().sum().sum():,}")

    new_columns = [
        "Global Ranking Score",
        "Research Impact Score",
        "Faculty-to-Student Ratio",
        "International Student Percentage",
        "Academic Reputation KPI",
        "Research Productivity Index",
    ]

    print(f"KPIs Generated       : {len(new_columns)}")

    print("\nGenerated KPI Columns")

    for i, column in enumerate(new_columns, start=1):
        print(f"{i}. {column}")

    print("\nOutput Files")

    print(f"CSV   : {CSV_OUTPUT}")

    try:
        import openpyxl

        print(f"Excel : {EXCEL_OUTPUT}")

    except ModuleNotFoundError:
        print("Excel : Not exported (openpyxl not installed)")

    print("\nModule 3 completed successfully.")
    print("=" * 60)


# ============================================================
# Main
# ============================================================

def main():
    """
    Main execution function.
    """

    # Load data
    df = load_dataset()

    # Validate dataset
    validate_columns(df)

    # Generate KPIs
    df = generate_kpis(df)

    # Export outputs
    export_dataset(df)

    # Print summary
    print_summary(df)

    print("\n" + "=" * 60)
    print("Module 3 KPI Engineering completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()