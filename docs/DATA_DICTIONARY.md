# Data Dictionary - EduVision DV Final Dataset


This document describes every column in the final merged dataset used by the Tableau dashboards.

---

## Core Identifiers

| Column Name | Description | Data Type | Example Value |
|-------------|-------------|-----------|---------------|
| university_name | Name of the university as it appears in the ranking source | String | Massachusetts Institute of Technology (MIT) |
| country | Country where the university is located, standardized across all sources | String | United States |
| year | Academic year of the record (2020-2024) | Integer | 2023 |
| region | Broad geographic region the country belongs to, used for regional filtering in dashboards | String | North America |
| source | Which ranking source this record came from - QS only, THE only, both, or unknown | String | qs_and_the |

---

## QS World University Rankings Metrics

These columns come from the QS (Quacquarelli Symonds) ranking system. Scores are on a 0-100 scale unless noted otherwise.

| Column Name | Description | Data Type | Example Value |
|-------------|-------------|-----------|---------------|
| qs_rank | The university's overall rank in the QS rankings for that year. Lower rank means better performance. | Float | 1.0 |
| qs_overall_score | QS composite overall score combining all six indicator pillars. Range is 0-100. | Float | 100.0 |
| qs_academic_reputation | Score measuring academic reputation based on a global survey of academics. Higher means more respected among academics worldwide. | Float | 100.0 |
| qs_employer_reputation | Score measuring how well-regarded the university is among graduate employers. Based on employer surveys. | Float | 100.0 |
| qs_faculty_student | Score reflecting the student-to-faculty ratio. Higher score means more faculty members relative to students. | Float | 100.0 |
| qs_citations_per_faculty | Score measuring research impact based on citations per faculty member. Higher means more influential research output. | Float | 100.0 |
| qs_international_faculty | Score measuring the proportion of international faculty members. Higher means more diverse teaching staff. | Float | 100.0 |
| qs_international_students | Score measuring the proportion of international students enrolled. Higher means more international diversity in the student body. | Float | 100.0 |

---

## Times Higher Education (THE) Metrics

These columns come from the Times Higher Education ranking system. Most scores are on a 0-100 scale.

| Column Name | Description | Data Type | Example Value |
|-------------|-------------|-----------|---------------|
| the_rank | The university's overall rank in the THE rankings for that year. Lower rank means better performance. | Float | 1.0 |
| the_overall_score | THE composite overall score derived from five performance pillars. Range is 0-100. | Float | 98.0 |
| the_teaching | Score measuring the learning environment including teaching reputation, staff-to-student ratio, and doctorate-to-bachelor ratio. | Float | 95.5 |
| the_research_environment | Score measuring research reputation, research income, and research productivity. Reflects how strong the university's research setup is. | Float | 99.0 |
| the_research_quality | Score measuring research strength including citation impact, research strength, and research excellence. Focuses on the quality rather than quantity of research. | Float | 97.0 |
| the_industry | Score measuring knowledge transfer - how much income the university generates from industry partnerships and patents. | Float | 98.0 |
| the_international_outlook | Score measuring the mix of international students, international staff, and international research collaborations. | Float | 99.0 |

---

## THE Key Statistics

These are student and staffing statistics from the Times Higher Education dataset.

| Column Name | Description | Data Type | Example Value |
|-------------|-------------|-----------|---------------|
| total_fte_students | Total number of full-time equivalent students enrolled at the university. FTE converts part-time students to a full-time equivalent count. | Float | 11520.0 |
| students_per_staff | Number of students for every staff member. Lower ratio generally means more individual attention for students. | Float | 10.2 |
| international_students_pct | Percentage of the student body that comes from outside the country. Higher values indicate more international diversity. | Float | 33.5 |
| female_pct | Percentage of students who are female. Gives a sense of gender balance at the university. | Float | 47.2 |

---

## Research Metrics (from OpenAlex)

These columns contain research output data collected from the OpenAlex academic database.

