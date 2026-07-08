import pandas as pd

# =====================================================
# LOAD DATASETS
# =====================================================

top1000 = pd.read_csv("Top 1000 Universities Worldwide.csv")
qs = pd.read_csv("2024 QS World University Rankings 1.1 (For qs.com).csv")
the = pd.read_csv("THE World University Rankings 2016-2026.csv")
cwur = pd.read_csv("WORLD UNIVERSITY RANKINGS.csv")
top100 = pd.read_csv("top_100_universities_dataset.csv")
unilist = pd.read_csv("list_of_universities.csv")

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
    "Merged_Raw_Dataset.csv",
    index=False
)

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