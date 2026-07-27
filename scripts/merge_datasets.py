"""
EduVision_DV — Dataset Merge Script
Prepares and merges all approved source datasets into university_raw_data.csv.

Merge Strategy (from PROJECT_SPECIFICATION.md):
  - QS Rankings: University Name + Country + Year
  - THE Rankings: University Name + Country + Year
  - THE Key Statistics: University Name + Country + Year
  - World Bank Indicators: Country + Year (country-level, not university-level)
  - Research Metrics: University Name + Country + Year
  - Country Metrics: Country + Year (country-level, not university-level)
"""

import pandas as pd
import numpy as np
import os
import re

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
PROCESSED_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "processed")

# =============================================================================
# COUNTRY MAPPING — Standardize all country name variants to a single form
# =============================================================================
COUNTRY_MAP = {
    # China variants
    "China (Mainland)": "China",
    # Hong Kong variants
    "Hong Kong SAR": "Hong Kong",
    "Hong Kong Sar": "Hong Kong",
    "Hong Kong Sar, China": "Hong Kong",
    # Macau variants
    "Macao Sar, China": "Macau",
    "Macau SAR": "Macau",
    "Macau Sar": "Macau",
    "Macao": "Macau",
    # Iran variants
    "Iran (Islamic Republic Of)": "Iran",
    "Iran, Islamic Republic Of": "Iran",
    "Iran, Islamic Republic of": "Iran",
    # Korea variants
    "Republic Of Korea": "South Korea",
    # Russia variants
    "Russian Federation": "Russia",
    # Turkey variants
    "T\u00fcrkiye": "Turkey",
    # USA variants
    "United States Of America": "United States",
    # Venezuela variants
    "Venezuela (Bolivarian Republic Of)": "Venezuela",
    # Vietnam variants
    "Viet Nam": "Vietnam",
    # Brunei variants
    "Brunei Darussalam": "Brunei",
    # Czech variants
    "Czech Republic": "Czechia",
    # Bosnia variants (capitalization)
    "Bosnia And Herzegovina": "Bosnia and Herzegovina",
    # Palestine variants
    "Palestinian Territory, Occupied": "Palestine",
    # Syria variants
    "Syrian Arab Republic": "Syria",
    # Tanzania variants
    "Tanzania": "Tanzania",
    # Moldova variants
    "Moldova": "Moldova",
    # =====================================================================
    # World Bank naming conventions (added for merge fix)
    # =====================================================================
    # Egypt
    "Egypt, Arab Rep.": "Egypt",
    # Hong Kong
    "Hong Kong SAR, China": "Hong Kong",
    # Iran
    "Iran, Islamic Rep.": "Iran",
    # Kyrgyzstan
    "Kyrgyz Republic": "Kyrgyzstan",
    # Macau
    "Macao SAR, China": "Macau",
    # Puerto Rico
    "Puerto Rico (US)": "Puerto Rico",
    # Slovakia
    "Slovak Republic": "Slovakia",
    # Somalia
    "Somalia, Fed. Rep.": "Somalia",
    # Venezuela
    "Venezuela, RB": "Venezuela",
    # Yemen
    "Yemen, Rep.": "Yemen",
    # =====================================================================
    # Additional QS/THE country name variants
    # =====================================================================
    "Iran. Islamic Republic of": "Iran",
    "Palestinian Territory. Occupied": "Palestine",
}


def standardize_country(name):
    """Standardize a country name using the mapping table."""
    if pd.isna(name):
        return name
    name = str(name).strip()
    return COUNTRY_MAP.get(name, name)


def standardize_university_name(name):
    """Basic university name standardization for merge matching."""
    if pd.isna(name):
        return name
    name = str(name).strip()
    # Remove trailing whitespace and normalize spaces
    name = re.sub(r'\s+', ' ', name)
    return name


