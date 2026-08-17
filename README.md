# EduVision_DV — Higher Education Performance Dashboard

A Power BI dashboard suite analyzing university rankings, research performance, student
diversity, and country-level education benchmarking.

---

## 1. Dataset Sources

| File | Description |
|---|---|
| `raw.csv` | Base university performance dataset — simulates the structure of publicly available global ranking sources such as the **QS World University Rankings** and **Times Higher Education (THE) World University Rankings**, covering `world_rank`, `overall_score`, reputation scores, research metrics, student metrics, and country-level benchmarks, per university per year (2016–2025). |
| `raw1.csv` | First-source extract of `raw.csv` — university identity, ranking, and research columns, with source-specific naming conventions (e.g. `Univ_ID`, `World Rank`). |
| `raw2.csv` | Second-source extract of `raw.csv` — student, diversity, and country-benchmark columns, with its own naming conventions (e.g. `uni_id`, `Intl_Student_Ratio_pct`). |
| `merged_education_dataset.csv` | `raw1` + `raw2` merged on `university_id` + `year` after column-name standardization (`merger.ipynb`). No cleaning applied at this stage. |
| `university_cleaned.csv` | Cleaned version of the merged dataset — duplicates removed, missing values imputed, text normalized, `gender_ratio` reconstructed (`education_cleaning.ipynb`). |
| `university_final_dataset.xlsx` | Final, KPI-enriched dataset used as the Power BI data source (`generate_education_kpis.py`). |

**Pipeline:** `raw.csv → raw1.csv + raw2.csv → merged_education_dataset.csv → university_cleaned.csv → university_final_dataset.xlsx → Power BI`

---

## 2. KPI Definitions

### Core KPIs (Module 3 requirement)

| KPI | Definition | Formula |
|---|---|---|
| **Global Ranking Score** | Normalized 0–100 score from `world_rank`, higher = better global standing | `100 × (max(world_rank) − world_rank) / (max(world_rank) − min(world_rank))` |
| **Research Impact Score** | Weighted composite of citation impact and productivity | `0.5 × citations_score + 0.3 × norm(citations_per_faculty) + 0.2 × norm(h_index)`, each term normalized 0–100 |
| **Faculty-to-Student Ratio** | Students per faculty member | `total_students / faculty_count` |
| **International Student Percentage** | Share of international students | `international_students_count / total_students × 100` |
| **Academic Reputation Score** | Pass-through of source reputation score | `academic_reputation_score` |
| **Research Productivity Index** | Pass-through of source productivity index | `research_productivity_index` |

### Dashboard measures built in Power BI

| Measure | Definition | Dashboard |
|---|---|---|
| Top Global Ranking | `MIN(world_rank)`, filtered/sliced context | University Overview |
| Top Performing Country | Country with the highest `country_avg_overall_score` (`TOPN` + `ALLSELECTED`) | Country Comparison |
| University with Max Students | University with the highest `total_students` (`TOPN` + `ALLSELECTED`) | Student Analytics |
| Top Research University | University with the highest `research_impact_score` (`TOPN` + `ALLSELECTED`) | Research Analytics |
| Avg Country [Metric] | Country-level average, deduplicated via `AVERAGEX(VALUES(country), ...)` to avoid double-counting countries with many universities | Country Comparison |

---

## 3. Education Analytics Methodology

**1. Data Collection** — Two independently-formatted source extracts (`raw1.csv`, `raw2.csv`) are simulated to mirror ingesting data from two different ranking providers, each with its own column naming convention, whitespace, and casing inconsistencies.

**2. Data Cleaning & Transformation** (`education_cleaning.ipynb`)
- Column names standardized to a single `snake_case` schema
- Duplicate rows removed
- Text fields stripped of whitespace and case-normalized
- Missing numeric values imputed with the column median; missing categorical values imputed with the column mode
- `gender_ratio` reconstructed from `female_percentage` / `male_percentage` using a hyphen separator (`"55-45"`) to prevent spreadsheet software from auto-converting the value into a time format

**3. KPI Engineering** (`generate_education_kpis.py`)
- Six core KPIs computed as live Excel formulas referencing a documented `Assumptions` sheet (min/max normalization constants), so the workbook recalculates if source values change
- Output validated with zero formula errors across 132,750+ formulas

**4. Power BI Modeling**
- All aggregations built as **measures**, not calculated columns, so every KPI updates live with slicer selections (`year`, `region`, `country`, `subject_field`)
- Rank-type fields (`world_rank`, `national_rank`) use ascending sort / "≤ N" filters rather than `Top N` — since `Top N` selects the *largest* values, which is the wrong direction for a field where smaller = better
- Country-level pre-aggregated columns (`country_avg_*`) are deduplicated with `AVERAGEX(VALUES(country), ...)` before averaging, since they repeat once per university row within a country
- "Top X by Y" KPI cards use a `TOPN(1, ALLSELECTED(...), ...)` pattern so the result respects active slicers while still ranking across the full (filtered) dataset

**5. Dashboard Development** — Four interconnected dashboards (University Overview, Research Analytics, Student Analytics, Country Comparison) built with synchronized slicers and consistent dark-theme styling.

---

## Project Structure

```
/data        raw.csv, raw1.csv, raw2.csv, merged_education_dataset.csv,
             university_cleaned.csv, university_final_dataset.xlsx
/scripts     merger.ipynb, education_cleaning.ipynb, generate_education_kpis.py
/dashboard   EduVision_DV.pbix
/docs        README.md, Dashboard_Guide.pdf
```
