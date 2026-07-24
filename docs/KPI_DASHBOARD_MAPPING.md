# EduVision_DV — Complete KPI & Dashboard Mapping

**Version:** 2.0

**Date:** 2026-07-22

---

# Project Data Pipeline

This document defines the complete data lineage for the EduVision_DV project. It explains how multiple source datasets are transformed into a single cleaned analytical dataset and finally into a Tableau-ready dataset.

All KPI calculations and dashboard visualizations must follow this workflow.

```text
Multiple Source Datasets
(QS Rankings, THE Rankings,
THE Key Statistics,
World Bank Indicators,
Research Dataset if Approved)
                    │
                    ▼
Validate Individual Source Datasets
                    │
                    ▼
Merge All Validated Datasets
                    │
                    ▼
university_raw_data.csv
(Master Raw Dataset)
                    │
                    ▼
Data Cleaning &
Standardization
                    │
                    ▼
university_cleaned.csv
(< 2% Missing Values)
                    │
                    ▼
Feature Engineering
&
KPI Engineering
                    │
                    ▼
university_final_dataset.xlsx
                    │
                    ▼
Tableau Dashboards
```

---

# Dataset Responsibilities

## 1. Source Datasets

These are the original datasets collected from different organizations.

Examples include:

- QS World University Rankings
- Times Higher Education Rankings
- THE Key Statistics
- World Bank Indicators
- Research Dataset (if approved)

These datasets are considered read-only sources and must never be modified directly.

---

## 2. Master Raw Dataset

**File Name**

```
university_raw_data.csv
```

Purpose:

Create one unified dataset by merging all validated source datasets into a common structure.

Characteristics:

- May contain duplicate records.
- May contain inconsistent university names.
- May contain inconsistent country names.
- May contain missing values.
- May contain inconsistent column formats.
- Contains no engineered KPIs.
- Contains no calculated features.

This dataset represents the raw integrated data before cleaning.

---

## 3. Clean Dataset

**File Name**

```
university_cleaned.csv
```

Purpose:

Generate a standardized analytical dataset from the merged raw dataset.

Cleaning includes:

- Duplicate removal
- Missing value handling
- University name standardization
- Country name standardization
- Data type correction
- Ranking normalization
- Percentage conversion
- Consistent column naming
- Validation of merged records

Requirements:

- Less than 2% missing values
- Consistent formatting
- Ready for feature engineering

---

## 4. Final Dataset

**File Name**

```
university_final_dataset.xlsx
```

Purpose:

Generate the final Tableau-ready dataset after KPI engineering.

This dataset contains:

- Engineered KPIs
- Derived metrics
- Aggregated statistics
- Dashboard-ready columns

Only this dataset should be used by Tableau.

---

# Data Lineage

Every field in the final dashboard must follow the same lineage.

```
Source Dataset
        │
        ▼
Merged into
university_raw_data.csv
        │
        ▼
Cleaned inside
university_cleaned.csv
        │
        ▼
Feature Engineering
        │
        ▼
Stored in
university_final_dataset.xlsx
        │
        ▼
Visualized in Tableau
```

Every KPI documented in this file identifies:

- Original Source Dataset
- Original Source Column
- Raw Dataset Location
- Clean Dataset Location
- Final KPI Column
- Dashboard Usage

This ensures complete traceability from source data to dashboard visualization.

---

# Part 1: Actual Dataset Schemas

This section documents the structure of every original source dataset before merging.

These schemas represent the source data exactly as downloaded.

No cleaning, feature engineering, or KPI generation has been performed at this stage.

---

# Dataset 1 — QS World University Rankings

## QS 2020 (Double Header)

```
Row 1:
Rank in 2020,
Rank in 2019,
Institution Name,
Country,
Classification,
[7 empty],
Academic Reputation,
[empty],
Employer Reputation,
[empty],
Faculty Student,
[empty],
Citations per Faculty,
[empty],
International Faculty,
[empty],
International Students,
[empty],
Overall Score

Row 2:
[empty],
[empty],
[empty],
[empty],
SIZE,
FOCUS,
RESEARCH INTENSITY,
AGE,
STATUS,
SCORE,
RANK,
SCORE,
RANK,
SCORE,
RANK,
SCORE,
RANK,
SCORE,
RANK,
SCORE,
RANK
```

**Useful Columns**

