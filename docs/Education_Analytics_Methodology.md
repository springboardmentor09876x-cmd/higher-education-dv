# Education Analytics Methodology

## 1. Overview

The Education Analytics component analyzes university-level academic, research, student, faculty, and international education indicators using the final university dataset.

The analysis is implemented through Power BI dashboards, KPIs, calculated measures, rankings, charts, tables, and interactive filters.

---

## 2. Data Source

The analysis uses the final university dataset:

- **Dataset:** University Final Dataset
- **Rows:** 22,125
- **Columns:** 44
- **Sheet:** Sheet1

The cleaned and prepared data is used as the primary source for educational analysis and dashboard visualizations.

---

## 3. Education Metrics

The following metrics are used in the analysis:

### Academic Reputation

**Field:** `academic_reputation_score`

Measures the academic reputation performance of universities.

### Faculty-to-Student Ratio

**Field:** `faculty_to_student_ratio`

Measures the relationship between faculty members and students.

### International Student Ratio

**Field:** `international_student_ratio`

Measures the proportion of international students within the university student population.

### International Student Percentage

**Field:** `international_student_percentage_kpi`

Represents the prepared international student percentage KPI used in the dashboard.

### Research Productivity

**Field:** `research_productivity_index`

Measures the research productivity performance of universities.

### Research Impact

**Field:** `research_impact_score`

Represents the research impact measure prepared for the dashboard.

---

## 4. KPI Calculation Approach

The dashboard uses aggregation and calculated measures to summarize educational performance.

Common calculation approaches include:

- **Average** – Used for average academic, research, faculty, and international student metrics.
- **Sum** – Used for total students, publications, and citations.
- **Count / Distinct Count** – Used for universities and countries.
- **Ranking** – Used to identify high-performing universities and countries.
- **Filtering** – Used to calculate metrics for selected countries, years, or universities.

---

## 5. Academic Performance Analysis

Academic performance is analyzed using:

- Academic Reputation Score
- Employer Reputation Score
- Overall Score
- World Rank
- National Rank

Universities can be compared based on their academic performance and ranking indicators.

---

## 6. Research Performance Analysis

Research performance is analyzed using:

- Publications Count
- Citations Count
- Citations per Faculty
- H Index
- Research Productivity Index
- Research Impact Score

These indicators help identify universities and countries with stronger research performance.

---

## 7. Student and Faculty Analysis

Student and faculty performance is analyzed using:

- Total Students
- International Students Count
- International Student Ratio
- Faculty Count
- Faculty-to-Student Ratio
- Undergraduate Count
- Postgraduate Count
- Female Percentage
- Male Percentage

These indicators support analysis of student population, diversity, and faculty availability.

---

## 8. Country-Level Analysis

Country-level educational performance is analyzed using:

- Country Average Rank
- Country Average Overall Score
- Country Average Academic Reputation
- Country Average Citations
- Country Average International Ratio
- Best University Rank

These measures allow comparison of educational performance between countries.

---

## 9. Dashboard Filtering

The educational analysis can be filtered using available dashboard filters such as:

- Country
- Year
- University Name
- Region
- University Type
- Subject Field
- Degree Level

Filtering allows users to analyze a specific subset of universities.

---

## 10. Visualization Approach

Educational metrics are represented using:

- KPI cards
- Bar charts
- Column charts
- Line charts
- Tables
- Ranking visuals
- Maps
- Interactive slicers

The visualizations allow users to compare universities, countries, years, and educational indicators.

---

## 11. Analysis Workflow

The overall education analytics workflow is:

1. Load the final university dataset.
2. Prepare and validate the required fields.
3. Select the educational indicators.
4. Create calculated measures and KPIs.
5. Apply filters and aggregation functions.
6. Build Power BI visualizations.
7. Compare university and country performance.
8. Validate the displayed results.
9. Present the results through the interactive dashboard.

---

## 12. Outcome

The Education Analytics methodology provides a structured approach for analyzing university academic performance, research productivity, student characteristics, faculty indicators, and internationalization.

The resulting Power BI dashboard enables users to explore educational performance interactively and compare universities and countries using standardized metrics.