# Dashboard Testing Report

## 1. Project Overview

The **University Ranking Analytics Dashboard** is an interactive Power BI dashboard developed to analyze university rankings, academic performance, research productivity, student-related metrics, and country-wise university information.

The dashboard provides KPIs, charts, tables, maps, rankings, and interactive filters for analyzing university performance.

## 2. Testing Objective

The objective of dashboard testing is to verify:

- KPI calculations
- Ranking calculations
- Dashboard filters and interactions
- Educational metrics
- Correct response of dashboard visuals to user selections

## 3. Dashboards Tested

| Dashboard | Testing Area |
|---|---|
| **University Overview** | KPI, ranking and filter validation |
| **Country Comparison** | Country ranking validation |
| **Research Analytics** | Research metric and ranking validation |
| **Student Analytics** | Student-related metric validation |

## 4. KPI Validation

KPI values were checked against their corresponding dashboard calculations.

| Category | Total Tests | Passed | Failed |
|---|---:|---:|---:|
| KPI Validation | 19 | 19 | 0 |

**Result:** All KPI validation tests passed successfully.

## 5. Ranking Validation

| Test ID | Test Case | Status |
|---|---|---|
| **RANK-01** | Top 10 Universities | PASS |
| **RANK-02** | Top 10 Research Institutions | PASS |
| **RANK-03** | Top 10 Performing Countries | PASS |
| **RANK-04** | Country Ranking Comparison | PASS |

**Result:** All ranking tests passed successfully.

## 6. Dashboard Interaction Testing

| Test ID | Test Case | Actual Result | Status |
|---|---|---|---|
| **INT-01** | Country Slicer | Selecting a country updated the dashboard visuals correctly. | PASS |
| **INT-02** | Year Slicer | Selecting a year updated the relevant dashboard data. | PASS |
| **INT-03** | University Slicer | Selecting a university filtered the dashboard correctly. | PASS |
| **INT-04** | Chart-to-Chart Interaction | Related visuals responded to the selected chart element. | PASS |
| **INT-05** | Multiple Filters | Multiple filters worked together correctly. | PASS |

**Result:** All dashboard interaction tests passed successfully.

## 7. Educational Metrics Validation

| Test ID | Metric | Actual Result | Status |
|---|---|---:|---|
| **MET-01** | Average International Student Ratio | 49.34 | PASS |
| **MET-02** | Average Academic Reputation | 31.04 | PASS |
| **MET-03** | Average Faculty Student Ratio | 13.27 | PASS |
| **MET-04** | Average Research Productivity | 3.37 | PASS |

**Result:** All educational metric tests passed successfully.

## 8. Overall Test Summary

| Testing Category | Total | Passed | Failed |
|---|---:|---:|---:|
| KPI Validation | 19 | 19 | 0 |
| Ranking Validation | 4 | 4 | 0 |
| Dashboard Interaction | 5 | 5 | 0 |
| Educational Metrics | 4 | 4 | 0 |
| **Total** | **32** | **32** | **0** |

**Overall Result:** 32 test cases passed and 0 test cases failed.

## 9. Conclusion

The **University Ranking Analytics Dashboard** was tested for KPI accuracy, ranking accuracy, dashboard interactions, and educational metrics. All **32 completed test cases passed successfully**, demonstrating that the tested dashboard components functioned as expected.
