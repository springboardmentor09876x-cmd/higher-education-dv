EduVision_DV — Higher Education Performance Analytics Dashboard

An interactive business intelligence project for analyzing university rankings, research performance, student demographics, academic indicators, and country-level higher-education trends.

📌 Project Overview

EduVision_DV is a higher-education data analytics and visualization project developed to transform multiple university-ranking and education datasets into an interactive dashboard suite.

The project brings together university-level ranking, research, academic, faculty, and student information to help users:

Compare universities across ranking indicators

Analyze research output and research impact

Understand student and international-student characteristics

Compare higher-education performance across countries

Explore academic reputation and faculty-to-student indicators

Identify patterns and trends through interactive Power BI dashboards

The final solution is designed as a portfolio-ready higher-education analytics dashboard suite.

🎯 Objectives

Integrate data from multiple higher-education sources.

Clean, standardize, and merge university-level datasets.

Engineer meaningful educational analytics KPIs.

Build interactive dashboards for different analytical perspectives.

Validate data, KPI calculations, rankings, and dashboard interactions.

Document the complete data-to-dashboard methodology.

Deliver the project through a structured GitHub repository.

📊 Dashboard Suite

The project contains four major analytical dashboards.

1. University Overview

Provides a high-level view of university performance.

Key areas:

University ranking

Overall score

Academic reputation

Employer reputation

Faculty-to-student ratio

International student percentage

University and country-level comparison

2. Research Analytics

Focuses on research performance and research impact.

Key metrics include:

Publications

Citations

H-Index

Citations per Faculty

Research Output Score

Research Impact Score

Research Productivity Index

Typical analysis:

Research performance comparison

Publication and citation patterns

Research leaderboards

Relationship between research output and impact

3. Student Analytics

Analyzes student-related educational indicators.

Key areas:

Total students

Undergraduate students

Postgraduate students

International student percentage

Faculty-to-student ratio

Gender-related indicators

Degree-level information

4. Country Comparison

Provides country-level higher-education comparisons.

Key areas:

Average university rank

Number of ranked universities

Best university rank

Average overall score

Academic reputation

Citation performance

International student indicators

🗂️ Data Sources

The project uses multiple higher-education datasets, including:

QS World University Rankings 2026

Times Higher Education (THE) Rankings

CWUR University Rankings

THE 2023 Student Dataset

Additional processed and enriched university-level data used during integration

The raw and processed datasets are maintained separately in the repository.

🔄 Data Processing Pipeline

The project follows a multi-stage data analytics pipeline:

Raw Data Sources
      ↓
Data Collection
      ↓
Data Cleaning & Standardization
      ↓
University Matching & Integration
      ↓
KPI Engineering
      ↓
Final Dataset
      ↓
Power BI Dashboard Development
      ↓
Testing & Validation
      ↓
Documentation & Delivery

Data processing includes:

Column standardization

Data type conversion

Ranking normalization

Missing-value treatment

University-name standardization

Dataset integration

Fuzzy matching where required

Student and research metric preparation

KPI engineering

📁 Final Dataset

The current final dataset is:

datasets/processed datasets/university_final_dataset (1).xlsx

Dataset validation

Validation

Result

Records

668

Columns

44

Duplicate rows

0

Important data-quality observations

world_rank_numeric is used as the standardized numeric ranking field for analytical ranking calculations.

Some world_rank values are unavailable in the source data.

overall_score_numeric remains missing where the source explicitly reports Not Published.

Not Published values are not treated as zero.

📈 KPI Framework

The project contains six major educational analytics KPIs.

1. Global Ranking Score

Combines QS, THE, and overall-score performance.

Component

Weight

QS Rank

40%

THE Rank

30%

Overall Score

30%

Better rankings receive higher normalized contributions.

2. Research Impact Score

Measures research impact using:

Component

Weight

Citation Score

50%

Research Quality

50%

3. Faculty-to-Student Ratio KPI

Uses the standardized faculty-to-student ratio as an analytical KPI.

4. International Student Percentage

Represents the international-student percentage from the education data pipeline.

The source and transformation are documented in the cleaning and KPI-generation notebooks.

5. Academic Reputation Score KPI

Uses the standardized academic reputation score as the analytical KPI.

6. Research Productivity Index

Combines publication volume and H-Index.

Component

Weight

Publication Count

60%

H-Index

40%

🔢 KPI Normalization

For KPIs using normalization, the project uses min-max normalization on a 0–100 scale:

Normalized Score =
((Value - Minimum) / (Maximum - Minimum)) × 100

For an input series where all values are identical, the KPI-generation logic assigns a neutral score of 50.

🛠️ Technologies Used

Data Processing

Python

Pandas

NumPy

Jupyter Notebook

Excel / CSV

Data Visualization & BI

Microsoft Power BI

Development

Visual Studio Code

Git

GitHub

Data Sources / Enrichment

QS

Times Higher Education

CWUR

Higher-education student datasets

