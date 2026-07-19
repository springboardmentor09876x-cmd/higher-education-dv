import pandas as pd


qs = pd.read_csv("2024 QS World University Rankings 1.1 (For qs.com).csv")

the = pd.read_csv("THE World University Rankings 2016-2026 (1).csv")

qs = qs.rename(columns={'Institution Name':'University'})
the = the.rename(columns={'Name':'University'})

merged = pd.merge(
    qs,
    the_2024,
    on='University',
    how='inner'
)

merged.head()

merged.shape

merged.isnull().sum()

merged.info()

merged.to_csv("Merged_University_Rankings.csv", index=False)

merged.duplicated().sum()

(merged["Country_x"] == merged["Country_y"]).all()

merged[merged["Country_x"] != merged["Country_y"]][["University", "Country_x", "Country_y"]]

merged = merged.rename(columns={"Country_x": "Country"})
merged = merged.drop(columns=["Country_y"])

merged.columns

merged.to_csv("Merged_University_Rankings.csv", index=False)

import pandas as pd

df3 = pd.read_csv("A Comprehensive Overview of the Worlds Top 1000 Universities a 14-column dataset (1).csv")
df4 = pd.read_csv("Top 1000 Universities Worldwide.csv")

import os

os.listdir()

df3 = df3.rename(columns={
    "Institution": "University",
    "National Rank": "National_Rank",
    "Research Output": "Research_Output",
    "Quality Publications": "Quality_Publications",
    "Citations": "Citations_Count"
})

df4 = df4.rename(columns={
    "University_Name": "University"
})

merged = pd.merge(
    merged,
    df3,
    on="University",
    how="left"
)

merged.shape

merged = pd.merge(
    merged,
    df4,
    on="University",
    how="left"
)

merged.shape

merged.head()

import os

os.listdir()

import pandas as pd

df5 = pd.read_csv("qs-world-university-rankings-2017-to-2022-V2.csv")
df6 = pd.read_csv("universities.csv")

df5 = df5.rename(columns={"university": "University"})

df5.shape

df5 = df5[[
    "University",
    "city",
    "region",
    "type",
    "research_output",
    "student_faculty_ratio",
    "faculty_count"
]]

merged = pd.merge(
    merged,
    df5,
    on="University",
    how="left"
)

merged.shape

df5 = df5.rename(columns={"university": "University"})

merged = pd.merge(
    merged,
    df5,
    on="University",
    how="left"
)

merged.shape

merged.head()

merged = pd.merge(
    merged,
    df5,
    on="University",
    how="left"
)

merged.shape

merged[["University", "city", "region", "type"]].head(10)

merged[["city", "region", "type"]].isnull().sum()

df6 = df6.rename(columns={"name": "University"})

merged = pd.merge(
    merged,
    df6,
    on="University",
    how="left",
    suffixes=("", "_new")
)

merged["city"] = merged["city"].fillna(merged["city_new"])
merged["type"] = merged["type"].fillna(merged["type_new"])

merged.drop(columns=["city_new", "type_new"], inplace=True)

merged[["city", "region", "type"]].isnull().sum()

merged.to_csv("Merged_University_Dataset_Phase1.csv", index=False)

merged.columns.tolist()

df_2023 = merged.copy()
df_2024 = merged.copy()

merged["Year"].unique()

merged["universities_ranked_count"] = merged.groupby("Country_x")["University"].transform("count")

merged["best_university_rank"] = merged.groupby("Country_x")["Rank"].transform("min")

merged["country_avg_overall_score"] = merged.groupby("Country_x")["Overall Score"].transform("mean")

merged["country_avg_academic_reputation"] = merged.groupby("Country_x")["Academic Reputation Score"].transform("mean")

merged["Academic Reputation Score"].dtype

merged["Academic Reputation Score"] = pd.to_numeric(
    merged["Academic Reputation Score"],
    errors="coerce"
)

merged["Academic Reputation Score"].dtype

merged["country_avg_rank"] = merged.groupby("Country_x")["Rank"].transform("mean")

merged["country_avg_citations"] = merged.groupby("Country_x")["Citations_Count"].transform("mean")

merged["country_avg_international_ratio"] = merged.groupby("Country_x")["International_Students (%)"].transform("mean")

merged["research_productivity_index"] = (
    merged["Research Quality"] +
    merged["Research Environment"] +
    merged["Industry Impact"]
) / 3

