"""
EduVision_DV — Module 3: KPI Engineering
Generates six KPIs from university_cleaned.csv for the final dataset.

Input:  data/processed/university_cleaned.csv
Output: data/final/university_final_dataset.xlsx

KPIs:
1. Global Ranking Score
2. Research Impact Score
3. Faculty-to-Student Ratio
4. International Student Percentage
5. Academic Reputation Score
6. Research Productivity Index
"""
import pandas as pd
import numpy as np
import os
import sys
import warnings
warnings.filterwarnings('ignore')
sys.stdout.reconfigure(encoding='utf-8')

# =============================================================================
# CONFIGURATION
# =============================================================================
INPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'university_cleaned.csv')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'final')
OUTPUT_PATH = os.path.join(OUTPUT_DIR, 'university_final_dataset.xlsx')
REPORT_PATH = os.path.join(os.path.dirname(__file__), '..', 'reports', 'kpi_engineering_report.md')

# =============================================================================
# KPI DEFINITIONS
# =============================================================================
# Each KPI is defined with:
# - name: KPI column name
# - description: What the KPI measures
# - source_columns: Columns used in calculation
# - formula: How the KPI is calculated
# - normalize: Whether normalization is applied

KPI_DEFINITIONS = {
    'global_ranking_score': {
        'description': 'Composite score combining QS and THE overall scores (0-100 scale)',
        'source_columns': ['qs_overall_score', 'the_overall_score'],
        'formula': 'Weighted average of QS and THE overall scores, normalized to 0-100',
        'normalize': True,
    },
    'research_impact_score': {
        'description': 'Composite score measuring research quality and impact',
        'source_columns': ['qs_citations_per_faculty', 'the_research_quality', 'the_research_environment'],
        'formula': 'Weighted average of citations per faculty, research quality, and research environment, normalized to 0-100',
        'normalize': True,
    },
    'faculty_student_ratio': {
        'description': 'Number of students per faculty member',
        'source_columns': ['students_per_staff'],
        'formula': 'Direct value from students_per_staff (lower is better)',
        'normalize': False,
    },
    'international_student_percentage': {
        'description': 'Percentage of international students',
        'source_columns': ['international_students_pct'],
        'formula': 'Direct value from international_students_pct',
        'normalize': False,
    },
    'academic_reputation_score': {
        'description': 'QS Academic Reputation Score (0-100 scale)',
        'source_columns': ['qs_academic_reputation'],
        'formula': 'Direct value from qs_academic_reputation, normalized to 0-100',
        'normalize': True,
    },
    'research_productivity_index': {
        'description': 'Composite measure of research output and citation impact',
        'source_columns': ['publications_count', 'citations_count', 'h_index'],
        'formula': 'Geometric mean of normalized publications, citations, and h-index, scaled to 0-100',
        'normalize': True,
    },
}


def load_data():
    """Load the cleaned dataset."""
    df = pd.read_csv(INPUT_PATH)
    print(f'Loaded: {INPUT_PATH}')
    print(f'Shape: {df.shape[0]} rows x {df.shape[1]} columns')
    return df


def normalize_min_max(series):
    """Normalize a series to 0-100 scale using min-max normalization."""
    min_val = series.min()
    max_val = series.max()
    if max_val == min_val:
        return pd.Series([50.0] * len(series), index=series.index)
    return ((series - min_val) / (max_val - min_val)) * 100


