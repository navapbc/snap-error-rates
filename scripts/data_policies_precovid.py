import numpy as np
import pandas as pd

file_path = "data/raw/SNAPPolicyDatabase.xlsx"
print(f"Extracting pre-COVID policies from {file_path}")

policies = [
    "bbce",
    "bbce_fpl",
    "bbce_asset",
    "bbce_child",
    "bbce_senior",
    "cap",
]

df = pd.read_excel(file_path, sheet_name="SNAP Policy Database")

df["state"] = df["statename"].str.upper()

# Convert yearmonth (YYYYMM) to year
df["year"] = df["yearmonth"] // 100

# Recode policies
df["bbce_fpl"] = df["bbce_inclmt"].replace(-9, np.nan)
df["bbce_asset"] = (df["bbce_asset"] == 1).astype(int)
df["bbce_child"] = (df["bbce_child"] == 1).astype(int)
df["bbce_senior"] = (df["bbce_elddisinclmt"].isin([-7, -8])).astype(int)

# Group by state and year, then compute mean of all numeric policy variables
df = df.groupby(["state", "year"])[policies].mean(numeric_only=True).reset_index()

# Filter years
df = df[df["year"].isin([2017, 2018, 2019])]

# Standardize FPL
df["bbce_fpl"] = ((df["bbce_fpl"] - df["bbce_fpl"].mean()) / df["bbce_fpl"].std()).fillna(0)

# Write output
df.to_csv("data/policies_precovid.csv", index=False)