- Rank
- Institution Name
- Country
- Academic Reputation Score
- Employer Reputation Score
- Faculty Student Score
- Citations per Faculty Score
- International Faculty Score
- International Students Score
- Overall Score

---

## QS 2021

```
Columns:

ranking
institution name
code
country
size
focus
res.
age
status
academic reputation
employer reputation
faculty student
citations per faculty
international faculty
international students
overall
```

**Useful Columns**

- Ranking
- Institution Name
- Country
- Academic Reputation
- Employer Reputation
- Faculty Student
- Citations per Faculty
- International Faculty
- International Students
- Overall

---

## QS 2022

```
Columns:

Rank
University
Overall Score
International Students Ratio
International Faculty Ratio
Faculty Student Ratio
Citations per Faculty
Academic Reputation
Employer Reputation
```

**Useful Columns**

- Rank
- University
- Overall Score
- International Students Ratio
- International Faculty Ratio
- Faculty Student Ratio
- Citations per Faculty
- Academic Reputation
- Employer Reputation

**Known Issue**

- Country column is missing.

---

## QS 2023

```
Columns:

rank display
rank display2
institution
location code
location
size
focus
research
age band
status
ar score
ar rank
er score
er rank
fsr score
fsr rank
cpf score
cpf rank
ifr score
ifr rank
isr score
isr rank
irn score
irn rank
ger score
ger rank
score scaled
```

**Useful Columns**

- Rank Display
- Institution
- Location (Country)
- Academic Reputation Score
- Employer Reputation Score
- Faculty Student Score
- Citations per Faculty Score
- International Faculty Score
- International Student Score
- Overall Score

---

## QS 2024

```
Row 1

2024 QS World University Rankings

Row 2

2024
2023
Institution Name
Location
Classification
Academic Reputation
Employer Reputation
Faculty Student
Citations per Faculty
International Faculty
International Students
International Research Network
Employment Outcomes
Sustainability
Overall

Row 3

Actual column names and ranking fields
```

**Useful Columns**

- Rank (2024)
- Institution Name
- Country
- Academic Reputation Score
- Employer Reputation Score
- Faculty Student Score
- Citations per Faculty Score
- International Faculty Score
- International Student Score
- Overall Score

**Known Issues**

- Semicolon delimiter
- Multiple header rows
- European decimal separator

# Dataset 2 — Times Higher Education (THE) World University Rankings

The Times Higher Education (THE) World University Rankings provide institutional performance metrics across multiple academic dimensions including teaching, research, industry collaboration, and international outlook.

These datasets will be merged with QS Rankings during the master dataset creation stage.

---

## THE Rankings (2020–2024)

```
Columns:

year
Rank
Name
Country
Overall
Teaching
Research Environment
Research Quality
Industry
International Outlook
rank_prefix
```

### Useful Columns

- Year
- Rank
- University Name
- Country
- Overall Score
- Teaching Score
- Research Environment
- Research Quality
- Industry Score
- International Outlook

### Purpose in Project

THE Rankings contribute institutional performance indicators that complement QS Rankings.

These columns will later support:

- Global Ranking Score
- Research Impact Score
- Country Comparison
- Institutional Performance Analysis

### Known Issues

- University naming differences compared to QS
- Ranking formats differ across years
- Requires university name standardization before merging

---

# Dataset 3 — THE Key Statistics

THE Key Statistics provide detailed institutional characteristics that are not available in QS Rankings.

These datasets primarily support Student Analytics and several KPI calculations.

---

## THE Key Statistics (2020–2024)

```
Columns:

year
Rank
Name
Country
No. of FTE students
No. of students per staff
International students
Female:Male ratio
rank_prefix
```

### Useful Columns

- Year
- Rank
- University Name
- Country
- Number of FTE Students
- Students per Staff
- International Students
- Female : Male Ratio

### Purpose in Project

THE Key Statistics provide actual institutional statistics rather than normalized scores.

These values will support:

- Faculty-to-Student Ratio
- International Student Percentage
- Enrollment Analysis
- Student Diversity Analysis

### Known Issues

- Percentages stored as text
- Student counts require numeric conversion
- Gender ratios require parsing before analysis

---

# Dataset 4 — World Bank Indicators

World Bank indicators provide country-level socioeconomic and education statistics.

Unlike QS and THE, these datasets are not university-level datasets.

They will be merged at the country level after university datasets have been standardized.

---

## World Bank JSON Structure

