# QA Checklist - EduVision DV


## 1. Data Quality Checks

These checks make sure the final dataset is clean and ready for Tableau.

| # | Check | Status | Comments |
|---|-------|--------|----------|
| 1.1 | Missing values in `university_name` column are zero | | Should be 0 NaN university names |
| 1.2 | Missing values across all columns are below 2% | | Target: <2% overall. Final result was 0.0% (135 cells out of ~680,000) |
| 1.3 | No exact duplicate rows in the final dataset | | Checked with `df.duplicated().sum()` |
| 1.4 | No duplicate university-year combinations that should be unique | | Same university should not appear twice for the same year from the same source |
| 1.5 | University names are standardized (no trailing spaces, consistent casing) | | Lowercase normalization was applied during cleaning |
| 1.6 | Country names are consistent across all records | | 134 unique countries. No variants like "USA" vs "United States" |
| 1.7 | Region column values are valid (no blank or unexpected region names) | | Regions should be: North America, Europe, Asia, etc. |
| 1.8 | Year values are within expected range (2020-2024) | | No years outside this range should exist |
| 1.9 | Numeric columns do not contain text or special characters | | Columns like `gdp_per_capita`, `h_index` should be pure numeric |
| 1.10 | `total_fte_students` has no comma formatting left from source data | | Was "34,002" in raw, should be 34002.0 in final |
| 1.11 | `international_students_pct` has no "%" signs | | Was "33.5%" in raw, should be 33.5 in final |
| 1.12 | `female_pct` is parsed from ratio format and is between 0-100 | | Was "1.2:1" ratio, now a percentage |

---

## 2. KPI Validation

These checks verify that the six engineered KPIs are calculated correctly.

| # | Check | Status | Comments |
|---|-------|--------|----------|
| 2.1 | `global_ranking_score` is between 0 and 100 | | Formula: 0.6 * qs_overall_score + 0.4 * the_overall_score, normalized |
| 2.2 | `global_ranking_score` is null only when both QS and THE scores are missing | | If one source is available, score should still be calculated |
| 2.3 | `research_impact_score` is between 0 and 100 | | Formula: 0.4 * citations_per_faculty + 0.35 * the_research_quality + 0.25 * the_research_environment |
| 2.4 | `research_impact_score` favors universities with high citations AND strong research environment | | Should not be high if only one component is strong |
| 2.5 | `faculty_student_ratio` matches `students_per_staff` value | | These should be identical - direct passthrough |
| 2.6 | `international_student_percentage` matches `international_students_pct` value | | These should be identical - direct passthrough |
| 2.7 | `academic_reputation_score` matches `qs_academic_reputation` value | | These should be identical - direct passthrough |
| 2.8 | `research_productivity_index` is between 0 and 100 | | Geometric mean of normalized publications, citations, h-index |
| 2.9 | `research_productivity_index` penalizes universities weak in any one dimension | | Geometric mean should ensure balanced performance is rewarded |
| 2.10 | Pick 5 random universities and manually verify KPI values against source columns | | Cross-check with QS/THE raw files for sample universities |

---

## 3. Dashboard Testing

Test each of the four dashboards in Tableau. Open `eduvision_prototype_final.twbx` and check each tab.

### 3.1 Overview Dashboard

| # | Check | Status | Comments |
|---|-------|--------|----------|
| 3.1.1 | Dashboard loads without errors | | Should open in Tableau Desktop or Tableau Public |
| 3.1.2 | Global Ranking Score is displayed for universities | | Should show ranked list or bar chart |
| 3.1.3 | Academic Reputation Score is visible | | Should be one of the main visual elements |
| 3.1.4 | University names display correctly (no truncation or encoding issues) | | Check for special characters in names |
| 3.1.5 | Year-over-year trend is visible when a university is selected | | Should show how ranking changes across 2020-2024 |
| 3.1.6 | Summary statistics show correct counts (universities, countries) | | Should match dataset totals |

### 3.2 Research Dashboard

| # | Check | Status | Comments |
|---|-------|--------|----------|
| 3.2.1 | Dashboard loads without errors | | |
| 3.2.2 | Research Impact Score is displayed | | Should show comparative bars or rankings |
| 3.2.3 | Publication count and citation metrics are visible | | These come from OpenAlex data |
| 3.2.4 | H-index values display correctly | | Should be numeric, no null issues |
| 3.2.5 | Research Productivity Index is shown | | Should combine publications, citations, and h-index |
| 3.2.6 | Country-level research comparison works | | Should be able to compare research output between countries |

### 3.3 Country Dashboard

| # | Check | Status | Comments |
|---|-------|--------|----------|
| 3.3.1 | Dashboard loads without errors | | |
| 3.3.2 | GDP per capita is displayed per country | | From World Bank data |
| 3.3.3 | Education expenditure (% of GDP) shows correctly | | From World Bank data |
| 3.3.4 | Tertiary enrollment rate is visible | | From World Bank data |
| 3.3.5 | Literacy rate displays per country | | From World Bank data |
| 3.3.6 | Number of ranked universities per country is shown | | Should match `country_universities_ranked` column |
| 3.3.7 | GDP vs. university ranking scatter plot loads | | Should show correlation between wealth and ranking |

