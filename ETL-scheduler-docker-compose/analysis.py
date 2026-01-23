import pandas as pd
import matplotlib.pyplot as plt
import glob


def parse_mem(mem_str):
    """Converts Docker memory strings (e.g., '10.25MiB / 7.6GiB') to float MiB."""
    try:
        val = mem_str.split(" / ")[0].strip()
        if "GiB" in val:
            return float(val.replace("GiB", "")) * 1024
        elif "MiB" in val:
            return float(val.replace("MiB", ""))
        elif "KiB" in val:
            return float(val.replace("KiB", "")) / 1024
        return float(val)
    except:
        return 0.0


def generate_report(num_jobs=5):
    """
    Reads all results_*.csv files, plots the data, and calculates
    efficiency metrics for the Medium article summary.
    """
    plt.figure(figsize=(12, 7))
    summary_data = []

    # 1. FIX: Only look for the raw data files, skip summary reports
    csv_files = glob.glob("results/*.csv")

    # Filter out the summary file if it accidentally matches the pattern
    csv_files = [f for f in csv_files if "summary" not in f.lower()]

    if not csv_files:
        print(
            "No CSV files found. Ensure you have files like results_ofelia.csv in the directory."
        )
        return

    for file in csv_files:
        name = file.replace(".csv", "").capitalize()
        df = pd.read_csv(file)

        if "Timestamp" not in df.columns:
            print(f"⚠️ Warning: No headers found in {file}. Assigning default names.")
            # Manually assign names based on our benchmark.sh format
            df.columns = ["Timestamp", "Container", "CPU_Perc", "Mem_Usage", "Mem_Perc"]

        # Data Cleaning
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], format="%H:%M:%S")
        df["Mem_MiB"] = df["Mem_Usage"].apply(parse_mem)

        # Data Cleaning
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], format="%H:%M:%S")
        df["Mem_MiB"] = df["Mem_Usage"].apply(parse_mem)

        # Group by timestamp (summing all containers in the stack)
        timeline = df.groupby("Timestamp")["Mem_MiB"].sum().reset_index()

        # Calculate Stats
        idle_mem = timeline["Mem_MiB"].min()
        peak_mem = timeline["Mem_MiB"].max()
        avg_mem = timeline["Mem_MiB"].mean()

        # Efficiency Metric: RAM 'Tax' per Job
        # (Peak RAM / Number of jobs fired during the 5-min window)
        efficiency = peak_mem / num_jobs

        summary_data.append(
            {
                "Orchestrator": name,
                "Idle_RAM_MiB": round(idle_mem, 2),
                "Peak_RAM_MiB": round(peak_mem, 2),
                "Avg_RAM_MiB": round(avg_mem, 2),
                "RAM_Per_Job": round(efficiency, 2),
            }
        )

        # Plot the timeline
        plt.plot(
            timeline["Timestamp"],
            timeline["Mem_MiB"],
            label=f"{name} (Peak: {peak_mem:.1f}MB)",
            linewidth=2,
        )

    # Styling the Plot
    plt.title("Infrastructure Tax: Memory Usage Over Time", fontsize=16, pad=20)
    plt.xlabel("Time (5-Minute Window)", fontsize=12)
    plt.ylabel("Total Stack Memory (MiB)", fontsize=12)
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save visuals
    plt.savefig("results/orchestrator_efficiency_chart.png")

    # Create and save summary table
    summary_df = pd.DataFrame(summary_data).sort_values(by="Peak_RAM_MiB")
    summary_df.to_csv("results/final_summary_report.csv", index=False)

    print("\n--- BENCHMARK SUMMARY REPORT ---")
    print(summary_df.to_markdown(index=False))
    print("\nVisuals saved to: orchestrator_efficiency_chart.png")
    print("Data saved to: final_summary_report.csv")


if __name__ == "__main__":
    # Assuming 5 jobs ran during the 5-minute benchmark
    generate_report(num_jobs=5)
