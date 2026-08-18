# 🎓 Higher Education Performance Dashboard

An interactive data analytics project developed to analyze and visualize **QS World University Rankings from 2016 to 2026**. The project combines Python-based data preparation with Tableau to transform historical university ranking data into an interactive analytical dashboard.

## 📌 Project Overview

The **Higher Education Performance Dashboard** provides a consolidated view of university rankings and performance across an 11-year period.

The project enables users to:

* Analyze university ranking trends from **2016–2026**
* Compare universities across different years
* Examine academic and research performance
* Analyze university distribution by country and region
* Explore student-related indicators
* Compare institutional performance
* Interactively filter and explore university data

## 🗂️ Dataset

The project uses **QS World University Rankings data covering 2016–2026**.

The datasets contain information such as:

* University / Institution Name
* World Ranking
* Previous Year Ranking
* Country / Territory
* Region
* Institution Status
* Institution Size
* Academic Reputation
* Employer Reputation
* Faculty–Student Ratio
* Citations per Faculty
* International Faculty Ratio
* International Student Ratio
* Research indicators
* Other QS performance metrics

Historical ranking data was consolidated to support year-wise university comparison and trend analysis.

## 🐍 Data Preparation Using Python

Python was used for data collection, cleaning, standardization, integration, and validation before the data was imported into Tableau.

### Data Preparation Process

1. Collected QS university ranking datasets for multiple years.
2. Imported the datasets using **Pandas**.
3. Standardized column names and data formats.
4. Cleaned and standardized university names.
5. Integrated historical ranking information from **2016–2026**.
6. Handled missing and inconsistent values.
7. Standardized different ranking formats, including:

   * `800+`
   * `700=`
   * `691–700`
   * `801–850`
   * `951–1000`
8. Preserved ranking ranges where exact rankings were unavailable.
9. Validated the merged dataset.
10. Generated the final cleaned dataset for dashboard development.

## 📊 Tableau Dashboard

The cleaned dataset was used to develop an interactive Tableau dashboard consisting of four major analytical sections.

### 1. University Overview

Provides a high-level overview of university performance through:

* Total Universities
* Total Countries
* Average Academic Reputation
* Average Overall Score
* Top University Rankings
* Global University Distribution
* Academic Reputation Analysis
* University Performance Trends
* Institutional Comparison

### 2. Research Analytics

Focuses on research-related university performance and enables users to analyze research indicators across universities, countries, and regions.

### 3. Student Analytics

Provides insights into student-related indicators, including international student representation and other relevant student-focused metrics.

### 4. Country Comparison

Enables users to compare university performance across countries and regions using ranking and performance indicators.

## 🔎 Interactive Features

The dashboard provides interactive functionality for exploring the data:

* Year filters
* Region filters
* Country filters
* University filters
* Subject-area filtering
* Interactive university selection
* Parameter actions
* Dynamic KPI updates
* Interactive charts
* University comparisons
* Reset Filters functionality
* Dashboard navigation

Selecting a university dynamically updates the relevant KPIs and visualizations, allowing users to explore institutional performance interactively.

## 🛠️ Technologies Used

| Technology  | Purpose                                      |
| ----------- | -------------------------------------------- |
| **Python**  | Data preparation and cleaning                |
| **Pandas**  | Data manipulation and integration            |
| **CSV**     | Data storage and exchange                    |
| **Tableau** | Data visualization and dashboard development |
| **GitHub**  | Version control and project documentation    |

## 📁 Project Structure

```text
University-Ranking-Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── python/
│   ├── data_collection.py
│   ├── clean_data.py
│   ├── education_cleaning.py
│   ├── merge.py
│   ├── fuzzy_merge_2024.py
│   ├── fill_missing_ranks.py
│   └── check_unmatched.py
│
├── tableau/
│   └── University_Ranking_Dashboard.twbx
│
├── University_Cleaned_Data.csv
│
└── README.md
```

## 🚀 Project Workflow

```text
QS Ranking Datasets (2016–2026)
              ↓
       Data Collection
              ↓
    Data Cleaning & Standardization
              ↓
      Historical Data Integration
              ↓
      Missing Value Handling
              ↓
        Data Validation
              ↓
      Final Clean Dataset
              ↓
       Tableau Visualization
              ↓
      Interactive Dashboard
```

## 🎯 Key Outcomes

The project provides an integrated analytical view of university rankings over an **11-year period from 2016 to 2026**.

The dashboard helps users:

* Track university ranking changes over time
* Compare institutions across multiple years
* Analyze academic reputation
* Explore research and student-related indicators
* Identify leading universities
* Examine country and regional patterns
* Compare institutional performance
* Discover trends through interactive visualizations

## 💡 Skills Demonstrated

* Data Collection
* Data Cleaning
* Data Transformation
* Data Integration
* Data Validation
* Exploratory Data Analysis
* Missing Data Handling
* Data Visualization
* Dashboard Development
* Interactive Analytics
* Python
* Pandas
* Tableau
* GitHub

## 📌 Project Highlights

* **11 years of historical university ranking data**
* **2016–2026 ranking analysis**
* Python-based data preparation pipeline
* Consolidated university ranking dataset
* Interactive Tableau dashboard
* Multiple analytical dashboard sections
* Dynamic KPIs and visualizations
* Parameter-driven university comparison
* Country and regional analysis
* Historical ranking trend analysis

## 👩‍💻 Project

**Higher Education Performance Dashboard**

A data analytics and visualization project that transforms historical **QS World University Rankings (2016–2026)** into an interactive Tableau dashboard using Python-based data preparation and analysis.
