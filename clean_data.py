import pandas as pd

# Read the merged dataset
df = pd.read_csv("University_Final_Data.csv", encoding="utf-8-sig")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Remove extra spaces from all text columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Replace empty strings with missing values
df.replace("", pd.NA, inplace=True)

# Show missing values
print("Missing Values:")
print(df.isnull().sum())

# Save cleaned data
df.to_csv("University_Cleaned_Data.csv", index=False, encoding="utf-8-sig")

print("\n✅ Data cleaned successfully!")
print("Output file: University_Cleaned_Data.csv")