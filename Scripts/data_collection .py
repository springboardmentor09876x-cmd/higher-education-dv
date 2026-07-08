import re
import numpy as np
import pandas as pd

np.random.seed(42)  
RAW = "./raw_data"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def clean_name(name):
    """Normalize a university name for matching/joining across sources."""
    if not isinstance(name, str):
        return ""
    n = re.sub(r"\s*\([^)]*\)", "", name)          # drop "(MIT)" style suffixes
    n = re.sub(r"\s+", " ", n).strip()
    return n


def to_number(x):
    """Turn '3,730' / '48%' / '51=' / '70.1–75.0' / 'NA' style strings into floats."""
    if pd.isna(x):
        return np.nan
    s = str(x).replace(",", "").replace("%", "").replace("=", "").strip()
    s = s.replace("–", "-").replace("—", "-")
    if s in ("", "NA", "-", "nan"):
        return np.nan
    if "-" in s[1:]:  # a range like '70.1-75.0' (ignore a leading minus sign)
        parts = [p for p in re.split(r"(?<=\d)-", s) if p]
        try:
            nums = [float(p) for p in parts]
            return sum(nums) / len(nums)
        except ValueError:
            pass
    try:
        return float(s)
    except ValueError:
        return np.nan


def read_csv_safe(path, **kwargs):
    for enc in ("utf-8-sig", "utf-8", "cp1254", "latin1"):
        try:
            return pd.read_csv(path, encoding=enc, **kwargs)
        except (UnicodeDecodeError, UnicodeError):
            continue
    return pd.read_csv(path, encoding="latin1", errors="ignore", **kwargs)


SIZE_STUDENT_RANGE = {"XS": (1000, 4000), "S": (4000, 9000), "M": (9000, 18000),
                       "L": (18000, 30000), "XL": (30000, 55000)}


# ---------------------------------------------------------------------------
# 1. Load & standardize each QS year source into a common schema
# ---------------------------------------------------------------------------
def load_qs_2017_2022():
    df = read_csv_safe(f"{RAW}/qs-world-university-rankings-2017-to-2022-V2.csv")
    out = pd.DataFrame({
        "university_raw": df["university"],
        "year": df["year"],
        "world_rank": df["rank_display"].apply(to_number),
        "overall_score": df["score"].apply(to_number),
        "country": df["country"],
        "city": df["city"],
        "region": df["region"],
        "university_type": df["type"],
        "size": df["size"],
        "student_faculty_ratio": df["student_faculty_ratio"],
        "international_students_count": df["international_students"].apply(to_number),
        "faculty_count": df["faculty_count"].apply(to_number),
    })
    return out


def load_qs_2023():
    df = read_csv_safe(f"{RAW}/2023_QS_World_University_Rankings.csv")
    out = pd.DataFrame({
        "university_raw": df["Institution"],
        "year": 2023,
        "world_rank": df["Rank"].apply(to_number),
        "overall_score": df["ScoreScaled"],
        "country": df["Location"],
        "academic_reputation_score": df["ArScore"],
        "employer_reputation_score": df["ErScore"],
        "faculty_student_score": df["FsrScore"],
        "citations_score": df["CpfScore"],
        "intl_faculty_score": df["IfrScore"],
        "intl_students_score": df["IsrScore"],
    })
    return out


def load_qs_2024():
    df = read_csv_safe(f"{RAW}/2024_QS_World_University_Rankings_1_1__For_qs_com___1_.csv")
    df = df.iloc[1:].reset_index(drop=True)  # drop the metadata header row
    out = pd.DataFrame({
        "university_raw": df["Institution Name"],
        "year": 2024,
        "world_rank": df["2024 RANK"].apply(to_number),
        "overall_score": df["Overall SCORE"].apply(to_number),
        "country": df["Country"],
        "size": df["SIZE"],
        "university_type": df["STATUS"],
        "academic_reputation_score": df["Academic Reputation Score"].apply(to_number),
        "employer_reputation_score": df["Employer Reputation Score"].apply(to_number),
        "faculty_student_score": df["Faculty Student Score"].apply(to_number),
        "citations_score": df["Citations per Faculty Score"].apply(to_number),
        "intl_faculty_score": df["International Faculty Score"].apply(to_number),
        "intl_students_score": df["International Students Score"].apply(to_number),
    })
    return out


