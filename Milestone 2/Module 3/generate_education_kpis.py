import pandas as pd
import numpy as np
import os
import glob

def clean_num(series):
    """Helper function to convert percentage strings, commas, and text into numeric floats."""
    return pd.to_numeric(
        series.astype(str)
        .str.replace('%', '', regex=False)
        .str.replace(',', '', regex=False)
        .str.strip(),
        errors='coerce'
    )

def find_input_file(target_names):
    """Dynamically search for dataset files in current folder and subdirectories."""
    for name in target_names:
        matches = glob.glob(f"**/{name}", recursive=True)
        if matches:
            return matches[0]
            
    fallback_files = glob.glob("**/*university*.xlsx", recursive=True) + glob.glob("**/*university*.csv", recursive=True)
    if fallback_files:
        return fallback_files[0]
        
    return None

def generate_kpis(output_file="university_final_dataset.csv"):
    possible_inputs = [
        "university_cleaned.csv",
        "university_final_dataset.csv",
        "university_final_dataset.xlsx"
    ]
    
    input_file = find_input_file(possible_inputs)
    
    if not input_file:
        raise FileNotFoundError("Could not locate any dataset file (CSV/XLSX) in the directory or subfolders!")

    print(f" Loading input dataset: {input_file}...")
    
    if input_file.endswith('.xlsx'):
        df = pd.read_excel(input_file)
    else:
        df = pd.read_csv(input_file)
        
    print(f" Loaded {len(df)} rows and {len(df.columns)} columns.")
    print(" Calculating core Education KPIs...")

    # 1. Faculty-to-Student Ratio
    if 'faculty_count' in df.columns and 'total_students' in df.columns:
        fac_num = clean_num(df['faculty_count'])
        stud_num = clean_num(df['total_students'])
        df['faculty_to_student_ratio'] = np.where(
            stud_num > 0, 
            np.round(fac_num / stud_num, 4), 
            np.nan
        )

    # 2. International Student Percentage
    intl_col = next((c for c in df.columns if c.strip().lower() in ['international_student_ratio', 'international_students_count']), None)
    if intl_col:
        df['international_student_percentage'] = clean_num(df[intl_col])

    # 3. Global Ranking Score (Inverted 0-100 scale)
    rank_col = next((c for c in df.columns if c.strip().lower() in ['world_rank_numeric', 'world_rank']), None)
    if rank_col:
        wr_num = clean_num(df[rank_col])
        valid_ranks = wr_num[wr_num < 999]
        max_rank = valid_ranks.max() if not valid_ranks.empty else 1000
        min_rank = valid_ranks.min() if not valid_ranks.empty else 1
        df['global_ranking_score'] = np.where(
            wr_num < 999,
            np.round(100 - ((wr_num - min_rank) / (max_rank - min_rank) * 100), 2),
            0.0
        )

    # 4. Research Impact Score
    cit_fac_col = next((c for c in df.columns if 'citations per faculty' in c.lower() or 'citations_per_faculty' in c.lower()), None)
    cit_fac = clean_num(df[cit_fac_col]) if cit_fac_col else pd.Series(50, index=df.index)
    res_out = clean_num(df['research_output_score']) if 'research_output_score' in df.columns else pd.Series(50, index=df.index)
    cit_score = clean_num(df['citations_score']) if 'citations_score' in df.columns else pd.Series(50, index=df.index)
    
    df['research_impact_score'] = np.round(
        0.4 * cit_fac.fillna(cit_fac.median()) + 
        0.4 * res_out.fillna(res_out.median()) + 
        0.2 * cit_score.fillna(cit_score.median()), 2
    )

    # 5. Academic Reputation Score (Case-insensitive match)
    acad_rep_col = next((c for c in df.columns if c.strip().lower() in ['academic reputation score', 'academic_reputation_score']), None)
    if acad_rep_col:
        df['academic_reputation_score'] = clean_num(df[acad_rep_col]).fillna(50.0).round(2)

    # 6. Research Productivity Index (Fill missing publication counts with 0)
    pub_count = clean_num(df['publications_count']).fillna(0) if 'publications_count' in df.columns else pd.Series(0, index=df.index)
    max_pub = pub_count.max() if pub_count.max() > 0 else 1
    norm_pub = (pub_count / max_pub) * 100
    df['research_productivity_index'] = np.round(
        0.5 * norm_pub + 0.5 * res_out.fillna(res_out.median()), 2
    )

    # Export directly to CSV
    print(f" Saving output dataset to: {output_file}...")
    df.to_csv(output_file, index=False)
    print(" All KPIs generated and exported successfully!")

if __name__ == "__main__":
    generate_kpis()