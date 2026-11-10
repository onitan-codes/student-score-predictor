from pathlib import Path
import pandas as pd
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "record.csv"
RESULTS_FILE = BASE_DIR / "record_with_results.csv"
CHART_FILE = BASE_DIR / "screenshots" / "pass-fail-chart.png"
PASS_MARK = 60


def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Sample data not found: {DATA_FILE}")

    df = pd.read_csv(DATA_FILE)
    if "previous_score" not in df.columns:
        raise ValueError("record.csv must contain a 'previous_score' column.")

    df["result"] = df["previous_score"].apply(
        lambda score: "Pass" if score >= PASS_MARK else "Fail"
    )
    counts = df["result"].value_counts().reindex(["Pass", "Fail"], fill_value=0)

    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(RESULTS_FILE, index=False)

    CHART_FILE.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(counts.index, counts.values, color=["#198754", "#dc3545"])
    ax.set_title("Synthetic Sample: Pass and Fail Counts")
    ax.set_xlabel("Result")
    ax.set_ylabel("Number of records")
    ax.bar_label(bars, padding=3)
    ax.set_ylim(0, max(counts.max() + 3, 5))
    fig.tight_layout()
    fig.savefig(CHART_FILE, dpi=160, bbox_inches="tight")
    plt.close(fig)

    print(f"Processed {len(df)} synthetic sample records.")
    print(f"Pass: {counts['Pass']} | Fail: {counts['Fail']}")
    print(f"Results saved to: {RESULTS_FILE.name}")
    print(f"Chart saved to: {CHART_FILE.relative_to(BASE_DIR)}")


if __name__ == "__main__":
    main()
