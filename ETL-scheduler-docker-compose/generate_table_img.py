import pandas as pd
import matplotlib.pyplot as plt


def save_table_as_img(df):
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.axis("tight")
    ax.axis("off")

    # Create the table
    table = ax.table(
        cellText=df.values, colLabels=df.columns, loc="center", cellLoc="center"
    )
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.2)  # Adjust size

    plt.savefig("results/final_results_table.png", dpi=300, bbox_inches="tight")


def main():
    df = pd.read_csv("results/final_summary_report.csv")
    save_table_as_img(df)


if __name__ == "__main__":
    main()
