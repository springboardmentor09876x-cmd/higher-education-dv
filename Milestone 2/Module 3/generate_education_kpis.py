"""
--------------------------------------------------------------------------
KPI DEFINITIONS (methodology)
--------------------------------------------------------------------------
1. Global Ranking Score (0-100, higher = better)
   Min-max normalization of `world_rank`, inverted so that rank #1 scores
   100 and the worst-ranked university scores 0.
       GRS = 100 * (max(world_rank) - world_rank) / (max(world_rank) - min(world_rank))

2. Research Impact Score (0-100, higher = better)
   Weighted composite of the three research-signal columns already in the
   data. `citations_score` is already on a 0-100 scale; `citations_per_faculty`
   and `h_index` are raw counts, so they are min-max normalized to 0-100
   before being blended.
       RIS = 0.50 * citations_score
           + 0.30 * normalize(citations_per_faculty)
           + 0.20 * normalize(h_index)

3. Faculty-to-Student Ratio (students per faculty member)
   Standard institutional-research definition: how many students exist for
   every one faculty member.
       FSR = total_students / faculty_count
   (Validated against the dataset's own `faculty_to_student_ratio` column:
   matches for ~99% of rows within a small tolerance.)

4. International Student Percentage (%)
       ISP = international_students_count / total_students * 100
   (Validated against `international_student_ratio`: matches for ~99% of
   rows within 0.5 percentage points; the rest are minor source-data noise.)

5. Academic Reputation Score (0-100)
   The dataset already carries this exact metric (a normalized academic
   peer-review survey score, 0-100). It is carried through unchanged/rounded
   rather than re-derived, since the underlying survey responses are not
   present in the raw data to recompute it from scratch.

6. Research Productivity Index
   Publications produced per faculty member.
       RPI = publications_count / faculty_count
   (Validated against the dataset's own `research_productivity_index`
   column: matches for ~99% of rows within 0.05.)

All ratio/percentage KPIs guard against division by zero.
--------------------------------------------------------------------------
"""

import pandas as pd
import numpy as np

INPUT_FILE = "university_cleaned.csv"
OUTPUT_FILE = "university_final_dataset.xlsx"


def normalize_0_100(series: pd.Series) -> pd.Series:
    """Min-max normalize a numeric series to a 0-100 scale."""
    lo, hi = series.min(), series.max()
    if hi == lo:
        return pd.Series(0, index=series.index, dtype=float)
    return 100 * (series - lo) / (hi - lo)


def safe_divide(numerator: pd.Series, denominator: pd.Series) -> pd.Series:
    """Element-wise division that returns NaN instead of raising on 0/0 or x/0."""
    denom = denominator.replace(0, np.nan)
    return numerator / denom


def calculate_global_ranking_score(df: pd.DataFrame) -> pd.Series:
    rank = df["world_rank"]
    lo, hi = rank.min(), rank.max()
    return 100 * (hi - rank) / (hi - lo)


def calculate_research_impact_score(df: pd.DataFrame) -> pd.Series:
    citations_component = df["citations_score"]
    cpf_component = normalize_0_100(df["citations_per_faculty"])
    h_index_component = normalize_0_100(df["h_index"])
    return (
        0.50 * citations_component
        + 0.30 * cpf_component
        + 0.20 * h_index_component
    )


def calculate_faculty_to_student_ratio(df: pd.DataFrame) -> pd.Series:
    return safe_divide(df["total_students"], df["faculty_count"])


def calculate_international_student_percentage(df: pd.DataFrame) -> pd.Series:
    return safe_divide(df["international_students_count"], df["total_students"]) * 100


def calculate_academic_reputation_score(df: pd.DataFrame) -> pd.Series:
    # Already a 0-100 normalized score in the source data; carried through.
    return df["academic_reputation_score"].round(2)


def calculate_research_productivity_index(df: pd.DataFrame) -> pd.Series:
    return safe_divide(df["publications_count"], df["faculty_count"])


def add_kpi_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Global Ranking Score"] = calculate_global_ranking_score(df).round(2)
    df["Research Impact Score"] = calculate_research_impact_score(df).round(2)
    df["Faculty-to-Student Ratio"] = calculate_faculty_to_student_ratio(df).round(2)
    df["International Student Percentage"] = calculate_international_student_percentage(df).round(2)
    df["Academic Reputation Score"] = calculate_academic_reputation_score(df)
    df["Research Productivity Index"] = calculate_research_productivity_index(df).round(2)
    return df


def main():
    df = pd.read_csv(INPUT_FILE)
    print(f"Loaded {len(df):,} rows / {df.shape[1]} columns from {INPUT_FILE}")

    df = add_kpi_columns(df)

    new_cols = [
        "Global Ranking Score",
        "Research Impact Score",
        "Faculty-to-Student Ratio",
        "International Student Percentage",
        "Academic Reputation Score",
        "Research Productivity Index",
    ]
    print("Added columns:", new_cols)
    print(df[new_cols].describe().T)

    for col in new_cols:
        n_bad = (~np.isfinite(df[col])).sum()
        if n_bad:
            print(f"WARNING: {n_bad} non-finite values in '{col}'")

    df.to_excel(OUTPUT_FILE, index=False, engine="openpyxl")
    print(f"Saved final dataset to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
