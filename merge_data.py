import pandas as pd

# Load Dataset 1
df1 = pd.read_csv("qs-world-university-rankings-2017-to-2022-V2 (1).csv")

# Load Dataset 2
df2 = pd.read_csv("world_university_rankings_2026 (4).csv")   

# Rename columns
df1.rename(columns={"university": "university_name"}, inplace=True)
df2.rename(columns={"university": "university_name"}, inplace=True)

# Merge datasets
merged = pd.merge(
    df1,
    df2,
    on=["university_name", "country"],
    how="outer"
)

# Remove duplicate columns
merged = merged.loc[:, ~merged.columns.duplicated()]

# Save merged dataset
merged.to_csv("university_raw_data.csv", index=False)

print("Merge completed successfully!")
print(merged.shape)