```json
{
  "indicator": {
    "id": "NY.GDP.PCAP.CD",
    "value": "GDP per capita (current US$)"
  },
  "country": {
    "id": "AF",
    "value": "Afghanistan"
  },
  "countryiso3code": "AFG",
  "date": "2020",
  "value": 510.787063366811,
  "unit": "",
  "obs_status": "",
  "decimal": 1
}
```

---

### Available Indicators

- GDP per Capita
- Education Expenditure
- Literacy Rate
- Population
- Tertiary Enrollment

---

### Common Fields

- Country Name
- Country ISO3 Code
- Year
- Indicator Value

---

### Purpose in Project

World Bank indicators support country-level analytics including:

- Country Comparison Dashboard
- Education Benchmarking
- Economic Context
- Regional Trend Analysis

### Known Issues

- Country-level dataset
- Cannot be merged directly using university names
- Must be joined using standardized country names and year

---

# Dataset 5 — Research Dataset (Conditional)

Research-specific metrics are required to calculate publication-based KPIs.

If an approved research dataset is used, it will be merged after university matching has been completed.

Possible sources include:

- OpenAlex
- Other approved public research datasets

---

### Expected Fields

- University Name
- Year
- Publications Count
- Citation Count
- Research Output
- Research Impact Metrics

---

### Purpose in Project

These fields support:

- Research Productivity Index
- Publications Analysis
- Research Trend Analysis
- Advanced Research Dashboard Metrics

---

### Status

Conditional.

This dataset will only be included if it satisfies the project requirements and can be reliably matched with the university master dataset.

---

# Master Dataset Integration Strategy

After validating every source dataset, they will be integrated into a common structure.

The integration order is:

```text
QS Rankings
        │
        ▼
THE Rankings
        │
        ▼
THE Key Statistics
        │
        ▼
World Bank Indicators
        │
        ▼
Research Dataset (if approved)
        │
        ▼
university_raw_data.csv
```

The resulting master raw dataset serves as the single source for all subsequent cleaning operations.

No KPI engineering or dashboard preparation is performed before the master raw dataset has been created.

---

# Source Dataset Summary

| Dataset | Level | Primary Join Key | Purpose |
|----------|-------|------------------|---------|
| QS Rankings | University | University Name + Year | Rankings and Reputation |
| THE Rankings | University | University Name + Year | Academic Performance |
| THE Key Statistics | University | University Name + Year | Student Statistics |
| World Bank Indicators | Country | Country + Year | Country Analytics |
| Research Dataset | University | University Name + Year | Research KPIs |

---

End of **Part 1 – Actual Dataset Schemas**

The next section begins:

# Part 2: Required KPIs — Column Mapping
# Part 2: Required KPIs — Column Mapping

This section defines how each Key Performance Indicator (KPI) is generated throughout the data pipeline.

Every KPI follows the same implementation workflow:

```text
Original Source Dataset
        │
        ▼
Merged into
university_raw_data.csv
        │
        ▼
Cleaned and Standardized
inside
university_cleaned.csv
        │
        ▼
Feature Engineering
        │
        ▼
Stored in
university_final_dataset.xlsx
        │
        ▼
Used by Tableau Dashboards
```

Each KPI includes:

- Original source dataset
- Source column(s)
- Processing logic
- Final KPI column
- Dashboard usage

---

# KPI 1 — Global Ranking Score

### Purpose

Represents the overall academic performance of a university using ranking scores from QS and THE.

### Original Source

- QS World University Rankings
- THE World University Rankings

### Source Columns

| Dataset | Column |
|----------|--------|
| QS | Overall Score |
| THE | Overall |

### Processing

- Merge QS and THE scores.
- Normalize scores onto a common scale.
- Handle missing values.
- Calculate composite ranking score.

### Pipeline

```
QS + THE
      ↓
university_raw_data.csv
      ↓
university_cleaned.csv
      ↓
Global Ranking Score
      ↓
university_final_dataset.xlsx
```

### Final KPI Column

```
global_ranking_score
```

### Used In

- University Overview Dashboard
- Country Comparison Dashboard

---

# KPI 2 — Research Impact Score

### Purpose

Measures research quality using citation and research quality indicators.

### Original Source

- QS Rankings
- THE Rankings
- Research Dataset (if approved)

### Source Columns

| Dataset | Column |
|----------|--------|
| QS | Citations per Faculty |
| THE | Research Quality |
| THE | Research Environment |
| Research Dataset | Citation Count |

