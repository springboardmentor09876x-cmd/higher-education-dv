# EduVision_DV – Higher Education Performance Dashboard

## 📊 Project Overview

**EduVision_DV** is an interactive higher education analytics and data visualization project developed using **Python, Pandas, NumPy, and Tableau**.

The project integrates university ranking, academic, research, and student-related datasets to provide a consolidated view of higher education performance across universities, countries, and regions.

The final Tableau workbook contains four interconnected dashboards that help users explore university performance, research analytics, student analytics, and country-level comparisons.

---

## 🎯 Project Objectives

The main objectives of the project are to:

* Collect and integrate higher education datasets from multiple sources.
* Clean and standardize university-related data.
* Handle missing values, duplicate records, and inconsistent data formats.
* Engineer meaningful education performance KPIs.
* Analyze university rankings and academic performance.
* Analyze research output, citations, and research impact.
* Analyze student population, international students, diversity, and faculty-to-student ratio.
* Compare higher education performance across countries and regions.
* Develop interactive Tableau dashboards for data exploration and comparison.
* Validate KPI calculations, rankings, visualizations, filters, and dashboard interactions.

---

## 📚 Dataset & Data Sources

The project uses publicly available higher education and university ranking datasets, including:

* **QS World University Rankings**
* **Times Higher Education (THE) World University Rankings**
* **Top 1000 Universities Worldwide**
* Additional university datasets used to provide academic, research, and student-related metrics.

The datasets were collected in raw form, processed using Python, and integrated into a final dataset for dashboard development.

---

## 🔄 Data Processing Workflow

```text
Data Collection
      ↓
Data Understanding
      ↓
Data Cleaning & Preprocessing
      ↓
Dataset Integration / Merging
      ↓
KPI Engineering
      ↓
Dashboard Planning
      ↓
Tableau Worksheet Development
      ↓
Dashboard Integration
      ↓
Testing & Validation
      ↓
Documentation & Final Delivery
```

### Data Processing

Python and Pandas were used for:

* Inspecting datasets and their structures.
* Standardizing column names and formats.
* Handling missing and inconsistent values.
* Identifying duplicate records.
* Preparing datasets for integration.
* Merging relevant university information.
* Preparing the final dataset for Tableau analysis.

---

## 📈 Key Performance Indicators

The project uses meaningful KPIs to summarize higher education performance.

| KPI                                  | Description                                                               |
| ------------------------------------ | ------------------------------------------------------------------------- |
| **Total Universities**               | Number of unique universities represented in the dataset.                 |
| **Countries Covered**                | Number of unique countries represented in the dataset.                    |
| **Global Ranking Score**             | Ranking-related metric used for university and country comparison.        |
| **Overall Score**                    | Overall university performance score.                                     |
| **Academic Reputation Score**        | Metric representing academic reputation.                                  |
| **Research Impact Score**            | Metric used to compare research-related institutional impact.             |
| **Faculty-to-Student Ratio**         | Represents the relationship between faculty and student population.       |
| **International Student Percentage** | Percentage of students who are international.                             |
| **Student Population**               | Number of students represented in the dataset.                            |
| **Publication Count**                | Number of research publications represented by an institution or country. |
| **Citation Score**                   | Indicates the citation performance of research.                           |

---

# 🖥️ Dashboard Suite

EduVision_DV consists of four interconnected Tableau dashboards.

## 1. University Overview

### Purpose

Provides an overall view of university performance and rankings.

### Key Analysis

* Top University Rankings
* Global University Distribution
* Academic Reputation Analysis
* University Performance Trends
* Institutional Comparison

### Main Visualizations

* Bar charts
* Map
* Scatter plot
* Line chart
* Comparison visualizations

---

## 2. Research Analytics

### Purpose

Focuses on research output, citation performance, research productivity, and research impact.

### Key Analysis

* Publications Analysis
* Citation Performance
* Research Productivity Trends
* Top Research Institutions
* Research Impact Comparison

