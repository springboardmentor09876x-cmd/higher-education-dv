# EduVision_DV — Dashboard Testing Report

**Project:** EduVision_DV (Higher Education Performance Dashboard)
**Tool:** Power BI
**File Tested:** EduVision_DV.pbix
**Prepared by:** Adyasha Pattanaik, B.Tech Computer Science and Engineering

---

## 1. Scope

This report summarizes the testing carried out on the final EduVision_DV Power BI workbook, covering all 4 dashboards:

- University Overview
- Research Analytics
- Student Analytics
- Country Comparison

The workbook contains 4 interconnected pages with a total of 88 visuals and 24 KPI cards (6 per dashboard), built on the cleaned dataset `university_cleaned.csv`.

## 2. Testing Method

- KPI values were checked against the source dataset to confirm calculations are accurate.
- Ranking logic was verified by comparing the Top 10 university table against the source data.
- All filters (Year, Region, Country, Subject Area) were tested individually and in combination.
- Cross-page filter synchronization was tested by changing a filter on one page and confirming it applied on the others.
- Every chart, table, and KPI card was reviewed for correct labeling and accurate data display.
- Navigation between all 4 dashboard pages was tested.

## 3. Results

| Area | Result |
| --- | --- |
| KPI calculations | Verified correct |
| Ranking calculations | Verified correct |
| Dashboard interactions (filters, navigation) | Working as expected |
| Educational metrics (publications, citations, students, faculty ratios) | Verified correct |
| Cross-page filter sync | Working correctly |
| Chart labeling and formatting | Correct and consistent |

**KPI Accuracy:** Above 95%, meeting the project target.

**Major Issues Found:** None.

## 4. Conclusion

The EduVision_DV dashboard suite has been tested end-to-end and meets the project's evaluation criteria — all KPIs are accurate, dashboard interactions function correctly, and the four dashboards work together as a unified, interactive Power BI workbook. The project is ready for final delivery.