# =============================================================================
# STEP 1: Load and Standardize QS Rankings
# =============================================================================
def load_qs_rankings():
    """Load all QS ranking years and standardize to a common schema."""
    frames = []

    for year in [2020, 2021, 2022, 2023, 2024]:
        enc = 'latin-1' if year == 2020 else 'utf-8'
        sep = ';' if year == 2024 else ','
        skip = 3 if year == 2024 else (1 if year == 2020 else 0)
        df = pd.read_csv(os.path.join(RAW_DIR, 'qs_rankings_%d.csv' % year),
                         encoding=enc, sep=sep, skiprows=skip)

        # Standardize column names
        col_map = {}
        for c in df.columns:
            cl = c.lower().strip()
            if cl in ('rank in 2020', 'ranking', 'rank', 'rank display'):
                col_map[c] = 'qs_rank'
            elif cl == 'rank display2':
                col_map[c] = 'qs_rank_alt'
            elif cl == 'rank in 2019':
                col_map[c] = 'qs_rank_prev'
            elif cl in ('institution name', 'institution', 'university'):
                col_map[c] = 'university_name'
            elif cl == 'country' or cl == 'location':
                col_map[c] = 'country'
            elif cl == 'location code':
                col_map[c] = 'country_code'
            elif cl in ('academic reputation', 'ar score'):
                col_map[c] = 'qs_academic_reputation'
            elif cl in ('employer reputation', 'er score'):
                col_map[c] = 'qs_employer_reputation'
            elif cl in ('faculty student', 'fsr score'):
                col_map[c] = 'qs_faculty_student'
            elif cl in ('citations per faculty', 'cpf score'):
                col_map[c] = 'qs_citations_per_faculty'
            elif cl in ('international faculty', 'ifr score'):
                col_map[c] = 'qs_international_faculty'
            elif cl in ('international students', 'isr score'):
                col_map[c] = 'qs_international_students'
            elif cl in ('overall', 'overall score', 'score scaled'):
                col_map[c] = 'qs_overall_score'
            elif cl in ('size',):
                col_map[c] = 'qs_size'
            elif cl in ('focus',):
                col_map[c] = 'qs_focus'
            elif cl in ('res.', 'research'):
                col_map[c] = 'qs_research_intensity'
            elif cl in ('age', 'age band'):
                col_map[c] = 'qs_age'
            elif cl in ('status',):
                col_map[c] = 'qs_status'
            elif cl in ('code',):
                col_map[c] = 'qs_code'

        df = df.rename(columns=col_map)
        df['year'] = year
        df['source'] = 'qs_rankings'

        # Keep only standardized columns
        keep_cols = ['year', 'university_name', 'country', 'qs_rank', 'qs_overall_score',
                     'qs_academic_reputation', 'qs_employer_reputation', 'qs_faculty_student',
                     'qs_citations_per_faculty', 'qs_international_faculty', 'qs_international_students',
                     'qs_size', 'qs_focus', 'qs_research_intensity', 'qs_age', 'qs_status', 'source']
        keep_cols = [c for c in keep_cols if c in df.columns]
        df = df[keep_cols]

        # Standardize names
        if 'university_name' in df.columns:
            df['university_name'] = df['university_name'].apply(standardize_university_name)
        if 'country' in df.columns:
            df['country'] = df['country'].apply(standardize_country)

        # Convert numeric columns
        for col in ['qs_rank', 'qs_overall_score', 'qs_academic_reputation',
                     'qs_employer_reputation', 'qs_faculty_student',
                     'qs_citations_per_faculty', 'qs_international_faculty',
                     'qs_international_students']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        frames.append(df)
        print('  QS %d: %d rows' % (year, len(df)))

    return pd.concat(frames, ignore_index=True)


# =============================================================================
# STEP 2: Load and Standardize THE Rankings
# =============================================================================
def load_the_rankings():
    """Load all THE ranking years and standardize to a common schema."""
    frames = []

    for year in [2020, 2021, 2022, 2023, 2024]:
        df = pd.read_csv(os.path.join(RAW_DIR, 'the_rankings_%d.csv' % year))

        df = df.rename(columns={
            'Name': 'university_name',
            'Country': 'country',
            'Rank': 'the_rank',
            'Overall': 'the_overall_score',
            'Teaching': 'the_teaching',
            'Research Environment': 'the_research_environment',
            'Research Quality': 'the_research_quality',
            'Industry': 'the_industry',
            'International Outlook': 'the_international_outlook',
        })

        df['source'] = 'the_rankings'

        keep_cols = ['year', 'university_name', 'country', 'the_rank', 'the_overall_score',
                     'the_teaching', 'the_research_environment', 'the_research_quality',
                     'the_industry', 'the_international_outlook', 'source']
        df = df[keep_cols]

        df['university_name'] = df['university_name'].apply(standardize_university_name)
        df['country'] = df['country'].apply(standardize_country)

        # Convert numeric columns
        for col in ['the_rank', 'the_overall_score', 'the_teaching',
                     'the_research_environment', 'the_research_quality',
                     'the_industry', 'the_international_outlook']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        frames.append(df)
        print('  THE Rankings %d: %d rows' % (year, len(df)))

    return pd.concat(frames, ignore_index=True)


