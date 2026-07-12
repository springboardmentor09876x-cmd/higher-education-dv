# 🎓 Higher Education Data Cleaning & Preparation

## 📌 Project Overview
This repository contains the data cleaning pipeline for the **"Top 1000 Universities (2020-2026)"** dataset. The goal of this script is to clean, standardize, and prepare the raw data for advanced Data Visualization (Tableau/Power BI) and statistical analysis.

## 🗂️ Dataset Information
* **Original Dataset:** `top_1000_universities_2020_2026_.csv` (7,000 rows, 38 columns)
* **Cleaned Dataset:** `cleaned_top_1000_universities.csv` (6,915 rows, 37 columns)
* **Key Features:** University rankings, country, academic reputation, international student ratio, faculty-to-student ratio, etc.

## 🛠️ Data Cleaning Process (datacleaning.py)
The Python script (`pandas`) performs the following critical data quality improvements:

1. **Removed Redundant Data:** 
   * Dropped the corrupted `gender_ratio` column (which had spreadsheet time-formatting errors like `63:37:00`) because accurate `female_percentage` and `male_percentage` columns already exist.
2. **Handled Missing & Tied Rankings:** 
   * Removed ~1% of rows with completely missing rank data.
   * **Crucial Step:** Kept `world_rank` and `national_rank` as decimals (`float`) to accurately preserve ranking ties (e.g., multiple universities correctly sharing a rank of `725.5`).
3. **Outlier Removal:** 
   * Filtered out extreme and impossible anomalies in the `faculty_to_student_ratio` (capped at maximum 200).
4. **Text Standardization:** 
   * Applied `.str.strip()` across all categorical/text columns to remove hidden trailing and leading whitespaces, ensuring accurate grouping for visualizations.