def compute_global_ranking_score(df):
    """
    KPI 1: Global Ranking Score
    
    Combines QS Overall Score and THE Overall Score into a single composite score.
    Uses weighted average (60% QS, 40% THE) to account for different methodologies.
    Both scores are on 0-100 scale, so no additional normalization needed.
    
    Formula: 0.6 * qs_overall_score + 0.4 * the_overall_score
    """
    print('\nKPI 1: Global Ranking Score')
    print('-' * 50)
    
    # Check source columns exist
    assert 'qs_overall_score' in df.columns, 'qs_overall_score not found'
    assert 'the_overall_score' in df.columns, 'the_overall_score not found'
    
    # Weighted average: 60% QS, 40% THE
    # Both are already on 0-100 scale
    qs_weight = 0.6
    the_weight = 0.4
    
    # Calculate composite score
    # If both exist, use weighted average
    # If only one exists, use that one
    df['global_ranking_score'] = np.where(
        (df['qs_overall_score'] > 0) & (df['the_overall_score'] > 0),
        qs_weight * df['qs_overall_score'] + the_weight * df['the_overall_score'],
        np.where(
            df['qs_overall_score'] > 0,
            df['qs_overall_score'],
            df['the_overall_score']
        )
    )
    
    # Normalize to 0-100 if needed
    if df['global_ranking_score'].max() > 100:
        df['global_ranking_score'] = normalize_min_max(df['global_ranking_score'])
    
    print(f'  Source: qs_overall_score (60%), the_overall_score (40%)')
    print(f'  Missing: {df["global_ranking_score"].isna().sum()}')
    print(f'  Range: {df["global_ranking_score"].min():.1f} - {df["global_ranking_score"].max():.1f}')
    print(f'  Mean: {df["global_ranking_score"].mean():.1f}')
    
    return df


def compute_research_impact_score(df):
    """
    KPI 2: Research Impact Score
    
    Combines three research quality metrics into a single score.
    Uses weighted average to account for different scales.
    
    Formula: 0.4 * citations_per_faculty + 0.35 * research_quality + 0.25 * research_environment
    All components normalized to 0-100 before averaging.
    """
    print('\nKPI 2: Research Impact Score')
    print('-' * 50)
    
    assert 'qs_citations_per_faculty' in df.columns, 'qs_citations_per_faculty not found'
    assert 'the_research_quality' in df.columns, 'the_research_quality not found'
    assert 'the_research_environment' in df.columns, 'the_research_environment not found'
    
    # Normalize each component to 0-100
    cpf_norm = normalize_min_max(df['qs_citations_per_faculty'])
    rq_norm = normalize_min_max(df['the_research_quality'])
    re_norm = normalize_min_max(df['the_research_environment'])
    
    # Weighted average
    df['research_impact_score'] = (
        0.40 * cpf_norm +
        0.35 * rq_norm +
        0.25 * re_norm
    )
    
    print(f'  Source: qs_citations_per_faculty (40%), the_research_quality (35%), the_research_environment (25%)')
    print(f'  Missing: {df["research_impact_score"].isna().sum()}')
    print(f'  Range: {df["research_impact_score"].min():.1f} - {df["research_impact_score"].max():.1f}')
    print(f'  Mean: {df["research_impact_score"].mean():.1f}')
    
    return df


def compute_faculty_student_ratio(df):
    """
    KPI 3: Faculty-to-Student Ratio
    
    Direct use of students_per_staff from THE Key Statistics.
    Lower values indicate more faculty per student (better).
    
    Formula: students_per_staff (direct value)
    """
    print('\nKPI 3: Faculty-to-Student Ratio')
    print('-' * 50)
    
    assert 'students_per_staff' in df.columns, 'students_per_staff not found'
    
    df['faculty_student_ratio'] = df['students_per_staff']
    
    print(f'  Source: students_per_staff')
    print(f'  Missing: {df["faculty_student_ratio"].isna().sum()}')
    print(f'  Range: {df["faculty_student_ratio"].min():.1f} - {df["faculty_student_ratio"].max():.1f}')
    print(f'  Mean: {df["faculty_student_ratio"].mean():.1f}')
    
    return df


def compute_international_student_percentage(df):
    """
    KPI 4: International Student Percentage
    
    Direct use of international_students_pct from THE Key Statistics.
    
    Formula: international_students_pct (direct value)
    """
    print('\nKPI 4: International Student Percentage')
    print('-' * 50)
    
    assert 'international_students_pct' in df.columns, 'international_students_pct not found'
    
    df['international_student_percentage'] = df['international_students_pct']
    
    print(f'  Source: international_students_pct')
    print(f'  Missing: {df["international_student_percentage"].isna().sum()}')
    print(f'  Range: {df["international_student_percentage"].min():.1f} - {df["international_student_percentage"].max():.1f}')
    print(f'  Mean: {df["international_student_percentage"].mean():.1f}')
    
    return df