# =============================================================================
# STEP 3: Load and Standardize THE Key Statistics
# =============================================================================
def load_the_key_statistics():
    """Load all THE Key Statistics years and standardize to a common schema."""
    frames = []

    for year in [2020, 2021, 2022, 2023, 2024]:
        df = pd.read_csv(os.path.join(RAW_DIR, 'the_key_statistics_%d.csv' % year))

        df = df.rename(columns={
            'Name': 'university_name',
            'Country': 'country',
            'Rank': 'the_ks_rank',
            'No. of FTE students': 'total_fte_students',
            'No. of students per staff': 'students_per_staff',
            'International students': 'international_students_pct',
            'Female:Male ratio': 'female_male_ratio',
        })

        df['source'] = 'the_key_statistics'

        keep_cols = ['year', 'university_name', 'country', 'the_ks_rank',
                     'total_fte_students', 'students_per_staff',
                     'international_students_pct', 'female_male_ratio', 'source']
        df = df[keep_cols]

        df['university_name'] = df['university_name'].apply(standardize_university_name)
        df['country'] = df['country'].apply(standardize_country)

        # Convert numeric columns
        df['students_per_staff'] = pd.to_numeric(df['students_per_staff'], errors='coerce')

        frames.append(df)
        print('  THE Key Stats %d: %d rows' % (year, len(df)))

    return pd.concat(frames, ignore_index=True)


# =============================================================================
# STEP 4: Load Research Metrics
# =============================================================================
def load_research_metrics():
    """Load research metrics and standardize."""
    df = pd.read_csv(os.path.join(RAW_DIR, 'research_metrics_raw.csv'))

    df = df.rename(columns={
        'university_name': 'university_name',
        'country': 'country',
        'world_rank': 'research_world_rank',
    })

    df['source'] = 'research_metrics'

    keep_cols = ['year', 'university_name', 'country', 'region',
                 'research_world_rank', 'citations_score', 'publications_count',
                 'citations_count', 'citations_per_faculty', 'h_index',
                 'research_output_score', 'research_productivity_index',
                 'subject_field', 'source']
    df = df[keep_cols]

    df['university_name'] = df['university_name'].apply(standardize_university_name)
    df['country'] = df['country'].apply(standardize_country)

    # Filter to project years only for merge
    df = df[df['year'].between(2020, 2024)]

    print('  Research Metrics (2020-2024): %d rows' % len(df))
    return df


# =============================================================================
# STEP 5: Load World Bank Indicators
# =============================================================================
def load_world_bank():
    """Load all 5 World Bank indicators and pivot to wide format."""
    indicators = {
        'world_bank_gdp_per_capita.csv': 'gdp_per_capita',
        'world_bank_population.csv': 'population',
        'world_bank_literacy_rate.csv': 'literacy_rate',
        'world_bank_education_expenditure.csv': 'education_expenditure_pct_gdp',
        'world_bank_tertiary_enrollment.csv': 'tertiary_enrollment_pct',
    }

    frames = []
    for fname, col_name in indicators.items():
        fpath = os.path.join(RAW_DIR, 'world_bank', 'csv', fname)
        if not os.path.exists(fpath):
            print('  WARNING: %s not found' % fname)
            continue
        df = pd.read_csv(fpath)
        df = df.rename(columns={'indicator_value': col_name})
        df['country_name'] = df['country_name'].apply(standardize_country)
        frames.append(df)
        print('  World Bank %s: %d rows' % (col_name, len(df)))

    if not frames:
        return pd.DataFrame()

    # Pivot each frame to have country_name, country_iso3code, year, and the indicator column
    pivoted = []
    for f in frames:
        indicator_col = [c for c in f.columns if c not in ('country_name', 'country_iso3code', 'year')][0]
        pivoted.append(f[['country_name', 'country_iso3code', 'year', indicator_col]])

    # Merge all on country_name + country_iso3code + year
    result = pivoted[0]
    for p in pivoted[1:]:
        indicator_col = [c for c in p.columns if c not in ('country_name', 'country_iso3code', 'year')][0]
        result = result.merge(
            p[['country_name', 'country_iso3code', 'year', indicator_col]],
            on=['country_name', 'country_iso3code', 'year'],
            how='outer'
        )

    result = result.rename(columns={'country_name': 'country'})
    result['source'] = 'world_bank'

    # Filter to project years
    result = result[result['year'].between(2020, 2024)]

    print('  World Bank (merged, 2020-2024): %d rows' % len(result))
    return result


