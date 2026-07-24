# Data Quality Baseline Report

**Dataset:** `data/processed/university_raw_data.csv`
**Generated:** 2026-07-22
**Status:** Before Cleaning — Official Benchmark

---

## SECTION 1 — Dataset Overview

| Metric | Value |
|--------|-------|
| Total Rows | 15,200 |
| Total Columns | 49 |
| Memory Usage | 13.0 MB |
| Total Unique Universities | 4,125 |
| Total Countries | 136 |
| Years Covered | 2020–2024 |
| Source Datasets | `the_rankings`, `qs_rankings` |

### Rows by Year

| Year | Rows |
|------|------|
| 2020 | 2,951 |
| 2021 | 2,528 |
| 2022 | 2,896 |
| 2023 | 3,227 |
| 2024 | 3,598 |

### Rows by Source

| Source | Rows |
|--------|------|
| the_rankings | 7,259 |
| qs_rankings | 6,544 |

---

## SECTION 2 — Missing Value Summary

### Overall Statistics

| Metric | Value |
|--------|-------|
| Total Missing Cells | 312,717 |
| Overall Missing % | 42.0% |
| Columns >50% Missing | 17 |
| Columns >25% Missing | 35 |
| Columns >10% Missing | 37 |

### Column-Level Analysis

| Column | Missing | % | Missing Type |
|--------|---------|---|--------------|
| year | 0 | 0.0% | — |
| university_name | 1,024 | 6.7% | Data Quality Issue |
| country | 1,033 | 6.8% | Data Quality Issue |
| source | 1,397 | 9.2% | Data Quality Issue |
| **QS Rankings (12 cols)** | | | Structural Missing |
| qs_rank | 13,919 | 91.6% | Structural Missing |
| qs_overall_score | 13,698 | 90.1% | Structural Missing |
| qs_academic_reputation | 11,178 | 73.5% | Structural Missing |
| qs_employer_reputation | 11,179 | 73.5% | Structural Missing |
| qs_faculty_student | 12,481 | 82.1% | Structural Missing |
| qs_citations_per_faculty | 11,183 | 73.6% | Structural Missing |
| qs_international_faculty | 12,648 | 83.2% | Structural Missing |
| qs_international_students | 12,560 | 82.6% | Structural Missing |
| qs_size | 9,979 | 65.7% | Structural Missing |
| qs_focus | 9,981 | 65.7% | Structural Missing |
| qs_age | 11,488 | 75.6% | Structural Missing |
| qs_status | 10,047 | 66.1% | Structural Missing |
| qs_research_intensity | 11,072 | 72.8% | Structural Missing |
| **THE Rankings (7 cols)** | | | Structural Missing |
| the_rank | 14,194 | 93.4% | Structural Missing |
| the_overall_score | 14,194 | 93.4% | Structural Missing |
| the_teaching | 6,909 | 45.5% | Data Quality Issue |
| the_research_environment | 6,909 | 45.5% | Data Quality Issue |
| the_research_quality | 6,909 | 45.5% | Data Quality Issue |
| the_industry | 6,909 | 45.5% | Data Quality Issue |
| the_international_outlook | 6,909 | 45.5% | Data Quality Issue |
| **THE Key Stats (4 cols)** | | | Structural Missing |
| total_fte_students | 5,149 | 33.9% | Structural Missing |
| students_per_staff | 5,150 | 33.9% | Structural Missing |
| international_students_pct | 5,149 | 33.9% | Structural Missing |
| female_male_ratio | 5,550 | 36.5% | Structural Missing |
| **Research Metrics (8 cols)** | | | Structural Missing |
| research_world_rank | 4,111 | 27.0% | Structural Missing |
| citations_score | 4,111 | 27.0% | Structural Missing |
| publications_count | 4,111 | 27.0% | Structural Missing |
| citations_count | 4,111 | 27.0% | Structural Missing |
| citations_per_faculty | 4,111 | 27.0% | Structural Missing |
| h_index | 4,111 | 27.0% | Structural Missing |
| research_output_score | 4,111 | 27.0% | Structural Missing |
| research_productivity_index | 4,111 | 27.0% | Structural Missing |
| **World Bank (5 cols)** | | | Merge Failure |
| gdp_per_capita | 2,683 | 17.7% | Merge Failure |
| population | 2,663 | 17.5% | Merge Failure |
| literacy_rate | 12,582 | 82.8% | Merge Failure |
| education_expenditure_pct_gdp | 8,764 | 57.7% | Merge Failure |
| tertiary_enrollment_pct | 4,875 | 32.1% | Merge Failure |
| **Country Metrics (8 cols)** | | | Merge Failure |
| region | 1,183 | 7.8% | Merge Failure |
| country_avg_rank | 1,183 | 7.8% | Merge Failure |
| country_universities_ranked | 1,183 | 7.8% | Merge Failure |
| country_best_rank | 1,183 | 7.8% | Merge Failure |
| country_avg_overall_score | 1,183 | 7.8% | Merge Failure |
| country_avg_academic_reputation | 1,183 | 7.8% | Merge Failure |
| country_avg_citations | 1,183 | 7.8% | Merge Failure |
| country_avg_intl_ratio | 1,183 | 7.8% | Merge Failure |

