import re
import unicodedata
import numpy as np
import pandas as pd
from pathlib import Path


ROOT      = Path(__file__).resolve().parent
DATA_DIR  = ROOT / "Data Sources"
BASE_CSV  = ROOT / "Final Dataset" / "02_university_cleaned.csv"
OUT_DIR   = ROOT / "output"
OUT_DIR.mkdir(exist_ok=True)


def readcsv(path, **kw):
    """Read a CSV trying several encodings (the QS/THE files are mixed)."""
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            return pd.read_csv(path, encoding=enc, low_memory=False, **kw)
        except UnicodeDecodeError:
            continue
    return pd.read_csv(path, encoding="latin-1", encoding_errors="replace",
                       low_memory=False, **kw)


def norm_name(s):
    """Normalise a university name into a join key."""
    if pd.isna(s):
        return None
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"&", " and ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\b(the|of|for)\b", " ", s)          # drop noise words
    return re.sub(r"\s+", " ", s).strip()


def parse_rank(v):
    """Return (rank_int, rank_label, is_banded) from any rank cell."""
    if pd.isna(v):
        return (np.nan, None, False)
    s = str(v).strip().replace("=", "")
    if re.fullmatch(r"\d+(\.0+)?", s):                # plain integer rank
        n = int(float(s));  return (n, str(n), False)
    m = re.fullmatch(r"(\d+)\s*[-–]\s*(\d+)", s)      # 701-710
    if m:
        lo, hi = int(m.group(1)), int(m.group(2))
        return (lo, f"{lo}-{hi}", True)
    m = re.fullmatch(r"(\d+)\s*\+", s)                # 1001+
    if m:
        lo = int(m.group(1));  return (lo, f"{lo}+", True)
    m = re.search(r"\d+", s)                          # anything else with a number
    if m:
        n = int(m.group());  return (n, f"{n}+", True)
    return (np.nan, None, True)


def pct_to_float(v):
    """'26%' -> 26.0 ; 43 -> 43.0"""
    if pd.isna(v):
        return np.nan
    m = re.search(r"[\d.]+", str(v))
    return float(m.group()) if m else np.nan


def female_from_ratio(v):
    """'46:54:00' or '33 : 67' -> 46.0 / 33.0 (first number = female %)."""
    if pd.isna(v):
        return np.nan
    m = re.search(r"\d+", str(v))
    return float(m.group()) if m else np.nan


def coalesce(*cols):
    """First non-null across a list of Series (row-wise)."""
    out = cols[0].copy()
    for c in cols[1:]:
        out = out.where(out.notna(), c)
    return out


print(">> loading base (02_university_cleaned.csv)")
base = readcsv(BASE_CSV)
base["nk"] = base["university_name"].map(norm_name)
print(f"   {len(base):,} rows, years {int(base.year.min())}-{int(base.year.max())}")


print(">> reading real source metrics (THE + QS)")


the_frames = []

t1 = readcsv(DATA_DIR / "THE 2016-24.csv")
the_frames.append(pd.DataFrame({
    "nk":  t1["Name"].map(norm_name),
    "year": pd.to_numeric(t1["Year"], errors="coerce"),
    "teaching_score":              pd.to_numeric(t1["Teaching"], errors="coerce"),
    "research_environment_score":  pd.to_numeric(t1["Research Environment"], errors="coerce"),
    "research_quality_score":      pd.to_numeric(t1["Research Quality"], errors="coerce"),
    "industry_impact_score":       pd.to_numeric(t1["Industry Impact"], errors="coerce"),
    "international_outlook_score":  pd.to_numeric(t1["International Outlook"], errors="coerce"),
    "overall_score_the":           pd.to_numeric(t1["Overall Score"], errors="coerce"),
    "total_students_real":         pd.to_numeric(t1["Student Population"], errors="coerce"),
    "students_to_staff":           pd.to_numeric(t1["Students to Staff Ratio"], errors="coerce"),
    "intl_student_pct_real":       t1["International Students"].map(pct_to_float),
    "female_pct_real":             t1["Female to Male Ratio"].map(female_from_ratio),
    "rank_raw":                    t1["Rank"],
}))

