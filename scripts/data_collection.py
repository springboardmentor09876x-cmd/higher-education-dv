import pandas as pd

ref2 = pd.read_csv("data/raw/reference2.csv")

siena = ref2[
    ref2["University_Name"] == "University of Siena"
]

print(siena.head(20))