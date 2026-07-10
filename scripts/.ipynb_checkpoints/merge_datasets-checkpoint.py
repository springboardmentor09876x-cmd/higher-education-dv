import pandas as pd

# =====================================================
# LOAD DATASETS
# =====================================================

top1000 = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\Top 1000 Universities Worldwide.csv")
qs = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\2024 QS World University Rankings 1.1 (For qs.com).csv")
the = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\THE World University Rankings 2016-2026.csv")
cwur = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\WORLD UNIVERSITY RANKINGS.csv")
top100 = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\top_100_universities_dataset.csv")
unilist = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\list_of_universities.csv")

print("All datasets loaded successfully!")

# =====================================================
# RENAME COLUMNS
# =====================================================

qs.rename(columns={
    "Institution Name": "University_Name",
    "2024 RANK": "QS_2024_Rank",
    "Overall SCORE": "QS_Overall_Score"
}, inplace=True)

the.rename(columns={
    "Name": "University_Name",
    "Rank": "THE_Rank_Current",
    "Overall Score": "THE_Overall_Score"
}, inplace=True)

cwur.rename(columns={
    "Institution": "University_Name",
    "Location": "Country",
    "World Rank": "CWUR_World_Rank",
    "National Rank": "CWUR_National_Rank",
    "Score": "CWUR_Score"
}, inplace=True)

unilist.rename(columns={
    "name": "University_Name",
    "country": "Country"
}, inplace=True)

# =====================================================
# KEEP REQUIRED COLUMNS
# =====================================================

top1000 = top1000[
[
'Country',
'University_Name',
'World_Rank',
'National_Rank',
'QS_Rank',
'THE_Rank',
'ARWU_Rank',
'Enrollment',
'Undergrad_Students',
'Postgrad_Students',
'Faculty_Count',
'Student_Faculty_Ratio',
'Research_Output',
'International_Students (%)',
'Tuition_Fee_USD',
'Acceptance_Rate (%)',
'Graduation_Rate (%)',
'Employability_Rank',
'QS_Subject_Rank'
]
]

qs = qs[
[
'University_Name',
'Country',
'QS_2024_Rank',
'Academic Reputation Score',
'Employer Reputation Score',
'Faculty Student Score',
'Citations per Faculty Score',
'International Faculty Score',
'International Students Score',
'International Research Network Score',
'Employment Outcomes Score',
'Sustainability Score',
'QS_Overall_Score'
]
]

the = the[
[
'University_Name',
'Country',
'THE_Rank_Current',
'Student Population',
'Students to Staff Ratio',
'International Students',
'THE_Overall_Score',
'Teaching',
'Research Environment',
'Research Quality',
'Industry Impact',
'International Outlook',
'Year'
]
]

# Keep only latest THE ranking (2026)
the = the[the["Year"] == 2026]

cwur = cwur[
[
'University_Name',
'Country',
'CWUR_World_Rank',
'CWUR_National_Rank',
'Education Rank',
'Employability Rank',
'Faculty Rank',
'Research Rank',
'CWUR_Score'
]
]

top100 = top100[
[
'University_Name',
'Established_Year',
'Total_Students',
'Number_of_Campuses',
'Programs_Offered',
'University_Type',
'Total_Faculty',
'Campus_Area_Acres'
]
]

unilist = unilist[
[
'id',
'University_Name',
'Country',
'country_code',
'web_pages'
]
]

# =====================================================
# STANDARDIZE KEYS
# =====================================================

datasets = [top1000, qs, the, cwur, top100, unilist]

for df in datasets:

    if "University_Name" in df.columns:
        df["University_Name"] = (
            df["University_Name"]
            .astype(str)
            .str.strip()
            .str.lower()
        )

    if "Country" in df.columns:
        df["Country"] = (
            df["Country"]
            .astype(str)
            .str.strip()
            .str.lower()
        )

print("Columns standardized successfully.")
print("Data ready for merging.")

# =====================================================
# MERGE DATASETS
# =====================================================

print("Merging datasets...")

# Start from University List (Master Dataset)
merged = unilist.copy()

# Merge QS
merged = merged.merge(
    qs,
    on=["University_Name", "Country"],
    how="left"
)

# Merge Top1000
merged = merged.merge(
    top1000,
    on=["University_Name", "Country"],
    how="left"
)

# Merge CWUR
merged = merged.merge(
    cwur,
    on=["University_Name", "Country"],
    how="left"
)

# Merge THE (2026 only)
merged = merged.merge(
    the,
    on=["University_Name", "Country"],
    how="left"
)

# Merge Top100
merged = merged.merge(
    top100,
    on="University_Name",
    how="left"
)

print("All datasets merged successfully.")

merged.to_csv(
    r"C:\Users\yadav\higher-education-dv\datasets\processed_data\Merged_Raw_Dataset.csv",
    index=False
)

print("\nMerged dataset saved successfully!")

print(merged.shape)
print(merged.head())

print("\n==============================")
print("FINAL DATASET INFORMATION")
print("==============================")

print("\nShape:")
print(merged.shape)

print("\nMissing values:")
print(merged.isnull().sum())

print("\nDuplicate Universities:")
print(merged.duplicated(subset=["University_Name"]).sum())

print("\nSample:")
print(merged.head(10))

#missing columns merging

cwur_data = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\cwurData.csv")
qs_2017_2022 = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\qs-world-university-rankings-2017-to-2022-V2.csv")

