# 🎓 EduVision_DV – Higher Education Performance Dashboard

> **A comprehensive higher education analytics dashboard for analyzing university rankings, research performance, student diversity, academic excellence, and global education trends.**

## 📌 Project Overview

**EduVision_DV** is a higher education analytics project designed to transform publicly available university ranking and education datasets into meaningful, interactive insights.

The project integrates university ranking data from sources such as **QS World University Rankings** and **Times Higher Education World University Rankings**, followed by data cleaning, transformation, KPI engineering, and interactive dashboard development using **Tableau**.

The final solution consists of **four interconnected dashboards** that allow users to analyze university performance, research output, student diversity, and country-level education trends.

---

## 🎯 Project Objectives

* Collect and integrate global university ranking datasets.
* Clean and transform raw educational data.
* Develop meaningful higher education KPIs.
* Analyze university rankings and institutional performance.
* Evaluate research productivity and citation performance.
* Analyze international students and student diversity.
* Compare education performance across countries and regions.
* Build interactive Tableau dashboards with filters and drill-down capabilities.
* Provide portfolio-ready higher education analytics.

The project targets students, academic researchers, university administrators, policymakers, and education consultants who need data-driven insights into global higher education.

---

## 📊 Dashboard Suite

The project contains **four interconnected Tableau dashboards**:

### 1. 🏆 University Overview

Provides a high-level view of global university performance.

**Key analysis includes:**

* Top university rankings
* Global university distribution
* Academic reputation analysis
* University performance trends
* Institutional comparison
* Overall university performance KPIs

### 2. 🔬 Research Analytics

Focuses on research performance and institutional research impact.

**Key analysis includes:**

* Publications analysis
* Citation performance
* Research productivity trends
* Top research institutions
* Research impact comparison

### 3. 👨‍🎓 Student Analytics

Analyzes student population and diversity indicators.

**Key analysis includes:**

* International student analysis
* Faculty-to-student ratio
* Student diversity trends
* Enrollment comparisons
* Student distribution analysis

### 4. 🌎 Country Comparison

Provides country and regional benchmarking.

**Key analysis includes:**

* Country ranking comparison
* Education performance benchmarking
* Regional education trends
* Top-performing countries

These four dashboards are integrated using global filters, navigation controls, parameter actions, and dashboard linking.

---

## 📈 Key Performance Indicators (KPIs)

The project engineers several education-focused KPIs:

| KPI                                 | Purpose                                                |
| ----------------------------------- | ------------------------------------------------------ |
| 🌍 Global Ranking Score             | Measures overall global university ranking performance |
| 🔬 Research Impact Score            | Evaluates research impact                              |
| 👥 Faculty-to-Student Ratio         | Measures faculty availability relative to students     |
| 🌐 International Student Percentage | Measures international student representation          |
| ⭐ Academic Reputation Score         | Represents academic reputation                         |
| 📚 Research Productivity Index      | Measures research productivity                         |

The project specification requires **6+ KPIs** and emphasizes KPI accuracy and Tableau-ready data.

---

## 🔄 Project Workflow

```text
Collect University Datasets
          ↓
Data Cleaning & Transformation
          ↓
Education KPI Engineering
          ↓
Dashboard Development
          ↓
Dashboard Integration
          ↓
Testing & Validation
          ↓
Documentation & Delivery
```

This workflow follows the project's defined development process from data collection to final documentation and delivery.

---

## 🧹 Data Preparation

The data preparation stage includes:

* Removing duplicate records
* Standardizing university names
* Standardizing country names
* Normalizing ranking metrics
* Merging ranking datasets
* Creating Tableau-ready datasets
* Validating dataset completeness
* Handling missing values

The project specification targets **more than 95% dataset completeness** and **less than 2% missing values** after cleaning.

---

## 🛠️ Tech Stack

| Area                  | Technologies                                   |
| --------------------- | ---------------------------------------------- |
| Data Collection       | Python, QS Rankings, World University Rankings |
| Data Processing       | Pandas, NumPy                                  |
| Data Cleaning         | Python                                         |
| KPI Engineering       | Python                                         |
| Data Visualization    | Tableau Desktop / Tableau Public               |
| Dashboard Integration | Tableau Filters, Parameters, Actions           |
| Documentation         | Markdown, GitHub                               |

The technology stack follows the tools specified in the project document.

---

## 📁 Project Structure

```text
EduVision_DV/
│
├── data/
│   ├── university_raw_data.csv
│   ├── university_cleaned.csv
│   └── university_final_dataset.xlsx
│
├── scripts/
│   ├── data_collection.py
│   ├── education_cleaning.ipynb
│   └── generate_education_kpis.py
│
├── dashboard/
│   ├── EduVision_DV.twbx
│   └── eduvision_prototype.twbx
│
├── docs/
│   ├── dashboard_storyboard.pdf
│   ├── QA_Checklist
│   └── Dashboard_Testing_Report
│
└── README.md
```

