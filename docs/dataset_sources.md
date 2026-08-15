# EduVision_DV — Dataset Sources

## Project Data Sources

EduVision_DV integrates publicly available higher-education ranking datasets
to support university, research, student, and country-level analysis.

### 1. QS World University Rankings

Used for:

- Global university rankings
- Academic reputation
- Employer reputation
- Faculty-to-student indicators
- Citations per faculty
- International student indicators
- International faculty indicators
- International research network
- Employment outcomes
- Sustainability indicators

### 2. Times Higher Education World University Rankings

Used for:

- Teaching performance
- Research performance
- Citations
- International outlook
- Industry/income indicators
- Overall Times ranking

### 3. Academic Ranking of World Universities (ShanghaiRanking)

Used for:

- Global university ranking
- Research-related indicators
- Research performance comparison

## Data Processing

The datasets were integrated and prepared using Python and Pandas.

The preparation process included:

- Removing duplicate university records
- Standardizing university names
- Standardizing country names
- Converting ranking fields into numeric values
- Handling missing and unavailable values
- Engineering education performance KPIs
- Preparing the final dataset for Tableau

## Final Dataset

The processed dataset used by the Tableau dashboards is:

`data/university_final_dataset.xlsx`