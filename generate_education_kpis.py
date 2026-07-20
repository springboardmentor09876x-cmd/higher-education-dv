#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


final_dataset = pd.read_csv(
    r"C:\Users\ADMIN\Desktop\Muskan Programs\EduVision\data\university_cleaned.csv",
    low_memory=False
)


# In[3]:


print(final_dataset.shape)
print(final_dataset.columns.tolist())


# In[4]:


numeric_cols = [
    "qs_rank",
    "qs_overall_score",
    "academic_reputation",
    "employer_reputation",
    "citations_per_faculty",
    "the_overall_score",
    "P",
    "MNCS",
    "PP_top_10",
    "score"
]

for col in numeric_cols:
    if col in final_dataset.columns:
        final_dataset[col] = pd.to_numeric(
            final_dataset[col],
            errors="coerce"
        )


# In[5]:


final_dataset["Global Ranking Score"] = (
    final_dataset["qs_overall_score"].fillna(0)*0.40 +
    final_dataset["the_overall_score"].fillna(0)*0.30 +
    final_dataset["score"].fillna(0)*0.30
)


# In[7]:


research_cols = [col for col in final_dataset.columns
                 if "citation" in col.lower()
                 or "research" in col.lower()
                 or "mncs" in col.lower()
                 or "pp_" in col.lower()
                 or "p_" in col.lower()
                 or "h_index" in col.lower()]

print(research_cols)


# In[8]:


print(sorted(final_dataset.columns))


# In[9]:


final_dataset["Global Ranking Score"] = (
    final_dataset["qs_overall_score"].fillna(0)*0.40 +
    final_dataset["the_overall_score"].fillna(0)*0.30 +
    final_dataset["score"].fillna(0)*0.30
)


# In[10]:


final_dataset["Research Impact Score"] = (
    final_dataset["Citation Impact Score"].fillna(0)*0.60 +
    final_dataset["Research Excellence Score"].fillna(0)*0.40
)


# In[11]:


final_dataset["Faculty-to-Student Ratio"] = (
    final_dataset["faculty_student_ratio"]
)


# In[13]:


student_cols = [col for col in final_dataset.columns
                if "student" in col.lower()
                or "faculty" in col.lower()
                or "ratio" in col.lower()]

print(student_cols)


# In[14]:


location_cols = [col for col in final_dataset.columns
                 if "international" in col.lower()]

print(location_cols)


# In[15]:


final_dataset["Global Ranking Score"] = (
    final_dataset["qs_overall_score"].fillna(0) * 0.40 +
    final_dataset["the_overall_score"].fillna(0) * 0.30 +
    final_dataset["score"].fillna(0) * 0.30
)


# In[16]:


final_dataset["Research Impact Score"] = (
    final_dataset["Citation Impact Score"].fillna(0) * 0.60 +
    final_dataset["Research Excellence Score"].fillna(0) * 0.40
)


# In[17]:


final_dataset["Faculty-to-Student Ratio"].head()


# In[18]:


final_dataset["International Student Percentage"] = (
    final_dataset["international_student_ratio"]
)


# In[19]:


final_dataset["Academic Reputation Score"] = (
    final_dataset["academic_reputation"]
)


# In[20]:


final_dataset["Research Productivity Index"].head()


# In[21]:


kpis = [
    "Global Ranking Score",
    "Research Impact Score",
    "Faculty-to-Student Ratio",
    "International Student Percentage",
    "Academic Reputation Score",
    "Research Productivity Index"
]

final_dataset[kpis].head()


# In[22]:


final_dataset[kpis].isnull().sum()


# In[23]:


final_dataset[kpis] = final_dataset[kpis].fillna(0)


# In[24]:


final_dataset.to_csv("university_final_dataset.csv", index=False)
final_dataset.to_excel("university_final_dataset.xlsx", index=False)


# In[25]:


existing_kpis = [col for col in final_dataset.columns if any(
    word in col.lower() for word in [
        "score", "index", "ratio", "performance", "impact", "reputation"
    ]
)]

print(existing_kpis)


# In[26]:


kpis = [
    "Global Ranking Score",
    "Research Impact Score",
    "Faculty-to-Student Ratio",
    "International Student Percentage",
    "Academic Reputation Score",
    "Research Productivity Index"
]

print(final_dataset[kpis].head())


# In[27]:


final_dataset.to_csv("university_final_dataset.csv", index=False)
final_dataset.to_excel("university_final_dataset.xlsx", index=False)


# In[28]:


print(existing_kpis)


# In[29]:


kpis = [
    "Global Ranking Score",
    "Research Productivity Index",
    "Research Impact Score",
    "Faculty-to-Student Ratio",
    "Academic Reputation Score",
    "Overall Performance Index",
    "Citation Impact Score",
    "Research Excellence Score",
    "Internationalization Score"
]

print(final_dataset[kpis].describe())


# In[30]:


print(final_dataset[kpis].isnull().sum())


# In[31]:


final_dataset[kpis] = final_dataset[kpis].fillna(0)


# In[32]:


final_dataset.to_csv(
    "university_final_dataset.csv",
    index=False
)

final_dataset.to_excel(
    "university_final_dataset.xlsx",
    index=False
)


# In[33]:


import os
print(os.getcwd())


# In[34]:


final_dataset.to_excel(
    r"C:\Users\ADMIN\Desktop\Muskan Programs\EduVision\data\university_final_dataset.xlsx",
    index=False
)


# In[ ]:




