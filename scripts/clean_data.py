import pandas as pd

df = pd.read_csv("output/university_raw_data.csv")

country_mapping = {
    "Brunei Darussalam": "Brunei",
    "Hong Kong SAR": "Hong Kong",
    "Iran, Islamic Republic of": "Iran",
    "Russian Federation": "Russia",
    "Korea, South": "South Korea",
    "China (Mainland)": "China"
}

df["country"] = df["country"].replace(country_mapping)

print(sorted(df["country"].unique()))
df.to_csv(
    "output/university_cleaned.csv",
    index=False
)

print("university_cleaned.csv created successfully!")

print("\nFinal Shape:")
print(df.shape)

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nMissing Values:")
print(df.isnull().sum().sum())

df.loc[
    df["international_student_ratio"] > 100,
    "international_student_ratio"
] = None

df.to_csv(
    "output/university_cleaned.csv",
    index=False
)