merged.info()

merged.insert(
    0,
    "university_id",
    ["U{:04d}".format(i) for i in range(1, len(merged) + 1)]
)

merged["Female to Male Ratio"].head(10)

# Split the ratio into three parts
ratio = merged["Female to Male Ratio"].str.split(":", expand=True)

# Create female and male percentage columns
merged["female_percentage"] = pd.to_numeric(ratio[0], errors="coerce")
merged["male_percentage"] = pd.to_numeric(ratio[1], errors="coerce")

merged[["Female to Male Ratio", "female_percentage", "male_percentage"]].head(10)

import os

os.listdir()

df7 = pd.read_csv("2011_2015_rankings.csv")

df7 = df7.rename(columns={
    "name": "University",
    "subjects_offered": "subject_field",
    "scores_citations": "citations_score",
    "Year": "Year"
})

merged = pd.merge(
    merged,
    df7,
    on=["University", "Year"],
    how="left"
)

merged[["subject_field", "citations_score"]].isnull().sum()

df7 = df7.rename(columns={
    "name": "University",
    "subjects_offered": "subject_field",
    "scores_citations": "citations_score"
})

df7 = df7[["University", "subject_field", "citations_score"]]

# Keep only one record per university
df7 = df7.drop_duplicates(subset="University")

merged = pd.merge(
    merged,
    df7,
    on="University",
    how="left"
)

merged.columns[-15:]

merged["subject_field"] = merged["subject_field_x"].combine_first(merged["subject_field_y"])

merged["citations_score"] = merged["citations_score_x"].combine_first(merged["citations_score_y"])

merged[["subject_field", "citations_score"]].isnull().sum()

merged.drop(
    columns=[
        "subject_field_x",
        "subject_field_y",
        "citations_score_x",
        "citations_score_y"
    ],
    inplace=True
)

merged.columns[-10:]

for col in merged.columns:
    print(col)

merged["research_output"].unique()

research_map = {
    "Very High": 100,
    "Very high": 100,
    "High": 75,
    "Medium": 50,
    "Low": 25
}

merged["research_output_score"] = merged["research_output"].map(research_map)

merged[["research_output", "research_output_score"]].head(10)

merged.to_csv("Final_University_Dataset.csv", index=False)

import os

os.listdir()

merged.to_csv(r"C:\Users\s sai vaishnavi\OneDrive\Desktop\Higher_Education_Project\Final_University_Dataset.csv", index=False)

missing = merged.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)
print(missing)

cols_to_drop = [
    "Country_y",
    "World_Rank",
    "National_Rank_y",
    "ARWU_Rank",
    "THE_Rank",
    "QS_Rank",
    "Enrollment",
    "Undergrad_Students",
    "Postgrad_Students",
    "Faculty_Count",
    "Student_Faculty_Ratio",
    "Research_Output_y",
    "International_Students (%)",
    "Tuition_Fee_USD",
    "Acceptance_Rate (%)",
    "Graduation_Rate (%)",
    "Employability_Rank",
    "QS_Subject_Rank"
]

merged.drop(columns=cols_to_drop, inplace=True)

missing = merged.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)
print(missing)

for i, col in enumerate(merged.columns, start=1):
    print(f"{i}. {col}")

merged = pd.merge(
    merged,
    df4[
        [
            "University",
            "Enrollment",
            "Undergrad_Students",
            "Postgrad_Students",
            "Faculty_Count",
            "Student_Faculty_Ratio",
            "Research_Output",
            "International_Students (%)",
            "Tuition_Fee_USD",
            "Acceptance_Rate (%)",
            "Graduation_Rate (%)",
            "Employability_Rank",
            "QS_Subject_Rank",
            "QS_Rank",
            "THE_Rank",
            "ARWU_Rank"
        ]
    ],
    on="University",
    how="left"
)

merged.columns.tolist()

missing = merged.isnull().sum().sort_values(ascending=False)
print(missing[missing > 0])

# Categorical columns
merged["FOCUS"] = merged["FOCUS"].fillna(merged["FOCUS"].mode()[0])
merged["AGE"] = merged["AGE"].fillna(merged["AGE"].mode()[0])
merged["SIZE"] = merged["SIZE"].fillna(merged["SIZE"].mode()[0])
merged["STATUS"] = merged["STATUS"].fillna(merged["STATUS"].mode()[0])

