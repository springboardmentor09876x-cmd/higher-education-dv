import pandas as pd

qs = pd.read_csv("2024 QS World University Rankings 1.1 (For qs.com).csv")

the = pd.read_csv("THE World University Rankings 2016-2026 (1).csv")

qs.head()

the.head()

qs.columns

the.columns

qs = qs.rename(columns={'Institution Name':'University'})
the = the.rename(columns={'Name':'University'})

the_2024 = the[the['Year'] == 2024]

the_2024.head()

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

df3.head()

df4.head()

df3.columns

df4.columns

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

df3.columns

df4.columns

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

df5.columns

df6.columns

df5.head()

df6.head()

df5 = df5.rename(columns={"university": "University"})

df5 = df5[df5["year"] == 2022]

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

df5.columns

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

df6 = df6[["University", "city", "type"]]

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

df_2023["Year"] = 2023
df_2024["Year"] = 2024

df_2023[["University", "Year"]].head()

df_2023["Rank"] = df_2023["2023 RANK"]
df_2024["Rank"] = df_2024["2024 RANK"]

df_2023.drop(columns=["2023 RANK", "2024 RANK"], inplace=True)
df_2024.drop(columns=["2023 RANK", "2024 RANK"], inplace=True)

final_df = pd.concat([df_2023, df_2024], ignore_index=True)

final_df.head()

df_2023[["University", "Year"]].head()

final_df.columns

print(final_df.columns.tolist())

cols = final_df.columns.tolist()

# Remove Year from its current position
cols.remove("Year")

# Insert it after University
cols.insert(1, "Year")

# Reorder the dataframe
final_df = final_df[cols]

final_df.head()

final_df["Year"].value_counts()

final_df[final_df["Year"] == 2023][["University", "Year", "Rank"]].head()

final_df[final_df["Year"] == 2024][["University", "Year", "Rank"]].head()

merged["Year"].unique()

final_df["Year"].unique()

final_df["Year"].value_counts()

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

df7.columns

df7.head()

df7 = df7.rename(columns={
    "name": "University",
    "subjects_offered": "subject_field",
    "scores_citations": "citations_score",
    "Year": "Year"
})

df7 = df7[[
    "University",
    "Year",
    "subject_field",
    "citations_score"
]]

df7.head()

merged = pd.merge(
    merged,
    df7,
    on=["University", "Year"],
    how="left"
)

merged[["subject_field", "citations_score"]].isnull().sum()

df7["Year"].unique()

df7["Year"].value_counts(dropna=False)

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

df7.columns

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

os.getcwd()

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

df4.columns

df3.columns

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

final_df.columns.tolist()

missing = final_df.isnull().sum().sort_values(ascending=False)
print(missing[missing > 0])

final_df.head()