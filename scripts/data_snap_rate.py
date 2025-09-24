import pandas as pd
import re
import sys

file_path = sys.argv[1]
print(f"Extracing SNAP rate from {file_path}")
year = re.search(r"ACSST1Y(\d{4})\.", file_path).groups(0)[0]

data = pd.read_csv(file_path, index_col="Label (Grouping)")
columns = dict([
    (x, x.partition("!")[0].upper())
    for x in data.columns
    if x.endswith("!!Percent households receiving food stamps/SNAP!!Estimate")
])
data = (
    data
    .rename(columns=columns)
    .loc["Households", columns.values()]
    .to_frame("snap_rate")
)
data.index.name = "state"
data["snap_rate"] = data["snap_rate"].str.strip("%")
data["year"] = year
data.to_csv(f"data/snap_rate_{year}.csv")
