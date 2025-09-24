import pandas as pd
from glob import glob

def standardize(x):
    return (x - x.mean()) / x.std()

print("Building controls")

print("Merging SNAP rate")
snap_rate = pd.concat(
    [pd.read_csv(f) for f in glob("data/snap_rate_*.csv")],
    ignore_index=True
)
snap_rate["snap_rate"] = standardize(snap_rate["snap_rate"])

print("Merging households")
households = pd.concat(
    [pd.read_csv(f) for f in glob("data/households_*.csv")],
    ignore_index=True
)
households["households"] = standardize(households["households"])

print("Merging governor party")
governor = pd.read_csv("data/governor_party.csv")
governor["republican_governor"] = (governor["party"] == "Republican").astype(int)
governor.drop("party", axis=1, inplace=True)

controls = (
    snap_rate
    .merge(households, how="inner", on=["year", "state"])
    .merge(governor, how="inner", on=["year", "state"])
)

controls.to_csv("data/controls.csv", index=False)