| Column Name | Description | Data Type | Example Value |
|-------------|-------------|-----------|---------------|
| research_world_rank | The university's global rank based on research output. Lower rank means more research output and impact. | Float | 1.0 |
| citations_score | A normalized score measuring the overall citation impact of the university's research. Higher means more influential research. | Float | 85.3 |
| publications_count | Total number of academic publications (papers, articles, conference proceedings) produced by the university. | Float | 12450.0 |
| citations_count | Total number of times the university's publications have been cited by other researchers. Higher indicates more widely referenced work. | Float | 543210.0 |
| citations_per_faculty | Average number of citations per faculty member. Combines research output with staffing levels to show per-person research impact. | Float | 45.6 |
| h_index | The h-index measures both productivity and impact - a university has an h-index of N if N of its papers have each been cited at least N times. | Float | 412.0 |

---

## Country-Level World Bank Indicators

These columns contain socioeconomic data from the World Bank, aggregated at the country level. The same values apply to all universities in a given country and year.

| Column Name | Description | Data Type | Example Value |
|-------------|-------------|-----------|---------------|
| gdp_per_capita | Gross Domestic Product per person in the country, measured in current US dollars. Higher values generally indicate a wealthier economy. | Float | 76330.0 |
| population | Total population of the country for that year. | Integer | 331900000 |
| literacy_rate | Percentage of the population aged 15 and above who can read and write. Higher means better basic education access. | Float | 99.0 |
| education_expenditure_pct_gdp | Government spending on education as a percentage of GDP. Shows how much of the country's economic output goes toward education. | Float | 5.0 |
| tertiary_enrollment_pct | Gross enrollment ratio in tertiary education (universities, colleges). Shows what percentage of the eligible age group is enrolled in higher education. | Float | 88.0 |

---

## Country-Level Aggregated Metrics

These columns are averages and summaries computed across all ranked universities in each country. They help compare countries on the dashboards.

| Column Name | Description | Data Type | Example Value |
|-------------|-------------|-----------|---------------|
| country_avg_rank | Average rank of all ranked universities from that country. Lower average means the country has stronger universities overall. | Float | 450.0 |
| country_universities_ranked | Number of universities from that country that appear in the rankings. Shows how many institutions are globally competitive. | Integer | 55 |
| country_best_rank | The best (lowest) rank achieved by any university from that country. Shows the country's top-performing institution. | Float | 1.0 |
| country_avg_overall_score | Average overall score across all ranked universities in the country. Higher means stronger average performance. | Float | 62.5 |
| country_avg_academic_reputation | Average academic reputation score across all ranked universities in the country. Shows how the country's universities are perceived by academics globally. | Float | 58.3 |
| country_avg_citations | Average citation score across all ranked universities in the country. Reflects the country's overall research impact. | Float | 55.7 |
| country_avg_intl_ratio | Average international student ratio across all ranked universities in the country. Shows how internationalized the country's higher education system is. | Float | 22.4 |

---

## Engineered KPIs (Key Performance Indicators)

These are the six composite metrics I created by combining and normalizing values from the source datasets. These are the main metrics used in the Tableau dashboards.

| Column Name | Description | Data Type | Example Value |
|-------------|-------------|-----------|---------------|
| global_ranking_score | A combined score that merges QS overall score (60% weight) and THE overall score (40% weight), normalized to a 0-100 scale. Gives a single unified ranking metric that accounts for both ranking systems. | Float | 95.2 |
| research_impact_score | A weighted combination of citations per faculty (40%), research quality from THE (35%), and research environment from THE (25%). Normalized to 0-100. Measures how strong and impactful a university's research is. | Float | 88.7 |
| faculty_student_ratio | The number of students per staff member. Copied from students_per_staff for direct use in the Student dashboard. Lower values are generally better. | Float | 10.2 |
| international_student_percentage | The percentage of international students. Copied from international_students_pct for direct use in the Student dashboard. | Float | 33.5 |
| academic_reputation_score | The QS academic reputation score. Included as a standalone KPI for the Overview dashboard to highlight how academics view the institution. | Float | 98.0 |
| research_productivity_index | A geometric mean of normalized publications count, citations count, and h-index, scaled to 0-100. Captures both the quantity and quality of research output in a single balanced metric. | Float | 82.1 |

---
