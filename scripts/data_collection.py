import pandas as pd
import numpy as np
import re
import warnings

warnings.filterwarnings("ignore")

# ==========================
# Load Raw Datasets
# ==========================

world = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\WORLD UNIVERSITY RANKINGS.csv")

qs2024 = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\2024 QS World University Rankings 1.1 (For qs.com).csv")

cwur = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\cwurData.csv")

list_uni = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\list_of_universities.csv")

qs_full = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\QS 2024.csv")

qs_history = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\qs-world-university-rankings-2017-to-2022-V2.csv")

the = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\THE World University Rankings 2016-2026.csv")

top100 = pd.read_csv(r"C:\Users\yadav\higher-education-dv\datasets\raw_data\top_100_universities_dataset.csv")

print("✅ All datasets loaded successfully.")

# WORLD
world.rename(columns={
    "Institution":"University_Name",
    "Location":"Country"
}, inplace=True)

# QS2024
qs2024.rename(columns={
    "Institution Name":"University_Name"
}, inplace=True)

# CWUR
cwur.rename(columns={
    "institution":"University_Name",
    "country":"Country"
}, inplace=True)

# LIST
list_uni.rename(columns={
    "name":"University_Name",
    "country":"Country"
}, inplace=True)

# QS FULL
qs_full.rename(columns={
    "University":"University_Name",
    "Country_x":"Country"
}, inplace=True)

# QS HISTORY
qs_history.rename(columns={
    "university":"University_Name",
    "country":"Country"
}, inplace=True)

# THE
the.rename(columns={
    "Name":"University_Name"
}, inplace=True)

# TOP100
top100.rename(columns={
    "Location":"Country"
}, inplace=True)

print("✅ Columns standardized.")

# Remove duplicate header row
qs2024 = qs2024[
    qs2024["University_Name"]!="institution"
].reset_index(drop=True)

# Keep latest CWUR year
cwur = cwur[cwur["year"]==cwur["year"].max()].copy()

# Keep latest THE year
the = the[the["Year"]==the["Year"].max()].copy()

# Keep latest QS History year
qs_history = qs_history[
    qs_history["year"]==qs_history["year"].max()
].copy()

print("CWUR :", cwur.shape)
print("THE :", the.shape)
print("QS HISTORY :", qs_history.shape)

def clean_name(name):

    if pd.isna(name):
        return ""

    name=str(name).lower()

    name=re.sub(r"\(.*?\)","",name)

    name=re.sub(r"[^\w\s]","",name)

    name=name.replace("&","and")

    name=name.replace("the ","")

    name=name.replace("univ ","university ")

    name=re.sub(r"\s+"," ",name).strip()

    return name

datasets=[
    world,
    qs2024,
    cwur,
    list_uni,
    qs_full,
    qs_history,
    the,
    top100
]

for df in datasets:

    df["Merge_Key"]=df["University_Name"].apply(clean_name)

print("✅ Merge keys created.")

datasets = [
    world,
    qs2024,
    cwur,
    list_uni,
    qs_full,
    qs_history,
    the,
    top100
]

for df in datasets:

    df.drop_duplicates(
        subset="Merge_Key",
        inplace=True
    )

print("Duplicates removed.")

merged_df = qs_full.copy()

print("Base Dataset Shape :", merged_df.shape)

merged_df.head()

# ==========================================
# Merge THE Dataset
# ==========================================

the_merge = the[
    [
        "Merge_Key",
        "Teaching",
        "Research Environment",
        "Research Quality",
        "Industry Impact",
        "International Outlook"
    ]
].copy()

merged_df = merged_df.merge(
    the_merge,
    on="Merge_Key",
    how="left",
    suffixes=("", "_THE")
)

print(merged_df.shape)

# ==========================================
# Merge CWUR Dataset
# ==========================================

cwur_merge = cwur[
    [
        "Merge_Key",
        "quality_of_education",
        "alumni_employment",
        "quality_of_faculty",
        "publications",
        "influence",
        "citations",
        "broad_impact",
        "patents"
    ]
].copy()

merged_df = merged_df.merge(
    cwur_merge,
    on="Merge_Key",
    how="left"
)

print(merged_df.shape)

# ==========================================
# Merge WORLD Dataset
# ==========================================

world_merge = world[
    [
        "Merge_Key",
        "Education Rank",
        "Employability Rank",
        "Faculty Rank",
        "Research Rank"
    ]
].copy()

merged_df = merged_df.merge(
    world_merge,
    on="Merge_Key",
    how="left"
)

print(merged_df.shape)

print(merged_df.shape)
print(merged_df.isnull().sum().sort_values(ascending=False).head(20))

# Fill missing values from CWUR

mapping = {
    "Quality of Education": "quality_of_education",
    "Alumni Employment": "alumni_employment",
    "Quality of Faculty": "quality_of_faculty",
    "Influence": "influence",
    "Citations_Count": "citations",
    "Patents": "patents"
}

for main_col, cwur_col in mapping.items():

    if main_col in merged_df.columns and cwur_col in merged_df.columns:

        merged_df[main_col] = merged_df[main_col].fillna(
            merged_df[cwur_col]
        )

print("CWUR missing values filled successfully.")

drop_cols = [
    "quality_of_education",
    "alumni_employment",
    "quality_of_faculty",
    "publications",
    "influence",
    "citations",
    "broad_impact",
    "patents"
]

merged_df.drop(
    columns=[c for c in drop_cols if c in merged_df.columns],
    inplace=True
)

print(merged_df.shape)

website = list_uni[
    [
        "Merge_Key",
        "web_pages",
        "country_code"
    ]
].copy()

merged_df = merged_df.merge(
    website,
    on="Merge_Key",
    how="left"
)

print(merged_df.shape)

# Merge duplicate city columns

duplicate_columns = [
    ("city", "city_x"),
    ("city", "city_y"),
    ("region", "region_x"),
    ("region", "region_y"),
    ("faculty_count", "faculty_count_x"),
    ("faculty_count", "faculty_count_y"),
    ("student_faculty_ratio", "student_faculty_ratio_x"),
    ("student_faculty_ratio", "student_faculty_ratio_y"),
]

for main, duplicate in duplicate_columns:

    if main in merged_df.columns and duplicate in merged_df.columns:

        merged_df[main] = merged_df[main].fillna(
            merged_df[duplicate]
        )

        merged_df.drop(columns=duplicate, inplace=True)

print("Duplicate columns merged successfully.")

print(merged_df.shape)

print(
    merged_df.isnull()
             .sum()
             .sort_values(ascending=False)
             .head(25)
)

merged_df.to_csv(
    r"C:\Users\yadav\higher-education-dv\datasets\processed_data\university_raw_data.csv",
    index=False
)

print("Merged dataset saved successfully.")

print(merged_df.shape)
print(merged_df.duplicated().sum())
print(merged_df.isnull().sum().sort_values(ascending=False).head(30))
