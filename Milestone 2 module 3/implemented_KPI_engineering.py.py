import pandas as pd 
df = pd.read_csv("final dataset university_cleaned.csv")
df.head()
df.info()
df.describe(include="all")
print(df.shape)
df.isnull().sum()
df.isnull().sum().sort_values(ascending=False)
(df.isnull().mean() * 100).round(2)
print(df.duplicated().sum())
df = df.drop_duplicates()
print(df.duplicated().sum())
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].str.strip()
    df["country"] = df["country"].replace({
    "USA": "United States",
    "U.S.A.": "United States",
    "UK": "United Kingdom"
})
    df["country"] = df["country"].str.title()
    df.dtypes
    df["year"] = df["year"].astype(int)

df["world_rank"] = df["world_rank"].astype(int)

df["overall_score"] = df["overall_score"].astype(float)
numeric_columns = df.select_dtypes(include=["int64","float64"]).columns

for col in numeric_columns:
    print(col, (df[col] < 0).sum())
    df = df[df["total_students"] >= 0]
    df["total_percentage"] = (
    df["female_percentage"] +
    df["male_percentage"]
)
    df[df["total_percentage"] != 100]
    df["male_percentage"] = 100 - df["female_percentage"]
    df["calculated_ratio"] = (
    df["faculty_count"] /
    df["total_students"]
)
    df[
    abs(df["calculated_ratio"] -
        df["faculty_to_student_ratio"]) > 0.01
]
    df["calculated_ratio"] = (
    df["international_students_count"] /
    df["total_students"] * 100
).round(2)
    df[
    abs(df["calculated_ratio"] -
        df["international_student_ratio"]) > 0.1
]
    df[df["world_rank"] <= 0]
    df["world_rank"].max()
    df["total_students"].describe()
    Q1 = df["total_students"].quantile(0.25)
Q3 = df["total_students"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["total_students"] < lower) |
    (df["total_students"] > upper)
]
duplicates = df.duplicated(
    subset=["university_name","year"],
    keep=False
)

df[duplicates]
country_avg = df.groupby("country")["overall_score"].mean()

print(country_avg)
df["citations_per_faculty"] = (
    df["citations_count"] /
    df["faculty_count"]
).round(2)
df["faculty_to_student_ratio"] = (
    df["faculty_count"] /
    df["total_students"]
).round(3)
df["international_student_ratio"] = (
    df["international_students_count"] /
    df["total_students"] * 100
).round(2)
df["country"].unique()
df["region"].unique()
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.shape)
df["expected_ratio"] = (
    df["faculty_count"] /
    df["total_students"]
).round(3)

incorrect = df[
    abs(df["expected_ratio"] -
        df["faculty_to_student_ratio"]) > 0.001
]

print(len(incorrect))
df["faculty_to_student_ratio"] = (
    df["faculty_count"] /
    df["total_students"]
).round(3)
df["expected_cpf"] = (
    df["citations_count"] /
    df["faculty_count"]
).round(2)

incorrect = df[
    abs(df["expected_cpf"] -
        df["citations_per_faculty"]) > 0.01
]

print(len(incorrect))
df["citations_per_faculty"] = (
    df["citations_count"] /
    df["faculty_count"]
).round(2)
df["expected_ratio"] = (
    df["international_students_count"] /
    df["total_students"]
    *100
).round(2)

incorrect = df[
    abs(df["expected_ratio"] -
        df["international_student_ratio"]) > 0.1
]

print(len(incorrect))
df["international_student_ratio"] = (
    df["international_students_count"] /
    df["total_students"]
    *100
).round(2)
df["gender_total"] = (
    df["female_percentage"] +
    df["male_percentage"]
).round(2)

incorrect = df[
    df["gender_total"] != 100
]

print(len(incorrect))
df["male_percentage"] = (
100 -
df["female_percentage"]
).round(2)
df[
(
df["undergraduate_count"] +
df["postgraduate_count"]
)
!=
df["total_students"]
]
df["total_students"] = (
df["undergraduate_count"] +
df["postgraduate_count"]
)
invalid = df[
df["faculty_count"] >
df["total_students"]
]

print(len(invalid))
invalid = df[
df["international_students_count"]
>
df["total_students"]
]

print(len(invalid))
invalid = df[
df["world_rank"] <
df["national_rank"]
]

print(len(invalid))
country_rank = (
df.groupby("country")
["world_rank"]
.mean()
.round(2)
)
country_score = (
df.groupby("country")
["overall_score"]
.mean()
.round(2)
)
country_citations = (
df.groupby("country")
["citations_count"]
.mean()
.round(2)
)
country_rep = (
df.groupby("country")
["academic_reputation_score"]
.mean()
.round(2)
)
country_ratio = (
df.groupby("country")
["international_student_ratio"]
.mean()
.round(2)
)
duplicates = df[
df.duplicated(
subset=[
"university_name",
"year"
],
keep=False
)
]
df.drop(
columns=[
"expected_ratio",
"expected_cpf",
"gender_total"
],
errors="ignore",
inplace=True
)
df.to_csv("cleaned_university_rankings.csv", index=False)