### Processing

- Normalize research metrics.
- Combine citation indicators.
- Calculate weighted research score.

### Pipeline

```
QS
THE
Research Dataset
        ↓
university_raw_data.csv
        ↓
university_cleaned.csv
        ↓
Research Impact Score
        ↓
university_final_dataset.xlsx
```

### Final KPI Column

```
research_impact_score
```

### Used In

- Research Analytics Dashboard

---

# KPI 3 — Faculty-to-Student Ratio

### Purpose

Measures faculty availability relative to student population.

### Original Source

THE Key Statistics

### Source Column

```
No. of students per staff
```

### Processing

- Convert numeric values.
- Validate missing entries.
- Standardize ratio format.

### Pipeline

```
THE Key Statistics
        ↓
university_raw_data.csv
        ↓
university_cleaned.csv
        ↓
faculty_student_ratio
        ↓
university_final_dataset.xlsx
```

### Final KPI Column

```
faculty_student_ratio
```

### Used In

- Student Analytics Dashboard

---

# KPI 4 — International Student Percentage

### Purpose

Represents the percentage of international students within a university.

### Original Source

THE Key Statistics

### Source Column

```
International students
```

### Processing

- Remove percentage symbols.
- Convert to numeric values.
- Validate percentages.

### Pipeline

```
THE Key Statistics
        ↓
university_raw_data.csv
        ↓
university_cleaned.csv
        ↓
international_student_percentage
        ↓
university_final_dataset.xlsx
```

### Final KPI Column

```
international_student_percentage
```

### Used In

- Student Analytics Dashboard

---

# KPI 5 — Academic Reputation Score

### Purpose

Measures institutional academic reputation using QS survey data.

### Original Source

QS Rankings

### Source Column

```
Academic Reputation Score
```

### Processing

- Merge yearly QS values.
- Standardize score format.
- Normalize across years.

### Pipeline

```
QS Rankings
        ↓
university_raw_data.csv
        ↓
university_cleaned.csv
        ↓
academic_reputation_score
        ↓
university_final_dataset.xlsx
```

### Final KPI Column

```
academic_reputation_score
```

### Used In

- University Overview Dashboard

---

# KPI 6 — Research Productivity Index

### Purpose

Measures research output produced by each university.

### Original Source

Research Dataset (if approved)

### Source Columns

- Publications Count
- Citation Count

### Processing

- Validate publication records.
- Aggregate yearly output.
- Normalize publication metrics.

### Pipeline

```
Research Dataset
        ↓
university_raw_data.csv
        ↓
university_cleaned.csv
        ↓
research_productivity_index
        ↓
university_final_dataset.xlsx
```

### Final KPI Column

```
research_productivity_index
```

### Used In

- Research Analytics Dashboard

---

# KPI Implementation Summary

| KPI | Primary Source | Final Column | Dashboard |
|------|---------------|--------------|-----------|
| Global Ranking Score | QS + THE | global_ranking_score | University Overview |
| Research Impact Score | QS + THE + Research Dataset | research_impact_score | Research Analytics |
| Faculty-to-Student Ratio | THE Key Statistics | faculty_student_ratio | Student Analytics |
| International Student Percentage | THE Key Statistics | international_student_percentage | Student Analytics |
| Academic Reputation Score | QS Rankings | academic_reputation_score | University Overview |
| Research Productivity Index | Research Dataset | research_productivity_index | Research Analytics |
# Part 3: Dashboard-to-Dataset Mapping

This section defines how the final Tableau dashboards consume the engineered dataset.

After KPI engineering, all dashboards must use:

```
university_final_dataset.xlsx
```

The source datasets (QS, THE, THE Key Statistics, World Bank, Research Dataset) are **not** connected directly to Tableau.

Their data flows through the complete data engineering pipeline before visualization.

```text
Source Datasets
        │
        ▼
university_raw_data.csv
        │
        ▼
university_cleaned.csv
        │
        ▼
Feature Engineering
        │
        ▼
university_final_dataset.xlsx
        │
        ▼
Tableau Dashboards
```

---

# Dashboard 1 — University Overview

## Purpose

Provide an overall view of university rankings, academic performance, and institutional comparison.

---

## Dashboard Dataset

```
university_final_dataset.xlsx
```

---

## Primary Source Datasets

- QS Rankings
- THE Rankings

---

## Required KPIs

- Global Ranking Score
- Academic Reputation Score

---

## Required Fields

