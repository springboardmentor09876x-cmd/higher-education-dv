# EduVision — Project Documentation

## 1. Project Overview

EduVision is an interactive Power BI dashboard project developed as part of the Infosys Springboard Virtual Internship 7.0. The project integrates, cleans, analyzes, and visualizes global higher-education ranking data from QS, THE, and Research datasets.

The final dashboard suite enables meaningful comparison of universities, countries, research performance, student characteristics, and academic performance across **2017–2026**.

## 2. Project Objectives

- Integrate higher-education datasets from multiple sources.
- Standardize and improve the quality of the collected data.
- Engineer reusable KPIs for higher-education analysis.
- Develop interactive Power BI dashboards.
- Integrate the dashboards through navigation, filters, and visual interactions.
- Validate the dashboard calculations and interactions.
- Document the complete project workflow and final deliverables.

## 3. Project Workflow

The project followed the workflow:

**Dataset Collection → Data Cleaning → KPI Engineering → Dashboard Planning → Dashboard Development → Dashboard Integration → Testing → Documentation**

## 4. Module-wise Development

### Module 1 — Dataset Preparation

- Collected QS, THE, and Research datasets.
- Generated source-specific master datasets.
- Merged datasets into a unified master dataset.
- Standardized schemas across ranking systems.
- Recovered university and geographic information.
- Generated `university_raw_data.csv`.

### Module 2 — Data Cleaning & Preprocessing

- Performed missing-value analysis.
- Applied rule-based data recovery.
- Applied statistical and iterative imputation.
- Applied Random Forest-based imputation for selected missing values.
- Recovered metadata across university records.
- Achieved **99.82% dataset completeness**.
- Generated `university_cleaned.csv`.

### Module 3 — KPI Engineering

The KPI engineering stage generated the project's core analytical measures:

- Global Ranking Score
- Research Impact Score
- Faculty-to-Student Ratio
- International Student Percentage
- Academic Reputation KPI
- Research Productivity Index

Outputs included:

- `generate_education_kpis.py`
- `university_final_dataset.csv`
- `university_final_dataset.xlsx`

### Module 4 — Dashboard Planning & Prototyping

Four dashboard storyboards were completed:

1. University Overview
2. Research Analytics
3. Student Analytics
4. Country Comparison

The Power BI prototype established the initial visual structure, KPI cards, slicers, filled map, top university ranking, overall-score trend, and university comparison table.

### Module 5 — Dashboard Development

The dashboard development stage produced the four analytical views:

- University Overview
- Research Analytics
- Student Analytics
- Country Comparison

Implemented features include:

- Interactive page navigation
- Dynamic KPI cards
- Cross-filtering and drill-down
- Responsive slicers
- Geographic visualizations
- Executive-summary dashboard layouts

### Module 6 — Dashboard Integration & Expansion

#### Student Analytics

- Student population analysis
- Student-to-staff/faculty ratio analysis
- International student analysis
- Student diversity analysis
- Enrollment comparisons
- Student distribution analysis

#### Country Comparison

- Country ranking comparison
- Education performance benchmarking
- Regional education trends
- Top-performing country analysis

#### Integration

- Global filters
- Navigation controls
- Dashboard linking
- Interactive filtering
- Cross-dashboard navigation

### Module 7 — Testing & Validation

Testing and validation covered:

- KPI calculation validation
- Ranking calculation validation
- Dashboard interaction testing
- Filter and slicer validation
- Navigation testing
- Educational metric validation
- Visual and dashboard consistency checks

The completed QA checklist and dashboard testing report are included in the `docs/` directory.

### Module 8 — Documentation & Project Delivery

The final delivery includes:

- Project documentation
- KPI definitions
- Dashboard usage guidance
- Education analytics methodology
- QA documentation
- Dashboard testing report
- Final Power BI dashboard
- Final datasets
- KPI generation scripts
- GitHub repository

## 5. Final Dashboard Suite

### University Overview

Provides an overview of university performance, ranking-oriented analysis, geographic distribution, trends, and institutional comparison.

### Research Analytics

Focuses on research performance, research impact, publications/citations-related analysis, and research productivity.

### Student Analytics

Focuses on student population, student-to-staff/faculty relationships, international students, diversity, enrollment, and student distribution.

### Country Comparison

Provides country-level and regional benchmarking, ranking comparison, education-performance comparison, and top-performing country analysis.

## 6. Data Assets

The final repository contains:

- QS master dataset
- THE master dataset
- Research master dataset
- Education master dataset
- Consolidated master dataset
- Raw university data
- Cleaned university data
- KPI-ready final dataset
- Excel version of the final dataset

## 7. Power BI Implementation

Power BI serves as the reporting and interactive visualization layer. The repository retains the Module 4 prototype, Module 5 dashboard-development workbook, and Module 6 integrated workbook.

The dashboard suite uses navigation, filters, slicers, cross-filtering, drill-down interactions, and geographic visualizations to support exploratory analysis.

## 8. Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- Power BI
- Git
- GitHub

## 9. Repository Documentation

The `docs/` directory contains:

- `PROJECT_DOCUMENTATION.md`
- `KPI_DEFINITIONS.md`
- `QA_CHECKLIST.md`
- `DASHBOARD_TESTING_REPORT.md`

## 10. Project Status

**EduVision is completed. All eight project modules have been completed, including dataset preparation, preprocessing, KPI engineering, dashboard planning, dashboard development, integration, testing and validation, and documentation/project delivery.**
