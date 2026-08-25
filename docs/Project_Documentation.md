# EduVision – Higher Education Performance Dashboard

## 1. Project Overview

EduVision is an interactive higher education analytics dashboard developed to analyze university and country-level education performance.

The project uses academic, ranking, research and student-related metrics to compare universities, countries and regions.

The final dashboard suite contains four main dashboards:

- University Overview
- Research Analytics
- Student Analytics
- Country Comparison

---

## 2. Project Objectives

The main objectives of the project are:

- Analyze university performance.
- Compare universities and countries.
- Analyze academic and research performance.
- Analyze student population and international student participation.
- Analyze faculty-to-student ratios.
- Identify top-performing universities and countries.
- Compare educational performance across regions.
- Provide interactive dashboards for decision-making.

---

## 3. Data Sources

The project uses university ranking and higher education datasets collected and prepared for analysis.

The main sources used include:

- QS World University Rankings
- World University Ranking datasets
- University-level academic performance data
- Research performance data
- Student-related university data

The final Tableau-ready dataset is:

`university_final_dataset.xlsx`

---

## 4. Data Collection and Processing

The data preparation process follows this flow:

Data Collection
↓
Raw Datasets
↓
Data Cleaning
↓
Data Integration
↓
KPI Engineering
↓
Final Dataset
↓
Tableau Visualization
↓
Dashboard Development
↓
Testing and Validation

### Data Cleaning

The data cleaning process included:

- Removing duplicate records.
- Standardizing university names.
- Standardizing country names.
- Checking data types.
- Checking missing values.
- Preparing data for Tableau.

### KPI Engineering

The project uses calculated and prepared indicators such as:

- Global Ranking Score
- Research Impact
- Faculty-to-Student Ratio
- International Student Percentage
- Academic Reputation
- Student Population
- International Student Ratio

---

## 5. Dashboard Suite

### University Overview

Provides an overview of university performance using ranking, academic and research indicators.

### Research Analytics

Analyzes research performance, research impact, citations and research-related indicators.

### Student Analytics

Analyzes:

- Student population
- International students
- International student percentage
- Faculty-to-student ratio
- Student diversity
- Enrollment comparisons

### Country Comparison

Provides:

- Country ranking comparison
- Education performance benchmarking
- Regional education trends
- Top performing countries

---

## 6. Technology Stack

| Area | Technology |
|---|---|
| Data Collection | Python |
| Data Processing | Pandas, NumPy |
| Data Cleaning | Python / Pandas |
| KPI Engineering | Python / Pandas |
| Visualization | Tableau |
| Dashboard Development | Tableau Desktop |
| Dashboard Interaction | Tableau Filters and Actions |
| Documentation | Markdown |
| Version Control | GitHub |

---

## 7. Project Structure

```text
higher-education-dv/
├── scripts/
├── data/
├── dashboard/
└── docs/