📂 Project Structure

higher-education-dv/
│
├── datasets/
│   ├── raw datasets/
│   │   ├── raw datasets required/
│   │   ├── cwur_clean.csv
│   │   ├── final_merged_eduvision_dataset.csv
│   │   ├── fuzzy_match_details_cleaned.csv
│   │   ├── master_common_universities.csv
│   │   ├── qs2026_clean.csv
│   │   ├── the_clean.csv
│   │   ├── the2023_clean.csv
│   │   └── university_raw_data.csv
│   │
│   └── processed datasets/
│       ├── EduVision_Final_Dataset_uncleaned.csv
│       ├── University_Cleaned.csv
│       ├── university_final_dataset.xlsx
│       └── university_final_dataset (1).xlsx
│
├── notebooks/
│   ├── education_cleaning.ipynb
│   └── generate_education_kpis.ipynb
│
├── Module 4/
│   ├── dashboard_Storyboard.pdf
│   └── eduvision_prototype.pbix
│
├── Module 5/
│   ├── overview_dashboard.pbix
│   └── research_dashboard.pbix
│
├── Module 6/
│   ├── Countrycomparison_dashboard.pbix
│   └── Student_dashboard.pbix
│
├── Module 7/
│   ├── QA_Checklist.md
│   └── Dashboard_Testing_Report.md
│
├── Module 8/
│   ├── KPI_Definitions.md
│   ├── Education_Analytics_Methodology.md
│   └── Final_Project_Documentation.md
│
├── Education day 2.csv
├── final dashboard.pbix
└── README.md

🧪 Testing & Validation

Testing is organized into four areas.

1. Dataset Validation

Checks include:

Record count

Column count

Duplicate records

Missing values

Ranking fields

Student metrics

Research metrics

2. KPI Validation

The KPI-generation methodology is reviewed against the source fields and implemented formulas.

3. Dashboard Testing

The following are tested:

KPI cards

Charts

Filters

Slicers

Navigation

Tooltips

University selection

Country selection

Cross-dashboard consistency

Layout and readability

4. Final QA

Detailed QA documentation is available in:

Module 7/
├── QA_Checklist.md
└── Dashboard_Testing_Report.md

Quantitative KPI accuracy should only be reported after all KPI reconciliation tests are completed.

📚 Documentation

Detailed project documentation is available in Module 8/:

Document

Purpose

KPI_Definitions.md

KPI formulas and definitions

Education_Analytics_Methodology.md

Data and analytics methodology

Final_Project_Documentation.md

Complete project documentation

🚀 How to Use the Project

1. Clone the repository

git clone <repository-url>
cd higher-education-dv

2. Install Python dependencies

pip install pandas numpy openpyxl

If using the Jupyter notebooks:

pip install jupyter

3. Review the notebooks

Start with:

notebooks/education_cleaning.ipynb

Then review:

notebooks/generate_education_kpis.ipynb

4. Open the dashboard

Open:

final dashboard.pbix

using Microsoft Power BI Desktop.

🖥️ Dashboard Navigation

The dashboard suite is organized into four analytical views:

University Overview
       ↓
Research Analytics
       ↓
Student Analytics
       ↓
Country Comparison

Users can apply available filters and interact with visualizations to explore university and country-level performance.

📌 Project Deliverables

The repository contains:

Raw datasets

Cleaned datasets

Final integrated dataset

Data-cleaning notebook

KPI-generation notebook

Dashboard storyboard

Dashboard prototype

Four dashboard development files

Final Power BI dashboard

QA checklist

Dashboard testing report

KPI definitions

Education analytics methodology

Final project documentation

README

⚠️ Data Limitations

The project depends on publicly available ranking and education datasets. Therefore:

Ranking methodologies differ between sources.

Some universities may have missing or unpublished scores.

Source datasets may contain inconsistent naming conventions.

Some metrics are available only for selected universities or years.

Rankings and educational statistics represent the source data period and should not be interpreted as continuously updated values.

🔮 Future Scope

Potential improvements include:

Automated dataset refresh

Additional ranking sources

Time-series ranking analysis

Predictive university performance modeling

Advanced statistical analysis

Automated data-quality checks

More granular subject-level analysis

Public Power BI deployment

Automated KPI recalculation pipelines

👩‍💻 Project Status

Status: Dashboard development and documentation completed; final QA and validation are part of the delivery stage.

The project is structured as a portfolio-ready higher-education analytics solution with reproducible data-processing notebooks, engineered KPIs, interactive Power BI dashboards, and supporting documentation.

👩‍💻 Author

Sneha Sahu

B.Tech — Computer Science & Engineering (AI & ML)

GitHub: snehaaa3

⭐ Acknowledgement

This project was developed as an educational data analytics and visualization project to demonstrate skills in:

Data cleaning

Data integration

Exploratory data analysis

KPI engineering

Business intelligence

Data visualization

Dashboard design

Data validation

Technical documentation