def compute_academic_reputation_score(df):
    """
    KPI 5: Academic Reputation Score
    
    Direct use of qs_academic_reputation from QS Rankings.
    Already on 0-100 scale.
    
    Formula: qs_academic_reputation (direct value)
    """
    print('\nKPI 5: Academic Reputation Score')
    print('-' * 50)
    
    assert 'qs_academic_reputation' in df.columns, 'qs_academic_reputation not found'
    
    df['academic_reputation_score'] = df['qs_academic_reputation']
    
    print(f'  Source: qs_academic_reputation')
    print(f'  Missing: {df["academic_reputation_score"].isna().sum()}')
    print(f'  Range: {df["academic_reputation_score"].min():.1f} - {df["academic_reputation_score"].max():.1f}')
    print(f'  Mean: {df["academic_reputation_score"].mean():.1f}')
    
    return df


def compute_research_productivity_index(df):
    """
    KPI 6: Research Productivity Index
    
    Composite measure combining publications, citations, and h-index.
    Uses geometric mean to balance different scales.
    
    Formula: geometric_mean(normalized_publications, normalized_citations, normalized_h_index) * 100
    All components normalized to 0-100 before geometric mean.
    """
    print('\nKPI 6: Research Productivity Index')
    print('-' * 50)
    
    assert 'publications_count' in df.columns, 'publications_count not found'
    assert 'citations_count' in df.columns, 'citations_count not found'
    assert 'h_index' in df.columns, 'h_index not found'
    
    # Normalize each component to 0-100
    pub_norm = normalize_min_max(df['publications_count'])
    cit_norm = normalize_min_max(df['citations_count'])
    h_norm = normalize_min_max(df['h_index'])
    
    # Add small constant to avoid log(0) in geometric mean
    epsilon = 0.01
    
    # Geometric mean
    df['research_productivity_index'] = (
        ((pub_norm + epsilon) * (cit_norm + epsilon) * (h_norm + epsilon)) ** (1/3)
    ) - epsilon
    
    # Scale to 0-100
    df['research_productivity_index'] = normalize_min_max(df['research_productivity_index'])
    
    print(f'  Source: publications_count, citations_count, h_index')
    print(f'  Method: Geometric mean of normalized components')
    print(f'  Missing: {df["research_productivity_index"].isna().sum()}')
    print(f'  Range: {df["research_productivity_index"].min():.1f} - {df["research_productivity_index"].max():.1f}')
    print(f'  Mean: {df["research_productivity_index"].mean():.1f}')
    
    return df


def validate_kpis(df):
    """Validate that all KPIs are properly created."""
    print('\n' + '=' * 70)
    print('KPI VALIDATION')
    print('=' * 70)
    
    kpi_cols = [
        'global_ranking_score', 'research_impact_score', 'faculty_student_ratio',
        'international_student_percentage', 'academic_reputation_score',
        'research_productivity_index'
    ]
    
    all_valid = True
    
    for kpi in kpi_cols:
        if kpi in df.columns:
            missing = df[kpi].isna().sum()
            min_val = df[kpi].min()
            max_val = df[kpi].max()
            mean_val = df[kpi].mean()
            
            status = 'PASS' if missing == 0 else f'WARN ({missing} missing)'
            print(f'  {kpi:40s} {status}')
            print(f'    Range: {min_val:.2f} - {max_val:.2f}, Mean: {mean_val:.2f}')
            
            if missing > 0:
                all_valid = False
        else:
            print(f'  {kpi:40s} FAIL (column not created)')
            all_valid = False
    
    print()
    if all_valid:
        print('All KPIs validated successfully.')
    else:
        print('WARNING: Some KPIs have issues.')
    
    return all_valid