- University Name
- Country
- Year
- Global Ranking Score
- Academic Reputation Score
- Overall Score

---

## Visualizations

- Top Ranked Universities
- University Performance Comparison
- Academic Reputation Analysis
- Global University Distribution
- University Ranking Trends

---

## Status

FULLY SUPPORTED

---

# Dashboard 2 — Research Analytics

## Purpose

Analyze research quality, citation impact, and research productivity.

---

## Dashboard Dataset

```
university_final_dataset.xlsx
```

---

## Primary Source Datasets

- THE Rankings
- Research Dataset (if approved)
- QS Rankings

---

## Required KPIs

- Research Impact Score
- Research Productivity Index

---

## Required Fields

- University Name
- Country
- Year
- Research Impact Score
- Research Productivity Index
- Citation Metrics
- Research Quality

---

## Visualizations

- Citation Performance
- Research Productivity
- Research Impact Comparison
- Top Research Universities
- Research Trends

---

## Status

PARTIALLY SUPPORTED

Research Productivity Index depends on the availability of the approved research dataset.

---

# Dashboard 3 — Student Analytics

## Purpose

Analyze student population, diversity, and faculty availability.

---

## Dashboard Dataset

```
university_final_dataset.xlsx
```

---

## Primary Source Datasets

- THE Key Statistics
- QS Rankings

---

## Required KPIs

- Faculty-to-Student Ratio
- International Student Percentage

---

## Required Fields

- University Name
- Country
- Year
- Total Students
- Faculty-to-Student Ratio
- International Student Percentage
- Female-to-Male Ratio

---

## Visualizations

- Student Enrollment Analysis
- Faculty-to-Student Ratio
- International Student Distribution
- Gender Diversity
- Student Comparison Across Universities

---

## Status

FULLY SUPPORTED

---

# Dashboard 4 — Country Comparison

## Purpose

Compare higher education performance across countries.

---

## Dashboard Dataset

```
university_final_dataset.xlsx
```

---

## Primary Source Datasets

- World Bank Indicators
- QS Rankings
- THE Rankings

---

## Required KPIs

- Global Ranking Score
- Country-Level Education Indicators

---

## Required Fields

- Country
- Year
- GDP per Capita
- Education Expenditure
- Literacy Rate
- Population
- Tertiary Enrollment
- Global Ranking Score

---

## Visualizations

- Country Ranking Comparison
- GDP vs University Performance
- Education Expenditure Comparison
- Regional Education Trends
- Top Performing Countries

---

## Status

FULLY SUPPORTED

---

# Dashboard Summary

| Dashboard | Final Dataset | Primary Source | Status |
|------------|---------------|----------------|--------|
| University Overview | university_final_dataset.xlsx | QS + THE | Fully Supported |
| Research Analytics | university_final_dataset.xlsx | THE + Research Dataset | Partially Supported |
| Student Analytics | university_final_dataset.xlsx | THE Key Statistics | Fully Supported |
| Country Comparison | university_final_dataset.xlsx | World Bank + QS + THE | Fully Supported |

---

# Dashboard Data Flow

Every dashboard follows the same implementation pipeline.

```text
Source Datasets
        │
        ▼
Merge into
university_raw_data.csv
        │
        ▼
Clean and Standardize
        │
        ▼
university_cleaned.csv
        │
        ▼
Generate KPIs
        │
        ▼
university_final_dataset.xlsx
        │
        ▼
Tableau Dashboard
```

This architecture ensures:

- Single source of truth for all dashboards.
- No direct dependency on raw datasets.
- Consistent KPI calculations across dashboards.
- Simplified dashboard maintenance.
- Better scalability for future enhancements.
# Part 4: Gap Analysis

This section identifies remaining technical gaps, implementation challenges, and data quality considerations before generating the final analytical dataset.

---

# Current Project Status

| Stage | Status |
|--------|--------|
| Source Dataset Collection | Completed |
| Source Dataset Validation | Completed |
| Dataset Schema Documentation | Completed |
| KPI Mapping | Completed |
| Dashboard Mapping | Completed |
| Master Dataset Design | Completed |
| Merge Strategy | Defined |
| Cleaning Strategy | Defined |
| KPI Engineering | Pending |
| Tableau Development | Pending |

---

# Critical Gaps

## Gap 1 — Research Dataset Availability

### Impact

Research Productivity Index cannot be generated without an approved research dataset.

### Resolution

