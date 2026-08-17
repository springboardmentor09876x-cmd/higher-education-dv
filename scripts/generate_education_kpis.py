"""
generate_education_kpis.py
EduVision_DV - Module 3: Education KPI Engineering

Loads the cleaned university dataset (Module 2 output), removes merge-artifact
duplicates, calculates 6 required KPIs, and saves the final dataset for Tableau.
"""

import pandas as pd
import numpy as np


# ---------------------------------------------------------------------------
# Normalization helpers
# ---------------------------------------------------------------------------

def normalize_rank(series):
    """
    Converts a rank (lower = better) into a 0-100 score (higher = better),
    using min-max normalization, inverted.
    """
    min_val, max_val = series.min(), series.max()
    return 100 - ((series - min_val) / (max_val - min_val) * 100)


def normalize_score(series):
    """
    Converts a raw score (higher = better already) into a 0-100 scale
    using standard min-max normalization.
    """
    min_val, max_val = series.min(), series.max()
    return (series - min_val) / (max_val - min_val) * 100


def normalize_name(name):
    """
    Creates a normalization key for matching near-duplicate university names
    that differ only in punctuation/spacing (e.g. hyphens vs spaces, commas).
    Used only for grouping -- the original university_name column is preserved
    for display.
    """
    name = str(name).lower().strip()
    name = name.replace('-', ' ')
    name = name.replace(',', '')
    name = ' '.join(name.split())
    return name


# ---------------------------------------------------------------------------
# Deduplication (fixes Module 1 merge artifacts)
# ---------------------------------------------------------------------------

def deduplicate_multiyear_rows(df):
    """
    Module 1 merged multi-year Times and Shanghai tables on university_name,
    creating a cartesian product of (times_year x shanghai_year) combinations
    per university (e.g. 6 Times years x 11 Shanghai years = 66 fake rows).

    Fix: keep only the row with the most recent times_year AND shanghai_year
    per university, since this project targets current-state benchmarking,
    not historical trend analysis.
    """
    df = (
        df.sort_values(['times_year', 'shanghai_year'], ascending=[False, False])
          .groupby('university_name', as_index=False)
          .first()
    )
    return df


def deduplicate_near_matching_names(df):
    """
    Catches near-duplicate university names that differ only in punctuation
    (e.g. 'aix marseille university' vs 'aix-marseille university'), which
    exact-string groupby cannot catch.

    For each near-duplicate group, keeps the row with the fewest missing
    values (i.e. the most complete data).
    """
    df = df.copy()
    df['name_key'] = df['university_name'].apply(normalize_name)
    df['missing_count'] = df.isnull().sum(axis=1)

    df = (
        df.sort_values('missing_count')
          .groupby('name_key', as_index=False)
          .first()
          .drop(columns=['missing_count', 'name_key'])
    )
    return df


# ---------------------------------------------------------------------------
# KPI calculations
# ---------------------------------------------------------------------------

def calculate_global_ranking_score(df):
    """
    Combines QS 2025, Times, and Shanghai world ranks into one 0-100 score.
    Each source is normalized independently, then averaged row-wise
    (ignoring NaN), so a university ranked by only 1-2 sources isn't
    penalized for missing sources.
    """
    qs_norm = normalize_rank(df['rank_2025_numeric'])
    times_norm = normalize_rank(df['times_world_rank_numeric'])
    shanghai_norm = normalize_rank(df['shanghai_world_rank_numeric'])

    df['global_ranking_score'] = pd.concat(
        [qs_norm, times_norm, shanghai_norm], axis=1
    ).mean(axis=1)
    return df


def calculate_research_impact_score(df):
    """
    Combines research-related signals from all 3 sources into one 0-100 score:
    - QS: citations_per_faculty_score_2025 (already 0-100, used as-is)
    - Times: 'research' and 'citations' sub-scores (normalized)
    - Shanghai: 'pub' and 'hici' (publication count, highly-cited researchers; normalized)
    """
    qs_component = df['citations_per_faculty_score_2025']
    times_research = normalize_score(df['research'])
    times_citations = normalize_score(df['citations'])
    shanghai_pub = normalize_score(df['pub'])
    shanghai_hici = normalize_score(df['hici'])

    df['research_impact_score'] = pd.concat(
        [qs_component, times_research, times_citations, shanghai_pub, shanghai_hici],
        axis=1
    ).mean(axis=1)
    return df


