"""
generate_education_kpis.py

Higher Education Performance Dashboard

This script generates and validates the Key Performance Indicators (KPIs)
required for the Higher Education Dashboard and saves the final dataset.
"""

import pandas as pd


def load_dataset(file_path):
    """Load the input dataset."""
    print("Loading dataset...")

    df = pd.read_excel(file_path)

    print(f"Dataset loaded successfully.")
    print(f"Shape: {df.shape}")

    return df


def validate_columns(df):
    """Validate that all required columns exist."""

    required_columns = [
        "world_rank",
        "academic_reputation_score",
        "citations_count",
        "Research_Output_x",
        "research_productivity_index",
        "faculty_count",
        "student_population",
        "international_student_percentage"
    ]

    missing = [
        col
        for col in required_columns
        if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    print("All required columns are available.\n")


def generate_kpis(df):
    """Generate all required KPIs."""

    print("Generating KPIs...")

    # -------------------------------------------------------
    # KPI 1 - Global Ranking Score
    # -------------------------------------------------------
    df["global_ranking_score"] = (
        1000 - pd.to_numeric(
            df["world_rank"],
            errors="coerce"
        )
    )

    # -------------------------------------------------------
    # KPI 2 - Research Impact Score
    # -------------------------------------------------------
    df["research_impact_score"] = (
        df[
            [
                "citations_count",
                "Research_Output_x",
                "research_productivity_index"
            ]
        ]
        .mean(axis=1)
    )

    # -------------------------------------------------------
    # KPI 3 - Faculty-to-Student Ratio
    # -------------------------------------------------------
    mask = (
        df["faculty_count"].notna()
        &
        df["student_population"].notna()
        &
        (df["faculty_count"] > 0)
        &
        (df["student_population"] > 0)
    )

    df.loc[
        mask,
        "faculty_to_student_ratio"
    ] = (
        df.loc[mask, "student_population"]
        /
        df.loc[mask, "faculty_count"]
    )

    # -------------------------------------------------------
    # KPI 4 - International Student Percentage
    # -------------------------------------------------------
    df["international_student_percentage"] = pd.to_numeric(
        df["international_student_percentage"],
        errors="coerce"
    )

    # -------------------------------------------------------
    # KPI 5 - Academic Reputation Score
    # -------------------------------------------------------
    df["academic_reputation_score"] = pd.to_numeric(
        df["academic_reputation_score"],
        errors="coerce"
    )

    # -------------------------------------------------------
    # KPI 6 - Research Productivity Index
    # -------------------------------------------------------
    df["research_productivity_index"] = pd.to_numeric(
        df["research_productivity_index"],
        errors="coerce"
    )

    print("All KPIs generated successfully.\n")

    return df


def save_dataset(df, output_path):
    """Save the final dataset."""

    df.to_excel(
        output_path,
        index=False
    )

    print("Dataset saved successfully.")
    print(f"Output File: {output_path}")
    print(f"Final Shape: {df.shape}")


def main():

    input_path = "../datasets/final_dataset/university_final_dataset.xlsx"

    output_path = "../datasets/final_dataset/university_final_dataset.xlsx"

    df = load_dataset(input_path)

    validate_columns(df)

    df = generate_kpis(df)

    save_dataset(df, output_path)

    print("\nKPI Engineering Completed Successfully!")


if __name__ == "__main__":
    main()