# KPI Engineering Report

**Module:** 3 — KPI Engineering
**Input:** `data/processed/university_cleaned.csv`
**Output:** `data/final/university_final_dataset.xlsx`

---

## KPI Summary

| KPI | Formula | Source Columns | Missing | Min | Max | Mean |
|-----|---------|----------------|---------|-----|-----|------|
| global_ranking_score | Weighted average of QS and THE overall scores, normalized to... | qs_overall_score, the_overall_score | 0 | 12.4 | 100.0 | 55.6 |
| research_impact_score | Weighted average of citations per faculty, research quality,... | qs_citations_per_faculty, the_research_quality, the_research_environment | 0 | 1.4 | 99.5 | 28.5 |
| faculty_student_ratio | Direct value from students_per_staff (lower is better) | students_per_staff | 0 | 0.3 | 493.5 | 18.6 |
| international_student_percentage | Direct value from international_students_pct | international_students_pct | 0 | 0.0 | 100.0 | 10.1 |
| academic_reputation_score | Direct value from qs_academic_reputation, normalized to 0-10... | qs_academic_reputation | 0 | 1.0 | 100.0 | 14.7 |
| research_productivity_index | Geometric mean of normalized publications, citations, and h-... | publications_count, citations_count, h_index | 0 | 0.0 | 100.0 | 4.4 |

---

## KPI Details

### global_ranking_score

**Description:** Composite score combining QS and THE overall scores (0-100 scale)

**Formula:** Weighted average of QS and THE overall scores, normalized to 0-100

**Source Columns:** qs_overall_score, the_overall_score

**Normalization:** Yes (min-max to 0-100)

**Statistics:**
- Missing values: 0
- Min: 12.37
- Max: 100.00
- Mean: 55.56
- Std: 15.00

### research_impact_score

**Description:** Composite score measuring research quality and impact

**Formula:** Weighted average of citations per faculty, research quality, and research environment, normalized to 0-100

**Source Columns:** qs_citations_per_faculty, the_research_quality, the_research_environment

**Normalization:** Yes (min-max to 0-100)

**Statistics:**
- Missing values: 0
- Min: 1.40
- Max: 99.49
- Mean: 28.50
- Std: 18.70

### faculty_student_ratio

**Description:** Number of students per faculty member

**Formula:** Direct value from students_per_staff (lower is better)

**Source Columns:** students_per_staff

**Normalization:** No (direct value)

**Statistics:**
- Missing values: 0
- Min: 0.30
- Max: 493.50
- Mean: 18.58
- Std: 12.08

### international_student_percentage

**Description:** Percentage of international students

**Formula:** Direct value from international_students_pct

**Source Columns:** international_students_pct

**Normalization:** No (direct value)

**Statistics:**
- Missing values: 0
- Min: 0.00
- Max: 100.00
- Mean: 10.08
- Std: 11.87

### academic_reputation_score

**Description:** QS Academic Reputation Score (0-100 scale)

**Formula:** Direct value from qs_academic_reputation, normalized to 0-100

**Source Columns:** qs_academic_reputation

**Normalization:** Yes (min-max to 0-100)

**Statistics:**
- Missing values: 0
- Min: 1.00
- Max: 100.00
- Mean: 14.74
- Std: 14.41

### research_productivity_index

**Description:** Composite measure of research output and citation impact

**Formula:** Geometric mean of normalized publications, citations, and h-index, scaled to 0-100

**Source Columns:** publications_count, citations_count, h_index

**Normalization:** Yes (min-max to 0-100)

**Statistics:**
- Missing values: 0
- Min: 0.00
- Max: 100.00
- Mean: 4.41
- Std: 5.15

---

## Dashboard Compatibility

| Dashboard | KPIs Used | Status |
|-----------|-----------|--------|
| University Overview | global_ranking_score, academic_reputation_score | COMPATIBLE |
| Research Analytics | research_impact_score, research_productivity_index | COMPATIBLE |
| Student Analytics | faculty_student_ratio, international_student_percentage | COMPATIBLE |
| Country Comparison | global_ranking_score | COMPATIBLE |

---