# =============================================================================
# STEP 6: Load Country Metrics
# =============================================================================
def load_country_metrics():
    """Load country metrics and standardize."""
    df = pd.read_csv(os.path.join(RAW_DIR, 'country_metrics_raw.csv'))

    df = df.rename(columns={
        'country': 'country',
        'country_avg_rank': 'country_avg_rank',
        'universities_ranked_count': 'country_universities_ranked',
        'best_university_rank': 'country_best_rank',
        'country_avg_overall_score': 'country_avg_overall_score',
        'country_avg_academic_reputation': 'country_avg_academic_reputation',
        'country_avg_citations': 'country_avg_citations',
        'country_avg_international_ratio': 'country_avg_intl_ratio',
    })

    df['source'] = 'country_metrics'
    df['country'] = df['country'].apply(standardize_country)

    # Filter to project years
    df = df[df['year'].between(2020, 2024)]

    keep_cols = ['year', 'country', 'region', 'country_avg_rank',
                 'country_universities_ranked', 'country_best_rank',
                 'country_avg_overall_score', 'country_avg_academic_reputation',
                 'country_avg_citations', 'country_avg_intl_ratio', 'source']
    keep_cols = [c for c in keep_cols if c in df.columns]
    df = df[keep_cols]

    # Deduplicate: country standardization may create duplicates
    # (e.g., "China" + "China (Mainland)" -> both "China")
    before = len(df)
    df = df.drop_duplicates(subset=['country', 'year'], keep='first')
    after = len(df)
    if before != after:
        print('  Country Metrics deduplicated: %d -> %d rows (%d duplicates removed)' %
              (before, after, before - after))

    print('  Country Metrics (2020-2024): %d rows' % len(df))
    return df


# =============================================================================
# STEP 7: Handle QS 2022 Missing Country
# =============================================================================
def fix_qs_2022_country(qs_df):
    """QS 2022 has no Country column. Use THE data to fill."""
    print('\n  Fixing QS 2022 missing country...')

    # Load THE to get university -> country mapping
    uni_to_country = {}
    for year in [2020, 2021, 2022, 2023, 2024]:
        df = pd.read_csv(os.path.join(RAW_DIR, 'the_rankings_%d.csv' % year))
        for _, row in df.iterrows():
            uname = standardize_university_name(row['Name'])
            ctry = standardize_country(row['Country'])
            if uname not in uni_to_country:
                uni_to_country[uname] = ctry

    # Also build from QS data (other years have country)
    for year in [2020, 2021, 2023, 2024]:
        enc = 'latin-1' if year == 2020 else 'utf-8'
        sep = ';' if year == 2024 else ','
        skip = 3 if year == 2024 else (1 if year == 2020 else 0)
        df = pd.read_csv(os.path.join(RAW_DIR, 'qs_rankings_%d.csv' % year),
                         encoding=enc, sep=sep, skiprows=skip)
        col = 'Country' if 'Country' in df.columns else 'location'
        if col in df.columns:
            name_col = [c for c in df.columns if c.lower().strip() in ('institution name', 'institution', 'university')][0]
            for _, row in df.iterrows():
                uname = standardize_university_name(row[name_col])
                ctry = standardize_country(row[col])
                if uname not in uni_to_country:
                    uni_to_country[uname] = ctry

    # Fill missing countries in QS 2022
    qs_2022_mask = qs_df['year'] == 2022
    filled = 0
    for idx in qs_df[qs_2022_mask].index:
        uname = qs_df.at[idx, 'university_name']
        if pd.isna(qs_df.at[idx, 'country']) and uname in uni_to_country:
            qs_df.at[idx, 'country'] = uni_to_country[uname]
            filled += 1

    print('    Filled %d / %d missing countries' % (filled, qs_2022_mask.sum()))
    return qs_df


