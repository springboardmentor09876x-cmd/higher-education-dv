# EduVision DV - Higher Education Performance Dashboard

## A Data Visualization Project Report

---

## 1. Introduction

Higher education is one of the most important drivers of economic and social development. Every year, organizations like QS and Times Higher Education release rankings that try to measure how good universities are at teaching, doing research, and attracting international students. On top of that, the World Bank collects data on how much countries spend on education, how many people are literate, and how many young people actually make it to university.

The problem is that all this data lives in different places, uses different formats, and is hard to compare side by side. If someone wants to understand how universities in a particular country are performing relative to their government's education spending, they would have to manually download, clean, and merge data from four or five different sources. That is a lot of work, and most people just do not bother.

This project, called EduVision DV, tries to solve that problem. I built an interactive Tableau dashboard that pulls together data from QS World University Rankings, Times Higher Education Rankings, OpenAlex research data, and World Bank education indicators into one clean, unified dataset. The goal was to make it easy to explore and compare higher education performance across universities, countries, and years.

The project covers five years of data (2020 to 2024), includes over 3,800 unique universities from 134 countries, and produces four different dashboard views that let users explore the data from different angles.

---

## 2. Problem Statement

There is no single place where someone can go to compare universities across multiple ranking systems, look at their research output, and also see how the country they are in performs on education-related economic indicators. The data exists, but it is scattered across different websites, published in different formats, and uses different naming conventions for countries and universities.

Specifically, the challenges are:

- QS and THE use different column structures and different naming conventions for the same universities. For example, QS might call a university "University of Oxford" while THE calls it "Oxford University."
- World Bank data is at the country level, not the university level, so it needs to be joined carefully using country names and years.
- Research data from OpenAlex has its own institution naming system that does not always match the ranking datasets.
- Each source has missing values in different places. QS 2022 is missing country information for some universities. THE key statistics have percentages stored as text strings instead of numbers.
- There is no standard set of KPIs that works across all these sources.

The core problem is data integration: how do you take four fundamentally different datasets and turn them into one clean table that a dashboard tool like Tableau can consume?

---

## 3. Project Objectives

The main objectives of this project were:

1. **Collect and consolidate** data from four major higher education data sources (QS, THE, OpenAlex, World Bank) covering 2020-2024.
2. **Clean and standardize** the merged dataset so that university names, country names, and data types are consistent across all records.
3. **Engineer meaningful KPIs** that combine metrics from multiple sources into standardized scores that can be compared fairly across universities.
4. **Build interactive Tableau dashboards** that let users explore the data from four different perspectives: university overview, research output, country comparison, and student demographics.
5. **Achieve a data quality target** of less than 2% missing values in the final dataset.
6. **Document the entire process** so that the project can be reproduced and extended by others.

---

## 4. Data Sources

Four main data sources were used in this project:

### 4.1 QS World University Rankings (2020-2024)

QS (Quacquarelli Symonds) is one of the most widely referenced university ranking systems in the world. The dataset includes overall rank, overall score, and six individual indicator scores: academic reputation, employer reputation, faculty-student ratio, citations per faculty, international faculty, and international students. All scores are on a 0-100 scale.

One challenge with QS data is that the format changes from year to year. QS 2020 uses a double header row. QS 2022 is missing the country column entirely. QS 2024 uses semicolons as delimiters instead of commas and uses European-style decimal separators (commas instead of dots). Each year had to be handled separately during the merge process.

### 4.2 Times Higher Education Rankings (2020-2024)

THE (Times Higher Education) is the other major global university ranking. The dataset includes overall rank, overall score, and five pillar scores: teaching, research environment, research quality, industry, and international outlook. THE also publishes a separate "Key Statistics" dataset that includes FTE student counts, students per staff ratio, international student percentage, and female-to-male ratio.

THE data is generally more consistent across years than QS, but there are still differences in how percentages and ratios are formatted.

### 4.3 OpenAlex Research Data

OpenAlex is an open-access database of academic research. I used Python scripts to query the OpenAlex API and collect institution-level research metrics including publication counts, citation counts, h-index, i10-index, and yearly research output for each university found in the QS and THE datasets.

The challenge with OpenAlex is that institution names do not always match the names used in ranking datasets. For example, "MIT" in QS might be "Massachusetts Institute of Technology" in OpenAlex. The collection scripts handle this by searching for each university name and picking the best match.

### 4.4 World Bank Open Data

The World Bank publishes country-level indicators including GDP per capita, education expenditure as a percentage of GDP, literacy rate, population, and tertiary enrollment ratio. I used the World Bank API to download this data for all countries, covering 2020-2024.

World Bank data is at the country level, not the university level, so it gets joined to the university dataset using standardized country names and year. This means every university in the same country in the same year gets the same World Bank values.

---

## 5. Data Collection

Data collection was done using a combination of downloaded CSV files and API calls.

### 5.1 QS and THE Rankings

The QS and THE ranking files were downloaded directly from the respective websites as CSV files. Five years of data were collected for each source (2020-2024), plus five years of THE Key Statistics.

Files collected:

- `qs_rankings_2020.csv` through `qs_rankings_2024.csv`
- `the_rankings_2020.csv` through `the_rankings_2024.csv`
- `the_key_statistics_2020.csv` through `the_key_statistics_2024.csv`

### 5.2 World Bank Indicators

A Python script (`scripts/download_world_bank.py`) was written to query the World Bank API for five indicators:

| Indicator | API Code |
|-----------|----------|
| GDP per Capita | NY.GDP.PCAP.CD |
| Population | SP.POP.TOTL |
| Literacy Rate | SE.ADT.LITR.ZS |
| Education Expenditure | SE.XPD.TOTL.GD.ZS |
| Tertiary Enrollment | SE.TER.ENRR |

The script handles pagination (the API returns results in pages of 1,000 records), saves raw JSON responses, and then a second script (`scripts/convert_world_bank_json.py`) converts the JSON files into clean CSVs with standardized columns: country_name, country_iso3code, year, and indicator_value.

### 5.3 OpenAlex Research Data

Two Python scripts were written for OpenAlex data collection:

- `scripts/collect_openalex_data.py` - Queries the OpenAlex institutions endpoint for every unique university name found in the QS and THE datasets. This results in thousands of API calls with rate limiting (500ms between requests, exponential backoff on 429 errors).
- `scripts/collect_openalex_top_universities.py` - A lighter version that only queries the top 500 universities from each ranking to reduce API calls.

The collected data includes total works count, total citation count, h-index, i10-index, 2-year mean citedness, and yearly breakdowns of works and citations for 2020-2024.

---

## 6. Data Cleaning

The raw merged dataset had significant quality issues. Here is what the cleaning pipeline addressed, step by step.

### 6.1 Initial State

After merging all sources, the raw dataset had:

- 15,193 rows and 49 columns
- 310,033 missing cells (41.6%)

This is expected when merging datasets that do not have perfect overlap. Not every university appears in both QS and THE, not every university has OpenAlex research data, and World Bank indicators are only available at the country level.

### 6.2 Removing Non-Required Columns

Seven columns that were not needed for any dashboard or KPI were dropped: male_pct, qs_size, qs_focus, qs_age, qs_status, qs_research_intensity, and research_output_score. This removed 56,636 missing cells right away.

### 6.3 Removing Invalid Rows

1,024 rows with NaN university names were removed. These were artifacts from the QS 2020 parsing, where the double header caused some rows to be read incorrectly.

### 6.4 Standardizing Country Names

Different sources use different names for the same country. For example:

- QS uses "China (Mainland)" while World Bank uses "China"
- THE uses "Iran (Islamic Republic of)" while World Bank uses "Iran"
- QS uses "Palestinian Territory, Occupied" while World Bank uses "Palestine"

A comprehensive country mapping dictionary with 30+ entries was used to standardize all country names to a single consistent form. After this step, there were 134 unique countries.

### 6.5 Merging University Name Variants

The same university can have different names across sources and even across years within the same source. For example, "University of Toronto" might appear as "Univ. of Toronto" in one year and the full name in another.

The cleaning step normalizes all names (lowercase, remove non-alphanumeric characters), identifies duplicates, and merges them. This resulted in 1,086 record changes and removed 8 duplicate entries. The final count was 3,845 unique universities.

### 6.6 Converting Data Types

Several columns had data type issues:

- `total_fte_students` had commas in the numbers (e.g., "34,002") and needed to be converted to numeric
- `international_students_pct` had percentage signs (e.g., "33.5%") that needed to be stripped
- `female_male_ratio` was stored as a ratio string (e.g., "1.2:1") and needed to be parsed into a female percentage

