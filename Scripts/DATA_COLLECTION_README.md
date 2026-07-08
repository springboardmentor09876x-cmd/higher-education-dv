# University Data Collection — Module 1

Output: `university_raw_data.csv` (22,117 rows × 38 columns, one row per university per year, 2017–2026)

**99.94% overall**, every individual column above 95% (target met). Printed automatically each time the script runs.

| Real (from QS/THE datasets) | Formula-derived (real inputs, computed) | Simulated |
|---|---|---|
| world_rank, overall_score, country, region, city, university_type, academic_reputation_score, employer_reputation_score, citations_score, total_students (2017-22), faculty_count (2017-22), gender split (THE) | national_rank, faculty_to_student_ratio, international_student_ratio, country-level averages (all `country_avg_*`, `universities_ranked_count`, `best_university_rank`) | publications_count, citations_count, citations_per_faculty, h_index, research_output_score, research_productivity_index, subject_field, undergraduate/postgraduate split, and any real column's gaps for years/universities not covered by that source |

Simulated values aren't random noise — they're generated *correlated with each university's real rank/score/size* (e.g. a top-10 school gets proportionally higher simulated citation counts than a rank-800 school), so the dataset stays internally consistent for dashboard/demo purposes.

- **QS is the primary ranking source**; THE fills in gaps and supplies gender-split and student-population data QS doesn't report.
- A university's country/city/type/size is carried forward/backward across its own years where a real value exists in any year, before falling back to simulation — this is a legitimate imputation, not fabrication.
- `national_rank` is computed by ranking each university's `world_rank` within its own country/year — fully derived from real rank data.
- Country-level aggregates are `groupby` calculations over the merged data — not simulated at all.
