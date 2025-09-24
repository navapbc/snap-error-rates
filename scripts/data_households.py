import pandas as pd
import re
import sys

file_path = sys.argv[1]
print(f"Extacting households from {file_path}")
year = re.search(r"ACSST1Y(\d{4})\.", file_path).groups(0)[0]

data = pd.read_csv(file_path, index_col="Label (Grouping)")
columns = dict([
    (x, x.partition("!")[0].upper())
    for x in data.columns
    if x.endswith("!!Total!!Estimate")
])
data = (
    data
    .rename(columns=columns)
    .loc["Households", columns.values()]
    .to_frame("households")
)
data.index.name = "state"
data["households"] = data["households"].str.replace(",", "")
data["year"] = year
data.to_csv(f"data/households_{year}.csv")