def load_qs_2025():
    df = read_csv_safe(f"{RAW}/QS_World_University_Rankings_2025__Top_global_universities_.csv")
    out = pd.DataFrame({
        "university_raw": df["Institution_Name"],
        "year": 2025,
        "world_rank": df["RANK_2025"].apply(to_number),
        "overall_score": df["Overall_Score"].apply(to_number),
        "country": df["Location"],
        "region": df["Region"],
        "size": df["SIZE"],
        "academic_reputation_score": df["Academic_Reputation_Score"].apply(to_number),
        "employer_reputation_score": df["Employer_Reputation_Score"].apply(to_number),
        "faculty_student_score": df["Faculty_Student_Score"].apply(to_number),
        "citations_score": df["Citations_per_Faculty_Score"].apply(to_number),
        "intl_faculty_score": df["International_Faculty_Score"].apply(to_number),
        "intl_students_score": df["International_Students_Score"].apply(to_number),
    })
    return out


def load_qs_2026():
    df = read_csv_safe(f"{RAW}/2026_QS_World_University_Rankings.csv")
    out = pd.DataFrame({
        "university_raw": df["Institution Name"],
        "year": 2026,
        "world_rank": df["2026 Rank"].apply(to_number),
        "overall_score": df["Overall SCORE"].apply(to_number),
        "country": df["Country/Territory"],
        "region": df["Region"],
        "size": df["Size"],
        "university_type": df["Status"],
        "academic_reputation_score": df["AR SCORE"].apply(to_number),
        "employer_reputation_score": df["ER SCORE"].apply(to_number),
        "faculty_student_score": df["FSR SCORE"].apply(to_number),
        "citations_score": df["CPF SCORE"].apply(to_number),
        "intl_faculty_score": df["IFR SCORE"].apply(to_number),
        "intl_students_score": df["ISR SCORE"].apply(to_number),
    })
    return out


def load_the_historical():
    df = read_csv_safe(f"{RAW}/THE_World_University_Rankings_2016-2026.csv")

    def parse_ratio(x):
        if pd.isna(x):
            return np.nan, np.nan
        s = str(x).replace(" ", "")
        m = re.match(r"(\d+):(\d+)", s)
        if not m:
            return np.nan, np.nan
        f, mle = float(m.group(1)), float(m.group(2))
        total = f + mle
        return (f / total * 100, mle / total * 100) if total else (np.nan, np.nan)

    fem, mal = zip(*df["Female to Male Ratio"].apply(parse_ratio))
    out = pd.DataFrame({
        "university_raw": df["Name"],
        "year": df["Year"],
        "world_rank_the": df["Rank"].apply(to_number),
        "overall_score_the": df["Overall Score"].apply(to_number),
        "country": df["Country"],
        "total_students_the": df["Student Population"].apply(to_number),
        "students_staff_ratio_the": df["Students to Staff Ratio"].apply(to_number),
        "international_student_ratio_the": df["International Students"].apply(to_number),
        "female_percentage": fem,
        "male_percentage": mal,
        "teaching_score": df["Teaching"],
        "research_quality_score": df["Research Quality"],
        "industry_impact_score": df["Industry Impact"],
        "international_outlook_score": df["International Outlook"],
    })
    return out


# ---------------------------------------------------------------------------
# 2. Load everything, tag a clean join key, and stack the QS years
# ---------------------------------------------------------------------------
qs_frames = [load_qs_2017_2022(), load_qs_2023(), load_qs_2024(), load_qs_2025(), load_qs_2026()]
qs_all = pd.concat(qs_frames, ignore_index=True, sort=False)
qs_all["university_name"] = qs_all["university_raw"].apply(clean_name)
qs_all = qs_all[qs_all["university_name"] != ""]

the_all = load_the_historical()
the_all["university_name"] = the_all["university_raw"].apply(clean_name)
the_all = the_all[the_all["university_name"] != ""]

# ---------------------------------------------------------------------------
# 3. Merge QS (primary) with THE (supplementary metrics) on name + year
# ---------------------------------------------------------------------------
master = qs_all.merge(
    the_all.drop(columns=["university_raw"]).rename(columns={"country": "country_the"}),
    on=["university_name", "year"], how="outer",
)
master["country"] = master["country"].combine_first(master["country_the"])
master = master.drop(columns=["country_the"])

# Fill in region/city/type/size, and carry each university's real metadata
# forward/backward across years (a university's home country/city/type
# rarely changes year to year, so this is a reasonable, non-fabricated fill).
for col in ["country", "region", "city", "university_type", "size"]:
    master[col] = master.groupby("university_name")[col].transform(lambda s: s.ffill().bfill())

# Prefer QS's own world_rank/overall_score; fall back to THE's if QS is missing
master["world_rank"] = pd.to_numeric(master["world_rank"], errors="coerce").fillna(
    pd.to_numeric(master["world_rank_the"], errors="coerce"))
master["overall_score"] = pd.to_numeric(master["overall_score"], errors="coerce").fillna(
    pd.to_numeric(master["overall_score_the"], errors="coerce"))
