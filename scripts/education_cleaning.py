#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re


# In[2]:


final_dataset = pd.read_csv(
    r"C:\Users\ADMIN\Desktop\Muskan Programs\EduVision\data\university_final_dataset_v2.csv"
)


# In[4]:


import os

path = r"C:\Users\ADMIN\Desktop\Muskan Programs\EduVision\data"

print(os.listdir(path))


# In[8]:


raw = pd.read_csv(
    r"C:\Users\ADMIN\Desktop\Muskan Programs\EduVision\data\university_raw_data (1).csv",
    low_memory=False
)


# In[9]:


print(raw.shape)
print(final_dataset.shape)


# In[10]:


print(raw.columns.tolist())


# In[11]:


print(final_dataset.columns.tolist())


# In[12]:


missing_cols = sorted(list(set(raw.columns) - set(final_dataset.columns)))

print("Columns present in RAW but missing in FINAL:")
print(missing_cols)


# In[13]:


print(raw.head())


# In[14]:


print(raw.columns)


# In[15]:


raw = pd.read_csv(
    r"C:\Users\ADMIN\Desktop\Muskan Programs\EduVision\data\university_raw_data (1).csv",
    sep=";",
    low_memory=False
)

print(raw.head())
print(raw.columns)


# In[16]:


raw = pd.read_csv(
    r"C:\Users\ADMIN\Desktop\Muskan Programs\EduVision\data\university_raw_data (1).csv",
    sep="\t",
    low_memory=False
)

print(raw.head())
print(raw.columns)


# In[17]:


with open(
    r"C:\Users\ADMIN\Desktop\Muskan Programs\EduVision\data\university_raw_data (1).csv",
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:
    for _ in range(5):
        print(f.readline())


# In[18]:


raw = pd.read_csv(
    r"C:\Users\ADMIN\Desktop\Muskan Programs\EduVision\data\university_raw_data (1).csv",
    header=1,
    low_memory=False
)


# In[19]:


print(raw.columns.tolist())


# In[20]:


raw = raw.rename(columns={
    "university_name": "university"
})


# In[22]:


import re
import pandas as pd

def clean_name(name):
    if pd.isna(name):
        return ""

    name = str(name).upper().strip()

    # Remove special characters
    name = name.replace("*", "")
    name = re.sub(r"[^\w\s]", "", name)

    # Expand common abbreviations
    name = name.replace("UNIV ", "UNIVERSITY ")
    name = name.replace("INST ", "INSTITUTE ")
    name = name.replace("&", "AND")

    # Remove extra spaces
    name = " ".join(name.split())

    return name


# In[23]:


raw["merge_key"] = raw["university"].apply(clean_name)
final_dataset["merge_key"] = final_dataset["university"].apply(clean_name)


# In[24]:


raw = raw[raw["year"] == 2026].copy()

missing_cols = sorted(list(set(raw.columns) - set(final_dataset.columns)))

print(missing_cols)


# In[26]:


cols_to_merge = [
    "merge_key",
    "city",
    "subject_field",
    "university_type",
    "degree_level",
    "faculty_count",
    "undergraduate_count",
    "postgraduate_count",
    "international_students_count",
    "international_student_ratio",
    "gender_ratio",
    "female_percentage",
    "male_percentage",
    "h_index",
    "research_output_score",
    "research_productivity_index"
]


# In[27]:


raw_small = raw[cols_to_merge].copy()


# In[28]:


raw_small = raw_small.drop_duplicates(subset="merge_key")


# In[29]:


final_dataset = final_dataset.merge(
    raw_small,
    on="merge_key",
    how="left"
)


# In[30]:


print(final_dataset.shape)


# In[31]:


print(final_dataset["city"].notna().sum())


# In[32]:


print(final_dataset.shape)

print(final_dataset["city"].isna().sum())

print(final_dataset["subject_field"].isna().sum())

print(final_dataset["faculty_count"].isna().sum())


# In[33]:


final_dataset.to_csv(
    r"C:\Users\ADMIN\Desktop\Muskan Programs\EduVision\data\university_final_dataset_v3.csv",
    index=False
)

final_dataset.to_excel(
    r"C:\Users\ADMIN\Desktop\Muskan Programs\EduVision\data\university_final_dataset_v3.xlsx",
    index=False
)

print("Final dataset exported successfully!")


# In[34]:


final_dataset = final_dataset.rename(columns={
    "university": "university_name",
    "qs_rank": "world_rank",
    "qs_overall_score": "overall_score",
    "academic_reputation": "academic_reputation_score",
    "employer_reputation": "employer_reputation_score"
})


# In[35]:


final_dataset.rename(columns={
    "university": "university_name",
    "qs_rank": "world_rank",
    "qs_overall_score": "overall_score",
    "academic_reputation": "academic_reputation_score",
    "employer_reputation": "employer_reputation_score",
    "citations_per_faculty": "citations_per_faculty_score"
}, inplace=True)


# In[36]:


print(final_dataset.columns.tolist())


# In[37]:


final_dataset.to_csv(
    r"C:\Users\ADMIN\Desktop\Muskan Programs\EduVision\data\university_final_dataset_final.csv",
    index=False
)

final_dataset.to_excel(
    r"C:\Users\ADMIN\Desktop\Muskan Programs\EduVision\data\university_final_dataset_final.xlsx",
    index=False
)

print("Final dataset exported successfully!")


# In[ ]:




