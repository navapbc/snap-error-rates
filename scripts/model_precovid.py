import matplotlib.pyplot as plt
import pandas as pd
from numpy import ones_like, triu
from seaborn import heatmap
from statsmodels.formula.api import ols


def plot_correlations(data, outname):
    """
    Plot a heatmap of pairwise correlations between the variables
    in the source data frame.
    """
    corr = data.corr()
    mask = triu(ones_like(corr, dtype=bool), k=1)
    fig = plt.figure(figsize=(12, 10))
    heatmap(
        corr.mask(mask == False),
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5,
        vmin=-1.0,
        vmax=1.0,
    )
    fig.tight_layout()
    fig.savefig(outname)


def estimate_model(outcome):
    name = f"precovid_{outcome}"
    print(f"Model {name}")
    data = (
        pd
        .read_csv("data/error_rates_precovid.csv", usecols=["year", "state", outcome])
        .merge(
            pd.read_csv("data/policies_precovid.csv"),
            how="inner",
            on=["year", "state"]
        )
        .merge(
            pd.read_csv("data/controls.csv"),
            how="inner",
            on=["year", "state"]
        )
    )
    variables = data.columns.tolist()[3:]
    plot_correlations(data[variables], f"results/{name}_correlations.pdf")
    rhs = " + ".join(variables)
    model = ols(data=data, formula=f"{outcome} ~ {rhs}").fit()
    with open(f"results/{name}_summary.txt", "w") as f:
        f.write(str(model.summary()))
    results = data[["year", "state"]].copy()
    results.loc[:, "y_true"] = data[outcome]
    results.loc[:, "y_pred"] = model.predict(data)
    results.to_csv(f"results/{name}_results.csv", index=False)

estimate_model("over_payment")
estimate_model("under_payment")