merged["Employment Outcomes Score"] = pd.to_numeric(
    merged["Employment Outcomes Score"], errors="coerce"
)

merged["Employment Outcomes Score"] = merged["Employment Outcomes Score"].fillna(
    merged["Employment Outcomes Score"].median()
)

merged["Undergrad_Students"] = merged["Undergrad_Students"].fillna(-1)
merged["Postgrad_Students"] = merged["Postgrad_Students"].fillna(-1)
merged["Faculty_Count"] = merged["Faculty_Count"].fillna(-1)

import pandas as pd

# Numeric columns
numeric_cols = [
    "World_Rank",
    "National_Rank_y",
    "QS_Rank",
    "THE_Rank",
    "ARWU_Rank",
    "Enrollment",
    "Undergrad_Students",
    "Postgrad_Students",
    "Faculty_Count",
    "Student_Faculty_Ratio",
    "International_Students (%)",
    "Tuition_Fee_USD",
    "Acceptance_Rate (%)",
    "Graduation_Rate (%)",
    "Employability_Rank",
    "QS_Subject_Rank"
]

for col in numeric_cols:
    if col in merged.columns:
        merged[col] = pd.to_numeric(merged[col], errors="coerce")
        merged[col] = merged[col].fillna(-1)

# Categorical column
if "Research_Output_y" in merged.columns:
    merged["Research_Output_y"] = merged["Research_Output_y"].fillna("Unknown")

for col in merged.columns:
    print(col)
    

import pandas as pd

numeric_cols = [
    "World Rank",
    "National_Rank_x",
    "QS_Rank",
    "THE_Rank",
    "ARWU_Rank",
    "Enrollment",
    "Undergrad_Students",
    "Postgrad_Students",
    "Faculty_Count",
    "Student_Faculty_Ratio",
    "International_Students (%)",
    "Tuition_Fee_USD",
    "Acceptance_Rate (%)",
    "Graduation_Rate (%)",
    "Employability_Rank",
    "QS_Subject_Rank"
]

for col in numeric_cols:
    if col in merged.columns:
        merged[col] = pd.to_numeric(merged[col], errors="coerce")
        merged[col] = merged[col].fillna(-1)

# Fill categorical column
merged["Research_Output"] = merged["Research_Output"].fillna("Unknown")

merged[numeric_cols + ["Research_Output"]].isnull().sum()

merged.to_csv(
    r"C:\Users\s sai vaishnavi\OneDrive\Desktop\Higher_Education_Project\Final_University_Dataset.csv",
    index=False
)

print("Dataset saved successfully!")

import pandas as pd

final_df = pd.read_csv(
    r"C:\Users\s sai vaishnavi\OneDrive\Desktop\Higher_Education_Project\Final_University_Dataset.csv"
)

final_df.shape

missing = final_df.isnull().sum().sort_values(ascending=False)
print(missing[missing > 0])

required_columns = [
    "publications_count",
    "h_index",
    "degree_level",
    "undergraduate_count",
    "postgraduate_count",
    "international_student_ratio"
]

for col in required_columns:
    print(col, col in merged.columns)

import pandas as pd

merged = pd.read_csv(
    r"C:\Users\s sai vaishnavi\OneDrive\Desktop\Higher_Education_Project\Final_University_Dataset.csv"
)

import os
os.getcwd()

import os

os.listdir()

import os

os.listdir(r"C:\Users\s sai vaishnavi\OneDrive\Desktop\Higher_Education_Project\datasets\processed_data")

merged = pd.read_csv(
    r"C:\Users\s sai vaishnavi\OneDrive\Desktop\Higher_Education_Project\datasets\processed_data\Final_University_Dataset.csv"
)

friend = pd.read_csv("university_raw_data (1).csv")

friend = pd.read_csv("university_raw_data (1).csv", low_memory=False)

friend.shape

friend.isnull().sum().sort_values(ascending=False)

my_cols = set(merged.columns.str.lower())
friend_cols = set(friend.columns.str.lower())

missing = friend_cols - my_cols

print(missing)

merged.rename(columns={
    "Undergrad_Students":"undergraduate_count",
    "Postgrad_Students":"postgraduate_count",
    "Faculty_Count":"faculty_count",
    "International_Students (%)":"international_student_ratio"
}, inplace=True)

friend.rename(columns={
    "university_name": "University",
    "year": "Year"
}, inplace=True)

merged["Year"] = merged["Year"].astype(str)
friend["Year"] = friend["Year"].astype(str)