def generate_kpi_report(df):
    """Generate a KPI engineering report."""
    kpi_cols = [
        'global_ranking_score', 'research_impact_score', 'faculty_student_ratio',
        'international_student_percentage', 'academic_reputation_score',
        'research_productivity_index'
    ]
    
    report = []
    report.append('# KPI Engineering Report')
    report.append('')
    report.append('**Module:** 3 — KPI Engineering')
    report.append('**Input:** `data/processed/university_cleaned.csv`')
    report.append('**Output:** `data/final/university_final_dataset.xlsx`')
    report.append('')
    report.append('---')
    report.append('')
    report.append('## KPI Summary')
    report.append('')
    report.append('| KPI | Formula | Source Columns | Missing | Min | Max | Mean |')
    report.append('|-----|---------|----------------|---------|-----|-----|------|')
    
    for kpi_name in kpi_cols:
        if kpi_name in df.columns:
            kpi_def = KPI_DEFINITIONS[kpi_name]
            missing = df[kpi_name].isna().sum()
            min_val = df[kpi_name].min()
            max_val = df[kpi_name].max()
            mean_val = df[kpi_name].mean()
            sources = ', '.join(kpi_def['source_columns'])
            formula = kpi_def['formula'][:60] + '...' if len(kpi_def['formula']) > 60 else kpi_def['formula']
            
            report.append(f'| {kpi_name} | {formula} | {sources} | {missing} | {min_val:.1f} | {max_val:.1f} | {mean_val:.1f} |')
    
    report.append('')
    report.append('---')
    report.append('')
    report.append('## KPI Details')
    report.append('')
    
    for kpi_name in kpi_cols:
        if kpi_name in df.columns:
            kpi_def = KPI_DEFINITIONS[kpi_name]
            report.append(f'### {kpi_name}')
            report.append('')
            report.append(f'**Description:** {kpi_def["description"]}')
            report.append('')
            report.append(f'**Formula:** {kpi_def["formula"]}')
            report.append('')
            report.append(f'**Source Columns:** {", ".join(kpi_def["source_columns"])}')
            report.append('')
            report.append(f'**Normalization:** {"Yes (min-max to 0-100)" if kpi_def["normalize"] else "No (direct value)"}')
            report.append('')
            
            # Statistics
            missing = df[kpi_name].isna().sum()
            report.append(f'**Statistics:**')
            report.append(f'- Missing values: {missing}')
            report.append(f'- Min: {df[kpi_name].min():.2f}')
            report.append(f'- Max: {df[kpi_name].max():.2f}')
            report.append(f'- Mean: {df[kpi_name].mean():.2f}')
            report.append(f'- Std: {df[kpi_name].std():.2f}')
            report.append('')
    
    report.append('---')
    report.append('')
    report.append('## Dashboard Compatibility')
    report.append('')
    report.append('| Dashboard | KPIs Used | Status |')
    report.append('|-----------|-----------|--------|')
    report.append('| University Overview | global_ranking_score, academic_reputation_score | COMPATIBLE |')
    report.append('| Research Analytics | research_impact_score, research_productivity_index | COMPATIBLE |')
    report.append('| Student Analytics | faculty_student_ratio, international_student_percentage | COMPATIBLE |')
    report.append('| Country Comparison | global_ranking_score | COMPATIBLE |')
    report.append('')
    report.append('---')
    report.append('')
    report.append('*Report generated by Module 3: KPI Engineering*')
    
    return '\n'.join(report)


def main():
    """Main execution function."""
    print('=' * 70)
    print('EduVision_DV — Module 3: KPI Engineering')
    print('=' * 70)
    
    # Load data
    df = load_data()
    initial_cols = len(df.columns)
    
    # Compute KPIs
    df = compute_global_ranking_score(df)
    df = compute_research_impact_score(df)
    df = compute_faculty_student_ratio(df)
    df = compute_international_student_percentage(df)
    df = compute_academic_reputation_score(df)
    df = compute_research_productivity_index(df)
    
    # Validate
    validate_kpis(df)
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Export to Excel
    df.to_excel(OUTPUT_PATH, index=False, engine='openpyxl')
    print(f'\nExported: {OUTPUT_PATH}')
    print(f'Shape: {df.shape[0]} rows x {df.shape[1]} columns')
    print(f'New columns added: {len(df.columns) - initial_cols}')
    
    # Generate report
    report = generate_kpi_report(df)
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f'Report: {REPORT_PATH}')
    
    print('\n' + '=' * 70)
    print('MODULE 3 COMPLETE')
    print('=' * 70)


if __name__ == '__main__':
    main()
