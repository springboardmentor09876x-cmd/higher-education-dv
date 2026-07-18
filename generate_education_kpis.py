import pandas as pd

# Read the cleaned dataset
df = pd.read_csv("university_cleaned.csv", encoding="utf-8-sig")

# -------------------------------
# Convert required columns to numeric
# -------------------------------
numeric_columns = [
    "Academic Reputation Scores",
    "Faculty-Student Ratio",
    "Citations per Faculty",
    "International Student Ratio",
    "International Research Network",
    "Employment Outcomes",
    "Overall SCORE"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# -------------------------------
# KPI 1: Global Ranking Score
# -------------------------------
df["Global Ranking Score"] = df["Overall SCORE"]

# -------------------------------
# KPI 2: Research Impact Score
# -------------------------------
df["Research Impact Score"] = df["Citations per Faculty"]

# -------------------------------
# KPI 3: Faculty-to-Student Ratio
# -------------------------------
df["Faculty-to-Student Ratio KPI"] = df["Faculty-Student Ratio"]

# -------------------------------
# KPI 4: International Student Percentage
# -------------------------------
df["International Student Percentage"] = df["International Student Ratio"]

# -------------------------------
# KPI 5: Academic Reputation Score
# -------------------------------
df["Academic Reputation Score"] = df["Academic Reputation Scores"]

# -------------------------------
# KPI 6: Research Productivity Index
# -------------------------------
df["Research Productivity Index"] = (
    df["Citations per Faculty"] +
    df["International Research Network"] +
    df["Employment Outcomes"]
) / 3

# Round KPI values
kpi_columns = [
    "Global Ranking Score",
    "Research Impact Score",
    "Faculty-to-Student Ratio KPI",
    "International Student Percentage",
    "Academic Reputation Score",
    "Research Productivity Index"
]

df[kpi_columns] = df[kpi_columns].round(2)

# Save as Excel
df.to_excel("university_final_dataset.xlsx", index=False)

print("✅ KPI Engineering Completed!")
print("Output file: university_final_dataset.xlsx")