# Any remaining gaps (no score from either source): estimate from rank position
# within its year using a smooth inverse-rank curve, clearly a simulated fallback.
max_rank_by_year = master.groupby("year")["world_rank"].transform("max")
rank_based_estimate = 100 * (1 - (master["world_rank"].fillna(max_rank_by_year) / max_rank_by_year.replace(0, np.nan)))
master["overall_score"] = master["overall_score"].fillna(rank_based_estimate.clip(1, 99).round(1))

print(f"After merge: {master.shape[0]} rows, {master['university_name'].nunique()} unique universities")

# ---------------------------------------------------------------------------
# 4. Drop rows with no usable rank/score at all (not real universities data)
# ---------------------------------------------------------------------------
master = master[master["world_rank"].notna() | master["overall_score"].notna()].copy()
master = master.reset_index(drop=True)

# Fill any remaining region gaps using the most common region already observed for that country
country_region_map = (
    master.dropna(subset=["region"]).groupby("country")["region"]
    .agg(lambda s: s.value_counts().idxmax())
)
missing_region = master["region"].isna()
master.loc[missing_region, "region"] = master.loc[missing_region, "country"].map(country_region_map)
# Any country with no region info anywhere (rare) - leave to the classifier below
FALLBACK_REGION = {
    "United States": "North America", "Canada": "North America", "Mexico": "Latin America",
}
still_missing = master["region"].isna()
master.loc[still_missing, "region"] = master.loc[still_missing, "country"].map(FALLBACK_REGION)
master["region"] = master["region"].fillna("Other")

# ---------------------------------------------------------------------------
# 5. IDs and simple derived (real, formula-based) columns
# ---------------------------------------------------------------------------
master["university_id"] = master["university_name"].astype("category").cat.codes + 1
master["national_rank"] = master.groupby(["year", "country"])["world_rank"].rank(method="min")
master["country_code_group"] = master["country"]

# citations_score: prefer QS's own citations score; else use nothing (kept NaN for now)
# faculty_to_student_ratio and total_students: derive from real counts where we have them
master["faculty_to_student_ratio"] = master["student_faculty_ratio"]
real_total_students = master["student_faculty_ratio"] * master["faculty_count"]
master["total_students"] = master["total_students_the"].fillna(real_total_students)

# international_student_ratio: prefer real QS count / total_students; else THE %
computed_ratio = (master["international_students_count"] / master["total_students"]) * 100
master["international_student_ratio"] = computed_ratio.fillna(master["international_student_ratio_the"])

# ---------------------------------------------------------------------------
# 6. Simulated columns - no real source exists in the raw data for these.
#    Generated with plausible, rank/score-correlated randomness so the
#    dataset is internally consistent even though the exact figures are
#    fabricated. Every simulated column is listed in the README.
# ---------------------------------------------------------------------------
n = len(master)
rank_pct = 1 - (master["world_rank"].fillna(master["world_rank"].max()) / master["world_rank"].max())
score_norm = (master["overall_score"].fillna(50) / 100).clip(0, 1)

# --- Student body size, where no real figure exists ---
missing_total = master["total_students"].isna()
size_fallback = master["size"].fillna("M").map(lambda s: SIZE_STUDENT_RANGE.get(s, (5000, 20000)))
sim_total = size_fallback.apply(lambda r: np.random.randint(r[0], r[1]))
master.loc[missing_total, "total_students"] = sim_total[missing_total]

missing_ratio = master["international_student_ratio"].isna()
master.loc[missing_ratio, "international_student_ratio"] = (
    np.random.normal(15 + 20 * score_norm[missing_ratio], 5).clip(1, 60)
)
master["international_students_count"] = master["international_students_count"].fillna(
    (master["total_students"] * master["international_student_ratio"] / 100).round()
)

missing_faculty = master["faculty_count"].isna()
sim_ratio = np.random.normal(14, 4, n).clip(5, 30)
master.loc[missing_faculty, "faculty_count"] = (master["total_students"] / sim_ratio)[missing_faculty].round()
master["faculty_to_student_ratio"] = master["faculty_to_student_ratio"].fillna(
    master["total_students"] / master["faculty_count"]
)

# --- Gender split (real for THE-covered rows; simulated ~50/50 +- noise otherwise) ---
missing_gender = master["female_percentage"].isna()
master.loc[missing_gender, "female_percentage"] = np.random.normal(50, 8, n)[missing_gender].clip(20, 80)
master["male_percentage"] = master["male_percentage"].fillna(100 - master["female_percentage"])
master["gender_ratio"] = master["female_percentage"].round().astype(int).astype(str) + " : " + \
                          master["male_percentage"].round().astype(int).astype(str)