def calculate_faculty_student_ratio(df):
    """
    Primary source: Times 'student_staff_ratio' (raw ratio, e.g. 12.3).
    Fallback: QS 'faculty_student_score_2025' is a SCORE (0-100), not a raw
    ratio, so it is NOT blended with the Times value -- units are different
    and averaging them would be meaningless. Source is flagged for transparency.
    """
    df['faculty_student_ratio'] = df['student_staff_ratio']
    df['faculty_student_ratio_source'] = np.where(
        df['student_staff_ratio'].notna(), 'Times (raw ratio)',
        np.where(df['faculty_student_score_2025'].notna(), 'QS (score, not ratio)', 'Missing')
    )
    return df


def calculate_international_student_pct(df):
    """
    Primary source: Times 'international_students' (raw percentage, stored
    as a string like '15%' -- converted to numeric here).
    Fallback: QS 'international_students_score_2025' is a SCORE, not a raw
    percentage, so it's flagged separately rather than blended in.
    """
    df['international_student_pct'] = (
        df['international_students']
        .astype(str)
        .str.replace('%', '', regex=False)
        .replace('nan', np.nan)
    )
    df['international_student_pct'] = pd.to_numeric(
        df['international_student_pct'], errors='coerce'
    )
    df['international_student_pct_source'] = np.where(
        df['international_students'].notna(), 'Times (raw %)',
        np.where(df['international_students_score_2025'].notna(), 'QS (score, not %)', 'Missing')
    )
    return df


def calculate_academic_reputation_score(df):
    """
    Average of QS 2025 and QS 2024 academic reputation scores. Both are
    already on a 0-100 scale from the same source, so a direct average is
    valid (no normalization needed).
    """
    df['academic_reputation_score'] = df[
        ['academic_reputation_score_2025', 'academic_reputation_score_2024']
    ].mean(axis=1)
    return df


def calculate_research_productivity_index(df):
    """
    Combines Shanghai's raw research-output indicators (pub = publications,
    hici = highly-cited researchers, award = Nobel/Fields awardees,
    alumni = award-winning alumni) with Times' 'research' reputation score.
    All normalized to 0-100 first since raw scales differ substantially.
    """
    pub_norm = normalize_score(df['pub'])
    hici_norm = normalize_score(df['hici'])
    award_norm = normalize_score(df['award'])
    alumni_norm = normalize_score(df['alumni'])
    times_research_norm = normalize_score(df['research'])

    df['research_productivity_index'] = pd.concat(
        [pub_norm, hici_norm, award_norm, alumni_norm, times_research_norm],
        axis=1
    ).mean(axis=1)
    return df


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def main():
    INPUT_FILE = "university_cleaned.csv"
    OUTPUT_FILE = "university_final_dataset.xlsx"

    print("Loading cleaned dataset...")
    df = pd.read_csv(INPUT_FILE)
    print(f"  Loaded: {df.shape}")

    print("Deduplicating multi-year merge artifacts...")
    df = deduplicate_multiyear_rows(df)
    print(f"  After year-collapse: {df.shape}")

    print("Deduplicating near-matching university names...")
    df = deduplicate_near_matching_names(df)
    print(f"  After name-normalization: {df.shape}")

    print("Calculating KPIs...")
    df = calculate_global_ranking_score(df)
    df = calculate_research_impact_score(df)
    df = calculate_faculty_student_ratio(df)
    df = calculate_international_student_pct(df)
    df = calculate_academic_reputation_score(df)
    df = calculate_research_productivity_index(df)
    print("  All 6 KPIs calculated.")

    print(f"Saving final dataset to {OUTPUT_FILE}...")
    df.to_excel(OUTPUT_FILE, index=False)
    print(f"  Saved: {df.shape}")

    print("\nDone. Module 3 complete.")


if __name__ == "__main__":
    main()