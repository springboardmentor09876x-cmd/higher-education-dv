import pandas as pd
import requests
import time
import re
# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv(
    r"C:\Users\yadav\higher-education-dv\datasets\processed_data\Merged_Raw_Dataset.csv"
)

print("Dataset Loaded:", df.shape)

# =====================================================
# TEST WITH FIRST 5 UNIVERSITIES
# =====================================================
def clean_name(name):
    name = name.lower()

    # Remove text inside ()
    name = re.sub(r"\(.*?\)", "", name)

    # Remove everything after comma
    name = name.split(",")[0]

    # Remove common words
    remove_words = [
        "switzerland",
        "usa",
        "uk",
        "campus"
    ]

    for word in remove_words:
        name = name.replace(word, "")

    return name.strip()
results = []

start = 1710   # Continue from where it stopped

for i, row in df.iloc[start:].iterrows():

    university = row["University_Name"]
    search_name = clean_name(university)

    print(f"{i+1}/{len(df)} : {search_name}")

    url = f"https://api.openalex.org/institutions?search={search_name}"

    try:
        response = requests.get(url, timeout=20)

    except Exception as e:
        print("Connection Error:", e)
        time.sleep(5)
        continue

    if response.status_code == 200:

        data = response.json()["results"]

        if len(data) > 0:

            inst = data[0]

            results.append({
                "University_Name": university,
                "Publications_Count": inst.get("works_count"),
                "Citations_Count": inst.get("cited_by_count"),
                "H_Index": inst.get("summary_stats", {}).get("h_index")
            })

    # Save every 100 records
    if len(results) > 0 and len(results) % 100 == 0:

        pd.DataFrame(results).to_csv(
            r"C:\Users\yadav\higher-education-dv\datasets\processed_data\openalex_data.csv",
            index=False
        )

        print("Progress Saved")

    time.sleep(0.5)
# =====================================================
# SAVE RESULTS
# =====================================================

result_df = pd.DataFrame(results)

result_df.to_csv(
    r"C:\Users\yadav\higher-education-dv\datasets\processed_data\openalex_data.csv",
    index=False
)

print("\nTest file saved successfully!")
print(result_df)

