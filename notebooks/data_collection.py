"""
EduVision_DV - Data Collection & Cleaning Script
Cleans QS, THE, and CWUR university ranking datasets individually and adds
a standardized matching key (Std_University_Name, Std_Country) to each,
so they can be linked in Tableau via Relationships (not merged in Python).

Why not a single pre-merged CSV?
QS covers 2017-2022, while THE (2011-2016) and CWUR (2012-2015) have ZERO
overlapping years. Force-merging them into one row per university would
misleadingly imply the three ranks/scores are from the same time period.
Keeping them as three linked tables in Tableau preserves each source's
correct year, and Tableau Relationships handle the differing granularity
without duplicating rows (unlike a traditional join).
"""

import pandas as pd
import numpy as np
import re
from rapidfuzz import fuzz, process

# ----------------------------------------------------------------------
# 1. COUNTRY STANDARDIZATION
# ----------------------------------------------------------------------
COUNTRY_MAP = {
    "united states of america": "United States",
    "unisted states of america": "United States",   # typo in timesData.csv
    "usa": "United States",
    "united states": "United States",
    "united kingdom": "United Kingdom",
    "unted kingdom": "United Kingdom",               # typo in timesData.csv
    "uk": "United Kingdom",
    "south korea": "South Korea",
    "korea, south": "South Korea",
    "republic of korea": "South Korea",
    "russian federation": "Russia",
    "hong kong": "Hong Kong",
    "china (hong kong)": "Hong Kong",
}

def clean_country(c):
    if pd.isna(c):
        return None
    c = str(c).strip()
    key = c.lower()
    return COUNTRY_MAP.get(key, c)  # fall back to original if no mapping needed


# ----------------------------------------------------------------------
# 2. UNIVERSITY NAME STANDARDIZATION (for matching only, not display)
# ----------------------------------------------------------------------
def normalize_name(name):
    """Lowercase, strip parenthetical abbreviations, punctuation, extra spaces."""
    if pd.isna(name):
        return ""
    n = str(name).strip()
    n = re.sub(r"\(.*?\)", "", n)          # remove "(MIT)", "(Caltech)" etc.
    n = n.lower()
    n = re.sub(r"[^a-z0-9\s]", " ", n)     # drop punctuation
    n = re.sub(r"\s+", " ", n).strip()
    return n


# ----------------------------------------------------------------------
# 3. NUMERIC CLEANERS
# ----------------------------------------------------------------------
def clean_rank(rank):
    """Handles '=39' (tie) and '201-225' (range) -> numeric (first number)."""
    if pd.isna(rank):
        return np.nan
    s = str(rank).strip().lstrip("=")
    s = s.split("-")[0]
    s = re.sub(r"[^\d.]", "", s)
    return float(s) if s else np.nan

def clean_numeric(val):
    """Strips commas, handles '-' placeholder."""
    if pd.isna(val):
        return np.nan
    s = str(val).strip()
    if s in ("-", "", "n/a", "N/A"):
        return np.nan
    s = s.replace(",", "").replace("%", "")
    try:
        return float(s)
    except ValueError:
        return np.nan


# ----------------------------------------------------------------------
# 4. LOAD + CLEAN EACH DATASET (dedupe to latest year per university)
# ----------------------------------------------------------------------
def load_qs(path):
    df = pd.read_csv(path)
    df["University_Name"] = df["university"].str.strip()
    df["Country"] = df["country"].apply(clean_country)
    df["QS_Rank"] = df["rank_display"].apply(clean_rank)
    df["QS_Overall_Score"] = df["score"].apply(clean_numeric)
    df["Faculty_Student_Ratio"] = df["student_faculty_ratio"].apply(clean_numeric)
    df["International_Students_Ratio"] = df["international_students"].apply(clean_numeric)
    df["Region"] = df["region"]
    df["Year"] = df["year"]

    # keep latest year per university+country
    df = df.sort_values("Year", ascending=False)
    df = df.drop_duplicates(subset=["University_Name", "Country"], keep="first")

    keep = ["University_Name", "Country", "Region", "Year", "QS_Rank",
            "QS_Overall_Score", "Faculty_Student_Ratio",
            "International_Students_Ratio"]
    out = df[keep].reset_index(drop=True)
    out["Std_Name_Key"] = out["University_Name"].apply(normalize_name)
    out["Std_Country"] = out["Country"]
    return out


def load_the(path):
    df = pd.read_csv(path)
    df["University_Name"] = df["university_name"].str.strip()
    df["Country"] = df["country"].apply(clean_country)
    df["THE_Rank"] = df["world_rank"].apply(clean_rank)
    df["Teaching_Score"] = df["teaching"].apply(clean_numeric)
    df["Research_Score"] = df["research"].apply(clean_numeric)
    df["Citation_Score"] = df["citations"].apply(clean_numeric)
    df["International_Outlook"] = df["international"].apply(clean_numeric)
    df["Industry_Income"] = df["income"].apply(clean_numeric)
    df["Total_Score"] = df["total_score"].apply(clean_numeric)
    df["Year"] = df["year"]

    df = df.sort_values("Year", ascending=False)
    df = df.drop_duplicates(subset=["University_Name", "Country"], keep="first")

    keep = ["University_Name", "Country", "Year", "THE_Rank", "Teaching_Score",
            "Research_Score", "Citation_Score", "International_Outlook",
            "Industry_Income", "Total_Score"]
    out = df[keep].reset_index(drop=True)
    out["Std_Name_Key"] = out["University_Name"].apply(normalize_name)
    out["Std_Country"] = out["Country"]
    return out


