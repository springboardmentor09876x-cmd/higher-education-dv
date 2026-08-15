Higher Education Data Visualization (DV) Project

📌 Project Overview

The **Higher Education Data Visualization (DV) Project** is an internship project focused on collecting, integrating, cleaning, analyzing, and visualizing higher education data from multiple global university ranking sources.

The project aims to create a **unified and reliable higher education dataset** that can be used to analyze university rankings, academic performance, research capabilities, student diversity, and global education trends.

The project follows a structured data pipeline:

**Data Collection → Data Integration → Data Cleaning → Data Analysis → Data Visualization**

The final processed dataset is intended to serve as the foundation for an interactive **Higher Education Dashboard** that enables users to explore and compare universities across different dimensions.

---

## 🎯 Objectives

The major objectives of this project are:

* To collect higher education and university ranking data from multiple reliable datasets.
* To integrate data from different ranking systems into a unified dataset.
* To clean and preprocess the collected data for further analysis.
* To handle missing, inconsistent, and duplicate values.
* To generate a standardized dataset containing important university-level attributes.
* To analyze university rankings, academic excellence, research performance, and student diversity.
* To identify global higher education trends using historical ranking data.
* To prepare the processed data for visualization and dashboard development.
* To provide meaningful insights that can support comparison and analysis of universities worldwide.

---

## 📊 Dataset Sources

The project uses data from multiple university ranking datasets to provide broader coverage and improve the analytical value of the final dataset.

The major datasets used are:

### 1. QS World University Rankings 2025

Contains information related to universities appearing in the QS World University Rankings, including ranking and academic-related indicators.

**File:**

```text
qs_rankings_2025.csv
```

---

### 2. Times Higher Education (THE) World University Rankings
Contains historical university ranking information covering multiple years.
**File:**
```text
THE World University Rankings 2016-2026.csv
```
This dataset is particularly useful for studying changes in university performance over time and identifying global education trends.
---

### 3. Center for World University Rankings (CWUR)

Contains university ranking and performance information from the Center for World University Rankings.

**File:**

```text
cwurData.csv
```

---

### 4. Times World University Rankings Dataset

Contains university-level ranking information and associated indicators.

**File:**

```text
timesData.csv
```

---

### 5. Academic Ranking of World Universities (Shanghai Ranking)

Contains university ranking information based on academic and research-oriented indicators.

**File:**

```text
shanghaiData.csv
```

---

### 6. University School and Country Dataset

Provides additional information connecting universities with their respective countries and geographical information.

**File:**

```text
school_and_country_table.csv
```

---

## 🗂️ Project Structure

```text
higher-education-dv/
│
├── data/
│   ├── raw/
│   │   ├── qs_rankings_2025.csv
│   │   ├── THE World University Rankings 2016-2026.csv
│   │   ├── cwurData.csv
│   │   ├── timesData.csv
│   │   ├── shanghaiData.csv
│   │   └── school_and_country_table.csv
│   │
│   └── processed/
│       ├── university_raw_data.csv
│       └── EduVision_Cleaned_Dataset.csv
│
├── scripts/
│   ├── data_collection.py
│   ├── data_collection_merge.py
│   └── data_cleaning.py
│
├── README.md
└── requirements.txt
```

> The exact folder contents may change as additional modules and dashboard components are developed.

---

# 🔄 Data Processing Pipeline

## 1. Data Collection

The first stage involves collecting and organizing university ranking datasets from different sources.

The collected datasets contain different:

* University names
* Rankings
* Countries
* Academic indicators
* Research indicators
* Student-related information
* Historical ranking information

Because the datasets originate from different sources, their structures and column names are not identical.

---

## 2. Data Integration

The datasets are integrated into a common structure using Python.

The integration process includes:

* Reading individual CSV files.
* Identifying relevant columns.
* Standardizing column names.
* Mapping equivalent fields between datasets.
* Combining information from different ranking systems.
* Generating consistent university identifiers.
* Preserving important information from each source.

The main integration script is:

```text
scripts/data_collection_merge.py
```

The goal is to create a consolidated raw dataset that provides a common structure for subsequent processing.

---

## 3. Data Cleaning

