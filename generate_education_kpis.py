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
# Formula:
# 60% Overall Score + 40% Academic Reputation
# -------------------------------
df["Global Ranking Score"] = (
    (df["Overall SCORE"] * 0.60) +
    (df["Academic Reputation Scores"] * 0.40)
)

# -------------------------------
# KPI 2: Research Impact Score
# Formula:
# 70% Citations per Faculty +
# 30% International Research Network
# -------------------------------
df["Research Impact Score"] = (
    (df["Citations per Faculty"] * 0.70) +
    (df["International Research Network"] * 0.30)
)

# -------------------------------
# KPI 3: Faculty-to-Student Ratio KPI
# Formula:
# Faculty Student Ratio itself
# -------------------------------
df["Faculty-to-Student Ratio KPI"] = df["Faculty-Student Ratio"]

# -------------------------------
# KPI 4: International Student Percentage
# Formula:
# 80% International Student Ratio +
# 20% International Research Network
# -------------------------------
df["International Student Percentage"] = (
    (df["International Student Ratio"] * 0.80) +
    (df["International Research Network"] * 0.20)
)

# -------------------------------
# KPI 5: Academic Reputation Score
# Formula:
# 70% Academic Reputation +
# 30% Employment Outcomes
# -------------------------------
df["Academic Reputation Score"] = (
    (df["Academic Reputation Scores"] * 0.70) +
    (df["Employment Outcomes"] * 0.30)
)

# -------------------------------
# KPI 6: Research Productivity Index
# Formula:
# Average of:
# - Citations per Faculty
# - International Research Network
# - Employment Outcomes
# -------------------------------
df["Research Productivity Index"] = (
    df["Citations per Faculty"] +
    df["International Research Network"] +
    df["Employment Outcomes"]
) / 3

# -------------------------------
# Round KPI values
# -------------------------------
kpi_columns = [
    "Global Ranking Score",
    "Research Impact Score",
    "Faculty-to-Student Ratio KPI",
    "International Student Percentage",
    "Academic Reputation Score",
    "Research Productivity Index"
]

df[kpi_columns] = df[kpi_columns].round(2)

# -------------------------------
# Save as Excel
# -------------------------------
df.to_excel("university_final_dataset.xlsx", index=False)

print("✅ KPI Engineering Completed!")
print("Output file: university_final_dataset.xlsx")