merged["University"] = merged["University"].str.strip()
friend["University"] = friend["University"].str.strip()

cols_to_take = [
    "University",
    "Year",
    "publications_count",
    "h_index",
    "degree_level",
    "undergraduate_count",
    "postgraduate_count",
    "international_student_ratio"
]

merged = merged.merge(
    friend[cols_to_take],
    on=["University", "Year"],
    how="left"
)

merged["Undergrad_Students"] = merged["Undergrad_Students"].fillna(
    merged["undergraduate_count"]
)

merged["Postgrad_Students"] = merged["Postgrad_Students"].fillna(
    merged["postgraduate_count"]
)

merged.columns.tolist()

[col for col in merged.columns if "under" in col.lower()]

[col for col in merged.columns if "post" in col.lower()]

[col for col in merged.columns if "international" in col.lower()]

merged["undergraduate_count_x"] = merged["undergraduate_count_x"].fillna(
    merged["undergraduate_count_y"]
)

merged["postgraduate_count_x"] = merged["postgraduate_count_x"].fillna(
    merged["postgraduate_count_y"]
)

merged["international_student_ratio_x"] = merged["international_student_ratio_x"].fillna(
    merged["international_student_ratio_y"]
)

merged.rename(columns={
    "undergraduate_count_x":"undergraduate_count",
    "postgraduate_count_x":"postgraduate_count",
    "international_student_ratio_x":"international_student_ratio"
}, inplace=True)

merged.drop(columns=[
    "undergraduate_count_y",
    "postgraduate_count_y",
    "international_student_ratio_y"
], inplace=True)

merged[
    [
        "undergraduate_count",
        "postgraduate_count",
        "international_student_ratio",
        "publications_count",
        "h_index",
        "degree_level"
    ]
].isnull().sum()

merged.columns[merged.columns == "faculty_count"]

merged[
    [
        "undergraduate_count",
        "postgraduate_count",
        "international_student_ratio",
        "publications_count",
        "h_index",
        "degree_level"
    ]
].isnull().sum()

merged.columns.tolist()

merged.columns.tolist()

merged[["Country_x","Country_y"]].isnull().sum()

merged[["city","city_x","city_y"]].isnull().sum()

merged[["region","region_x","region_y"]].isnull().sum()

merged[["faculty_count","faculty_count_x","faculty_count_y"]].isnull().sum()

merged[["Country_x","Country_y"]].isnull().sum()

merged[["city","city_x","city_y"]].isnull().sum()

merged[["region","region_x","region_y"]].isnull().sum()

merged[["faculty_count","faculty_count_x","faculty_count_y"]].isnull().sum()

(merged["region"] == merged["region_x"]).value_counts(dropna=False)

(merged["region"] == merged["region_y"]).value_counts(dropna=False)

(merged["faculty_count"] == merged["faculty_count_x"]).value_counts(dropna=False)

(merged["faculty_count"] == merged["faculty_count_y"]).value_counts(dropna=False)

merged[["National_Rank_x","National_Rank_y"]].isnull().sum()

merged[["Research_Output_x","Research_Output_y"]].isnull().sum()

merged.duplicated().sum()

merged.shape

merged = merged.drop_duplicates().reset_index(drop=True)

print("New Shape:", merged.shape)

columns_to_drop = [
    "Country_y",
    "city_x", "city_y",
    "region_x", "region_y",
    "type_x", "type_y",
    "faculty_count_x", "faculty_count_y",
    "student_faculty_ratio_x", "student_faculty_ratio_y",
    "National_Rank_y",
    "Research_Output_y"
]

merged = merged.drop(columns=columns_to_drop)

print("Remaining Columns:", len(merged.columns))

merged.shape

merged.columns.tolist()

merged[["research_output", "research_output_x", "research_output_y"]].isnull().sum()

(merged["research_output"] == merged["research_output_x"]).value_counts(dropna=False)

(merged["research_output"] == merged["research_output_y"]).value_counts(dropna=False)

merged = merged.drop(columns=["research_output_x", "research_output_y"])

merged[["Overall SCORE", "Overall Score"]].head(10)

merged[["2024 RANK", "World Rank", "World_Rank", "QS_Rank", "THE_Rank", "ARWU_Rank"]].head(10)

merged[["Overall SCORE", "Overall Score"]].head(10)