def load_cwur(path):
    df = pd.read_csv(path)
    df["University_Name"] = df["institution"].str.strip()
    df["Country"] = df["country"].apply(clean_country)
    df["CWUR_Rank"] = df["world_rank"].apply(clean_rank)
    df["Quality_of_Education"] = df["quality_of_education"].apply(clean_numeric)
    df["Alumni_Employment"] = df["alumni_employment"].apply(clean_numeric)
    df["Publications"] = df["publications"].apply(clean_numeric)
    df["Influence"] = df["influence"].apply(clean_numeric)
    df["Patents"] = df["patents"].apply(clean_numeric)
    df["Year"] = df["year"]

    df = df.sort_values("Year", ascending=False)
    df = df.drop_duplicates(subset=["University_Name", "Country"], keep="first")

    keep = ["University_Name", "Country", "Year", "CWUR_Rank",
            "Quality_of_Education", "Alumni_Employment", "Publications",
            "Influence", "Patents"]
    out = df[keep].reset_index(drop=True)
    out["Std_Name_Key"] = out["University_Name"].apply(normalize_name)
    out["Std_Country"] = out["Country"]
    return out


# ----------------------------------------------------------------------
# 5. CROSS-DATASET FUZZY MATCHING -> canonical Std_University_Name
# ----------------------------------------------------------------------
def build_canonical_names(qs, the, cwur, threshold=88):
    """
    Uses QS as the base reference (largest, most complete name list).
    For each THE/CWUR row, finds the best-matching QS name within the
    same standardized country. If found above threshold, adopts the QS
    canonical name; otherwise keeps its own cleaned name as canonical.
    """
    qs = qs.copy()
    qs["Std_University_Name"] = qs["University_Name"]

    def match_to_qs(df):
        df = df.copy()
        canonical_names = []
        match_scores = []
        for _, row in df.iterrows():
            country = row["Std_Country"]
            candidates = qs[qs["Std_Country"] == country]
            if candidates.empty:
                canonical_names.append(row["University_Name"])
                match_scores.append(0)
                continue
            result = process.extractOne(
                row["Std_Name_Key"],
                candidates["Std_Name_Key"],
                scorer=fuzz.token_sort_ratio,
            )
            if result and result[1] >= threshold:
                matched_idx = candidates.index[candidates["Std_Name_Key"] == result[0]][0]
                canonical_names.append(qs.loc[matched_idx, "University_Name"])
                match_scores.append(result[1])
            else:
                canonical_names.append(row["University_Name"])
                match_scores.append(0)
        df["Std_University_Name"] = canonical_names
        df["QS_Match_Score"] = match_scores
        return df

    the_matched = match_to_qs(the)
    cwur_matched = match_to_qs(cwur)
    return qs, the_matched, cwur_matched


# ----------------------------------------------------------------------
# 6. MAIN
# ----------------------------------------------------------------------
if __name__ == "__main__":
    qs = load_qs("/mnt/user-data/uploads/qs-world-university-rankings-2017-to-2022-V2.csv")
    the = load_the("/mnt/user-data/uploads/timesData.csv")
    cwur = load_cwur("/mnt/user-data/uploads/cwurData.csv")

    qs, the, cwur = build_canonical_names(qs, the, cwur)

    # drop helper columns not needed downstream, keep Std_University_Name front
    for df in (qs, the, cwur):
        df.drop(columns=["Std_Name_Key"], inplace=True)

    qs.to_csv("/mnt/user-data/outputs/qs_clean.csv", index=False)
    the.to_csv("/mnt/user-data/outputs/the_clean.csv", index=False)
    cwur.to_csv("/mnt/user-data/outputs/cwur_clean.csv", index=False)

    # Match quality report
    the_matched_pct = (the["QS_Match_Score"] >= 88).mean() * 100
    cwur_matched_pct = (cwur["QS_Match_Score"] >= 88).mean() * 100

    report = f"""
DATA CLEANING REPORT
=====================
QS   : {len(qs)} universities (latest year kept per university)
THE  : {len(the)} universities -> {the_matched_pct:.1f}% matched to a QS name
CWUR : {len(cwur)} universities -> {cwur_matched_pct:.1f}% matched to a QS name

Unmatched THE universities (sample, QS_Match_Score = 0):
{the[the['QS_Match_Score']==0][['University_Name','Country']].head(15).to_string(index=False)}

Unmatched CWUR universities (sample, QS_Match_Score = 0):
{cwur[cwur['QS_Match_Score']==0][['University_Name','Country']].head(15).to_string(index=False)}
"""
    print(report)
    with open("/mnt/user-data/outputs/match_report.txt", "w") as f:
        f.write(report)