Use an approved research dataset such as OpenAlex (if accepted for the project) or another publicly available research dataset that satisfies project requirements.

### Priority

HIGH

---

## Gap 2 — University Name Standardization

### Impact

Different datasets use different naming conventions.

Examples include abbreviations, punctuation differences, and alternate spellings.

Incorrect matching may reduce merge accuracy.

### Resolution

Create a standardized university naming strategy before merging datasets.

### Priority

HIGH

---

## Gap 3 — QS Dataset Format Variations

### Impact

Different QS datasets contain different structures.

Examples include:

- Multiple header rows
- Semicolon delimiters
- Different column names
- Missing country field in QS 2022

### Resolution

Create preprocessing scripts to standardize every QS dataset into a common schema before merging.

### Priority

HIGH

---

## Gap 4 — Country Name Standardization

### Impact

Country names differ between datasets.

Examples include:

- USA vs United States
- UK vs United Kingdom

Incorrect country matching affects World Bank integration.

### Resolution

Create a common country mapping dictionary before dataset merging.

### Priority

MEDIUM

---

## Gap 5 — Missing Values

### Impact

Merged datasets will naturally contain missing values because every source contains different information.

### Resolution

Handle missing values during the cleaning phase.

The final cleaned dataset must contain less than 2% missing values.

### Priority

HIGH

---

# Minor Gaps

## Percentage Formatting

Several datasets store percentages as text.

Examples

- 41%
- 18%

These values must be converted into numeric fields before KPI calculations.

---

## Data Type Standardization

Ranking values

Scores

Ratios

Population

GDP

Student counts

must all be converted into consistent numeric formats.

---

## Duplicate Universities

Universities appearing in multiple datasets must be merged into a single master record using standardized identifiers.

---

# Data Quality Validation Checklist

Before generating KPIs, verify:

- All datasets successfully loaded.
- All required columns exist.
- University names standardized.
- Country names standardized.
- Duplicate universities resolved.
- Missing values handled.
- Data types validated.
- Merge integrity verified.
- Raw dataset successfully generated.
- Clean dataset successfully generated.

Only after completing this checklist should KPI engineering begin.

---

# Part 5: Final Verification Summary

## Dataset Pipeline Verification

| Stage | Output |
|--------|--------|
| Collect Source Datasets | Multiple Raw Source Files |
| Validate Datasets | Validated Source Data |
| Merge Datasets | university_raw_data.csv |
| Clean Data | university_cleaned.csv |
| Feature Engineering | Engineered Features |
| KPI Engineering | university_final_dataset.xlsx |
| Dashboard Development | Tableau Workbook |

---

## KPI Support Summary

| KPI | Primary Source | Status |
|------|----------------|--------|
| Global Ranking Score | QS + THE | Supported |
| Research Impact Score | QS + THE | Supported |
| Faculty-to-Student Ratio | THE Key Statistics | Supported |
| International Student Percentage | THE Key Statistics | Supported |
| Academic Reputation Score | QS Rankings | Supported |
| Research Productivity Index | Research Dataset | Conditional |

---

## Dashboard Support Summary

| Dashboard | Status |
|------------|--------|
| University Overview | Fully Supported |
| Research Analytics | Supported (Research Dataset Required) |
| Student Analytics | Fully Supported |
| Country Comparison | Fully Supported |

---

# Project Readiness Assessment

## Completed

- Dataset collection
- Dataset validation
- Schema documentation
- Merge strategy
- KPI planning
- Dashboard planning
- Data lineage definition

---

## Next Phase

The next implementation phase should follow this exact sequence:

```text
Validated Source Datasets
            │
            ▼
Create university_raw_data.csv
            │
            ▼
Clean and Standardize Data
            │
            ▼
Generate university_cleaned.csv
            │
            ▼
Feature Engineering
            │
            ▼
Generate university_final_dataset.xlsx
            │
            ▼
Build Tableau Dashboards
```

This workflow must be followed throughout the project to ensure consistent data quality, reproducible KPI calculations, and reliable dashboard development.
# Part 6: Recommendations

This section defines the implementation recommendations and mandatory development rules for the EduVision_DV project.

The objective is to ensure that every implementation phase follows a consistent data engineering workflow from source datasets to Tableau dashboards.

---

# Implementation Roadmap

The remaining implementation should follow the sequence below.