### Missing by Type

| Missing Type | Cells | Columns |
|--------------|-------|---------|
| Structural Missing | 233,687 | 27 |
| Merge Failure | 41,031 | 13 |
| Data Quality Issue | 37,999 | 9 |

**Note:** Structural Missing values are expected — QS columns only have data for QS-sourced rows, THE columns only for THE-sourced rows. These do not indicate data quality problems.

---

## SECTION 3 — Duplicate Summary

### 1. Exact Duplicate Rows

**Count:** 396 rows

**Reason:** All 396 are rows with NaN `university_name`. These are artifacts from QS 2020 double-header parsing — the sub-header row was parsed as data.

**Action:** Remove all 396 rows.

### 2. Invalid Rows (NaN university_name)

**Count:** 1,024 rows

**Reason:** QS 2020 file has a double header (row 2 is sub-headers). The parser treated sub-headers as data rows, producing NaN university names.

**Action:** Remove all 1,024 rows.

### 3. University-Year Duplicates

**Count:** 19 pairs (19 extra rows)

| Sub-category | Count | Reason |
|--------------|-------|--------|
| Both QS+THE (cross-source) | 5 | QS uses "Iran. Islamic Republic of", THE uses "Iran" — country name mismatch caused separate rows instead of merge |
| Same source (parsing artifacts) | 14 | QS 2020 double-header or naming inconsistency within QS |

**Action:** For cross-source: merge both rows (combine QS + THE columns). For same-source: keep first occurrence.

### 4. Source Column Ambiguity

**Count:** 1,397 rows (9.2%)

**Reason:** Outer joins between QS and THE created rows where `source` is NaN (rows exist in one source but not the other).

**Action:** No removal needed — these are legitimate rows. Set source to the available source name.

### 5. Country Metric Duplicates

**Count:** 0 (already handled)

**Reason:** Country standardization collapsed "China" + "China (Mainland)" into single "China" entries. Deduplication applied during merge.

### Duplicate Summary

| Category | Rows | Action |
|----------|------|--------|
| Exact duplicates | 396 | Remove |
| Invalid (NaN name) | 1,024 | Remove |
| University-year (extra) | 19 | Merge/deduplicate |
| **Total to remove** | **1,439** | |

---

## SECTION 4 — University Name Quality

### Overview

| Metric | Value |
|--------|-------|
| Total Unique University Names | 4,125 |
| Similarity Threshold | ≥ 0.90 |

### Name Quality Categories

| Category | Count | Description |
|----------|-------|-------------|
| Automatically Safe Merge | 297 pairs | Same normalized name AND same country |
| Manual Review | 346 pairs | High similarity, country match ambiguous |
| False Similarities | 137 pairs | Similar names but different countries |

### Safe Merge Examples (Top 10)

| Score | Name A | Name B |
|-------|--------|--------|
| 0.99 | Peter the Great St Petersburg Polytechnic University | Peter the Great St. Petersburg Polytechnic University |
| 0.99 | King Mongkut's Institute of Technology Ladkrabang | King Mongkut's Institute of Technology Ladkrabang |
| 0.99 | National Institute of Technology, Tiruchirappalli | National Institute of Technology Tiruchirappalli |
| 0.99 | V. N. Karazin Kharkiv National University | V.N. Karazin Kharkiv National University |
| 0.98 | Sungkyunkwan University (SKKU) | Sungkyunkwan University(SKKU) |
| 0.98 | Washington University in St Louis | Washington University in St. Louis |
| 0.98 | Universidade de São Paulo | Universidade de SÃ£o Paulo |
| 0.97 | Universite libre de Bruxelles | Université Libre de Bruxelles |
| 0.96 | Pontificia Universidad Católica Argentina | Pontificia Universidad Católica Argentina |
| 0.95 | Johannes Kepler University Linz | Johannes Kepler University of Linz |

