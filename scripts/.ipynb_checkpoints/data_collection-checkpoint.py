import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("datasets/raw")

def load_datasets():
    print("Looking in:", RAW_DATA_PATH.resolve())
    print("Folder exists:", RAW_DATA_PATH.exists())

    files = list(RAW_DATA_PATH.glob("*.csv"))
    print("Files found:", files)

    datasets = {}

    for file in files:
        print("Loading:", file.name)
        try:
            df = pd.read_csv(file)
        except UnicodeDecodeError:
            df = pd.read_csv(file, encoding="latin1")

        datasets[file.stem] = df

    return datasets


def dataset_summary(datasets):

    summary = []

    for name, df in datasets.items():

        summary.append({
            "Dataset": name,
            "Rows": df.shape[0],
            "Columns": df.shape[1],
            "Missing Values": df.isnull().sum().sum()
        })

    return pd.DataFrame(summary)


def show_columns(datasets):

    for name, df in datasets.items():

        print("=" * 80)
        print(name)
        print("=" * 80)

        for column in df.columns:
            print(column)


def save_summary(summary):

    summary.to_csv("../outputs/dataset_summary.csv", index=False)