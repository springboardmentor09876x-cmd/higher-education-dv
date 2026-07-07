# EduVision DV — Higher Education Performance Dashboard

Author : PURBASA BHADURI 


A Tableau-based analytics suite for evaluating global university rankings, research performance, student diversity, and cross-country education trends, built from publicly available datasets including the QS World University Rankings and the Times Higher Education World University Rankings.

## Overview

EduVision_DV consolidates multi-source higher education data into a single, unified Tableau workbook (`.twbx`) containing four interconnected dashboards. It is intended to support students, researchers, university administrators, policymakers, and education consultants in evaluating institutional performance, comparing universities globally, and identifying trends in higher education.

## Dashboards

| Dashboard | Description |
|---|---|
| University Overview | Global rankings, score trends, regional distribution, and academic reputation analysis |
| Research Analytics | Publication counts, citation performance, research productivity, and top research institutions |
| Student Analytics | International student percentage, faculty-to-student ratio, diversity trends, and enrollment comparisons |
| Country Comparison | Country-level rankings, benchmarking, and regional education trends |

All dashboards share a common set of filters (Year, Region, Country, Subject Area) and are linked through navigation actions and parameters.

## Key Performance Indicators

The following KPIs were engineered as part of this project:

- Global Ranking Score
- Research Impact Score
- Faculty-to-Student Ratio
- International Student Percentage
- Academic Reputation Score
- Research Productivity Index

## Tech Stack

| Area | Tools / Libraries |
|---|---|
| Data Collection | Python, QS Rankings, World University Rankings |
| Data Processing | Pandas, NumPy |
| Data Cleaning | Python |
| Visualization | Tableau Desktop / Tableau Public |
| Dashboard Integration | Tableau Filters, Parameters, Actions |
| Documentation | Markdown, GitHub |

## Project Structure

```
EduVision_DV/
├── scripts/       Data collection and KPI generation scripts
├── data/          Raw and cleaned datasets
├── dashboard/     Tableau workbook(s)
└── docs/          Documentation and methodology
```

## Workflow

```
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

## Data Sources

- QS World University Rankings
- Times Higher Education World University Rankings
