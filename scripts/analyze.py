
"""
Statistical analysis of Finnish clay geotechnical data.

Laboratory 3 - ING8100
Polytechnique Montreal

Outputs:
- results/geotechnical_statistics.csv
- figures/mean_water_content.png
- figures/undrained_strength_boxplot.png
"""

from pathlib import Path
import pandas as pd
import matplotlib

# Non-interactive backend for reproducible figure generation
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# Project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = (
    PROJECT_ROOT / "data" / "processed"
    / "laboratory_data_clean.csv"
)

RESULTS_DIR = PROJECT_ROOT / "results"
FIGURES_DIR = PROJECT_ROOT / "figures"

SITES = ["Haarajoki", "Suurpelto", "Tolsa", "POKO"]
VARIABLES = ["w0", "su", "gamma"]


def analyze_data():
    """Calculate geotechnical indicators and generate figures."""

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            "Processed dataset not found. "
            "Run preprocess.py first."
        )

    # Load processed dataset
    df = pd.read_csv(INPUT_FILE)

    required_columns = ["site"] + VARIABLES
    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    # Convert analysis variables to numeric
    for variable in VARIABLES:
        df[variable] = pd.to_numeric(
            df[variable], errors="coerce"
        )

    # Calculate statistical indicators
    statistics = (
        df.groupby("site")[VARIABLES]
        .agg(["count", "mean", "std"])
        .round(3)
    )

    statistics.to_csv(
        RESULTS_DIR / "geotechnical_statistics.csv"
    )

    print("Geotechnical statistics:")
    print(statistics)

    # Figure 1: Mean initial water content
    water_stats = (
        df.groupby("site")["w0"]
        .agg(["mean", "count"])
        .reindex(SITES)
        .dropna(subset=["mean"])
    )

    if water_stats.empty:
        raise ValueError("No valid water content measurements.")

    fig, ax = plt.subplots(figsize=(9, 5))

    bars = ax.bar(
        water_stats.index,
        water_stats["mean"]
    )

    ax.set_title(
        "Mean Initial Water Content by Clay Deposit"
    )
    ax.set_xlabel("Clay Deposit")
    ax.set_ylabel(
        "Natural Water Content (%)"
    )

    for bar, count in zip(
        bars, water_stats["count"]
    ):
        ax.annotate(
            f"n={count}",
            (
                bar.get_x() + bar.get_width() / 2,
                bar.get_height()
            ),
            xytext=(0, 5),
            textcoords="offset points",
            ha="center"
        )

    ax.set_ylim(
        0, water_stats["mean"].max() * 1.2
    )

    fig.tight_layout()
    fig.savefig(
        FIGURES_DIR / "mean_water_content.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.close(fig)

    # Figure 2: Undrained shear strength distribution
    strength_data = [
        df.loc[df["site"] == site, "su"]
        .dropna()
        .to_numpy()
        for site in SITES
    ]

    valid = [
        (site, values)
        for site, values in zip(SITES, strength_data)
        if len(values) > 0
    ]

    if not valid:
        raise ValueError(
            "No valid undrained shear strength measurements."
        )

    valid_sites = [item[0] for item in valid]
    valid_data = [item[1] for item in valid]

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.boxplot(
        valid_data,
        tick_labels=valid_sites,
        showmeans=True
    )

    ax.set_title(
        "Undrained Shear Strength by Clay Deposit"
    )
    ax.set_xlabel("Clay Deposit")
    ax.set_ylabel(
        "Undrained Shear Strength (kPa)"
    )
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()
    fig.savefig(
        FIGURES_DIR / "undrained_strength_boxplot.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.close(fig)

    print("\nAnalysis completed successfully.")
    print("Results directory:", RESULTS_DIR)
    print("Figures directory:", FIGURES_DIR)


if __name__ == "__main__":
    analyze_data()
