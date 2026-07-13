
# EduVision_DV — Dataset Brief

## Overview
The dataset - `university_raw_data.csv` (22,117 rows × 38 columns, one row per university per year, 2017–2026) combines the QS World University Rankings (2017–2026) and the Times Higher Education (THE) World University Rankings (2016–2026) into a single, university-by-year table used to power the EduVision_DV Tableau dashboard suite.

**99.94% overall**, every individual column above 95% (target met).

| Real (from QS/THE datasets) | Formula-derived (real inputs, computed) | Simulated |
|---|---|---|
| world_rank, overall_score, country, region, city, university_type, academic_reputation_score, employer_reputation_score, citations_score, total_students (2017-22), faculty_count (2017-22), gender split (THE) | national_rank, faculty_to_student_ratio, international_student_ratio, country-level averages (all `country_avg_*`, `universities_ranked_count`, `best_university_rank`) | publications_count, citations_count, citations_per_faculty, h_index, research_output_score, research_productivity_index, subject_field, undergraduate/postgraduate split, and any real column's gaps for years/universities not covered by that source |

Simulated values aren't random noise — they're generated *correlated with each university's real rank/score/size*

- **QS is the primary ranking source**; THE fills in gaps and supplies gender-split and student-population data.
- A university's country/city/type/size is carried forward/backward across its own years where a real value exists in any year
- `national_rank` is computed by ranking each university's `world_rank` within its own country/year — fully derived from real rank data.
- Country-level aggregates are `groupby` calculations over the merged data

## Sources
| Source | Years covered | Provider |
|---|---|---|
| QS World University Rankings | 2017–2026 | Quacquarelli Symonds (QS) |
| THE World University Rankings | 2016–2026 | Times Higher Education (THE) |

Both are publicly published university ranking datasets. QS is treated as the primary ranking source; THE supplements it with metrics QS doesn't report (student population, staff ratio, gender split).

## Files
| File | Description |
|---|---|
| `university_raw_data.csv` | QS + THE merged on university name + year, standardized to one column layout. Produced by `data_collection.py` / `data_collection.ipynb` (Module 1). |
| `university_cleaned.csv` | Deduplicated, name/country/region-standardized, ranking metrics normalized. Produced by `education_cleaning.py` / `education_cleaning.ipynb` (Module 2). |


## Known Limitations
- Not every university appears in every year — coverage depends on which years QS/THE ranked that institution.
- Some columns are only available from one source (e.g. `academic_reputation_score` is QS-only, `total_students` is THE-only) so a university covered by only one source will have gaps in the other source's columns.
- Name-matching across sources is string-based; a small number of universities may not merge perfectly despite standardization.

## Attribution
Ranking data is owned by Quacquarelli Symonds (QS) and Times Higher Education (THE). This dataset is a personal/academic compilation for dashboard-building purposes and is not an official QS or THE product.