### 6.7 Imputation Strategy

Since the goal was to get below 2% missing values, a multi-step imputation strategy was used:

1. **Cross-impute QS/THE scores:** When QS overall score was missing but THE overall score was available (and vice versa), one was used to fill the other.
2. **Country median imputation for research metrics:** Missing research columns (publications count, citations count, h-index, etc.) were filled with the median value for universities in the same country.
3. **Country median imputation for THE key stats:** Missing student/staff data was filled using country-level medians.
4. **Forward-fill for country-level metrics:** World Bank indicators and country aggregated metrics were forward-filled within each country (carrying the previous year's value forward), then backward-filled, then filled with global median for any remaining gaps.
5. **Country median for remaining THE/QS columns:** Any remaining missing values in ranking-specific columns were filled using country medians.
6. **Rank-to-score estimation:** For records where the overall score was missing but the rank was available, the score was estimated using the formula: `score = 100 * (1 - rank / max_rank)`.

### 6.8 Final State

After all cleaning steps:

- 14,161 rows and 43 columns
- 135 missing cells (0.0%)
- 0 NaN university names
- 0 exact duplicates
- 0 non-standard country names

This was well under the 2% target.

---

## 7. Data Integration

The data integration process was handled by `scripts/merge_datasets.py`, which performs five sequential merges.

### 7.1 Merge Sequence

| Step | Action | Join Type | Join Keys |
|------|--------|-----------|-----------|
| 1 | QS + THE Rankings | Outer | university_name, country, year |
| 2 | + THE Key Statistics | Outer | university_name, country, year |
| 3 | + Research Metrics (aggregated) | Outer | university_name, country, year |
| 4 | + World Bank Indicators | Left | country, year |
| 5 | + Country Metrics | Left | country, year |

The first three merges use outer joins to keep all records from both sides, even if a university only appears in one source. The last two merges use left joins because World Bank and country metrics are supplementary data that should not create new university records.

### 7.2 Country Name Standardization During Merge

The merge script contains a 30-entry country mapping dictionary that handles the most common naming differences between sources. For example:

- "USA" variants are all mapped to "United States"
- "UK" variants are mapped to "United Kingdom"
- "China (Mainland)" is mapped to "China"

### 7.3 QS 2022 Country Fix

Since QS 2022 does not include country information, the merge script fills missing country values by looking up each university in THE rankings and other QS years. This is done using a university-to-country mapping built from the other datasets.

---

## 8. KPI Engineering

After cleaning, six KPIs were engineered in `scripts/generate_education_kpis.py`. Each KPI combines or transforms raw metrics into a standardized score that can be compared fairly across universities.

### 8.1 Global Ranking Score

**Formula:** Weighted average of QS overall score (60%) and THE overall score (40%), normalized to 0-100.

**Why:** Different ranking systems weigh factors differently. Combining them gives a more balanced view of overall university performance. QS gets a slightly higher weight because it covers more universities.

**Used in:** Overview Dashboard

### 8.2 Research Impact Score

**Formula:** Weighted average of normalized citations per faculty (40%), THE research quality (35%), and THE research environment (25%). Normalized to 0-100.

**Why:** Research impact cannot be measured by a single metric. Citations per faculty shows per-person impact, research quality shows the quality of the research environment, and research environment shows institutional research capacity.

**Used in:** Research Dashboard

### 8.3 Faculty-to-Student Ratio

**Formula:** Direct passthrough of students_per_staff.

**Why:** This is a straightforward metric that does not need transformation. Lower values generally mean more individual attention for students.

**Used in:** Student Dashboard

### 8.4 International Student Percentage

**Formula:** Direct passthrough of international_students_pct.

**Why:** Like faculty-to-student ratio, this is already on a 0-100 scale and does not need normalization.

**Used in:** Student Dashboard

### 8.5 Academic Reputation Score

**Formula:** Direct passthrough of QS academic reputation score.

**Why:** This is one of the most survey-driven metrics in the QS system and provides a unique view of how academics perceive universities globally.

**Used in:** Overview Dashboard

### 8.6 Research Productivity Index

**Formula:** Geometric mean of normalized publications count, citations count, and h-index, scaled to 0-100.

**Why:** The geometric mean ensures that a university must perform well on all three dimensions to score high. A university with tons of publications but few citations would not score as well as one that is strong on both.

**Used in:** Research Dashboard

### 8.7 Normalization Approach

All composite KPIs use min-max normalization to scale values to 0-100. This ensures that no single metric dominates simply because it has larger raw numbers.

---

## 9. Dashboard Design Approach

The dashboards were designed in Tableau Desktop and exported as a packaged workbook (`.twbx`). The design followed these principles:

1. **Four separate dashboards** for four different analytical perspectives, rather than trying to cram everything into one overcrowded view.
2. **Consistent filters** across all dashboards (year selector, country selector) so users can easily compare across views.
3. **Color coding** using a consistent palette - higher values in green/blue, lower values in red/orange.
4. **Interactive elements** - tooltips, highlighters, and filter actions so users can drill down into specific data points.
5. **Clean layout** with clear titles, subtitles explaining what each chart shows, and adequate white space.

A storyboard was created first (in `docs/Dashboard_Storyboard.pdf`) to plan the layout before building in Tableau. The KPI and dashboard mapping document (`docs/KPI_DASHBOARD_MAPPING.md`) served as the specification that defined which KPIs go on which dashboard and what data each dashboard needs.

---

## 10. Dashboard Pages

### 10.1 Overview Dashboard

The Overview Dashboard is the main entry point. It shows a high-level comparison of universities across all years.

**What it shows:**

- A bar chart or table of universities ranked by their Global Ranking Score
- Academic Reputation Score comparisons
- Year-over-year trends for selected universities
- A summary of how many universities and countries are represented

**Key filters:** Year, Country, Region

**Target audience:** Someone who wants a quick overview of which universities are performing best overall.

### 10.2 Research Dashboard

The Research Dashboard focuses specifically on research output and impact.

**What it shows:**

- Research Impact Score comparisons across universities
- Publication counts and citation metrics
- H-index distributions
- Research Productivity Index rankings
- Country-level research comparisons

**Key filters:** Year, Country, Region, Research metric selector

**Target audience:** Someone interested in understanding which universities are producing the most impactful research, not just teaching well.

### 10.3 Country Dashboard

The Country Dashboard compares countries on education-related economic and social indicators.

**What it shows:**

- GDP per capita vs. average university ranking (scatter plot)
- Education expenditure as percentage of GDP by country
- Tertiary enrollment rates
- Literacy rates
- How many universities each country has in the rankings
- Correlation between economic indicators and university performance

**Key filters:** Year, Region

**Target audience:** Someone who wants to understand how a country's economic and education policies relate to its university performance.

### 10.4 Student Dashboard

The Student Dashboard looks at student-related metrics.

**What it shows:**

- Faculty-to-student ratio comparisons
- International student percentage distributions
- Gender balance (female percentage) across universities
- How student demographics vary by country and region
- Relationships between student metrics and overall ranking

**Key filters:** Year, Country, Region

**Target audience:** Someone interested in the student experience - how many students per staff member, how international the environment is, and how gender-balanced the institution is.

---

## 11. Key Insights

After analyzing the data across all dashboards, several interesting patterns emerged.

### 11.1 US and UK Dominate the Top Ranks

Universities in the United States and United Kingdom consistently occupy the top positions in both QS and THE rankings. Institutions like MIT, Stanford, Cambridge, and Oxford appear in the top 5 across all five years. However, the gap between these traditional leaders and top Asian universities has been narrowing.

### 11.2 Asian Universities Are Rising

Universities from China, Singapore, and Hong Kong have shown steady improvement from 2020 to 2024. Tsinghua University, National University of Singapore, and Nanyang Technological University have climbed significantly in both QS and THE rankings, especially in research-related metrics.

### 11.3 GDP Per Capita Correlates With University Performance

There is a visible positive correlation between a country's GDP per capita and the average ranking of its universities. Wealthier countries tend to have better-ranked universities. However, there are notable exceptions. Countries like India and Brazil have universities that perform above what their GDP per capita would predict, suggesting that factors like government investment in education, historical academic traditions, and population size also play a role.

### 11.4 Research Impact and International Students Are Linked

Universities that score high on research impact metrics (citations per faculty, h-index) also tend to have higher percentages of international students. This suggests that strong research reputations attract international talent, and international collaboration in turn boosts research output.

### 11.5 Education Spending Does Not Always Equal Quality

Countries that spend a high percentage of their GDP on education do not necessarily have the best-ranked universities. Some countries with moderate education spending have universities that outperform expectations, while some high-spending countries have relatively lower-ranked institutions. This suggests that how money is spent matters more than how much is spent.

### 11.6 Faculty-to-Student Ratio Varies Widely

The range of faculty-to-student ratios across universities is enormous - from around 2 students per staff member to over 30. Universities with lower ratios tend to rank higher, but the relationship is not perfectly linear. Some highly ranked universities have higher ratios but compensate with other strengths.

---

## 12. Challenges Faced

### 12.1 Inconsistent Data Formats

The biggest challenge was dealing with the different data formats across sources and across years within the same source. QS 2020 had a double header, QS 2022 was missing country data, and QS 2024 used semicolons as delimiters. Each year required custom parsing logic.

### 12.2 University Name Mismatches

The same university often has slightly different names across datasets. Even after normalization, some names were hard to match. For example, "Hong Kong University of Science and Technology" versus "The Hong Kong University of Science and Technology." A manual review process was needed for some edge cases, and the results were saved in `reports/university_name_review.csv`.

### 12.3 Missing Data

The initial merged dataset had 41.6% missing values. Getting this down to 0.0% required a multi-step imputation strategy. While the imputed values are reasonable estimates, they are still estimates and could introduce bias in the analysis. This is documented as a limitation.

### 12.4 World Bank Data Joining

World Bank data is at the country level, while the rest of the data is at the university level. Joining these required careful standardization of country names. Some World Bank country names did not match any university's country name, and these gaps had to be investigated (results in `reports/world_bank_missing_investigation.csv`).

### 12.5 Rate Limiting on APIs

The OpenAlex API has rate limits. Collecting data for thousands of universities required writing scripts with exponential backoff and sleep delays. A single run could take several hours if querying all universities, which is why the top-500 variant was also created.

### 12.6 QS 2022 Missing Country Data

The QS 2022 dataset does not include a country column. This meant that after merging, many rows had missing country values. The solution was to build a university-to-country mapping from the other datasets and fill in the missing values using that mapping. This worked for most universities but not all.

---

## 13. Conclusion

This project successfully built an end-to-end data pipeline that collects, cleans, merges, and visualizes higher education data from four different sources. The final dataset contains 14,161 records across 48 columns with 0.0% missing values, covering 3,845 universities from 134 countries over five years (2020-2024).

The four Tableau dashboards provide different perspectives on the data - from a high-level university overview to detailed research metrics, country comparisons, and student demographics. The six engineered KPIs (Global Ranking Score, Research Impact Score, Faculty-to-Student Ratio, International Student Percentage, Academic Reputation Score, and Research Productivity Index) provide standardized metrics that make cross-university comparison fair and meaningful.

The key findings - that US and UK universities still dominate, that Asian universities are rising, that GDP correlates with university performance but is not the only factor, and that research impact attracts international students - are consistent with broader trends in higher education and demonstrate that the dashboard is capturing real patterns in the data.

The biggest takeaway from this project is that data integration is hard. Merging four different datasets with different formats, naming conventions, and coverage levels requires careful planning, extensive cleaning, and creative imputation strategies. But the end result - a single clean dataset that enables interactive multi-dimensional analysis - is worth the effort.

---

## 14. Future Scope

There are several ways this project could be extended:

1. **More years of data:** Adding pre-2020 data would allow trend analysis over a longer period and help identify whether the patterns we see are long-term trends or short-term fluctuations.

2. **Additional ranking sources:** Incorporating ARWU (Shanghai Rankings) would provide a third perspective on university performance and make the combined ranking more robust.

3. **Employment and salary data:** Adding graduate employment rates and average starting salaries would give a more complete picture of university value from a student perspective.

4. **Live data updates:** Building a scheduled pipeline that automatically fetches new data from the World Bank and OpenAlex APIs would keep the dashboard current without manual intervention.

5. **Predictive analytics:** Machine learning models could be trained on the historical data to predict future rankings or identify universities that are likely to improve or decline.

6. **Web-based dashboard:** Building the dashboard in a web framework like Streamlit or Dash would make it accessible to anyone with a browser, without needing Tableau Desktop or Tableau Public installed.

7. **Sentiment analysis:** Analyzing student reviews and social media mentions could add a qualitative dimension to the purely quantitative metrics currently used.

8. **Student mobility flows:** Incorporating data on where international students come from and where they go after graduation would add depth to the internationalization analysis.

---

