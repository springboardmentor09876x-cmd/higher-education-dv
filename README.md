# 🎓 Higher Education Performance Dashboard

> Infosys Springboard EduVision_DV Internship Project

---

## 👨‍💻 Intern

**Name:** GURU-SASANK

**Internship:** Infosys Springboard Virtual Internship 7.0

---

## 📖 Project Overview

This project aims to integrate, clean, analyze, and visualize global higher education ranking datasets from multiple sources (QS, THE, and Research datasets). The final outcome is an interactive Power BI dashboard that enables meaningful comparison of universities, countries, and academic performance across the years 2017–2026.

---

## 🚀 Current Progress

### ✅ Module 1 – Dataset Preparation

- Collected QS, THE and Research datasets
- Generated QS, THE and Research master datasets
- Merged datasets into a unified master dataset
- Standardized schema across ranking systems
- Recovered university and geographic information
- Generated `university_raw_data.csv`

### ✅ Module 2 – Data Cleaning & Preprocessing

- Performed missing value analysis
- Applied rule-based data recovery
- Applied statistical and iterative imputation
- Applied Random Forest–based imputation for selected missing values
- Recovered metadata across university records
- Achieved **99.82% dataset completeness**
- Generated `university_cleaned.csv`

---

## 📊 Final Dataset Summary

| Metric | Value |
|---------|------:|
| Rows | 23,263 |
| Columns | 36 |
| Missing Values | 1,504 |
| Missing Percentage | 0.18% |
| Completeness | **99.82%** |

---

## 📂 Project Structure

```text
higher-education-dv/
│
├── datasets/
│   ├── raw/
│   │   ├── qs/
│   │   ├── the/
│   │   └── research/
│   │
│   └── final/
│       ├── intermediate/
│       │   ├── qs_master.csv
│       │   ├── the_master.csv
│       │   ├── research_master.csv
│       │   ├── education_master.csv
│       │   └── master_dataset.csv
│       │
│       ├── Module_1_Deliverables/
│       │   └── university_raw_data.csv
│       │
│       └── Module_2_Deliverables/
│           └── university_cleaned.csv
│
├── notebooks/
│   ├── module1_dataset_preparation.ipynb
│   └── education_data_quality_enhancement.ipynb
│
├── scripts/
│
├── powerbi/
│
└── README.md
```
---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- Power BI
- Git
- GitHub

---

## 📅 Upcoming Modules

- 📊 Module 3 – Exploratory Data Analysis
- 📈 Module 4 – Dashboard Development
- 🎯 Module 5 – Final Dashboard & Insights

---

## 📌 Status

🟢 **Modules 1 & 2 Completed Successfully**

Current Progress:
- Dataset Integration ✅
- Dataset Preparation ✅
- Data Quality Enhancement ✅
- Power BI Dashboard ⏳

## 📊 Progress

| Module | Status |
|---------|--------|
| Module 1 – Dataset Preparation | ✅ Completed |
| Module 2 – Data Cleaning & Preprocessing | ✅ Completed |
| Module 3 – Exploratory Data Analysis | ⏳ Pending |
| Module 4 – Dashboard Development | ⏳ Pending |
| Module 5 – Final Dashboard & Insights | ⏳ Pending |

---

## 📦 Deliverables

### Module 1

- `scripts/`
- `module1_dataset_preparation.ipynb`
- `university_raw_data.csv`

### Module 2

- `education_data_quality_enhancement.ipynb`
- `university_cleaned.csv`

---

## 📌 Repository Updates

This repository is actively maintained as part of the Infosys Springboard EduVision_DV Internship. Additional modules, Power BI dashboards, and analytical insights will be added as the project progresses.