merged[[
    "2024 RANK",
    "World Rank",
    "World_Rank",
    "QS_Rank",
    "THE_Rank",
    "ARWU_Rank"
]].head(10)

merged[["2024 RANK","QS_Rank"]].head(15)

merged[["World Rank","World_Rank"]].head(15)

merged[[
    "2024 RANK",
    "World Rank",
    "World_Rank",
    "QS_Rank",
    "THE_Rank",
    "ARWU_Rank",
    "University",
    "Year"
]].head(20)

rename_dict = {
    "University": "university_name",
    "Country_x": "country",
    "Country Code": "country_code",
    "2024 RANK": "world_rank",
    "National_Rank_x": "national_rank",
    "Overall SCORE": "overall_score",
    "Year": "year",

    "Academic Reputation Score": "academic_reputation_score",
    "Academic Reputation Rank": "academic_reputation_rank",

    "Employer Reputation Score": "employer_reputation_score",
    "Employer Reputation Rank": "employer_reputation_rank",

    "Faculty Student Score": "faculty_student_score",
    "Faculty Student Rank": "faculty_student_rank",

    "Citations per Faculty Score": "citations_per_faculty",
    "Citations per Faculty Rank": "citations_per_faculty_rank",

    "International Faculty Score": "international_faculty_score",
    "International Faculty Rank": "international_faculty_rank",

    "International Students Score": "international_students_score",
    "International Students Rank": "international_students_rank",

    "International Research Network Score": "international_research_network_score",
    "International Research Network Rank": "international_research_network_rank",

    "Employment Outcomes Score": "employment_outcomes_score",
    "Employment Outcomes Rank": "employment_outcomes_rank",

    "Sustainability Score": "sustainability_score",
    "Sustainability Rank": "sustainability_rank",

    "Student Population": "total_students",
    "Students to Staff Ratio": "faculty_to_student_ratio",

    "International Students": "international_students_count",

    "Female to Male Ratio": "gender_ratio",

    "Teaching": "teaching_score",
    "Research Environment": "research_environment",
    "Research Quality": "research_quality",
    "Industry Impact": "industry_impact",
    "International Outlook": "international_outlook",

    "World Rank": "cwur_rank",
    "World_Rank": "alternate_world_rank",

    "Quality of Education": "quality_of_education",
    "Alumni Employment": "alumni_employment",
    "Quality of Faculty": "quality_of_faculty",

    "Research_Output_x": "research_output_score",

    "Quality_Publications": "quality_publications",
    "Influence": "influence",

    "Citations_Count": "citations_count",

    "Score": "cwur_score",

    "Latitude": "latitude",
    "Longitude": "longitude",

    "QS_Rank": "qs_rank",
    "THE_Rank": "the_rank",
    "ARWU_Rank": "arwu_rank",

    "Enrollment": "enrollment",

    "Undergrad_Students": "undergraduate_count",
    "Postgrad_Students": "postgraduate_count",

    "Faculty_Count": "faculty_count_dataset",

    "Student_Faculty_Ratio": "student_faculty_ratio_dataset",

    "International_Students (%)": "international_student_ratio",

    "Tuition_Fee_USD": "tuition_fee_usd",

    "Acceptance_Rate (%)": "acceptance_rate",

    "Graduation_Rate (%)": "graduation_rate",

    "Employability_Rank": "employability_rank",

    "QS_Subject_Rank": "qs_subject_rank",

    "city": "city",
    "region": "region",

    "type": "university_type",

    "research_output": "research_output",

    "student_faculty_ratio": "student_faculty_ratio",

    "faculty_count": "faculty_count",

    "universities_ranked_count": "universities_ranked_count",

    "best_university_rank": "best_university_rank",

    "country_avg_overall_score": "country_avg_overall_score"
}

merged.rename(columns=rename_dict, inplace=True)

print("Columns Renamed Successfully!")

merged[["citations_count", "faculty_count"]].dtypes

merged["faculty_count"].head(20)

import numpy as np
import pandas as pd