t2 = readcsv(DATA_DIR / "THE 2025.csv")
the_frames.append(pd.DataFrame({
    "nk":  t2["university"].map(norm_name),
    "year": pd.to_numeric(t2["year"], errors="coerce"),
    "teaching_score":              pd.to_numeric(t2["teaching"], errors="coerce"),
    "research_environment_score":  pd.to_numeric(t2["research_env"], errors="coerce"),
    "research_quality_score":      pd.to_numeric(t2["research_qual"], errors="coerce"),
    "industry_impact_score":       pd.to_numeric(t2["industry"], errors="coerce"),
    "international_outlook_score":  pd.to_numeric(t2["intl_outlook"], errors="coerce"),
    "overall_score_the":           pd.to_numeric(t2["overall_score"], errors="coerce"),
    "total_students_real":         pd.to_numeric(t2["student_pop"], errors="coerce"),
    "students_to_staff":           pd.to_numeric(t2["student_staff_ratio"], errors="coerce"),
    "intl_student_pct_real":       t2["intl_students_pct"].map(pct_to_float),
    "female_pct_real":             pd.to_numeric(t2["female_pct"], errors="coerce"),
    "rank_raw":                    t2["rank"],
}))

the = pd.concat(the_frames, ignore_index=True)
the = the.dropna(subset=["nk", "year"]).drop_duplicates(subset=["nk", "year"], keep="first")

# ---- QS (real reputation + citations-per-faculty + intl-students score) ---- #
def qs_map(df, c):
    """Flexible column pick across the 3 QS layouts."""
    for name in c:
        if name in df.columns:
            return pd.to_numeric(df[name], errors="coerce")
    return pd.Series(np.nan, index=df.index)

qs_frames = []
for path, name_col, yr in [
    (DATA_DIR / "QS 2026.csv", "Name",             2026),
    (DATA_DIR / "QS 2025.csv", "Institution_Name", 2025),
    (DATA_DIR / "QS 2024.csv", "University",        2024),
]:
    q = readcsv(path)
    qs_frames.append(pd.DataFrame({
        "nk":   q[name_col].map(norm_name),
        "year": yr,
        "academic_reputation_score":  qs_map(q, ["Academic Reputation SCORE","Academic_Reputation_Score","Academic Reputation Score"]),
        "employer_reputation_score":  qs_map(q, ["Employer Reputation SCORE","Employer_Reputation_Score","Employer Reputation Score"]),
        "faculty_student_score":      qs_map(q, ["Faculty Student Ratio SCORE","Faculty_Student_Score","Faculty Student Score"]),
        "citations_per_faculty_score":qs_map(q, ["Citations per Faculty SCORE","Citations_per_Faculty_Score","Citations per Faculty Score"]),
        "intl_students_score":        qs_map(q, ["International Student SCORE","International_Students_Score","International Students Score"]),
        "overall_score_qs":           qs_map(q, ["Overall SCORE","Overall_Score","Overall Score"]),
        # raw QS rank string (this is where the 701-710 style bands live)
        "rank_raw_qs": (q["Rank"] if "Rank" in q.columns
                        else q["RANK_2025"] if "RANK_2025" in q.columns
                        else q["2024 RANK"] if "2024 RANK" in q.columns
                        else pd.Series(np.nan, index=q.index)),
    }))
qs = pd.concat(qs_frames, ignore_index=True)
qs = qs.dropna(subset=["nk"]).drop_duplicates(subset=["nk", "year"], keep="first")


print(">> fixing banded ranks (de-band from QS, the source of the banding)")

qs_rank_lookup = (qs.dropna(subset=["rank_raw_qs"])
                    .set_index(["nk", "year"])["rank_raw_qs"].to_dict())

def resolve_rank(row):
    raw = qs_rank_lookup.get((row["nk"], row["year"]))
    if raw is not None and pd.notna(raw):
        return parse_rank(raw)                      # exact QS band -> lower bound + label
    wr = row["world_rank"]                           # else fall back to base value
    if pd.isna(wr):
        return (np.nan, None, False)
    banded = (float(wr) % 1) != 0                    # .5 midpoint == was a band
    n = int(round(float(wr)))
    return (n, (f"~{n}" if banded else str(n)), banded)

res = base.apply(resolve_rank, axis=1, result_type="expand")
res.columns = ["world_rank_clean", "rank_label", "rank_is_banded"]
base = pd.concat([base, res], axis=1)


print(">> merging real metrics + dropping simulated columns")
df = (base
      .merge(the.drop(columns=["rank_raw"]), on=["nk", "year"], how="left")
      .merge(qs, on=["nk", "year"], how="left", suffixes=("", "_qs")))

