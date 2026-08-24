# University Ranking Analytics Dashboard

## Project Overview

The **University Ranking Analytics Dashboard** is an interactive data analytics project developed to analyze university rankings, academic performance, research productivity, student information, faculty-related indicators, and country-wise educational performance.

The project transforms university-level data into meaningful Key Performance Indicators (KPIs), rankings, comparisons, and interactive Power BI dashboards.

The project also includes data preparation, KPI engineering, dashboard development, documentation, and quality assurance testing.

---

# 1. Project Objectives

The main objectives of this project are:

- Analyze university rankings and performance.
- Compare universities across different countries.
- Analyze academic reputation and overall performance.
- Evaluate research productivity and research impact.
- Analyze student and faculty-related metrics.
- Analyze international student participation.
- Calculate educational KPIs.
- Build interactive Power BI dashboards.
- Validate dashboard calculations and interactions.
- Document the complete analytics workflow.

---

# 2. Dataset

The project uses the final university dataset.

| Property | Details |
|---|---|
| Dataset Name | University Final Dataset |
| File | `university_final_dataset.xlsx` |
| Rows | 22,125 |
| Columns | 44 |
| Sheet | `Sheet1` |

## Dataset Categories

The dataset contains information related to:

- University information
- Country
- Region
- City
- University type
- Subject field
- Degree level
- World ranking
- National ranking
- Overall score
- Academic reputation
- Employer reputation
- Citations
- Publications
- Research performance
- Student population
- International students
- Faculty information
- Faculty-to-student ratio
- Gender information

---

# 3. Data Preparation

The dataset was prepared for dashboard analysis by:

1. Loading the university dataset.
2. Checking the available fields.
3. Preparing the required university, country, academic, research, student, and faculty fields.
4. Preparing KPI-related fields.
5. Organizing the final dataset for Power BI analysis.
6. Using the prepared dataset for dashboard development and testing.

---

# 4. Key Performance Indicators

The project includes KPIs covering university, academic, research, student, faculty, and international education performance.

## University KPIs

- Total Universities
- Countries Covered
- Average Overall Score
- Global Ranking Score
- World Rank
- National Rank
- Country Average Rank
- Best University Rank

## Academic KPIs

- Average Academic Reputation
- Academic Reputation Score
- Employer Reputation Score
- Academic Reputation KPI

## Research KPIs

- Total Publications
- Total Citations
- Average H Index
- Average Citations per Faculty
- Research Productivity Index
- Research Productivity KPI
- Research Impact Score

## Student and Faculty KPIs

- Total Students
- Total International Students
- International Student Ratio
- International Student Percentage
- Faculty Count
- Faculty-to-Student Ratio
- Faculty Student Ratio KPI

---

# 5. Dashboard

The project uses **Microsoft Power BI** for interactive dashboard development.

## Dashboard Components

### University Overview

Provides an overall view of university performance using:

- KPI cards
- University rankings
- Academic performance
- Overall scores
- University comparisons
- Interactive filters

### Country Comparison

Provides country-wise analysis including:

- Country rankings
- Average university scores
- Country performance comparison
- Best-performing countries
- Interactive country filters

### Research Analytics

Analyzes research performance using:

- Publications
- Citations
- H Index
- Citations per Faculty
- Research Productivity
- Research Impact
- Top research institutions

### Student Analytics

Analyzes:

- Total students
- International students
- International student ratio
- Faculty-to-student ratio
- Student population
- Student-related comparisons

---

# 6. Dashboard Filters

Interactive filters are used to analyze specific subsets of the data.

The available analysis dimensions include:

- Country
- Year
- University Name
- Region
- University Type
- Subject Field
- Degree Level

The filters dynamically update the dashboard visuals and KPI values.

---

# 7. Dashboard Visualizations

The project uses different Power BI visualizations, including:

- KPI Cards
- Bar Charts
- Column Charts
- Line Charts
- Tables
- Ranking Visuals
- Maps
- Interactive Slicers

These visuals are used to compare universities, countries, academic performance, research performance, and student-related indicators.

---

# 8. Education Analytics

The education analytics component focuses on university academic, research, student, faculty, and international education indicators.

## Academic Analysis

Academic performance is analyzed using:

- Academic Reputation Score
- Employer Reputation Score
- Overall Score
- World Rank
- National Rank