The proposed project organization follows the structure specified in the documentation: `/scripts`, `/data`, `/dashboard`, and `/docs`.

---

## 🗂️ Data Sources

The project uses publicly available higher education datasets, including:

* **QS World University Rankings**
* **Times Higher Education World University Rankings**
* University performance indicators

The data collection stage includes downloading ranking datasets, collecting university performance indicators, and merging them into a common structure.

> **Note:** Add the exact dataset URLs or source references here if they are included in your final project files.

---

## 📊 Dashboard Features

The dashboards are designed with interactive functionality such as:

* 🔎 Global filters
* 📅 Year filtering
* 🌎 Region filtering
* 🏳️ Country filtering
* 📚 Subject-area filtering
* 🔄 Interactive comparisons
* 📌 Parameter actions
* 🧭 Dashboard navigation
* 🔗 Dashboard linking
* 📉 Drill-down analysis

The sample dashboard shown in the project document includes filters for **Year, Region, Country, and Subject Area**, along with KPI cards, ranking tables, trend analysis, regional distribution, publication analysis, international student analysis, and faculty-to-student ratio analysis.

---

## 🖼️ Dashboard Preview

### University Overview

> Add your final dashboard screenshot here.

```markdown
![EduVision Dashboard](docs/images/dashboard_overview.png)
```

You can replace the image path with the actual screenshot location in your repository.

---

## 🧪 Testing & Validation

The project includes a dedicated testing and validation phase covering:

* KPI calculation validation
* Ranking calculation verification
* Dashboard interaction testing
* Educational metric validation
* Overall dashboard functionality

The project specification targets **KPI accuracy above 95%** and no major dashboard issues before delivery.

---

## 📋 Project Milestones

| Milestone | Focus Area                 | Target                    |
| --------- | -------------------------- | ------------------------- |
| 1         | Data Collection & Cleaning | >95% Dataset Completeness |
| 2         | KPI Engineering            | 6+ KPIs Generated         |
| 3         | Dashboard Development      | 4 Integrated Dashboards   |
| 4         | Documentation & Delivery   | Portfolio Ready           |

These milestones are defined in the project's evaluation criteria.

---

## 🚀 Expected Outcomes

The completed project delivers:

* Integrated global university datasets
* Clean and transformed educational data
* Six or more education-focused KPIs
* Four interconnected Tableau dashboards
* University ranking and performance analysis
* Research performance analysis
* Student diversity analysis
* Country-level education benchmarking
* Interactive filtering and navigation
* A portfolio-ready analytics project

The final deliverable specified by the project is a unified Tableau workbook containing the four interconnected dashboards.

---

## 📦 Final Deliverables

```text
✓ Raw University Dataset
✓ Cleaned University Dataset
✓ Final KPI Dataset
✓ Data Collection Script
✓ Data Cleaning Notebook
✓ KPI Generation Script
✓ Dashboard Storyboard
✓ Tableau Prototype
✓ Final Tableau Workbook
✓ QA Checklist
✓ Dashboard Testing Report
✓ Project Documentation
```

---

## 💡 Key Insights

EduVision_DV helps users understand:

* Which universities perform best globally.
* How university performance changes over time.
* Which institutions demonstrate strong research impact.
* How publications and citations vary between institutions.
* How international student populations differ by region.
* How faculty-to-student ratios vary across regions.
* How countries compare in higher education performance.

---

## 🔮 Future Enhancements

Potential future improvements include:

* Adding more years of university ranking data.
* Integrating additional global ranking sources.
* Adding predictive university performance analysis.
* Expanding country-level benchmarking.
* Adding automated data refresh pipelines.
* Publishing the final dashboards through Tableau Public.
* Adding more advanced education analytics and trend forecasting.

> These are proposed enhancements and are not part of the documented core deliverables.

---

## 👨‍💻 Project

**Project Name:** EduVision_DV
**Domain:** Higher Education Analytics
**Primary Visualization Tool:** Power BI
**Data Processing:** Python, Pandas, NumPy
**Documentation:** Markdown / GitHub

---

## 📄 License

This project is intended for educational, analytical, and portfolio purposes.

Please review the licensing and usage terms of the original datasets before redistributing them.

---

## ⭐ Conclusion

**EduVision_DV** converts complex higher education and university ranking data into an interactive analytics solution. By combining data collection, cleaning, KPI engineering, and Tableau visualization, the project provides a unified platform for exploring university performance, research impact, student diversity, and country-level education trends.

---

**EduVision_DV — Turning Higher Education Data into Actionable Insights.** 🎓📊
