# EduVision_DV — KPI Definitions

The EduVision_DV project uses six core education-performance KPIs
for university, research, and student analytics.

---

## 1. Global Ranking Score

**Field:** `global_ranking_score`

Represents the university's overall ranking performance after integrating
the available ranking indicators.

**Used in:**
- University Overview
- Country Comparison
- University ranking comparisons

**Interpretation:**
Higher values indicate stronger overall ranking performance.

---

## 2. Research Impact Score

**Field:** `research_impact_score`

Represents the research impact of an institution using available
research-related indicators from the integrated ranking datasets.

**Used in:**
- Research Analytics
- Institutional Comparison
- Research impact comparisons

**Interpretation:**
Higher values indicate stronger research impact.

---

## 3. Faculty-to-Student Ratio

**Field:** `faculty_student_ratio`

Measures the number of students relative to available faculty.

**Used in:**
- Student Analytics
- Faculty-to-student ratio analysis

**Interpretation:**
A lower ratio generally indicates fewer students per faculty member
and therefore potentially greater faculty availability.

---

## 4. International Student Percentage

**Field:** `international_student_pct`

Represents the proportion of students who are international students.

**Used in:**
- Student Analytics
- International student analysis
- Student diversity analysis

**Interpretation:**
Higher values indicate a greater proportion of international students.

---

## 5. Academic Reputation Score

**Field:** `academic_reputation_score`

Represents the academic reputation of a university based on the
available ranking data.

**Used in:**
- University Overview
- Institutional Comparison
- Country Comparison

**Interpretation:**
Higher values indicate stronger academic reputation.

---

## 6. Research Productivity Index

**Field:** `research_productivity_index`

Represents institutional research productivity using the available
research-performance indicators.

**Used in:**
- Research Analytics
- Research productivity analysis
- Regional research comparisons

**Interpretation:**
Higher values indicate stronger research productivity.

---

## KPI Validation

The KPIs were validated against the final processed dataset before
being used in Tableau.

Validation included:

- Checking KPI fields for unexpected NULL/invalid values
- Checking that KPI values appear correctly in Tableau
- Comparing dashboard values with the final dataset
- Testing filters and dashboard interactions