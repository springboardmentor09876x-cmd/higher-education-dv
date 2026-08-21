# EduVision_DV -- Higher Education Performance Dashboard

## 1. Project Overview

**EduVision_DV (Higher Education Performance Dashboard)** is a higher
education analytics and visualization project developed during the
Infosys internship. The project combines publicly available global
university-ranking datasets and transforms them into structured,
analysis-ready data for interactive Tableau dashboards.

The primary purpose of the project is to analyze:

-   University rankings and institutional performance
-   Research performance and productivity
-   Student diversity and internationalization
-   Academic excellence and reputation
-   Country-level higher education performance
-   Global education trends

The final solution is designed to help students, academic researchers,
university administrators, policymakers, and education consultants
compare institutions and identify meaningful patterns in higher
education data.

The project specification defines a unified Tableau workbook containing
four interconnected dashboards:

1.  **University Overview**
2.  **Research Analytics**
3.  **Student Analytics**
4.  **Country Comparison**

------------------------------------------------------------------------

## 2. Project Objectives

The major objectives of the project are:

-   Collect university-ranking and higher-education datasets from
    publicly available sources.
-   Integrate datasets with different schemas into a common structure.
-   Clean and standardize university, country, ranking, and performance
    information.
-   Prepare Tableau-ready datasets for analysis and visualization.
-   Engineer meaningful higher-education KPIs.
-   Develop interactive dashboards for institutional and country-level
    comparison.
-   Provide filters, navigation, parameters, and dashboard actions for
    interactive analysis.
-   Validate KPI calculations, ranking metrics, and dashboard
    interactions.
-   Deliver a well-documented, portfolio-ready analytics solution.

------------------------------------------------------------------------

## 3. Project Workflow

The project follows the pipeline below:

``` text
University Dataset Collection
            ↓
Data Cleaning & Transformation
            ↓
KPI Engineering
            ↓
Dashboard Planning & Prototyping
            ↓
Dashboard Development
            ↓
Dashboard Integration
            ↓
Testing & Validation
            ↓
Documentation & Delivery
```

This workflow follows the project modules defined for the internship,
from data collection through final documentation and delivery.

------------------------------------------------------------------------

## 4. Data Sources

The project uses publicly available university-ranking datasets. The
working repository contains datasets including:

-   **QS World University Rankings 2025**
-   **Times Higher Education World University Rankings 2016--2026**
-   **CWUR (Center for World University Rankings)**
-   **Times Higher Education ranking data**
-   **Shanghai Ranking data**
-   **School and Country reference data**

These datasets contain information related to university rankings,
academic performance, research, faculty/student information, countries,
and other institutional indicators.

Because the source datasets originate from different ranking systems,
the data preparation stage is important for standardizing names,
countries, metrics, and identifiers before analysis.

------------------------------------------------------------------------

## 5. Data Collection and Integration

### 5.1 Data Collection

The data collection stage involves gathering the available
university-ranking datasets and storing them in the project data
directory.

The main collection and integration scripts include:

-   `scripts/data_collection.py`
-   `scripts/data_collection_merge.py`

The collection process reads the source datasets and prepares them for
integration.

### 5.2 Dataset Integration

The datasets use different column names, ranking systems, years, and
structures. Therefore, a common schema is used during the integration
process.

The integration process includes:

1.  Reading individual ranking datasets.
2.  Identifying relevant university-level attributes.
3.  Mapping source-specific columns to common fields.
4.  Standardizing university and country information.
5.  Generating consistent university identifiers where required.
6.  Combining the datasets into a unified dataset.
7.  Removing completely empty records.
8.  Saving the integrated dataset for subsequent cleaning.

The project specification expects the raw integration deliverable to be
represented by `university_raw_data.csv`.

------------------------------------------------------------------------

## 6. Data Cleaning and Transformation

The cleaning stage prepares the integrated data for KPI calculation and
Tableau visualization.

The planned cleaning activities include:

-   Removing duplicate records.
-   Standardizing university names.
-   Standardizing country names.
-   Normalizing ranking-related metrics.
-   Handling missing and inconsistent values.
-   Converting fields into appropriate data types.
-   Creating Tableau-ready analytical fields.

The cleaning process is implemented through Python-based data-processing
scripts and uses libraries such as Pandas and NumPy.

The expected cleaned dataset is:

``` text
university_cleaned.csv
```

The project specification targets less than 2% missing values after
cleaning and consistent ranking indicators.

------------------------------------------------------------------------

## 7. KPI Engineering

The project defines higher-education KPIs to convert raw institutional
indicators into meaningful analytical measures.