merged["faculty_count"] = (
    merged["faculty_count"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.strip()
)

merged["faculty_count"] = pd.to_numeric(
    merged["faculty_count"],
    errors="coerce"
)

merged["citations_count"] = (
    merged["citations_count"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.strip()
)

merged["citations_count"] = pd.to_numeric(
    merged["citations_count"],
    errors="coerce"
)

merged["research_productivity_index"] = (
    merged["citations_count"] / merged["faculty_count"]
)

merged["research_productivity_index"] = (
    merged["research_productivity_index"]
    .replace([np.inf, -np.inf], np.nan)
)

import pandas as pd
import numpy as np

# Convert faculty_count to numeric
merged["faculty_count"] = (
    merged["faculty_count"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

merged["faculty_count"] = pd.to_numeric(
    merged["faculty_count"],
    errors="coerce"
)

# Convert citations_count to numeric (just to be safe)
merged["citations_count"] = pd.to_numeric(
    merged["citations_count"],
    errors="coerce"
)

# Create Research Productivity Index
merged["research_productivity_index"] = (
    merged["citations_count"] / merged["faculty_count"]
)

# Remove infinite values
merged["research_productivity_index"].replace(
    [np.inf, -np.inf],
    np.nan,
    inplace=True
)

merged[["faculty_count","citations_count","research_productivity_index"]].head()

merged["research_productivity_index"] = merged["research_productivity_index"].replace(
    [np.inf, -np.inf],
    np.nan
)

friend = pd.read_csv("university_raw_data (1).csv")

print(friend.shape)

friend = pd.read_csv("university_raw_data (1).csv", header=1)

print(friend.shape)
friend.columns.tolist()

set(merged["university_name"]).intersection(set(friend["university_name"])).__len__()

final = merged.merge(
    friend,
    on=["university_name", "year"],
    how="left",
    suffixes=("", "_friend")
)

final.shape

for col in friend.columns:

    if col in final.columns and col + "_friend" in final.columns:

        final[col] = final[col].fillna(final[col + "_friend"])

missing = final.isnull().sum()

missing[missing > 0].sort_values(ascending=False)

required_cols = friend.columns.tolist()

final[required_cols].isnull().sum().sort_values(ascending=False)

for col in ["city","region","university_type","faculty_count"]:

    if col in final.columns:

        if final[col].dtype == "object":

            final[col] = final[col].fillna(final[col].mode()[0])

        else:

            final[col] = final[col].fillna(final[col].median())

final[required_cols].isnull().sum().sum()

final = merged.merge(
    friend_latest,
    on="university_name",
    how="left",
    suffixes=("", "_friend")
)

for col in friend_latest.columns:
    if col in final.columns and col + "_friend" in final.columns:
        final[col] = final[col].fillna(final[col + "_friend"])

final[required_cols].isnull().sum().sort_values(ascending=False)

final[required_cols].isnull().sum().sort_values(ascending=False).head(20)

import re

merged["university_name"] = (
    merged["university_name"]
    .str.replace(r"\s*\(.*?\)", "", regex=True)
    .str.strip()
)

friend["university_name"] = (
    friend["university_name"]
    .str.replace(r"\s*\(.*?\)", "", regex=True)
    .str.strip()
)

friend_latest = (
    friend.sort_values("year")
          .drop_duplicates(subset="university_name", keep="last")
)

final = merged.merge(
    friend_latest,
    on="university_name",
    how="left",
    suffixes=("", "_friend")
)

for col in friend_latest.columns:
    if col in final.columns and col + "_friend" in final.columns:
        final[col] = final[col].fillna(final[col + "_friend"])

final.drop(columns=[c for c in final.columns if c.endswith("_friend")], inplace=True)

final["publications_count"].isnull().sum()

required_cols = [
    col for col in friend.columns
    if col != "Unnamed: 0"
]

final[required_cols].isnull().sum().sort_values(ascending=False)

final[required_cols].isnull().sum().sum()

final[final["national_rank"].isna()][
    ["university_name", "country", "world_rank"]
]

final["national_rank"] = final["national_rank"].fillna(1)

final["national_rank"] = final.groupby("country")["national_rank"].transform(
    lambda x: x.fillna(x.median())
)

final["national_rank"] = final["national_rank"].fillna(1)

final[required_cols].isnull().sum().sum()

print(final.shape)
print(final.duplicated().sum())

final.to_csv("final_cleaned_university_dataset.csv", index=False)

print("✅ Final dataset exported successfully!")

final[required_cols].isnull().sum().sum()

final.to_csv("final_cleaned_university_dataset.csv", index=False)

final.shape

final.to_csv("final_cleaned_university_dataset.csv", index=False)

import os

print(os.getcwd())

check = pd.read_csv("final_cleaned_university_dataset.csv")

check.head()

check.shape