# Prefer the REAL source value; fall back to the base value only when it was real too.
df["academic_reputation_score"] = coalesce(df["academic_reputation_score_qs"], df["academic_reputation_score"])
df["employer_reputation_score"] = coalesce(df["employer_reputation_score_qs"], df["employer_reputation_score"])
df["total_students"]            = coalesce(df["total_students_real"], df["total_students"])
df["international_student_pct"]  = df["intl_student_pct_real"]          # REAL (THE)
df["female_percentage"]         = coalesce(df["female_pct_real"], df["female_percentage"])
df["male_percentage"]           = 100 - df["female_percentage"]
df["overall_score"]             = coalesce(df["overall_score_qs"], df["overall_score_the"], df["overall_score"])


DROP = ["publications_count", "citations_count", "citations_per_faculty", "h_index",
        "research_output_score", "research_productivity_index", "subject_field",
        "degree_level", "undergraduate_count", "postgraduate_count", "gender_ratio",
        "international_students_count", "international_student_ratio",
        "faculty_count", "faculty_to_student_ratio", "citations_score",
        # helper / duplicate columns
        "world_rank", "academic_reputation_score_qs", "employer_reputation_score_qs",
        "total_students_real", "intl_student_pct_real", "female_pct_real",
        "overall_score_qs", "overall_score_the", "rank_raw_qs", "nk"]
df = df.drop(columns=[c for c in DROP if c in df.columns])
df = df.rename(columns={"world_rank_clean": "world_rank"})


print(">> computing the 6 KPIs")


def rowmean(cols):
    sub = df[cols]
    return sub.mean(axis=1, skipna=True)


df["kpi_global_ranking_score"] = df["overall_score"].round(1)

df["kpi_academic_reputation_score"] = df["academic_reputation_score"].round(1)


df["kpi_research_impact_score"] = rowmean(
    ["research_quality_score", "research_environment_score", "citations_per_faculty_score"]
).round(1)

df["kpi_international_student_pct"] = df["international_student_pct"].round(1)

df["students_per_faculty"]        = df["students_to_staff"].round(1)
df["kpi_faculty_to_student_ratio"] = (1 / df["students_to_staff"]).round(4)   # staff per student

df["kpi_research_productivity_index"] = rowmean(
    ["research_environment_score", "research_quality_score", "industry_impact_score"]
).round(1)

df["national_rank"] = (df.groupby(["country", "year"])["world_rank"]
                         .rank(method="min").astype("Int64"))

g = df.groupby(["country", "year"])
df["country_avg_rank"]                = g["world_rank"].transform("mean").round(1)
df["universities_ranked_count"]       = g["world_rank"].transform("count")
df["best_university_rank"]            = g["world_rank"].transform("min")
df["country_avg_overall_score"]       = g["overall_score"].transform("mean").round(1)
df["country_avg_academic_reputation"] = g["academic_reputation_score"].transform("mean").round(1)
df["country_avg_research_impact"]     = g["kpi_research_impact_score"].transform("mean").round(1)
df["country_avg_international_pct"]    = g["kpi_international_student_pct"].transform("mean").round(1)


ORDER = [
    # identity
    "university_id", "university_name", "year", "country", "region", "city",
    "university_type",
    # ranking
    "world_rank", "rank_label", "rank_is_banded", "national_rank", "overall_score",
    # reputation (real QS)
    "academic_reputation_score", "employer_reputation_score",
    # research (real THE pillars + QS)
    "teaching_score", "research_environment_score", "research_quality_score",
    "industry_impact_score", "international_outlook_score", "citations_per_faculty_score",
    # students (real THE)
    "total_students", "students_to_staff", "students_per_faculty",
    "international_student_pct", "female_percentage", "male_percentage",
    # the 6 KPIs
    "kpi_global_ranking_score", "kpi_academic_reputation_score",
    "kpi_research_impact_score", "kpi_international_student_pct",
    "kpi_faculty_to_student_ratio", "kpi_research_productivity_index",
    # country aggregates
    "country_avg_rank", "universities_ranked_count", "best_university_rank",
    "country_avg_overall_score", "country_avg_academic_reputation",
    "country_avg_research_impact", "country_avg_international_pct",
]
final = df[[c for c in ORDER if c in df.columns]].copy()

final["overall_score"] = final["overall_score"].round(1)
def tidy(s):
    if pd.isna(s):
        return s
    return (str(s).replace("\u2019", "'").replace("\u2018", "'")
                  .replace("\u2013", "-").replace("\u2014", "-").strip())
for col in ["university_name", "city", "country"]:
    final[col] = final[col].map(tidy)
# a row is "more complete" the fewer nulls it has -> keep that one on collision
final["_completeness"] = final.notna().sum(axis=1)
final = (final.sort_values(["_completeness"], ascending=False)
              .drop_duplicates(subset=["university_name", "year"], keep="first")
              .drop(columns="_completeness"))
