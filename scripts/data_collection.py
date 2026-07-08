import pandas as pd

# -------------------------
# Load datasets
# -------------------------

qs = pd.read_csv(
    "data/qs_rankings_2025.csv",
    encoding="ISO-8859-1"
)

the = pd.read_csv(
    "data/THE World University Rankings 2016-2026.csv"
)

# -------------------------
# Rename QS columns
# -------------------------

qs = qs.rename(columns={
    "RANK_2025":"Rank",
    "Institution_Name":"University",
    "Location":"Country",
    "Academic_Reputation_Score":"Academic_Reputation",
    "Employer_Reputation_Score":"Employer_Reputation",
    "Faculty_Student_Score":"Faculty_Student_Ratio",
    "Citations_per_Faculty_Score":"Citations_per_Faculty",
    "International_Faculty_Score":"International_Faculty",
    "International_Students_Score":"International_Students",
    "International_Research_Network_Score":"International_Research_Network",
    "Employment_Outcomes_Score":"Employment_Outcomes",
    "Sustainability_Score":"Sustainability",
    "Overall_Score":"Overall_Score"
})

# -------------------------
# Rename THE columns
# -------------------------

the = the.rename(columns={
    "Name":"University",
    "Country":"Country",
    "Overall Score":"Overall_Score",
    "Students to Staff Ratio":"Faculty_Student_Ratio",
    "Teaching":"Teaching",
    "Research Environment":"Research_Environment",
    "Research Quality":"Research_Quality",
    "Industry Impact":"Industry_Impact",
    "International Outlook":"International_Outlook",
    "Student Population":"Student_Population",
    "Female to Male Ratio":"Female_Male_Ratio"
})

# -------------------------
# Add Source column
# -------------------------

qs["Source"] = "QS"
the["Source"] = "THE"

# -------------------------
# Required columns
# -------------------------

final_columns = [
    "Rank",
    "University",
    "Country",
    "Region",
    "Overall_Score",
    "Academic_Reputation",
    "Employer_Reputation",
    "Teaching",
    "Research_Environment",
    "Research_Quality",
    "Citations_per_Faculty",
    "Industry_Impact",
    "Student_Population",
    "Faculty_Student_Ratio",
    "International_Students",
    "International_Faculty",
    "Female_Male_Ratio",
    "International_Outlook",
    "International_Research_Network",
    "Employment_Outcomes",
    "Sustainability",
    "Year",
    "Source"
]

# -------------------------
# Create missing columns
# -------------------------

for col in final_columns:
    if col not in qs.columns:
        qs[col] = None

    if col not in the.columns:
        the[col] = None

# -------------------------
# Keep same structure
# -------------------------

qs = qs[final_columns]
the = the[final_columns]

# -------------------------
# Merge
# -------------------------

merged = pd.concat([qs, the], ignore_index=True)

# -------------------------
# Save
# -------------------------

merged.to_csv(
    "data/university_raw_data.csv",
    index=False
)

print("Merged Successfully!")
print("Rows :", merged.shape[0])
print("Columns :", merged.shape[1])