# EduVision — KPI Definitions

## 1. Overview

This document defines the key performance indicators used in the **EduVision — Higher Education Performance Dashboard**.

The KPIs are designed to measure university ranking performance, academic reputation, research impact, student diversity, faculty availability, and research productivity.

---

## 2. KPI Summary

| KPI                              | Category               | Purpose                                            |
| -------------------------------- | ---------------------- | -------------------------------------------------- |
| Global Ranking Score             | University Performance | Measures overall university ranking performance    |
| Research Impact Score            | Research               | Measures institutional research influence          |
| Faculty-to-Student Ratio         | Student & Faculty      | Measures faculty availability relative to students |
| International Student Percentage | Student Diversity      | Measures international student representation      |
| Academic Reputation Score        | Academic Performance   | Measures academic reputation                       |
| Research Productivity Index      | Research               | Measures research output and productivity          |

---

## 3. KPI Definitions

### KPI-01 — Global Ranking Score

**Definition:**
The Global Ranking Score represents the overall performance of a university based on its ranking-related performance indicators.

**Purpose:**
Used to compare universities and identify institutions with stronger overall global performance.

**Category:** University Performance

**Interpretation:**
A stronger score indicates better overall performance according to the selected ranking methodology.

**Used In:**

* University Overview
* Country Comparison

---

### KPI-02 — Research Impact Score

**Definition:**
The Research Impact Score represents the influence and effectiveness of an institution's research output using relevant research indicators.

**Purpose:**
Used to identify universities with strong research influence and impact.

**Category:** Research Performance

**Interpretation:**
A higher score indicates stronger research impact.

**Used In:**

* Research Analytics
* University Overview
* Country Comparison

---

### KPI-03 — Faculty-to-Student Ratio

**Definition:**
The Faculty-to-Student Ratio measures the number of students relative to the available faculty members.

**Formula:**

```text
Faculty-to-Student Ratio =
Total Students / Faculty Count
```

**Purpose:**
Used to understand faculty availability in relation to the student population.

**Interpretation:**
A lower ratio generally indicates fewer students per faculty member, while a higher ratio indicates more students per faculty member.

**Used In:**

* Student Analytics
* University Overview
* Country Comparison

---

### KPI-04 — International Student Percentage

**Definition:**
International Student Percentage measures the proportion of international students within the total student population.

**Formula:**

```text
International Student Percentage =
(International Students / Total Students) × 100
```

**Purpose:**
Used to evaluate the international diversity and global attractiveness of universities.

**Interpretation:**
A higher percentage indicates greater international student representation.

**Used In:**

* Student Analytics
* University Overview
* Country Comparison

---

### KPI-05 — Academic Reputation Score

**Definition:**
The Academic Reputation Score represents the academic standing and reputation of a university according to the selected ranking dataset.

**Purpose:**
Used to compare the perceived academic strength of universities.

**Category:** Academic Performance

**Interpretation:**
A higher score indicates stronger academic reputation.

**Used In:**

* University Overview
* Research Analytics
* Country Comparison

---

### KPI-06 — Research Productivity Index

**Definition:**
The Research Productivity Index measures the productivity of an institution in terms of its research output and related research indicators.

**Purpose:**
Used to compare research productivity across universities, countries, and regions.

**Category:** Research Performance

**Interpretation:**
A higher index indicates stronger research productivity.

**Used In:**

* Research Analytics
* Country Comparison

---

## 4. KPI Usage Across Dashboards

| KPI                              | University Overview | Research Analytics | Student Analytics | Country Comparison |
| -------------------------------- | :-----------------: | :----------------: | :---------------: | :----------------: |
| Global Ranking Score             |          ✅          |          —         |         —         |          ✅         |
| Research Impact Score            |          ✅          |          ✅         |         —         |          ✅         |
| Faculty-to-Student Ratio         |          ✅          |          —         |         ✅         |          ✅         |
| International Student Percentage |          ✅          |          —         |         ✅         |          ✅         |
| Academic Reputation Score        |          ✅          |          ✅         |         —         |          ✅         |
| Research Productivity Index      |          —          |          ✅         |         —         |          ✅         |

---

## 5. KPI Validation

Each KPI should be validated against the underlying dataset before final dashboard delivery.

Validation includes:

* Checking source fields
* Verifying calculation logic
* Comparing calculated values with dashboard values
* Checking percentage and ratio calculations
* Confirming correct aggregation
* Testing KPI behavior under filters
* Checking values across different years
* Validating country and regional results

---

## 6. KPI Filtering Behavior

The KPI values are designed to respond to relevant dashboard filters.

Common filters include:

* **Year**
* **Region**
* **Country**
* **University**
* **Subject Area**

When a filter is applied, the relevant KPI should update according to the selected data context.

---

## 7. KPI Interpretation Guidelines

KPI values should always be interpreted within the context of the selected:

* Year
* University
* Country
* Region
* Dataset
* Ranking methodology

Different ranking sources may use different methodologies and scoring systems. Therefore, KPI comparisons should be made using consistent source data and definitions.

---

## 8. KPI Quality Requirements

The EduVision project follows these KPI quality objectives:

* KPI calculations should be accurate.
* KPI formulas should be clearly documented.
* KPI values should match the underlying dataset.
* KPIs should respond correctly to dashboard filters.
* Numerical and percentage formatting should be consistent.
* KPI labels should be clear and understandable.
* KPI values should not contain invalid or unexpected results.

---

## 9. Conclusion

The six KPIs defined in this document provide the analytical foundation for the **EduVision Higher Education Performance Dashboard**.

Together, they enable users to evaluate:

* Overall university performance
* Academic reputation
* Research impact
* Research productivity
* Faculty availability
* International student diversity

These KPIs support interactive analysis across universities, countries, regions, and years, helping transform higher education data into meaningful and actionable insights.