### False Similarity Examples (Different Countries)

| Score | Name A (Country) | Name B (Country) |
|-------|------------------|------------------|
| 0.98 | Northwest University (China) | North-West University (South Africa) |
| 0.96 | Universidad de La Sabana (Colombia) | Universidad de La Habana (Cuba) |
| 0.95 | University of Freiburg (Germany) | University of Fribourg (Switzerland) |
| 0.95 | University of Malaya (Malaysia) | University of Malaga (Spain) |
| 0.95 | National University of Sciences and Tech (Pakistan) | National University of Science and Techn (Russia) |
| 0.95 | University of Sousse (Tunisia) | University of Sussex (United Kingdom) |
| 0.95 | University of Chester (United Kingdom) | University of Rochester (United States) |
| 0.94 | Shiraz University of Medical Sciences (Iran) | Shiga University of Medical Science (Japan) |
| 0.93 | Technical University of Berlin (Germany) | Technical University of Lublin (Poland) |
| 0.93 | University of Toronto (Canada) | University of Trento (Italy) |

### Action Plan

- **Safe Merge (297 pairs):** Merge automatically — same university, different spelling
- **Manual Review (346 pairs):** Review each pair individually before deciding
- **False Similarities (137 pairs):** Do NOT merge — different institutions

---

## SECTION 5 — Country Name Quality

### Overview

| Metric | Value |
|--------|-------|
| Total Country Variants | 136 |
| Standard Country Names | 130 |
| Non-standard Country Names | 6 |

### Non-standard Country Names

| Country | Records | Issue |
|---------|---------|-------|
| Iran | 305 | Standard name |
| Iran. Islamic Republic of | 6 | QS variant, should be "Iran" |
| Northern Cyprus | 13 | Not in World Bank |
| Cyprus | 20 | Check for confusion with Northern Cyprus |
| Oman | 15 | False positive in detection |
| Romania | 119 | False positive in detection |

**Remaining Issues:**
- "Iran. Islamic Republic of" (6 records) → should be "Iran"
- "Palestinian Territory. Occupied" (3 records) → should be "Palestine"

### COUNTRY_MAP Missing Entries (World Bank Fix)

| World Bank Name | University Name | Records Affected |
|-----------------|-----------------|------------------|
| Egypt, Arab Rep. | Egypt | 176 |
| Hong Kong SAR, China | Hong Kong | 55 |
| Iran, Islamic Rep. | Iran | 305 |
| Kyrgyz Republic | Kyrgyzstan | 2 |
| Macao SAR, China | Macau | 12 |
| Puerto Rico (US) | Puerto Rico | 10 |
| Slovak Republic | Slovakia | 46 |
| Somalia, Fed. Rep. | Somalia | 4 |
| Venezuela, RB | Venezuela | 49 |
| Yemen, Rep. | Yemen | 4 |
| **Total** | | **663** |

### Countries NOT Available in World Bank

| Country | Records | Status |
|---------|---------|--------|
| Taiwan | 253 | Not in WB — keep NULL |
| Palestine | 25 | Not in WB — keep NULL |
| Northern Cyprus | 13 | Not in WB — keep NULL |
| Iran. Islamic Republic of | 6 | Variant — standardize first |
| Palestinian Territory. Occupied | 3 | Variant — standardize first |
| **Total** | **300** | |

---

## SECTION 6 — World Bank Merge Quality

### Per-Indicator Analysis

| Indicator | Missing | Missing% | Merge Fail% | Genuine% | Countries Affected |
|-----------|---------|----------|-------------|----------|-------------------|
| GDP per Capita | 2,683 | 17.7% | 4.4% | 2.0% | Egypt, Hong Kong, Iran, Kyrgyzstan, Macau, Puerto Rico, Slovakia, Somalia, Venezuela, Yemen |
| Population | 2,663 | 17.5% | 4.4% | 2.0% | Same |
| Literacy Rate | 12,582 | 82.8% | 4.4% | 2.0% | Same + genuinely sparse reporting |
| Education Expenditure | 8,764 | 57.7% | 4.4% | 2.0% | Same + genuinely sparse reporting |
| Tertiary Enrollment | 4,875 | 32.1% | 4.4% | 2.0% | Same |

### Estimated Missing % After COUNTRY_MAP Fix

| Indicator | Before | After (Est.) | Reduction |
|-----------|--------|--------------|-----------|
| GDP per Capita | 17.7% | ~13.3% | -4.4% |
| Population | 17.5% | ~13.2% | -4.4% |
| Literacy Rate | 82.8% | ~78.4% | -4.4% |
| Education Expenditure | 57.7% | ~53.3% | -4.4% |
| Tertiary Enrollment | 32.1% | ~27.7% | -4.4% |