## Research Analysis

Research performance is analyzed using:

- Publications Count
- Citations Count
- Citations per Faculty
- H Index
- Research Productivity Index
- Research Impact Score

## Student and Faculty Analysis

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

## Country Analysis

Country-level performance is analyzed using:

- Country Average Rank
- Country Average Overall Score
- Country Average Academic Reputation
- Country Average Citations
- Country Average International Ratio
- Best University Rank

---

# 9. KPI Calculation Approach

The dashboard uses aggregation and calculated measures to summarize university performance.

Common calculation approaches include:

- `AVERAGE()` for average-based metrics
- `SUM()` for total-based metrics
- `COUNT()` for counting records
- `DISTINCTCOUNT()` for unique universities and countries
- Ranking calculations for university and country comparisons
- Filtering calculations based on dashboard selections

---

# 10. Dashboard Testing

The dashboard was tested to verify:

- KPI accuracy
- Ranking accuracy
- Dashboard interactions
- Slicer functionality
- Educational metric calculations

## Testing Summary

| Testing Category | Total | Passed | Failed |
|---|---:|---:|---:|
| KPI Validation | 19 | 19 | 0 |
| Ranking Validation | 4 | 4 | 0 |
| Dashboard Interaction | 5 | 5 | 0 |
| Educational Metrics | 4 | 4 | 0 |
| **Total** | **32** | **32** | **0** |

### Overall Testing Result

**32 test cases passed and 0 test cases failed.**

---

# 11. QA Testing

The QA process included validation of:

### KPI Testing

KPI values were checked against their corresponding calculations and dashboard results.

### Ranking Testing

Ranking visuals were checked to ensure that universities, research institutions, and countries were displayed in the expected order.

### Interaction Testing

Dashboard slicers and visual interactions were tested to verify that selections correctly updated related visuals.

### Educational Metric Testing

Selected educational metrics were checked against their dashboard calculations.

---

# 12. Documentation

The project documentation is maintained in the `docs` directory.

| Document | Description |
|---|---|
| `Dataset_Sources.md` | Dataset information and fields |
| `KPI_Definitions.md` | KPI definitions and calculation approach |
| `Dashboard_Guide.md` | Dashboard usage and visual descriptions |
| `Education_Analytics_Methodology.md` | Education analytics methodology |
| `Dashboard_Testing_Report.md` | Dashboard QA and testing results |

---

# 13. Project Structure

```text
University-Ranking-Analytics/
│
├── README.md
│
├── scripts/
│   └── Project scripts
│
├── data/
│   └── university_final_dataset.xlsx
│
├── dashboard/
│   └── University_Ranking_Analytics.pbix
│
└── docs/
    ├── Dataset_Sources.md
    ├── KPI_Definitions.md
    ├── Dashboard_Guide.md
    ├── Education_Analytics_Methodology.md
    └── Dashboard_Testin| Technology / Tool    
```  
# 14. Technologies Used

| Technology / Tool | Purpose |
|---|---|
| **Microsoft Power BI** | Dashboard development, KPI visualization, ranking analysis, and interactive reporting |
| **Microsoft Excel** | Final dataset storage and spreadsheet-based data handling |
| **Python** | Data processing, cleaning, and analytical processing |
| **Jupyter Notebook** | Data merging, cleaning, KPI development, and analysis |
| **Pandas** | Data manipulation and preprocessing |
| **GitHub** | Version control, project organization, documentation, and project delivery |
| **Markdown** | Project documentation |
| **CSV** | Storage and processing of raw and processed datasets |
| **Power BI DAX** | KPI and calculated measure creation |


# 15. Project Workflow

The complete project workflow is:

```text
Raw Datasets
     ↓
Data Collection
     ↓
Data Cleaning & Processing
     ↓
Dataset Merging
     ↓
KPI Development
     ↓
Final Dataset
     ↓
Power BI Dashboard Development
     ↓
Dashboard Testing
     ↓
QA Checklist
     ↓
Documentation
     ↓
GitHub Project Delivery
```

# 16. Future Scope

Predict future university rankings using Machine Learning.
Automate data updates and KPI calculations.
Add advanced research and performance analysis.
Improve dashboard interactivity and visualization.
Deploy the dashboard to the cloud for wider access.