import pandas as pd
import numpy as np

def clean_and_merge_pipeline():
    print("Loading consolidated raw database...")
    df = pd.read_csv("university_raw_data.csv", low_memory=False)
    
    print(" Merging overlapping suffixes and clearing text flags...")
    
    # 1. Safely handle duplicated join suffixes if they exist
    df['country'] = df['Country_x'].fillna(df.get('Country Code', np.nan)).fillna('Unknown')
    
    for base_col in ['city', 'region', 'type']:
        x_col = f'{base_col}_x'
        y_col = f'{base_col}_y'
        
        # Pull existing raw columns or create an empty fallback series
        s_base = df[base_col] if base_col in df.columns else pd.Series(np.nan, index=df.index)
        s_x = df[x_col] if x_col in df.columns else pd.Series(np.nan, index=df.index)
        s_y = df[y_col] if y_col in df.columns else pd.Series(np.nan, index=df.index)
        
        # Coalesce values
        if base_col == 'type':
            df['university_type'] = s_base.fillna(s_x).fillna(s_y).fillna('Unknown')
        else:
            df[base_col] = s_base.fillna(s_x).fillna(s_y).fillna('Unknown')

    # Handle faculty count duplicates safely
    s_fac = df['faculty_count'] if 'faculty_count' in df.columns else pd.Series(np.nan, index=df.index)
    s_fac_x = df['faculty_count_x'] if 'faculty_count_x' in df.columns else pd.Series(np.nan, index=df.index)
    s_fac_y = df['faculty_count_y'] if 'faculty_count_y' in df.columns else pd.Series(np.nan, index=df.index)
    df['faculty_count'] = s_fac.fillna(s_fac_x).fillna(s_fac_y).fillna(0)

    # 2. Standardize Missing Value Tokens
    sentinels = [-1, -1.0, '-1', '-1.0', 'Unknown', 'unknown', 'NaN', 'nan']
    
    numeric_metrics = [
        'Academic Reputation Score', 'Employer Reputation Score', 'Faculty Student Score', 
        'Citations per Faculty Score', 'International Faculty Score', 'International Students Score', 
        'International Research Network Score', 'Employment Outcomes Score', 'Sustainability Score', \
        'Overall SCORE', 'Overall Score', 'Teaching', 'Research Environment', 'Research Quality', \
        'Industry Impact', 'International Outlook', 'citations_score', 'research_output_score',\
        'country_avg_overall_score', 'country_avg_academic_reputation', 'country_avg_citations', \
        'country_avg_international_ratio', 'research_productivity_index', 'female_percentage', 'male_percentage'
    ]
    
    for col in numeric_metrics:
        if col in df.columns:
            df[col] = df[col].replace(sentinels, np.nan)
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # 3. Clean and Standardize Integer Counts
    integer_metrics = [
        'Student Population', 'Students to Staff Ratio', 'Citations_Count', \
        'universities_ranked_count', 'best_university_rank'
    ]
    for col in integer_metrics:
        if col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].astype(str).str.replace(',', '', regex=False)
            df[col] = df[col].replace(sentinels, np.nan)
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # 4. Parse Ranks from Strings to Clean Integers
    for rank_col in ['World Rank', 'National_Rank_x']:
        if rank_col in df.columns:
            df[rank_col] = df[rank_col].astype(str).str.replace('+', '', regex=False)
            df[rank_col] = df[rank_col].str.split('-').str[0]
            df[rank_col] = pd.to_numeric(df[rank_col], errors='coerce').fillna(999)

    # 5. Extract Ratios into explicit metrics if present
    if 'female_percentage' not in df.columns:
        df['female_percentage'] = np.nan
    if 'male_percentage' not in df.columns:
        df['male_percentage'] = np.nan

    if 'Female to Male Ratio' in df.columns and pd.Series(df['female_percentage']).isnull().all():
        def extract_female(val):
            if pd.isna(val) or not isinstance(val, str): return 50.0
            parts = [p.strip() for p in val.split(':') if p.strip().isdigit()]
            if len(parts) >= 2:
                tot = float(parts[0]) + float(parts[1])
                return round((float(parts[0]) / tot) * 100, 2) if tot > 0 else 50.0
            return 50.0
        df['female_percentage'] = df['Female to Male Ratio'].apply(extract_female)
        df['male_percentage'] = 100 - df['female_percentage']

    # 6. Apply Safe Fallback Defaults to Handle Missing Context Columns
    df['university_name'] = df['University'].fillna('Unknown') if 'University' in df.columns else 'Unknown'
    df['subject_field'] = df['subject_field'].fillna('General') if 'subject_field' in df.columns else 'General'
    df['gender_ratio'] = df['Female to Male Ratio'].fillna('50:50') if 'Female to Male Ratio' in df.columns else '50:50'
    df['degree_level'] = df['degree_level'].fillna('Undergraduate & Postgraduate') if 'degree_level' in df.columns else 'Undergraduate & Postgraduate'

    # 7. Apply target structural blueprint mapping exactly to the 38 pillars
    target_schema_38 = [
        'university_id', 'university_name', 'Year', 'World Rank', 'National_Rank_x', 
        'Overall SCORE', 'country', 'region', 'city', 'university_type',
        'Academic Reputation Score', 'Employer Reputation Score', 'citations_score',
        'Research_Output_x', 'Citations_Count', 'Citations per Faculty Score', 
        'research_output_score', 'research_productivity_index', 'subject_field', 
        'Student Population', 'International Students', 'faculty_count', 
        'Students to Staff Ratio', 'gender_ratio', 'female_percentage', 'male_percentage', 
        'degree_level', 'Enrollment', 'country_avg_rank', 'universities_ranked_count', 
        'best_university_rank', 'country_avg_overall_score', 'country_avg_academic_reputation', 
        'country_avg_citations', 'country_avg_international_ratio', 'Teaching', 
        'Research Environment', 'Research Quality'
    ]

    # Force create structural missing columns as clean null spaces
    for item in target_schema_38:
        if item not in df.columns:
            df[item] = np.nan

    df_output = df[target_schema_38].copy()

    # Rename variables into clean production metrics aligned with the blueprint
    df_output.rename(columns={
        'Year': 'year',
        'World Rank': 'world_rank',
        'National_Rank_x': 'national_rank',
        'Overall SCORE': 'overall_score',
        'Research_Output_x': 'publications_count',
        'Student Population': 'total_students',
        'Students to Staff Ratio': 'faculty_to_student_ratio',
        'International Students': 'international_students_count'
    }, inplace=True)

    # Remove duplicated indexing constraints cleanly
    df_output.drop_duplicates(subset=['university_id', 'year'], inplace=True)
    
    # Export clean structure
    df_output.to_csv("university_cleaned.csv", index=False)
    print(f" Success! Generated 'university_cleaned.csv' with exactly {df_output.shape[1]} columns ready for dashboard calculations.")

if __name__ == "__main__":
    clean_and_merge_pipeline()