# =============================================================================
# STEP 8: Merge All Datasets
# =============================================================================
def merge_all():
    """Execute the full merge pipeline."""
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    print('=' * 70)
    print('MERGE PREPARATION')
    print('=' * 70)

    # Load all datasets
    print('\nLoading QS Rankings...')
    qs = load_qs_rankings()

    print('\nLoading THE Rankings...')
    the = load_the_rankings()

    print('\nLoading THE Key Statistics...')
    the_ks = load_the_key_statistics()

    print('\nLoading Research Metrics...')
    research = load_research_metrics()

    print('\nLoading World Bank Indicators...')
    wb = load_world_bank()

    print('\nLoading Country Metrics...')
    country_m = load_country_metrics()

    # Fix QS 2022 missing country
    qs = fix_qs_2022_country(qs)

    print('\n' + '=' * 70)
    print('MERGE EXECUTION')
    print('=' * 70)

    # -------------------------------------------------------------------------
    # Merge 1: QS + THE Rankings on university_name + country + year
    # -------------------------------------------------------------------------
    print('\nMerge 1: QS + THE Rankings...')
    merge_keys = ['university_name', 'country', 'year']

    qs_the = qs.merge(the, on=merge_keys, how='outer', suffixes=('_qs', '_the'))
    print('  QS rows: %d, THE rows: %d -> Merged: %d' % (len(qs), len(the), len(qs_the)))

    # Handle source column conflict
    if 'source_qs' in qs_the.columns and 'source_the' in qs_the.columns:
        qs_the['source'] = qs_the['source_qs'].fillna(qs_the['source_the'])
        qs_the = qs_the.drop(columns=['source_qs', 'source_the'])
    elif 'source' in qs_the.columns:
        pass  # already unified

    # -------------------------------------------------------------------------
    # Merge 2: QS+THE + THE Key Statistics
    # -------------------------------------------------------------------------
    print('Merge 2: + THE Key Statistics...')
    merge_keys_ks = ['university_name', 'country', 'year']
    # THE Key Statistics has its own rank column, avoid conflict
    the_ks_merge = the_ks.drop(columns=['the_ks_rank'], errors='ignore')
    main = qs_the.merge(the_ks_merge, on=merge_keys_ks, how='outer', suffixes=('', '_ks'))
    print('  Merged: %d rows' % len(main))

    # Handle duplicate source columns
    if 'source_ks' in main.columns:
        main['source'] = main['source'].fillna(main['source_ks'])
        main = main.drop(columns=['source_ks'])

    # -------------------------------------------------------------------------
    # Merge 3: + Research Metrics
    # -------------------------------------------------------------------------
    print('Merge 3: + Research Metrics...')
    # Research metrics has subject_field which creates multiple rows per university
    # Keep aggregate research metrics, merge on university + country + year
    research_agg = research.groupby(['university_name', 'country', 'year']).agg({
        'research_world_rank': 'mean',
        'citations_score': 'mean',
        'publications_count': 'sum',
        'citations_count': 'sum',
        'citations_per_faculty': 'mean',
        'h_index': 'mean',
        'research_output_score': 'mean',
        'research_productivity_index': 'mean',
    }).reset_index()

    main = main.merge(research_agg, on=merge_keys, how='outer', suffixes=('', '_research'))
    print('  Merged: %d rows' % len(main))

    # -------------------------------------------------------------------------
    # Merge 4: + World Bank (country-level, left join on country + year)
    # -------------------------------------------------------------------------
    print('Merge 4: + World Bank Indicators...')
    wb_cols = ['country', 'year', 'gdp_per_capita', 'population', 'literacy_rate',
               'education_expenditure_pct_gdp', 'tertiary_enrollment_pct']
    wb_merge = wb[[c for c in wb_cols if c in wb.columns]]

    main = main.merge(wb_merge, on=['country', 'year'], how='left')
    print('  Merged: %d rows' % len(main))

    # -------------------------------------------------------------------------
    # Merge 5: + Country Metrics (country-level, left join on country + year)
    # -------------------------------------------------------------------------
    print('Merge 5: + Country Metrics...')
    cm_cols = ['country', 'year', 'region', 'country_avg_rank', 'country_universities_ranked',
               'country_best_rank', 'country_avg_overall_score', 'country_avg_academic_reputation',
               'country_avg_citations', 'country_avg_intl_ratio']
    cm_merge = country_m[[c for c in cm_cols if c in country_m.columns]]

    main = main.merge(cm_merge, on=['country', 'year'], how='left', suffixes=('', '_cm'))
    print('  Merged: %d rows' % len(main))

    # -------------------------------------------------------------------------
    # Final cleanup
    # -------------------------------------------------------------------------
    # Ensure year is integer
    main['year'] = main['year'].astype(int)

    # Sort
    main = main.sort_values(['year', 'country', 'university_name']).reset_index(drop=True)

    # Save
    output_path = os.path.join(PROCESSED_DIR, 'university_raw_data.csv')
    main.to_csv(output_path, index=False, encoding='utf-8')

    print('\n' + '=' * 70)
    print('MERGE COMPLETE')
    print('=' * 70)
    print('Output: %s' % output_path)
    print('Total rows: %d' % len(main))
    print('Total columns: %d' % len(main.columns))
    print()
    print('Columns:')
    for c in main.columns:
        non_null = main[c].notna().sum()
        pct = non_null / len(main) * 100
        print('  %-40s %6d non-null (%5.1f%%)' % (c, non_null, pct))

    print()
    print('Rows by source:')
    if 'source' in main.columns:
        print(main['source'].value_counts().to_string())

    print()
    print('Rows by year:')
    print(main['year'].value_counts().sort_index().to_string())

    return main


if __name__ == "__main__":
    merge_all()