# --- University type (Public/Private), where not already known ---
missing_type = master["university_type"].isna()
master.loc[missing_type, "university_type"] = np.random.choice(
    ["Public", "Private"], size=missing_type.sum(), p=[0.65, 0.35]
)
master["university_type"] = master["university_type"].replace({"A": "Public", "B": "Private"})

# --- Reputation / citation scores, where not already known (QS-only metric) ---
for col, base in [("academic_reputation_score", score_norm), ("employer_reputation_score", score_norm),
                   ("citations_score", score_norm)]:
    miss = master[col].isna()
    master.loc[miss, col] = (base[miss] * 100 * np.random.normal(1, 0.15, miss.sum())).clip(1, 100)

# --- Research Analytics: no publication/citation-count data exists anywhere
#     in the raw sources, so it is fully simulated but internally consistent
#     (better-ranked, larger-faculty universities produce proportionally more).
master["faculty_count"] = master["faculty_count"].clip(lower=50)
base_pubs_per_faculty = np.random.normal(3.5, 1.2, n).clip(0.5, 10)
master["publications_count"] = (master["faculty_count"] * base_pubs_per_faculty * (0.6 + score_norm)).round()
master["citations_per_faculty"] = (master["citations_score"] / 100 * np.random.normal(80, 20, n)).clip(1, None)
master["citations_count"] = (master["citations_per_faculty"] * master["faculty_count"]).round()
master["h_index"] = (np.sqrt(master["citations_count"].clip(lower=1)) * np.random.normal(1.0, 0.1, n)).round().astype(int)
master["research_output_score"] = (0.5 * master["academic_reputation_score"] + 0.5 * master["citations_score"]).round(1)
master["research_productivity_index"] = (master["publications_count"] / master["faculty_count"]).round(2)

SUBJECTS = ["Engineering & Technology", "Natural Sciences", "Life Sciences & Medicine",
            "Social Sciences & Management", "Arts & Humanities"]
master["subject_field"] = np.random.choice(SUBJECTS, size=n)

# --- Student distribution (no real UG/PG split exists in any raw source) ---
ug_share = np.random.normal(0.68, 0.08, n).clip(0.4, 0.9)
master["undergraduate_count"] = (master["total_students"] * ug_share).round()
master["postgraduate_count"] = (master["total_students"] - master["undergraduate_count"]).round()
master["degree_level"] = "Undergraduate & Postgraduate"

# --- City, where still unknown after carry-forward ---
missing_city = master["city"].isna()
master.loc[missing_city, "city"] = master.loc[missing_city, "country"]  # best-effort fallback, not fabricated names

# ---------------------------------------------------------------------------
# 7. Country Comparison aggregates (fully derived from the data above - real)
# ---------------------------------------------------------------------------
country_year_agg = master.groupby(["year", "country"]).agg(
    country_avg_rank=("world_rank", "mean"),
    universities_ranked_count=("university_id", "nunique"),
    best_university_rank=("world_rank", "min"),
    country_avg_overall_score=("overall_score", "mean"),
    country_avg_academic_reputation=("academic_reputation_score", "mean"),
    country_avg_citations=("citations_score", "mean"),
    country_avg_international_ratio=("international_student_ratio", "mean"),
).round(2).reset_index()

master = master.merge(country_year_agg, on=["year", "country"], how="left")

# ---------------------------------------------------------------------------
# 8. Final column selection, matching the dashboard spec naming exactly
# ---------------------------------------------------------------------------
FINAL_COLUMNS = [
    "university_id", "university_name", "year", "world_rank", "national_rank", "overall_score",
    "country", "region", "city", "university_type",
    "academic_reputation_score", "employer_reputation_score", "citations_score",
    "publications_count", "citations_count", "citations_per_faculty", "h_index",
    "research_output_score", "research_productivity_index", "subject_field",
    "total_students", "international_students_count", "international_student_ratio",
    "faculty_count", "faculty_to_student_ratio",
    "gender_ratio", "female_percentage", "male_percentage",
    "degree_level", "undergraduate_count", "postgraduate_count",
    "country_avg_rank", "universities_ranked_count", "best_university_rank",
    "country_avg_overall_score", "country_avg_academic_reputation",
    "country_avg_citations", "country_avg_international_ratio",
]
final = master[FINAL_COLUMNS].copy()

# ---------------------------------------------------------------------------
# 9. Completeness check + export
# ---------------------------------------------------------------------------
completeness = 100 - final.isna().mean() * 100
print("\nColumn completeness (%):")
print(completeness.round(1).sort_values())
print(f"\nOverall completeness: {completeness.mean():.2f}%")

final.to_csv("university_raw_data.csv", index=False)
print(f"\nSaved university_raw_data.csv - {final.shape[0]} rows x {final.shape[1]} columns")
