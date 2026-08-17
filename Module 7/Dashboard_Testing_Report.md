# EduVision_DV – Dashboard Testing Report

## 1. Purpose
This report documents the testing and validation activities performed for the EduVision_DV higher-education analytics dashboard suite.

## 2. Final Dataset
**File:** `datasets/processed datasets/university_final_dataset (1).xlsx`

- Records: 668
- Columns: 44
- Duplicate rows: 0

## 3. Data Validation
The final dataset was checked for duplicate records, missing values, ranking fields, student metrics, and research metrics.

The original `world_rank` field contains missing values in some records; the standardized `world_rank_numeric` field was reviewed for analytical ranking use.

The `overall_score_numeric` field contains expected nulls where the source value is `Not Published`. These values were not treated as zero.

## 4. KPI Validation

### Global Ranking Score
Weighted using:
- QS rank: 40%
- THE rank: 30%
- Overall score: 30%

Rank values are normalized after inversion so that better ranks receive higher scores.

### Research Impact Score
Weighted using:
- Citation Score: 50%
- Research Quality: 50%

### Faculty-to-Student Ratio KPI
The KPI is derived from the standardized faculty-to-student ratio field.

### International Student Percentage
The KPI source and cleaning logic were traced through the education-cleaning and KPI-generation notebooks. Final reconciliation is pending because historical output contains differences that need to be resolved before claiming 100% accuracy.

### Academic Reputation Score KPI
Uses the standardized academic reputation score as the KPI value.

### Research Productivity Index
Weighted using:
- Publication Count: 60%
- H-Index: 40%

The normalization method used in the KPI notebook is min-max normalization to a 0–100 scale.

## 5. Dashboard Testing Areas
The following areas are included in the final QA pass:
- KPI card values
- Filters
- Navigation
- Charts
- Tooltips
- University selection
- Country selection
- Cross-dashboard consistency
- Layout and readability

## 6. Current QA Status
The project has completed dataset-level validation and KPI formula documentation. Final KPI reconciliation and complete interaction sign-off remain before reporting a final KPI accuracy percentage.

## 7. Conclusion
The EduVision_DV dashboard suite has a documented testing process covering data quality, KPI calculations, dashboard interactions, and final delivery.