The integrated dataset is then cleaned and prepared for analysis.

The cleaning process includes:

* Handling missing values.
* Removing completely empty records.
* Removing unnecessary columns.
* Standardizing text values.
* Handling duplicate records.
* Correcting inconsistent university and country names.
* Converting values into appropriate data types.
* Validating the final dataset.
* Ensuring that required fields are populated.

The cleaning script is:

```text
scripts/data_cleaning.py
```

The resulting dataset is used as the primary input for analysis and visualization.

---

# 🧩 Major Data Categories

The final dataset is designed to support analysis across several major higher education dimensions.

### 🏆 University Rankings

Information related to the ranking position of universities across different ranking systems and years.

### 🔬 Research Performance

Indicators associated with university research output, research quality, citations, and academic impact.

### 🎓 Academic Excellence

Data related to academic reputation, teaching performance, faculty quality, and other academic indicators.

### 🌎 Student Diversity

Information that can be used to understand international representation and diversity within universities.

### 📈 Global Education Trends

Historical ranking information that can be used to identify changes and trends in global higher education.

### 📊 Research Analytics

Research-focused indicators that allow universities and regions to be compared based on research performance.

---

# 🛠️ Technologies Used

The project primarily uses Python-based data processing and visualization technologies.

| Technology               | Purpose                        |
| ------------------------ | ------------------------------ |
| Python                   | Data processing and analysis   |
| Pandas                   | Data manipulation and cleaning |
| NumPy                    | Numerical operations           |
| Matplotlib               | Data visualization             |
| Seaborn                  | Statistical visualization      |
| CSV                      | Dataset storage and exchange   |
| Git                      | Version control                |
| GitHub                   | Repository and collaboration   |
| Data Visualization Tools | Dashboard development          |

Additional technologies may be incorporated during later stages of the project.

---

# 🐍 Python Data Processing

The project uses Python scripts to automate the data pipeline rather than manually modifying datasets.

The general workflow is:

```text
Raw CSV Files
     ↓
Data Collection
     ↓
Column Mapping & Standardization
     ↓
Dataset Integration
     ↓
Raw Consolidated Dataset
     ↓
Data Cleaning
     ↓
Cleaned Dataset
     ↓
Exploratory Data Analysis
     ↓
Visualization
     ↓
Higher Education Dashboard
```

---

# 📁 Important Scripts

## `data_collection.py`

Responsible for processing and preparing the individual source datasets before integration.

---

## `data_collection_merge.py`

Responsible for combining the different university ranking datasets into a unified raw dataset.

Major operations include:

* Loading source datasets.
* Mapping source-specific columns.
* Standardizing university information.
* Generating university identifiers.
* Merging datasets.
* Removing completely empty records.
* Exporting the consolidated dataset.

---

## `data_cleaning.py`

Responsible for preparing the consolidated dataset for analysis.

Major operations include:

* Missing-value handling.
* Duplicate removal.
* Data type conversion.
* Text standardization.
* Column validation.
* Dataset quality checks.
* Exporting the cleaned dataset.

---

# 📦 Output Datasets

## Raw Dataset

The integrated raw dataset contains information collected and merged from the different university ranking sources.

```text
data/processed/university_raw_data.csv
```

This dataset represents the output of the data collection and integration stage.

---

## Cleaned Dataset

The cleaned dataset is the processed version of the raw dataset and is intended for analysis and visualization.

```text
data/processed/EduVision_Cleaned_Dataset.csv
```

The cleaned dataset is designed to minimize missing and inconsistent values and provide a standardized structure for dashboard development.

---

# 📈 Data Visualization and Dashboard

The processed dataset will be used to develop visualizations that make complex higher education data easier to understand.

Potential dashboard components include:

### University Ranking Analysis

* Top-ranked universities
* Ranking comparison
* Ranking distribution
* University-wise performance

### Country Analysis

* Number of ranked universities by country
* Country-wise ranking performance
* Regional comparisons

### Research Analysis

* Research performance comparison
* Research strength by university
* Research trends over time

### Academic Analysis

* Academic performance
* Teaching-related indicators
* Academic reputation comparisons

### Historical Trends