```text
Step 1
Collect Source Datasets
        │
        ▼
Step 2
Validate Individual Datasets
        │
        ▼
Step 3
Standardize Dataset Schemas
        │
        ▼
Step 4
Merge into
university_raw_data.csv
        │
        ▼
Step 5
Clean and Standardize Data
        │
        ▼
Generate
university_cleaned.csv
        │
        ▼
Step 6
Feature Engineering
        │
        ▼
Step 7
KPI Engineering
        │
        ▼
Generate
university_final_dataset.xlsx
        │
        ▼
Step 8
Build Tableau Dashboards
        │
        ▼
Step 9
Testing & Validation
        │
        ▼
Step 10
Documentation & Final Delivery
```

---

# Mandatory Implementation Rules

The following rules must be followed throughout the project.

## Rule 1

Never modify the original source datasets.

Source datasets are read-only.

---

## Rule 2

Always validate every dataset before merging.

Validation includes:

- Required columns
- Missing columns
- Duplicate records
- Invalid data types
- File integrity

---

## Rule 3

All validated datasets must first be merged into a single master raw dataset.

Output:

```
university_raw_data.csv
```

No KPI calculations or feature engineering should occur before this stage.

---

## Rule 4

Perform all cleaning operations only on

```
university_raw_data.csv
```

Cleaning includes:

- Duplicate removal
- Missing value handling
- University name standardization
- Country name standardization
- Data type correction
- Format normalization

---

## Rule 5

Generate

```
university_cleaned.csv
```

Requirements:

- Less than 2% missing values
- Consistent formatting
- Standardized values
- Ready for feature engineering

---

## Rule 6

Perform feature engineering only after the cleaned dataset has been created.

Feature engineering includes:

- Derived metrics
- Normalized scores
- Aggregated statistics
- Additional analytical fields

---

## Rule 7

Perform KPI engineering only on

```
university_cleaned.csv
```

Never calculate KPIs directly from source datasets.

---

## Rule 8

Generate the final analytical dataset.

Output:

```
university_final_dataset.xlsx
```

This dataset contains:

- All cleaned fields
- Engineered features
- Calculated KPIs
- Dashboard-ready columns

---

## Rule 9

Tableau must use only

```
university_final_dataset.xlsx
```

No dashboard should connect directly to:

- QS Rankings
- THE Rankings
- THE Key Statistics
- World Bank Indicators
- Research Dataset

---

## Rule 10

Every KPI and dashboard field must be traceable back to its original source dataset.

The data lineage should always be:

```text
Source Dataset
        │
        ▼
university_raw_data.csv
        │
        ▼
university_cleaned.csv
        │
        ▼
university_final_dataset.xlsx
        │
        ▼
Tableau Dashboard
```

---

# Final Deliverables

The completed project should include:

## Data

- Source datasets
- `university_raw_data.csv`
- `university_cleaned.csv`
- `university_final_dataset.xlsx`

---

## Python

- Data collection scripts
- Validation scripts
- Merge scripts
- Cleaning scripts
- Feature engineering scripts
- KPI generation scripts

---

## Tableau

One integrated Tableau workbook containing:

- University Overview
- Research Analytics
- Student Analytics
- Country Comparison

---

## Documentation

- Project documentation
- KPI documentation
- Dashboard documentation
- Data dictionary
- Implementation report

---

# Expected Project Structure

```text
EduVision_DV/

│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── final/
│
├── scripts/
│   ├── collection/
│   ├── validation/
│   ├── preprocessing/
│   ├── feature_engineering/
│   ├── kpi_generation/
│
├── dashboard/
│
├── docs/
│
├── notebooks/
│
└── README.md
```

---

# Conclusion

This document establishes the complete relationship between source datasets, data engineering, KPI generation, and Tableau dashboards.

The project follows a single, consistent pipeline:

```text
Source Datasets
        │
        ▼
Validation
        │
        ▼
Merge
        │
        ▼
university_raw_data.csv
        │
        ▼
Cleaning
        │
        ▼
university_cleaned.csv
        │
        ▼
Feature Engineering
        │
        ▼
KPI Engineering
        │
        ▼
university_final_dataset.xlsx
        │
        ▼
Tableau Dashboards
```

Following this workflow ensures:

- A single source of truth for all analyses.
- Consistent and reproducible KPI calculations.
- High-quality, standardized datasets.
- Reliable dashboard development.
- A scalable architecture for future enhancements.

---

**End of KPI_DASHBOARD_MAPPING.md**