The six primary KPIs specified for the project are:

### 7.1 Global Ranking Score

A standardized measure used to represent a university's overall global
ranking performance.

### 7.2 Research Impact Score

A measure intended to represent the research influence or impact of an
institution using available research-related indicators.

### 7.3 Faculty-to-Student Ratio

A measure comparing faculty strength with the student population.

This KPI can be used to understand relative faculty availability across
universities or regions.

### 7.4 International Student Percentage

A measure representing the proportion of students coming from
international backgrounds.

This supports analysis of student diversity and institutional
internationalization.

### 7.5 Academic Reputation Score

A measure representing institutional academic reputation based on the
available ranking indicators.

### 7.6 Research Productivity Index

A measure designed to represent research output/productivity using the
available research-related data.

The project specification identifies `generate_education_kpis.py` as the
KPI-generation script and `university_final_dataset.xlsx` as the
KPI-engineered dataset deliverable.

------------------------------------------------------------------------

## 8. Dashboard Suite

The final dashboard suite is organized into four major analytical views.

### 8.1 University Overview

The University Overview dashboard focuses on overall institutional
performance.

Key analytical areas include:

-   Top university rankings
-   Global university distribution
-   Academic reputation analysis
-   University performance trends
-   Institutional comparison

The sample dashboard layout in the project specification also
demonstrates KPI cards, ranking tables, regional distribution,
university score trends, and comparative visualizations.

### 8.2 Research Analytics

The Research Analytics dashboard focuses on research-related
institutional performance.

Key analytical areas include:

-   Publication analysis
-   Citation performance
-   Research productivity trends
-   Top research institutions
-   Research impact comparison

### 8.3 Student Analytics

The Student Analytics dashboard focuses on student-related indicators.

Key analytical areas include:

-   International student analysis
-   Faculty-to-student ratio
-   Student diversity trends
-   Enrollment comparisons
-   Student distribution

### 8.4 Country Comparison

The Country Comparison dashboard provides country and regional
benchmarking.

Key analytical areas include:

-   Country ranking comparison
-   Education performance benchmarking
-   Regional education trends
-   Identification of top-performing countries

------------------------------------------------------------------------

## 9. Dashboard Interactivity

The dashboard suite is designed to support interactive exploration.

The project specification includes:

-   Global filters
-   Navigation controls
-   Parameter actions
-   Dashboard actions
-   Dashboard linking
-   Interactive comparisons
-   Drill-down capabilities

Typical filtering dimensions include:

-   Year
-   Region
-   Country
-   Subject area

The sample dashboard shown in the project specification demonstrates a
dark-themed analytical interface with KPI cards, filters, ranking
tables, trend charts, regional distribution, research output,
international student analysis, and faculty-to-student comparisons.

------------------------------------------------------------------------

## 10. Technology Stack

  Area                    Technology
  ----------------------- ------------------------------------------------
  Data Collection         Python, QS Rankings, World University Rankings
  Data Processing         Pandas, NumPy
  Data Cleaning           Python
  Visualization           Tableau Desktop / Tableau Public
  Dashboard Integration   Tableau Filters, Parameters, Actions
  Documentation           Markdown, GitHub

------------------------------------------------------------------------

## 11. Project Structure

The project is organized into separate areas for scripts, datasets,
dashboards, and documentation.

``` text
EduVision_DV/
│
├── scripts/
│   ├── data_collection.py
│   ├── data_collection_merge.py
│   ├── data_cleaning.py
│   └── generate_education_kpis.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── dashboard/
│   └── EduVision_DV.twbx
│
├── docs/
│   ├── project_documentation.md
│   ├── dashboard_storyboard.pdf
│   └── QA_Checklist
│
└── README.md
```

> File names may be adjusted to match the final repository structure.

------------------------------------------------------------------------

## 12. Testing and Validation

Testing is performed to ensure that the analytical results and dashboard
behavior are reliable.

Validation activities include:

### Data Validation

-   Check for duplicate records.
-   Check for missing values.
-   Verify university and country names.
-   Verify data types.
-   Check ranking fields for inconsistent values.
-   Confirm that cleaned data can be consumed by Tableau.

### KPI Validation

-   Verify KPI formulas and calculations.
-   Check calculated values against source indicators.
-   Confirm that KPI values respond correctly to filters.

### Dashboard Validation

-   Verify dashboard navigation.
-   Test filters and parameters.
-   Test dashboard actions.
-   Check interactions between dashboards.
-   Verify ranking and comparison visuals.
-   Confirm that charts update correctly when selections change.

