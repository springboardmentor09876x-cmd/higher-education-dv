# EduVision_DV – KPI Definitions

## Normalization
The KPI notebook uses min-max normalization:

`Normalized Score = ((value - minimum) / (maximum - minimum)) × 100`

If all values are identical, the notebook assigns a score of 50.

## 1. Global Ranking Score
- QS Rank contribution: 40%
- THE Rank contribution: 30%
- Overall Score contribution: 30%

Better (lower) ranks are inverted before normalization.

## 2. Research Impact Score
- Citation Score: 50%
- Research Quality: 50%

## 3. Faculty-to-Student Ratio KPI
Uses the standardized faculty-to-student ratio as a numeric KPI.

## 4. International Student Percentage
Uses the international-student percentage field from the education data pipeline. The final output should be reconciled against the cleaned source before a final accuracy percentage is reported.

## 5. Academic Reputation Score KPI
Uses the standardized academic reputation score as a numeric KPI.

## 6. Research Productivity Index
- Publication Count: 60%
- H-Index: 40%

All KPI definitions should be interpreted together with the data-cleaning and KPI-generation notebooks.
