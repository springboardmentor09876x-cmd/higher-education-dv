# EduVision — KPI Definitions

## Purpose

This document defines the analytical KPIs generated and used in the EduVision project. The definitions follow the KPI terminology recorded in the project README and Module 3 workflow.

The implemented Power BI measures and KPI-generation workflow remain the authoritative calculation layer.

## KPI Catalogue

| KPI | Definition / Purpose | Dashboard Use |
|---|---|---|
| **Global Ranking Score** | Represents the ranking-oriented view of overall university performance. | University performance and comparison |
| **Research Impact Score** | Represents the research-impact dimension used for comparative analysis. | Research performance analysis |
| **Faculty-to-Student Ratio** | Represents the relationship between faculty/staff resources and students. | Student and institutional analysis |
| **International Student Percentage** | Represents the proportion of international students in the relevant student population. | Student diversity and internationalization |
| **Academic Reputation KPI** | Represents the academic-reputation dimension available in the project data. | University performance analysis |
| **Research Productivity Index** | Represents the engineered research-productivity measure used for comparison. | Research analytics |

## KPI Interpretation

### Global Ranking Score
Used to compare university-level performance within the selected report context and year.

### Research Impact Score
Used to analyze the impact dimension of research performance. It should be interpreted within the research-analysis context.

### Faculty-to-Student Ratio
Used to understand the relationship between students and faculty/staff resources. The displayed direction and aggregation follow the implemented dashboard measure.

### International Student Percentage
Used to compare the international composition of student populations across the selected university, country, region, or year context.

### Academic Reputation KPI
Used to analyze the academic-reputation component available in the underlying ranking data.

### Research Productivity Index
Used to support comparative analysis of research productivity based on the engineered KPI logic.

## KPI Governance Notes

- KPI names follow the terminology used throughout the EduVision project.
- KPI results depend on the active year, geography, university, and other report filters.
- Percentages, ratios, averages, and rankings must be interpreted at the intended aggregation level.
- The Power BI measures and Module 3 KPI-generation workflow are the authoritative implementation.
- If the underlying dataset or measure logic is changed, the affected KPI documentation and dashboard visuals should be revalidated.

## Dashboard Mapping

| Dashboard | Primary KPI Themes |
|---|---|
| University Overview | Global Ranking Score, Academic Reputation |
| Research Analytics | Research Impact Score, Research Productivity Index |
| Student Analytics | Faculty-to-Student Ratio, International Student Percentage |
| Country Comparison | Aggregated benchmarking using relevant ranking, research, and student indicators |
