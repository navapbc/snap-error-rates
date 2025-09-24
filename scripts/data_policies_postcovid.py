import pandas as pd

print("Extracting post-COVID policies")

file_path = "data/raw/ICPSR_39331_DS0001_39331-0001-Data.dta"
print(f"Merging ICPSR policies from {file_path}")
data = pd.read_stata(file_path)

# Filter
data = data[data["VALUE"] == "1. State implemented policy"]
data = data[data["YEAR"].isin([2022, 2023])]

# Group by year
data["state"] = data["STATE"].str.upper()
data["year"] = data["YEAR"]
data["policy"] = data["POLICY_NAME"].str.partition(" ")[2]
data["count"] = 1
data = data.groupby(["state", "year", "policy"])["count"].sum().reset_index()

# Normalize counts by total months observed
months = pd.DataFrame({"year": [2022, 2023], "months": [12, 6]})
data = data.merge(months, how="left", on=["year"])
data["value"] = data["count"] / data["months"]

# Pivot
data = data.pivot(index=["state", "year"], columns="policy", values="value").fillna(0)

file_path = "data/raw/SnapScreenerData.csv"
print(f"Merging SnapScreener policies from {file_path}")
data = data.reset_index().merge(pd.read_csv(file_path), how="inner", on=["state"])

# Standardize FPL
data["bbce"] = data["bbce"].astype(int)
data["bbce_fpl"] = ((data["bbce_fpl"] - data["bbce_fpl"].mean()) / data["bbce_fpl"].std()).fillna(0)

data.to_csv("data/policies_postcovid.csv", index=False)