### Main Research Metrics

* Publication Count
* Citation Count
* Citation Score
* Research Output
* Research Impact
* Academic Reputation

---

## 3. Student Analytics

### Purpose

Analyzes student-related higher education metrics.

### Key Analysis

* International Student Analysis
* Faculty-to-Student Ratio Analysis
* Student Diversity Trends
* Enrollment Comparisons
* Student Distribution Analysis

### Main Student Metrics

* Student Population
* International Student Percentage
* Female Percentage
* Male Percentage
* Faculty-to-Student Ratio

---

## 4. Country Comparison

### Purpose

Provides country- and region-level comparison of higher education performance.

### Key Analysis

* Country Ranking Comparison
* Education Performance Benchmarking
* Regional Education Trends
* Top Performing Countries

This dashboard helps compare educational performance between countries and regions using ranking, overall performance, research, and student-related metrics.

---

# 🔎 Dashboard Interactivity

The dashboards are designed to support interactive analysis through Tableau.

### Filters

Users can filter information using relevant dimensions such as:

* Country
* University

### Dashboard Navigation

Navigation controls allow users to move between:

* University Overview
* Research Analytics
* Student Analytics
* Country Comparison

### Dashboard Actions

Interactive chart selections and filters are used to explore related information across dashboard visualizations.

---

# 🧪 Testing & Validation

As part of the final project validation, the dashboards are checked for:

* KPI calculation accuracy.
* Ranking calculation accuracy.
* Correct aggregation of measures.
* Correct percentage representation.
* Correct totals, averages, and counts.
* Correct chart data.
* Filter functionality.
* Dashboard navigation.
* Dashboard interactions.
* Appropriate titles and labels.
* Appropriate units and legends.

The QA process is documented separately in the project testing documentation.

---

# 🛠️ Tools & Technologies

| Area                  | Tools / Technologies                  |
| --------------------- | ------------------------------------- |
| Data Collection       | Python, QS Rankings, THE Rankings     |
| Data Processing       | Pandas, NumPy                         |
| Data Cleaning         | Python / Pandas                       |
| Data Visualization    | Tableau Desktop                       |
| Dashboard Integration | Tableau Filters, Actions & Navigation |
| Version Control       | Git & GitHub                          |
| Documentation         | Markdown                              |

---

# 📁 Project Structure

```text
higher-education-dv/
│
├── data/
│
├── scripts/
|
│___ notebooks/
|
├── dashboard/
│   ├── development/
│   └── prototype/
│
├── docs/
│
└── README.md
```

The repository contains the project datasets, processing scripts, Tableau dashboards, prototype files, and project documentation.

---

# 📖 Documentation

Detailed project documentation covers:

* Dataset Sources
* KPI Definitions
* Dashboard Guide
* Education Analytics Methodology
* QA Testing and Validation

These documents provide additional information about the data, calculations, dashboards, and validation process.

---

# 🚀 Project Workflow Summary

```text
Collect
  ↓
Clean
  ↓
Merge
  ↓
Engineer KPIs
  ↓
Visualize
  ↓
Integrate
  ↓
Test
  ↓
Document
  ↓
Deliver
```

---

## 🔮 Future Scope

Potential future improvements include:

* Integration of regularly updated university datasets.
* Predictive analysis of university performance.
* AI-based university recommendations.
* Additional educational indicators.
* Deployment as a web-based analytics application.
* More advanced interactive analytics.

---

## 🎓 Project Purpose

EduVision_DV transforms raw higher education data into an interactive analytical platform that makes it easier to understand and compare **university performance, research performance, student metrics, and country-level education trends**.

---

## Author

Mansi Yadav

B.Tech Information Technology

Developed as part of the **Infosys Springboard Virtual Internship 7.0 - Higher Education Data Visualization project**.

---

## 📄 License

This project is developed for educational and academic purposes. Dataset ownership and attribution remain with their respective original sources.