### 3.4 Student Dashboard

| # | Check | Status | Comments |
|---|-------|--------|----------|
| 3.4.1 | Dashboard loads without errors | | |
| 3.4.2 | Faculty-to-student ratio is displayed | | Should show comparison across universities |
| 3.4.3 | International student percentage is visible | | Should show distribution or rankings |
| 3.4.4 | Gender balance (female percentage) is shown | | Should be between 0-100% |
| 3.4.5 | Student demographics vary correctly by country/region | | Should not show same values for all countries |

---

## 4. Filter Testing

Test that all filters work correctly across dashboards.

| # | Check | Status | Comments |
|---|-------|--------|----------|
| 4.1 | Year filter (2020-2024) works on Overview Dashboard | | Should update all visuals when year is changed |
| 4.2 | Year filter works on Research Dashboard | | |
| 4.3 | Year filter works on Country Dashboard | | |
| 4.4 | Year filter works on Student Dashboard | | |
| 4.5 | Country filter works on Overview Dashboard | | Should show only universities from selected country |
| 4.6 | Country filter works on Research Dashboard | | |
| 4.7 | Country filter works on Student Dashboard | | |
| 4.8 | Region filter works on Overview Dashboard | | Should show universities from selected region |
| 4.9 | Region filter works on Research Dashboard | | |
| 4.10 | Region filter works on Country Dashboard | | |
| 4.11 | Region filter works on Student Dashboard | | |
| 4.12 | Multiple filters can be applied at the same time | | e.g., Year = 2023 AND Country = United States |
| 4.13 | Filters reset correctly when cleared | | All visuals should return to full dataset view |
| 4.14 | Filter actions between charts work (if applicable) | | Clicking a bar should highlight related data |

---

## 5. Visualization Validation

Check that all visual elements render correctly.

| # | Check | Status | Comments |
|---|-------|--------|----------|
| 5.1 | KPI cards display correct values | | Should show numbers, not null or error |
| 5.2 | KPI cards update when filters are applied | | Value should change when year/country is filtered |
| 5.3 | Maps load and show correct country locations | | Countries should appear in right geographic positions |
| 5.4 | Maps color correctly by metric value | | Higher/lower values should show different shades |
| 5.5 | Bar charts display expected results | | Bars should be proportional to values |
| 5.6 | Scatter plots load with correct axis labels | | X and Y axes should be clearly labeled |
| 5.7 | Line charts show trends correctly across years | | Should show progression from 2020 to 2024 |
| 5.8 | Tooltips appear on hover and show useful information | | Should display university name, country, metric values |
| 5.9 | Tooltips do not show null or "NaN" values | | Nulls should either be hidden or shown as "N/A" |
| 5.10 | Color scheme is consistent across all dashboards | | Same colors should mean the same thing everywhere |
| 5.11 | Chart titles and subtitles are readable | | Font size should be appropriate |
| 5.12 | No overlapping text or elements | | Layout should be clean with no overlapping labels |
| 5.13 | Dashboard fits on screen without horizontal scrolling | | Should be viewable on a standard monitor |

---

## 6. Documentation Review

Make sure all project documentation is complete and accurate.

| # | Check | Status | Comments |
|---|-------|--------|----------|
| 6.1 | README.md is complete and accurate | | Should describe project, setup steps, folder structure |
| 6.2 | DATA_DICTIONARY.md covers all 48 columns | | Each column should have name, description, type, example |
| 6.3 | PROJECT_REPORT.md is complete | | Should have all 14 sections from intro to future scope |
| 6.4 | KPI_DASHBOARD_MAPPING.md documents all 6 KPIs | | Should include formulas, sources, and dashboard usage |
| 6.5 | Dashboard_Storyboard.pdf matches final dashboard layout | | Storyboard was created before building in Tableau |
| 6.6 | All data sources are documented | | QS, THE, OpenAlex, World Bank should all be listed |
| 6.7 | Folder structure in README matches actual project files | | All folders and files should exist as described |
| 6.8 | Scripts in `scripts/` are documented | | Each script should have a clear purpose |
| 6.9 | Reports in `reports/` are explained | | Duplicate review, name review, World Bank investigation |
| 6.10 | Installation steps in README are tested | | Follow the steps on a fresh machine to verify they work |

---

## 7. Final QA Approval

All checks must be PASS or N/A before this section is completed.

| Item | Details |
|------|---------|
| **Total Checks** | 65 |
| **Passed** | |
| **Failed** | |
| **N/A** | |
| **Pending** | |
| **Overall Status** | In Progress |
| **QA Reviewer** | [Student Name] |
| **Review Date** | [Date] |
| **Approved By** | [Supervisor/Instructor Name] |
| **Approval Date** | [Date] |

---

