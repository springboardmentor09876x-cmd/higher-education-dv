# IMPLEMENTATION_RULES.md

**Version:** 2.0

**Status:** Mandatory

---

# Purpose

This document defines the mandatory implementation rules for the EduVision_DV project.

These rules apply to every script, notebook, dataset, dashboard, and future implementation task.

If any instruction conflicts with these rules, these rules take priority unless explicitly approved by the user.

---

# Rule 1 — Follow the Project Documents

Always follow this document together with:

- PROJECT_SPECIFICATION.md
- IMPLEMENTATION_ROADMAP.md
- EduVision_DV_Project_Requirements_MASTER.md

---

# Rule 2 — Follow the Engineering Workflow

Always follow this sequence:

```
Requirements
    ↓
Dataset Collection
    ↓
Dataset Validation
    ↓
Merge
    ↓
university_raw_data.csv
    ↓
Cleaning
    ↓
university_cleaned.csv
    ↓
Feature Engineering
    ↓
KPI Engineering
    ↓
university_final_dataset.xlsx
    ↓
Tableau
    ↓
Testing
    ↓
Documentation
```

Never skip a stage.

---

# Rule 3 — Data First

Build the data pipeline before building dashboards.

Python performs engineering.

Tableau performs visualization.

---

# Rule 4 — Approved Datasets Only

Use only approved datasets.

- QS Rankings
- THE Rankings
- THE Key Statistics
- World Bank Indicators
- Research Dataset (if included)

Do not introduce additional datasets without approval.

---

# Rule 5 — Validate Before Use

Every dataset must be verified before use.

Check:

- Availability
- Required years
- Required columns
- Missing values
- Merge compatibility

---

# Rule 6 — Preserve Raw Data

Never modify original source datasets.

Always preserve the original files.

---

# Rule 7 — Dataset Pipeline

Maintain exactly three engineering datasets.

```
university_raw_data.csv
        ↓
university_cleaned.csv
        ↓
university_final_dataset.xlsx
```

---

# Rule 8 — Cleaning Standards

Cleaning must include:

- Duplicate removal
- Missing value treatment
- Name standardization
- Data type correction
- Validation

Target:

Less than **2% missing values**.

---

# Rule 9 — Feature Engineering Before KPIs

Always perform:

Cleaning

↓

Feature Engineering

↓

KPI Engineering

Never change this order.

---

# Rule 10 — KPI Rules

KPIs must:

- Be calculated
- Be documented
- Be reproducible
- Be validated

Never manually enter KPI values.

---

# Rule 11 — Tableau Rules

Tableau should only:

- Visualize
- Filter
- Navigate
- Interact

Tableau should never perform engineering calculations already completed in Python.

---

# Rule 12 — Coding Standards

Follow:

- PEP8
- Modular code
- Logging
- Exception handling
- Reusable functions

Avoid hardcoded values whenever possible.

---

# Rule 13 — Folder Structure

Maintain the approved project structure.

Store every file in its correct directory.

---

# Rule 14 — Documentation

Document:

- Datasets
- Merges
- Cleaning
- Features
- KPIs
- Dashboards

No undocumented implementation.

---

# Rule 15 — Validation

Every major phase must end with:

- Completed Tasks
- Validation Results
- Issues Found
- Next Step

---

# Rule 16 — Evidence Before Assumption

Never assume:

- Dataset columns
- Merge keys
- KPI formulas
- Data availability

Verify first.

If verification is not possible, stop and ask for approval.

---

# Rule 17 — Maintain Data Lineage

Every KPI and dashboard metric must be traceable back to its source dataset.

Always preserve complete data lineage.

---

# Rule 18 — Final Objective

Every implementation should move the project toward being:

- Portfolio Ready
- GitHub Ready
- Business Ready
- Research Ready
- Scalable
- Maintainable
- Professional

---

**End of IMPLEMENTATION_RULES.md**