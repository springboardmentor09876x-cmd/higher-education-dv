# KPI Definitions

## 1. Overview

The University Ranking Analytics Dashboard uses Key Performance Indicators (KPIs) to summarize university ranking, academic, research, faculty, and international student performance.

The KPIs are calculated using fields from the final university dataset.

---

## 2. University Overview KPIs

| KPI | Dataset Field | Definition |
|---|---|---|
| Total Universities | `university_name` | Total number of universities represented in the selected data. |
| Countries Covered | `country` | Number of countries represented in the selected data. |
| Average Overall Score | `overall_score` | Average overall university performance score. |
| Average Academic Reputation | `academic_reputation_score` | Average academic reputation score of universities. |
| Average Research Productivity | `research_productivity_index` | Average research productivity index of universities. |
| Average International Student Ratio | `international_student_ratio` | Average international student ratio across universities. |

---

## 3. Student Analytics KPIs

| KPI | Dataset Field | Definition |
|---|---|---|
| Total Students | `total_students` | Total number of students represented in the selected data. |
| Total International Students | `international_students_count` | Total number of international students. |
| Average Faculty Student Ratio | `faculty_to_student_ratio` | Average faculty-to-student ratio. |
| Average International Student % | `international_student_percentage_kpi` | Average international student percentage KPI. |

---

## 4. Research Analytics KPIs

| KPI | Dataset Field | Definition |
|---|---|---|
| Total Publications | `publications_count` | Total number of publications. |
| Total Citations | `citations_count` | Total number of citations. |
| Average H Index | `h_index` | Average H-index of universities. |
| Average Research Productivity | `research_productivity_index` | Average research productivity index. |
| Average Citations per Faculty | `citations_per_faculty` | Average citations per faculty member. |
| Research Impact Score | `research_impact_score` | Research impact measure based on the prepared dataset. |

---

## 5. Ranking KPIs

| KPI | Dataset Field | Definition |
|---|---|---|
| World Rank | `world_rank` | University's global ranking position. |
| National Rank | `national_rank` | University's ranking within its country. |
| Global Ranking Score | `global_ranking_score` | Prepared score representing global university ranking performance. |
| Country Average Rank | `country_avg_rank` | Average university rank for a country. |
| Best University Rank | `best_university_rank` | Best university ranking position within a country. |
| Country Average Overall Score | `country_avg_overall_score` | Average overall score of universities within a country. |

---

## 6. Academic KPIs

| KPI | Dataset Field | Definition |
|---|---|---|
| Academic Reputation Score | `academic_reputation_score` | Academic reputation score of a university. |
| Employer Reputation Score | `employer_reputation_score` | Employer reputation score of a university. |
| Academic Reputation KPI | `academic_reputation_kpi` | Prepared academic reputation KPI used for dashboard analysis. |

---

## 7. Faculty and International Student KPIs

| KPI | Dataset Field | Definition |
|---|---|---|
| Faculty-to-Student Ratio | `faculty_to_student_ratio` | Ratio between faculty and students. |
| Faculty Student Ratio KPI | `faculty_student_ratio_kpi` | Prepared KPI representing faculty-to-student performance. |
| International Student Ratio | `international_student_ratio` | Ratio of international students within the university student population. |
| International Student Percentage KPI | `international_student_percentage_kpi` | Prepared KPI representing international student percentage. |

---

## 8. Research Productivity KPI

| KPI | Dataset Field | Definition |
|---|---|---|
| Research Productivity Index | `research_productivity_index` | Index representing research productivity of a university. |
| Research Productivity KPI | `research_productivity_kpi` | Prepared KPI used to represent research productivity in the dashboard. |
| Research Impact Score | `research_impact_score` | Prepared measure representing research impact. |

---

## 9. KPI Calculation Approach

The dashboard uses aggregation functions such as:

- `AVERAGE()` for average-based KPIs
- `SUM()` for total-based KPIs
- `COUNT()` / `DISTINCTCOUNT()` for university and country counts
- Ranking and filtering logic for ranking-related KPIs

The KPI calculations respond to dashboard filters such as:

- Country
- Year
- University Name