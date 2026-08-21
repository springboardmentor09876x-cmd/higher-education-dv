# EduVision DV - Higher Education Performance Dashboard

## Project Overview

This project was done as part of my coursework in data visualization. The idea was to build an interactive dashboard that brings together different global education datasets into one place, so we can compare universities across countries, look at research output, student demographics, and how government spending ties into all of it.

I pulled together data from four major sources - QS World University Rankings, Times Higher Education Rankings, OpenAlex research data, and World Bank education indicators - cleaned and merged them, and then built a set of Tableau dashboards to visualize everything.

The main goal was to make it easy to explore higher education performance at the university level, country level, and even look at student-level metrics like international student ratios and faculty-to-student ratios.

---

## Features

- Merged dataset from 4 different sources covering 2020-2024
- 6 engineered KPIs for standardized comparison
- 4 interactive Tableau dashboards
- Automated data collection scripts for World Bank and OpenAlex APIs
- Full data cleaning pipeline that takes raw data from 41.6% missing values down to 0.0%
- Country name standardization across all datasets
- University name deduplication and normalization
- Cross-source imputation for missing scores

---

## Data Sources

| Source | What It Provides | Years |
|--------|-----------------|-------|
| QS World University Rankings | University rankings, academic reputation, employer reputation, citation metrics, international faculty/student scores | 2020-2024 |
| Times Higher Education Rankings | University rankings, teaching score, research environment, research quality, industry income, international outlook | 2020-2024 |
| OpenAlex | Research metrics - publications count, citation count, h-index, i10-index | 2020-2024 |
| World Bank Open Data | GDP per capita, education expenditure, literacy rate, population, tertiary enrollment (country-level) | 2020-2024 |

---

## Folder Structure

```
higher-education-dv/
├── dashboard/
│   └── eduvision_prototype_final.twbx    # Tableau workbook with 4 dashboards
├── data/
│   ├── raw/
│   │   ├── qs_rankings_2020-2024.csv     # QS ranking data by year
│   │   ├── the_rankings_2020-2024.csv    # THE ranking data by year
│   │   ├── the_key_statistics_2020-2024.csv  # THE student/faculty stats
│   │   ├── research_metrics_raw.csv       # OpenAlex research data
│   │   ├── country_metrics_raw.csv        # Aggregated country metrics
│   │   └── world_bank/
│   │       ├── csv/                       # World Bank indicator CSVs
│   │       └── json/                      # World Bank raw JSON responses
│   ├── processed/
│   │   ├── university_raw_data.csv        # Merged raw dataset
│   │   └── university_cleaned.csv         # Cleaned dataset (0.0% missing)
│   └── final/
│       └── university_final_dataset.xlsx  # Tableau-ready dataset with KPIs
├── docs/
│   ├── KPI_DASHBOARD_MAPPING.md           # Full KPI & dashboard spec
│   └── Dashboard_Storyboard.pdf           # Dashboard design storyboards
├── notebooks/
│   └── education_cleaning.ipynb           # Data cleaning & standardization
├── reports/
│   ├── cross_source_duplicate_review.csv
│   ├── university_name_review.csv
│   └── world_bank_missing_investigation.csv
└── scripts/
    ├── download_world_bank.py             # Downloads World Bank API data
    ├── convert_world_bank_json.py         # Converts JSON to CSV
    ├── collect_openalex_data.py           # Collects OpenAlex research data
    ├── collect_openalex_top_universities.py  # OpenAlex for top 500 universities
    ├── merge_datasets.py                  # Merges all source datasets
    └── generate_education_kpis.py         # Engineers 6 KPIs, exports final dataset
```

---

## Dashboards

### 1. Overview Dashboard
Shows a high-level comparison of universities. Includes global ranking scores, academic reputation, and how institutions compare across years. This is the main entry point to explore the data.

### 2. Research Dashboard
Focuses on research output and impact. Displays publications count, citation metrics, h-index, and a composite Research Impact Score. You can filter by country or year.

### 3. Country Dashboard
Compares countries on education indicators - GDP per capita, government education spending, tertiary enrollment, literacy rates, and how these relate to university performance in that country.

### 4. Student Dashboard
Looks at student-related metrics - faculty-to-student ratio, international student percentage, and gender distribution across universities and countries.

---

## KPIs

Six KPIs were engineered from the combined datasets:

| KPI | Description | Used In |
|-----|-------------|---------|
| Global Ranking Score | Weighted average of QS (60%) and THE (40%) overall scores, normalized to 0-100 | Overview |
| Research Impact Score | Weighted average of citations per faculty (40%), research quality (35%), and research environment (25%) | Research |
| Faculty-to-Student Ratio | Number of students per staff member | Student |
| International Student Percentage | Percentage of international students at a university | Student |
| Academic Reputation Score | QS academic reputation score | Overview |
| Research Productivity Index | Geometric mean of publications, citations, and h-index, scaled to 0-100 | Research |

---

## Tools Used

- **Python** - data collection, cleaning, merging, and KPI engineering
- **Pandas** - data manipulation and transformation
- **Tableau Desktop / Tableau Public** - interactive dashboard creation
- **Jupyter Notebook** - data cleaning pipeline
- **World Bank API** - fetching country-level education indicators
- **OpenAlex API** - fetching university-level research data
- **Git** - version control

---

## How to Run

### Prerequisites

- Python 3.8+
- Tableau Desktop or Tableau Public
- Git (optional)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/higher-education-dv.git
cd higher-education-dv
```

### 2. Install Python dependencies

```bash
pip install pandas requests
```

### 3. Download World Bank data (optional - raw data is already included)

```bash
python scripts/download_world_bank.py
python scripts/convert_world_bank_json.py
```

### 4. Collect OpenAlex research data (optional - raw data is already included)

```bash
python scripts/collect_openalex_data.py
```

### 5. Merge all datasets

```bash
python scripts/merge_datasets.py
```

This produces `data/processed/university_raw_data.csv`.

### 6. Run the cleaning notebook

Open `notebooks/education_cleaning.ipynb` in Jupyter and run all cells. This produces `data/processed/university_cleaned.csv`.

### 7. Generate KPIs and final dataset

```bash
python scripts/generate_education_kpis.py
```

This produces `data/final/university_final_dataset.xlsx`.

### 8. Open the Tableau dashboard

Open `dashboard/eduvision_prototype_final.twbx` in Tableau Desktop or Tableau Public. Point the data source to `data/final/university_final_dataset.xlsx` if prompted.

---

## Key Findings

- Universities in the US and UK consistently rank highest across both QS and THE rankings, but several Asian universities (especially from China, Singapore, and Hong Kong) have been climbing steadily from 2020 to 2024.
- There is a strong correlation between a country's GDP per capita and the average ranking of its universities, but some countries like India and Brazil perform above what their GDP would predict.
- International student percentages tend to be higher in universities that also score well on research impact, suggesting that research reputation attracts international students.
- Countries that spend more on education as a percentage of GDP don't always have the best-ranked universities - other factors like research funding and faculty quality matter a lot.

---

## Future Improvements

- Add more years of data (pre-2020) to observe longer-term trends
- Incorporate additional ranking sources like ARWU (Shanghai Rankings)
- Add salary and employment outcome data after graduation
- Build a live-updating version using scheduled API calls
- Explore machine learning models to predict university rankings
- Add a web-based dashboard using Streamlit or Dash for wider accessibility

---

## License

This project is for academic and educational purposes only.