print("\nCWUR DATA COLUMNS")
print(cwur_data.columns.tolist())

print("\nQS 2017-2022 COLUMNS")
print(qs_2017_2022.columns.tolist())

# =====================================================
# RENAME NEW DATASETS
# =====================================================

# QS 2017-2022
qs_2017_2022.rename(columns={
    "university": "University_Name",
    "country": "Country",
    "city": "City",
    "region": "Region",
    "type": "University_Type",
    "research_output": "Research_Output_New",
    "student_faculty_ratio": "Student_Faculty_Ratio_New",
    "international_students": "International_Students_New",
    "faculty_count": "Faculty_Count_New"
}, inplace=True)

# CWUR DATA
cwur_data.rename(columns={
    "institution": "University_Name",
    "country": "Country",
    "publications": "Publications_Count",
    "citations": "Citations_Count",
    "quality_of_education": "Quality_of_Education",
    "quality_of_faculty": "Quality_of_Faculty",
    "alumni_employment": "Alumni_Employment",
    "influence": "Influence",
    "patents": "Patents",
    "score": "CWUR_Score_New"
}, inplace=True)

# Keep latest QS year
qs_2017_2022 = qs_2017_2022[qs_2017_2022["year"] == 2022]

qs_2017_2022 = qs_2017_2022[
    [
        "University_Name",
        "Country",
        "City",
        "Region",
        "University_Type",
        "Research_Output_New",
        "Student_Faculty_Ratio_New",
        "International_Students_New",
        "Faculty_Count_New"
    ]
]

# Keep latest CWUR year
cwur_data = cwur_data[cwur_data["year"] == 2015]

cwur_data = cwur_data[
    [
        "University_Name",
        "Country",
        "Publications_Count",
        "Citations_Count",
        "Quality_of_Education",
        "Quality_of_Faculty",
        "Alumni_Employment",
        "Influence",
        "Patents",
        "CWUR_Score_New"
    ]
]

# =====================================================
# STANDARDIZE NEW DATASETS
# =====================================================

for df in [qs_2017_2022, cwur_data]:

    df["University_Name"] = (
        df["University_Name"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    df["Country"] = (
        df["Country"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

print("New datasets standardized successfully!")

# =====================================================
# FUNCTION TO MERGE DATASETS SAFELY
# =====================================================

def merge_dataset(master_df, new_df, merge_keys):
    """
    Merge two datasets without creating duplicate columns.
    Existing values are kept; missing values are filled from the new dataset.
    """

    merged_df = master_df.merge(
        new_df,
        on=merge_keys,
        how="left",
        suffixes=("", "_new")
    )

    # Fill missing values from new dataset
    for col in new_df.columns:

        if col in merge_keys:
            continue

        new_col = col + "_new"

        if new_col in merged_df.columns:

            merged_df[col] = merged_df[col].fillna(
                merged_df[new_col]
            )

            merged_df.drop(columns=[new_col], inplace=True)

    return merged_df

# =====================================================
# MERGE QS 2017-2022
# =====================================================

print("\nMerging QS 2017-2022...")

merged = merge_dataset(
    merged,
    qs_2017_2022,
    ["University_Name", "Country"]
)

print("QS 2017-2022 merged successfully!")
print("Current Shape:", merged.shape)

# =====================================================
# MERGE CWUR DATA
# =====================================================

print("\nMerging CWUR Data...")

merged = merge_dataset(
    merged,
    cwur_data,
    ["University_Name", "Country"]
)

print("CWUR Data merged successfully!")
print("Current Shape:", merged.shape)

print("\nChecking new columns...")

new_cols = [
    "Publications_Count",
    "Citations_Count",
    "Quality_of_Education",
    "Quality_of_Faculty",
    "Alumni_Employment",
    "Influence",
    "Patents",
    "CWUR_Score_New"
]

for col in new_cols:
    if col in merged.columns:
        print(f"✅ {col}")
    else:
        print(f"❌ {col}")

qs2024 = pd.read_csv(
    r"C:\Users\yadav\higher-education-dv\datasets\raw_data\QS 2024.csv"
)
qs2024 = qs2024[
    [
        "University",
        "Country_x",
        "Quality_Publications",
        "Citations_Count",
        "city",
        "region",
        "type",
        "research_output",
        "student_faculty_ratio",
        "faculty_count",
        "female_percentage",
        "male_percentage",
        "subject_field",
        "research_productivity_index"
    ]
]
qs2024.rename(columns={
    "University": "University_Name",
    "Country_x": "Country",
    "type": "University_Type",
    "research_output": "Research_Output",
    "student_faculty_ratio": "Student_Faculty_Ratio",
    "faculty_count": "Faculty_Count"
}, inplace=True)

qs2024["University_Name"] = (
    qs2024["University_Name"]
    .astype(str)
    .str.strip()
    .str.lower()
)

qs2024["Country"] = (
    qs2024["Country"]
    .astype(str)
    .str.strip()
    .str.lower()
)
merged = merge_dataset(
    merged,
    qs2024,
    ["University_Name", "Country"]
)

print("QS 2024 merged successfully!")
print(merged.shape)

merged.to_csv(
    r"C:\Users\yadav\higher-education-dv\datasets\processed_data\Merged_Raw_Dataset.csv",
    index=False
)

print("Dataset saved successfully!")