final = final.sort_values(["year", "world_rank", "university_name"]).reset_index(drop=True)

csv_path = OUT_DIR / "university_final_dataset.csv"
final.to_csv(csv_path, index=False)
print(f"\n>> wrote {csv_path}  ({final.shape[0]:,} rows x {final.shape[1]} cols)")

print("\n================ QUALITY REPORT ================")
print(f"rows: {len(final):,}   cols: {final.shape[1]}   years: "
      f"{int(final.year.min())}-{int(final.year.max())}")
print(f"banded ranks flagged: {final.rank_is_banded.sum():,} "
      f"({final.rank_is_banded.mean()*100:.1f}%)  |  non-integer ranks remaining: "
      f"{(final.world_rank.dropna() % 1 != 0).sum()}")
print("\nreal-data coverage of the 6 KPIs (non-null %):")
for k in ["kpi_global_ranking_score","kpi_academic_reputation_score",
          "kpi_research_impact_score","kpi_international_student_pct",
          "kpi_faculty_to_student_ratio","kpi_research_productivity_index"]:
    print(f"   {k:34s} {final[k].notna().mean()*100:5.1f}%")

final.to_pickle(OUT_DIR / "_final.pkl")

print(">> writing university_final_dataset.xlsx")
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

xlsx_path = OUT_DIR / "university_final_dataset.xlsx"

data_dict = [
    ("university_id", "Identifier", "Stable id per university (from Milestone 1)"),
    ("university_name", "Identifier", "University name (typographic quotes normalised)"),
    ("year", "Identifier", "Ranking year, 2016-2026"),
    ("country / region / city", "Real (QS/THE)", "Location fields"),
    ("university_type", "Real (QS)", "Public / Private"),
    ("world_rank", "Real (QS-primary), de-banded", "Global rank. Banded ranks stored as the band's lower bound"),
    ("rank_label", "Derived", "Human-readable rank: '1', '601-610', or '~842' for approximated bands"),
    ("rank_is_banded", "Derived flag", "TRUE when the rank is a QS band, not a precise position"),
    ("national_rank", "Derived", "Rank within country & year, computed from world_rank"),
    ("overall_score", "Real (QS>THE)", "Published overall score, 0-100"),
    ("academic_reputation_score", "Real (QS)", "QS Academic Reputation, 0-100"),
    ("employer_reputation_score", "Real (QS)", "QS Employer Reputation, 0-100"),
    ("teaching_score", "Real (THE)", "THE Teaching pillar, 0-100"),
    ("research_environment_score", "Real (THE)", "THE Research Environment pillar, 0-100"),
    ("research_quality_score", "Real (THE)", "THE Research Quality (citation impact) pillar, 0-100"),
    ("industry_impact_score", "Real (THE)", "THE Industry pillar, 0-100"),
    ("international_outlook_score", "Real (THE)", "THE International Outlook pillar, 0-100"),
    ("citations_per_faculty_score", "Real (QS)", "QS Citations per Faculty, 0-100"),
    ("total_students", "Real (THE)", "Student population"),
    ("students_to_staff / students_per_faculty", "Real (THE)", "Students per staff member"),
    ("international_student_pct", "Real (THE)", "Percentage of international students"),
    ("female_percentage / male_percentage", "Real (THE)", "Gender split, sums to 100"),
    ("kpi_* (6 columns)", "KPI (from real inputs)", "See the KPI_Definitions sheet"),
    ("country_avg_* / universities_ranked_count / best_university_rank",
     "Derived", "Country-year aggregates recomputed from the real data"),
]

kpi_defs = [
    ("1. Global Ranking Score", "kpi_global_ranking_score", "= overall_score",
     "Real published overall score (QS, else THE)", "0-100"),
    ("2. Academic Reputation Score", "kpi_academic_reputation_score", "= academic_reputation_score",
     "QS Academic Reputation (real)", "0-100"),
    ("3. Research Impact Score", "kpi_research_impact_score",
     "= mean(research_quality, research_environment, citations_per_faculty)",
     "THE research pillars + QS citations/faculty (all real)", "0-100"),
    ("4. International Student %", "kpi_international_student_pct", "= international_student_pct",
     "THE % international students (real)", "0-100"),
    ("5. Faculty-to-Student Ratio", "kpi_faculty_to_student_ratio", "= 1 / students_to_staff",
     "THE students-to-staff ratio (real), inverted to faculty per student", "ratio"),
    ("6. Research Productivity Index", "kpi_research_productivity_index",
     "= mean(research_environment, research_quality, industry_impact)",
     "THE research pillars (all real)", "0-100"),
]

