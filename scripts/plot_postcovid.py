import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["font.size"] = 11

colors = {
    "purple": "#651a94",
    "purple_dark": "#471385",
    "purple_light": "#a646b7",
    "gold": "#f8b712",
    "gold_dark": "#f37100",
    "gold_light": "#f8e21a",
    "plum": "#b14092",
    "plum_dark": "#5b0462",
    "plum_light": "#d98bc3",
    "sage": "#08a588",
    "sage_dark": "#004c31",
    "sage_light": "#83cab6",
    "navy": "#0a0539",
    "navy_mid": "#282e6c",
    "navy_light": "#8d91b2",
}

data = (
    pd
    .read_csv("results/postcovid_under_payment_results.csv")
    .merge(
        pd.read_csv("results/postcovid_over_payment_results.csv"),
        how="outer",
        on=["year", "state"]
    )
)
data["y_true"] = data["y_true_x"] + data["y_true_y"]
data["y_pred"] = data["y_pred_x"] + data["y_pred_y"]

def rsquared(y_true, y_pred):
    r = r2_score(y_true, y_pred)
    plt.annotate(f"R^2 = {r:.3f}", xy=(0.85, 0.97), xycoords="axes fraction", fontsize=10)

def remove_spines(ax):
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

def plot_state(state1, state2):
    selected1 = data["state"] == state1
    selected2 = data["state"] == state2
    unselected = ~data["state"].isin([state1, state2])
    plt.figure(figsize=(8, 8))
    plt.plot([0, 1], [0, 1], transform=plt.gca().transAxes, lw=0.5, c="gray", zorder=1)
    plt.scatter(
        x=data.loc[unselected, "y_true"],
        y=data.loc[unselected, "y_pred"],
        marker="+",
        color="gray",
        label="Other States",
        zorder=2,
    )
    for y, c in zip([2022, 2023], ["purple_light", "purple_dark"]):
        plt.scatter(
            x=data.loc[selected1 & (data["year"] == y), "y_true"],
            y=data.loc[selected1 & (data["year"] == y), "y_pred"],
            s=60,
            marker="o",
            color="none",
            ec=colors[c],
            lw=4,
            label=f"{state1.title()} ({y})",
            zorder=3,
        )
    for y, c in zip([2022, 2023], ["gold_light", "gold_dark"]):
        plt.scatter(
            x=data.loc[selected2 & (data["year"] == y), "y_true"],
            y=data.loc[selected2 & (data["year"] == y), "y_pred"],
            s=60,
            marker="o",
            color="none",
            ec=colors[c],
            lw=4,
            label=f"{state2.title()} ({y})",
            zorder=3,
        )
    limit = round(max(data["y_true"].max(), data["y_pred"].max()) + 1)
    plt.xlim([0, limit])
    plt.ylim([0, limit])
    plt.xlabel("Actual Error Rate", fontsize=12)
    plt.ylabel("Prediced Error Rate", fontsize=12)
    plt.title("Predicted SNAP error rate from state policies, post-COVID (2022-2023)", fontsize=16, loc="left")
    plt.legend(title=False)
    rsquared(data["y_true"], data["y_pred"])
    remove_spines(plt.gca())
    plt.tight_layout()
    plt.savefig("results/postcovid_snap_error_rate.pdf")
    plt.savefig("results/postcovid_snap_error_rate.png")

print("Plotting post-COVID")
plot_state("PENNSYLVANIA", "TENNESSEE")