The project specification sets a target of greater than 95% KPI accuracy
and requires that there be no major dashboard issues.

------------------------------------------------------------------------

## 13. Expected Deliverables

The internship project modules specify the following deliverables:

### Data Collection

-   `university_raw_data.csv`
-   `data_collection.py`

### Data Cleaning

-   `university_cleaned.csv`
-   `education_cleaning.ipynb`

### KPI Engineering

-   `university_final_dataset.xlsx`
-   `generate_education_kpis.py`

### Dashboard Planning

-   `dashboard_storyboard.pdf`
-   `eduvision_prototype.twbx`

### Dashboard Development

-   `eduvision_dashboard_v1.twbx`

### Dashboard Integration

-   `EduVision_DV.twbx`

### Testing

-   QA Checklist
-   Dashboard Testing Report

### Final Documentation and Delivery

-   GitHub Repository
-   Final Project Documentation
-   Tableau Workbook

------------------------------------------------------------------------

## 14. Evaluation Criteria

The project specification defines four major evaluation areas:

  Milestone   Focus Area                   Target
  ----------- ---------------------------- ----------------------------
  1           Data Collection & Cleaning   Dataset completeness \>95%
  2           KPI Engineering              6+ KPIs generated
  3           Dashboard Development        4 dashboards integrated
  4           Documentation & Delivery     Portfolio-ready project

The final project therefore combines data engineering, analytical KPI
development, visualization, dashboard integration, testing, and
documentation.

------------------------------------------------------------------------

## 15. Analytical Methodology

The analytical methodology follows a structured transformation process:

``` text
Raw Ranking Data
      ↓
Schema Mapping
      ↓
Data Standardization
      ↓
Data Cleaning
      ↓
KPI Calculation
      ↓
Tableau Data Preparation
      ↓
Interactive Visualization
      ↓
Comparative Analysis
```

The methodology allows information from different ranking systems to be
viewed through a common analytical framework while preserving the core
university and country-level indicators required by the project.

------------------------------------------------------------------------

## 16. Key Insights Supported by the Dashboard

The dashboard suite is designed to answer questions such as:

-   Which universities perform strongly in global rankings?
-   How does academic reputation vary between institutions?
-   Which universities demonstrate strong research productivity?
-   How does research impact differ across institutions?
-   How does international student representation vary by region?
-   How does the faculty-to-student ratio differ between regions?
-   Which countries perform strongly across higher-education indicators?
-   What trends can be observed in university and country-level
    performance over time?
-   How do universities compare across selected ranking and performance
    indicators?

------------------------------------------------------------------------

## 17. Project Outcomes

The completed project provides a unified analytical framework for higher
education performance analysis.

The major outcomes are:

-   Integration of multiple university-ranking datasets.
-   Structured and cleaned educational data.
-   Higher-education KPI definitions and calculations.
-   Four interconnected Tableau dashboards.
-   Interactive filtering and comparison capabilities.
-   A documented data-to-dashboard workflow.
-   A reusable project structure suitable for GitHub and portfolio
    presentation.

------------------------------------------------------------------------

## 18. Future Enhancements

Possible future enhancements include:

-   Automating periodic dataset updates.
-   Adding additional global ranking sources.
-   Introducing predictive analysis for ranking trends.
-   Adding more detailed research-domain analysis.
-   Expanding country-level benchmarking.
-   Adding institution-level drill-down pages.
-   Publishing the dashboard through Tableau Public where appropriate.
-   Adding automated data-quality checks to the data pipeline.
-   Creating scheduled refresh workflows for newly released ranking
    datasets.

------------------------------------------------------------------------

## 19. Conclusion

EduVision_DV demonstrates an end-to-end higher education analytics
workflow, beginning with public university-ranking data collection and
continuing through data cleaning, KPI engineering, Tableau
visualization, dashboard integration, testing, and documentation.

The project transforms complex and heterogeneous educational datasets
into an interactive dashboard suite that supports university comparison,
research analysis, student-diversity analysis, and country-level
benchmarking.

The final solution is intended to be both an internship deliverable and
a portfolio-ready demonstration of skills in **Python-based data
processing, data cleaning, KPI engineering, Tableau visualization,
dashboard design, and analytical storytelling**.

------------------------------------------------------------------------

## 20. References

The primary project specification and dashboard requirements are
documented in the provided **EduVision_DV (Higher Education Performance
Dashboard)** project document.

The project uses publicly available university-ranking sources,
including QS World University Rankings and Times Higher Education World
University Rankings, as specified in the project requirements.
