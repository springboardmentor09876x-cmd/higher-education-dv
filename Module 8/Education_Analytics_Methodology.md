# EduVision_DV – Education Analytics Methodology

## 1. Data Collection
The project combines higher-education ranking and student/research datasets, including QS, Times Higher Education, CWUR and related student data.

## 2. Data Cleaning
The cleaning pipeline standardizes university names, ranking fields, numeric values, student metrics, research metrics, country/region fields and missing values.

## 3. Data Integration
Datasets are integrated using university-level matching and standardized fields. The project maintains raw, processed and final datasets separately.

## 4. KPI Engineering
Custom educational analytics KPIs are created using weighted formulas and min-max normalization where applicable.

## 5. Dashboard Analytics
The final dashboard suite covers:
- University Overview
- Research Analytics
- Student Analytics
- Country Comparison

## 6. Validation
Validation includes duplicate checks, missing-value review, KPI formula checks, ranking checks and dashboard interaction testing.

## 7. Limitations
Some source ranking and score fields are not published for every university. Such values are retained as missing where appropriate rather than being converted to zero.

## 8. Future Scope
Future improvements can include automated data refresh, additional ranking sources, predictive analytics, deeper university benchmarking and deployment through a public BI platform.
