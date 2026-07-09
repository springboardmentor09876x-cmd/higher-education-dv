import pandas as pd

# Read the CSV files
main = pd.read_csv("University_Raw_Data.csv", encoding="latin1")
rank2024 = pd.read_csv("2024 QS World University Rankings.csv", encoding="latin1")
rank2023 = pd.read_csv("2023 QS World University Rankings.csv", encoding="latin1")

# Remove extra spaces from column names
main.columns = main.columns.str.strip()
rank2024.columns = rank2024.columns.str.strip()
rank2023.columns = rank2023.columns.str.strip()

# Remove extra spaces from Institution values
main["Institution"] = main["Institution"].str.strip()
rank2024["Institution"] = rank2024["Institution"].str.strip()
rank2023["Institution"] = rank2023["Institution"].str.strip()

# Merge 2024 Rank
main = pd.merge(
    main,
    rank2024[["Institution", "2024 Rank"]],
    on="Institution",
    how="left"
)

# Merge 2023 Rank
main = pd.merge(
    main,
    rank2023[["Institution", "2023 Rank"]],
    on="Institution",
    how="left"
)

# Reorder the columns
cols = list(main.columns)

# Remove the new columns from their current position
cols.remove("2024 Rank")
cols.remove("2023 Rank")

# Insert them after Previous Rank
cols.insert(2, "2024 Rank")
cols.insert(3, "2023 Rank")

# Apply the new order
main = main[cols]

# Save the file
main.to_csv("University_Final_Data.csv", index=False, encoding="utf-8-sig")

print("✅ Successfully merged!")