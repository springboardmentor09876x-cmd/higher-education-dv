# EduVision – Education Analytics Methodology

## 1. Overview

The EduVision project uses a structured analytics methodology to evaluate higher education performance.

The methodology combines academic, ranking, research and student-related indicators.

---

## 2. Data Preparation

The raw university datasets are first prepared for analysis.

The main preparation steps are:

1. Collect the required datasets.
2. Clean university and country information.
3. Remove duplicate records.
4. Standardize names and values.
5. Check missing values.
6. Combine relevant datasets.
7. Prepare the final Tableau-ready dataset.

---

## 3. University Performance Analysis

University performance is analyzed using indicators such as:

- Overall Score
- QS Score
- Global Ranking Score
- Academic Reputation
- Research Impact

Universities can then be compared using horizontal bar charts, tables and other visualizations.

---

## 4. Research Performance Analysis

Research performance is analyzed using research-related indicators.

The analysis considers metrics such as:

- Research Impact
- Research Output
- Citation Impact
- Research Quality
- Research-related ranking indicators

These metrics are used to compare universities and identify stronger research-performing institutions.

---

## 5. Student Analytics

Student performance is analyzed using:

- Student Population
- International Student Percentage
- International Student Ratio
- Faculty-to-Student Ratio
- Students-to-Staff Ratio

These indicators help understand student population, international participation and faculty availability.

---

## 6. Country-Level Analysis

Country performance is analyzed by aggregating university-level indicators at the country level.

The Country Comparison dashboard focuses on:

- Country Average Rank
- Country Average Score
- Education Performance
- Regional Performance
- International Student Ratio
- Top Performing Countries

---

## 7. Regional Analysis

Universities are grouped by region to compare education performance across geographical areas.

The major regional categories available in the dataset include:

- Africa
- Americas
- Asia
- Europe
- Oceania

Regional averages are used to identify differences in higher education performance.

---

## 8. Ranking Methodology

Ranking visualizations are created by sorting the selected metric and displaying the highest-performing records.

Top 10 visualizations are used where required by the dashboard design.

For country comparison, countries are ranked using the relevant country-level metric such as Country Average Score or Country Average Rank.

---

## 9. Interactive Analysis

Tableau filters allow users to dynamically change the analysis.

The main filters include:

- Country
- Region
- University
- University Type

The dashboard updates the relevant visualizations based on the selected filter values.

---

## 10. Validation Methodology

The results are validated by checking:

- KPI calculations
- Ranking calculations
- Educational metrics
- Dashboard interactions
- Filter behaviour
- Visual labels
- Units
- Percentage formatting
- Missing values

The detailed validation results are documented in the QA Checklist and Dashboard Testing Report.

---

## 11. Overall Methodology

The complete analytics process can be summarized as:

```text
Data Collection
      ↓
Data Cleaning
      ↓
Data Integration
      ↓
KPI Engineering
      ↓
University Analysis
      ↓
Research Analysis
      ↓
Student Analysis
      ↓
Country & Regional Analysis
      ↓
Tableau Visualization
      ↓
Testing & Validation