**Note:** The 4.4% reduction represents 663 rows across 10 countries where WB data exists but the merge failed due to COUNTRY_MAP gaps. The remaining missing values are genuine — either countries not in World Bank (Taiwan, Palestine, Northern Cyprus) or indicators not reported for certain years.

---

## SECTION 7 — Data Type Quality

### Summary

| Type | Count | Columns |
|------|-------|---------|
| Integer | 1 | year |
| Float | 37 | All numeric columns |
| String | 8 | university_name, country, source, region, qs_size, qs_focus, qs_status, qs_research_intensity |
| **Needs Conversion** | **2** | total_fte_students, international_students_pct |
| **Needs Parsing** | **1** | female_male_ratio |

### Columns Needing Conversion

| Column | Current Type | Target Type | Action |
|--------|--------------|-------------|--------|
| total_fte_students | string ("34,002") | int64 | Remove commas, convert |
| international_students_pct | string ("1%") | float64 | Remove % sign, convert |

### Columns Needing Parsing

| Column | Current Format | Target Format | Action |
|--------|----------------|---------------|--------|
| female_male_ratio | "65 : 35" | float64 (female_pct) | Parse ratio, extract female percentage |

---

## SECTION 8 — Cleaning Roadmap

### Ordered Cleaning Steps

| Step | Action | Priority |
|------|--------|----------|
| 1 | **Fix COUNTRY_MAP** — Add 10 missing WB name mappings | High |
| 2 | **Re-merge World Bank data** — Re-run merge with fixed COUNTRY_MAP | High |
| 3 | **Recalculate missing values** — Update counts after merge fix | High |
| 4 | **Remove invalid rows** — Drop 1,024 rows with NaN university_name | High |
| 5 | **Remove exact duplicates** — Drop 396 exact duplicate rows | High |
| 6 | **Standardize country names** — Fix "Iran. Islamic Republic of" → "Iran", "Palestinian Territory. Occupied" → "Palestine" | High |
| 7 | **Review university names** — Merge only 297 safe pairs (same normalized name + same country) | Medium |
| 8 | **Convert data types** — total_fte_students → int, international_students_pct → float, female_male_ratio → female_pct | Medium |
| 9 | **Handle remaining missing values** — Keep NaN for structural/ genuinely missing; do NOT forward-fill | Low |
| 10 | **Validate cleaned dataset** — Verify <2% missing in final columns | High |
| 11 | **Export university_cleaned.csv** — Save cleaned dataset | High |

### Key Constraints

- Do NOT merge university names with different countries (137 false similarities)
- Do NOT forward-fill World Bank data (Taiwan, Palestine, Northern Cyprus genuinely unavailable)
- Do NOT remove THE columns when QS exists (or vice versa) — they are complementary
- Maintain <2% missing target for final dataset after feature engineering

---

## Before Cleaning Scorecard

| Score | Value | Weight | Contribution |
|-------|-------|--------|--------------|
| Data Completeness Score | 58.0 / 100 | 30% | 17.4 |
| Consistency Score | 93.1 / 100 | 20% | 18.6 |
| Duplicate Score | 90.7 / 100 | 20% | 18.1 |
| Standardization Score | 96.1 / 100 | 15% | 14.4 |
| Merge Quality Score | 95.6 / 100 | 15% | 14.3 |
| **Overall Data Quality Score** | | | **82.9 / 100** |

### Score Methodology

| Score | Formula |
|-------|---------|
| Completeness | (1 - total_missing / total_cells) × 100 |
| Consistency | (1 - country_issues / total_rows) × 100 |
| Duplicates | (1 - (exact_dups + invalid_rows) / total_rows) × 100 |
| Standardization | (1 - merge_candidates / total_rows) × 100 |
| Merge Quality | (1 - merge_failures / total_rows) × 100 |
| Overall | Weighted: 30% + 20% + 20% + 15% + 15% |

### Interpretation

- **Completeness (58.0):** 42% missing cells — mostly structural (QS/THE columns only populated for respective sources)
- **Consistency (93.1):** 9 country name variants need standardization
- **Duplicates (90.7):** 1,420 rows to remove (exact dups + invalid rows)
- **Standardization (96.1):** 297 safe university name merges available
- **Merge Quality (95.6):** 663 rows affected by COUNTRY_MAP gaps
- **Overall (82.9):** Good baseline — cleaning will significantly improve scores

---