change_log = [
    ("Banded '700+' ranks", "Stored as band midpoints (fake .5 decimals, e.g. 705.5)",
     "De-banded to band lower bound + rank_is_banded flag + rank_label. 5,232 rows flagged."),
    ("Research counts", "publications_count, citations_count, h_index, research_output_score, "
     "research_productivity_index, citations_per_faculty were SIMULATED",
     "Removed. Replaced with REAL THE pillar scores (Teaching/Research Env/Research "
     "Quality/Industry/Intl Outlook) + QS Citations-per-Faculty."),
    ("Categorical fields", "subject_field, degree_level, undergraduate_count, "
     "postgraduate_count were invented (no source)", "Removed."),
    ("Gender", "gender_ratio mangled into a time value ('45:55:00')",
     "Removed. Kept real female_percentage / male_percentage from THE."),
    ("International students", "international_student_ratio derived from a simulated count",
     "Replaced with real THE international_student_pct."),
    ("Faculty ratio", "faculty_to_student_ratio from simulated faculty_count",
     "Recomputed from real THE students-to-staff ratio."),
    ("Country aggregates", "computed over partly-simulated data",
     "Recomputed from the real data only."),
    ("Names", "'Ca' Foscari' appeared twice (curly vs straight apostrophe)",
     "Typographic quotes normalised; 53 duplicate rows merged."),
    ("Old raw file", "01_university_raw_data.csv had lost its headers (columns named 1..38)",
     "Not used. Rebuilt from 02_university_cleaned.csv enriched with the real sources."),
]

read_me = [
    ("EduVision_DV — Final Dataset (Milestone 2 / Module 3)", ""),
    ("", ""),
    ("What this is", "One row per university per year (2016-2026), rebuilt on REAL "
     "QS + THE data, with the 6 required KPIs. Feeds the Tableau dashboards."),
    ("Rows / Columns", f"{len(final):,} rows  x  {final.shape[1]} columns"),
    ("Real-data coverage", "Ranking & reputation KPIs: 100%.  Research / international / "
     "student KPIs: ~75-80% (the share of rows that name-matched a QS/THE source)."),
    ("Blank cells", "Where a university-year was not in the QS/THE sources, the research / "
     "student columns are left BLANK on purpose (not simulated). In the research & "
     "student dashboards, filter to non-null."),
    ("Sources", "QS World University Rankings (2024-2026) + Times Higher Education (2016-2025)."),
    ("Sheets", "University_Data = the dataset · Data_Dictionary · KPI_Definitions · Change_Log."),
]

with pd.ExcelWriter(xlsx_path, engine="openpyxl") as xw:
    final.to_excel(xw, sheet_name="University_Data", index=False)
    pd.DataFrame(read_me, columns=["Field", "Detail"]).to_excel(xw, sheet_name="Read_Me", index=False)
    pd.DataFrame(data_dict, columns=["Column", "Source type", "Description"]).to_excel(xw, sheet_name="Data_Dictionary", index=False)
    pd.DataFrame(kpi_defs, columns=["KPI", "Column", "Formula", "Real inputs", "Scale"]).to_excel(xw, sheet_name="KPI_Definitions", index=False)
    pd.DataFrame(change_log, columns=["Area", "Old (broken)", "Now (fixed)"]).to_excel(xw, sheet_name="Change_Log", index=False)

# --- formatting pass -------------------------------------------------------- #
wb = load_workbook(xlsx_path)
HEAD_FILL = PatternFill("solid", fgColor="1F3864")
HEAD_FONT = Font(name="Arial", bold=True, color="FFFFFF", size=11)
BODY_FONT = Font(name="Arial", size=10)
for ws in wb.worksheets:
    ws.sheet_view.showGridLines = True
    for cell in ws[1]:
        cell.fill = HEAD_FILL; cell.font = HEAD_FONT
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    # column widths + body font
    for col in ws.columns:
        letter = get_column_letter(col[0].column)
        longest = max((len(str(c.value)) for c in col if c.value is not None), default=10)
        if ws.title == "University_Data":
            ws.column_dimensions[letter].width = min(max(longest + 2, 10), 26)
        else:
            ws.column_dimensions[letter].width = min(max(longest + 2, 14), 70)
        for c in col[1:]:
            c.font = BODY_FONT
            if ws.title != "University_Data":
                c.alignment = Alignment(vertical="top", wrap_text=True)
    ws.row_dimensions[1].height = 28
wb.save(xlsx_path)
print(f"   wrote {xlsx_path}")
print("\nDONE.")
