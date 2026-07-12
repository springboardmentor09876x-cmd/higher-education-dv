import pandas as pd

# 1. Load the dataset
file_path = "C:\Users\Varun Rana\OneDrive\Desktop\higher-education-dv\merged dataset\top_1000_universities_2020_2026_.csv"
df = pd.read_csv(file_path)

print(f"Original shape: {df.shape}")

# --- STEP 1: Remove the Corrupted gender_ratio Column ---
# Dropped because accurate female_percentage and male_percentage columns already exist
if 'gender_ratio' in df.columns:
    df = df.drop(columns=['gender_ratio'])
    print("Dropped redundant 'gender_ratio' column.")


# --- STEP 2: Handle Missing Rank Data & Keep Decimals ---
# Drop rows that are missing critical rank data entirely
df = df.dropna(subset=['world_rank', 'national_rank'])

# Explicitly ensure both columns remain as decimals (floats) to preserve ranking ties
df['world_rank'] = df['world_rank'].astype(float)
df['national_rank'] = df['national_rank'].astype(float)
print("Removed rows with missing ranks; preserved decimals for ranking ties.")


# --- STEP 3: Remove Extreme Outlier ---
# Remove the single impossible outlier in the faculty-to-student ratio column
df = df[df['faculty_to_student_ratio'] <= 200]
print("Filtered out the extreme outlier in 'faculty_to_student_ratio'.")


# --- STEP 4: Clean and Standardize Text Data ---
# Select all text (categorical) columns
text_columns = df.select_dtypes(include=['object']).columns

# Strip invisible leading or trailing whitespaces from all text values
for col in text_columns:
    df[col] = df[col].astype(str).str.strip()
print("Cleaned text columns by stripping hidden trailing and leading whitespace.")


# --- Final Output Verification ---
print("\n--- Cleaning Summary ---")
print(f"Final Cleaned Shape: {df.shape}")
print(f"Total Missing Values remaining: {df.isnull().sum().sum()}")
print(f"Duplicate Rows remaining: {df.duplicated().sum()}")
print(f"World Rank Column Type: {df['world_rank'].dtype}")
print(f"National Rank Column Type: {df['national_rank'].dtype}")

# Save the completely clean dataset to a new file
output_path = "C:\Users\Varun Rana\OneDrive\Desktop\higher-education-dv\data sources\cleaneddataset.csv"
df.to_csv(output_path, index=False)
print(f"\nSuccess! Cleaned dataset saved as: {output_path}")