* University ranking changes across years
* Country-level ranking trends
* Global higher education trends

### Diversity Analysis

* International representation
* Student diversity comparisons
* Country and university diversity patterns

---

# 🔍 Expected Insights

The project can be used to answer questions such as:

* Which universities consistently perform well across ranking systems?
* Which countries have the highest number of highly ranked universities?
* How have university rankings changed over time?
* Which universities demonstrate strong research performance?
* How does academic performance differ between universities?
* Which regions are emerging in global higher education?
* How does student diversity vary between universities?
* Are there universities that perform differently across different ranking systems?

---

# ✅ Data Quality Goals

The processed dataset is expected to maintain a high level of data quality.

The major quality requirements include:

* Consistent column names.
* Standardized university names.
* Standardized country names.
* Appropriate data types.
* Removal of unnecessary duplicate records.
* Handling of missing values.
* Removal of completely empty rows.
* Validation of important fields.
* Consistent university identifiers.
* Reliable integration of information from multiple sources.

---

# 🔀 Git and GitHub Workflow

GitHub is used for version control and collaborative development.

The project repository is maintained as a shared repository where individual contributors work through separate branches.

The general workflow is:

```bash
git checkout main
git pull origin main
git checkout -b <branch-name>
```

After making changes:

```bash
git add .
git commit -m "Add data processing changes"
git push -u origin <branch-name>
```

Changes can then be reviewed and merged into the main project branch.

---

# 🚀 How to Run the Project

## 1. Clone the Repository

```bash
git clone <repository-url>
cd higher-education-dv
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If a requirements file is not available, the primary packages can be installed using:

```bash
pip install pandas numpy matplotlib seaborn
```

---

## 4. Run Data Collection

```bash
python scripts/data_collection.py
```

---

## 5. Run Data Integration

```bash
python scripts/data_collection_merge.py
```

This generates the consolidated raw dataset.

---

## 6. Run Data Cleaning

```bash
python scripts/data_cleaning.py
```

This generates the cleaned dataset for analysis and visualization.

---

# 📋 Project Deliverables

The project follows a modular development approach.

### Module 1 — Data Collection and Integration

Deliverables:

* Raw source datasets
* Data collection Python script
* Dataset integration/merging script
* Consolidated raw dataset

### Module 2 — Data Cleaning

Deliverables:

* Data cleaning Python script
* Cleaned and standardized dataset
* Data quality validation

### Subsequent Modules

The processed dataset can be used for:

* Exploratory Data Analysis
* Data visualization
* Dashboard development
* Insight generation
* Final project presentation and documentation

---

# 🌟 Project Outcome

The final objective of the project is to transform multiple heterogeneous university ranking datasets into a **clean, structured, and analysis-ready higher education dataset**.

The resulting data pipeline provides a foundation for an interactive dashboard capable of presenting university rankings, academic excellence, research performance, student diversity, and global education trends in an intuitive and meaningful manner.

This project demonstrates practical applications of:

* Data Collection
* Data Integration
* Data Cleaning
* Data Preprocessing
* Exploratory Data Analysis
* Data Visualization
* Version Control
* Dashboard Development

---

# 👩‍💻 Internship Project

**Project:** Higher Education Data Visualization (DV)

**Organization:** Infosys

**Project Domain:** Data Science / Data Analytics / Data Visualization

**Repository:** Higher Education DV Project

**Primary Language:** Python

---

## 📌 Future Enhancements

Future development can include:

* Interactive dashboard implementation.
* Advanced exploratory data analysis.
* Additional ranking datasets.
* Automated data ingestion.
* Advanced statistical analysis.
* Interactive university comparison.
* Country and regional filtering.
* Historical trend visualization.
* Improved data validation and monitoring.
* Automated end-to-end data pipelines.

---

## 📄 License

This project is developed as part of an internship/project-based learning initiative. Dataset ownership and usage rights remain subject to the respective original data sources and their applicable terms.

---

## 🙏 Acknowledgements

The project makes use of publicly available university ranking datasets and is developed as part of the **Infosys Higher Education Data Visualization internship project**.

Special thanks to the project mentors and contributors for their guidance, collaboration, and support throughout the development of the project.
