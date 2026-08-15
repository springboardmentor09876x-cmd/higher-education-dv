# EduVision_DV — Education Analytics Methodology

## 1. Overview

EduVision_DV is a higher-education analytics project that integrates
university ranking and performance datasets to provide interactive
analysis of university, research, student, and country-level trends.

The methodology follows the project workflow:

Data Collection
→ Data Cleaning & Transformation
→ KPI Engineering
→ Tableau Dashboard Development
→ Testing & Validation
→ Documentation & Delivery

---

## 2. Data Collection

Publicly available higher-education ranking datasets were collected
from major university ranking sources.

The datasets contain information related to:

- University rankings
- Academic reputation
- Research performance
- Citations
- Faculty and student indicators
- International students
- International faculty
- Country and regional information

---

## 3. Data Cleaning and Transformation

The raw datasets were prepared using Python and Pandas.

The preparation process included:

- Removing duplicate records
- Standardizing university names
- Standardizing country names
- Organizing geographic regions
- Converting ranking fields into numeric values
- Handling missing and unavailable values
- Combining relevant indicators from multiple ranking sources
- Preparing a Tableau-ready final dataset

Open-ended ranking values such as `701+` were converted into numeric
lower-bound values where required for analytical processing.

---

## 4. KPI Engineering

Six core education KPIs were engineered:

1. Global Ranking Score
2. Research Impact Score
3. Faculty-to-Student Ratio
4. International Student Percentage
5. Academic Reputation Score
6. Research Productivity Index

The KPI fields were added to the final dataset and used consistently
across the Tableau dashboards.

---

## 5. Dashboard Development

The final Tableau workbook contains four interconnected dashboards:

### University Overview

Focuses on university rankings, academic reputation, global distribution,
performance trends, and institutional comparison.

### Research Analytics

Focuses on publications, citations, research productivity, research
impact, and leading research institutions.

### Student Analytics

Focuses on international students, student diversity, and
faculty-to-student indicators.

### Country Comparison

Focuses on country benchmarking, regional education trends, country
ranking comparisons, and top-performing countries.

---

## 6. Interactive Analysis

Tableau filters, navigation controls, and dashboard actions are used
to allow users to:

- Filter universities and countries
- Compare regions
- Explore ranking performance
- Analyze research indicators
- Examine student diversity
- Navigate between dashboards

---

## 7. KPI Validation

The KPI values were checked against the final processed dataset.

Validation included:

- Checking KPI values for unexpected invalid values
- Checking dashboard KPI cards
- Verifying ranking-related calculations
- Testing dashboard filters
- Testing navigation and dashboard interactions
- Checking visualizations for broken or misleading values

---

## 8. Handling Missing Data

Some ranking indicators are unavailable for certain universities.

Missing values were retained where appropriate rather than replacing
them with fabricated values.

For dashboard presentation, Tableau NULL indicators may be hidden when
they do not affect the analytical result.

KPIs and visualizations were checked to ensure that missing values do
not cause incorrect dashboard results.

---

## 9. Analytical Limitations

The integrated ranking datasets do not provide every indicator with
consistent coverage across all universities.

In particular, enrollment data was not treated as a universally
comparable KPI because the available student-count field does not
provide sufficiently consistent coverage for all institutions.

Therefore, the project prioritizes indicators with stronger
comparability across the integrated datasets.

---

## 10. Final Output

The final project consists of:

- Processed university dataset
- Python data-processing scripts
- Tableau `.twbx` workbook
- Four interconnected dashboards
- KPI documentation
- Dashboard user guide
- Project methodology documentation