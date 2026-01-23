import pandas as pd
import matplotlib.pyplot as plt
import glob
import os


def parse_mem(mem_str):
    """Converts Docker memory strings (e.g., '10.25MiB / 7.6GiB') to float MiB."""
    try:
        val = str(mem_str).split(" / ")[0].strip()
        if "GiB" in val:
            return float(val.replace("GiB", "")) * 1024
        if "MiB" in val:
            return float(val.replace("MiB", ""))
        if "KiB" in val:
            return float(val.replace("KiB", "")) / 1024
        return float("".join(c for c in val if c.isdigit() or c == "."))
    except:
        return 0.0


plt.figure(figsize=(12, 7))
files_found = 0

search_patterns = ["results/*.csv"]

for pattern in search_patterns:
    for file in glob.glob(pattern):
        # SKIP summary files to avoid the ValueError
        if "summary" in file.lower() or "report" in file.lower():
            continue

        base_name = os.path.basename(file)
        name = base_name.replace("results_", "").replace(".csv", "").capitalize()

        try:
            df = pd.read_csv(file)

            # Defensive check for headers
            if "Timestamp" not in df.columns:
                df.columns = [
                    "Timestamp",
                    "Container",
                    "CPU_Perc",
                    "Mem_Usage",
                    "Mem_Perc",
                ]

            # Use mixed format and coerce errors to avoid crashing on a single bad row
            df["Timestamp"] = pd.to_datetime(
                df["Timestamp"], format="%H:%M:%S", errors="coerce"
            )
            df = df.dropna(subset=["Timestamp"])

            if df.empty:
                continue

            # Normalize Time to start at 0
            start_time = df["Timestamp"].min()
            df["Seconds"] = (df["Timestamp"] - start_time).dt.total_seconds()

            # Aggregate Memory
            df["Mem_MiB"] = df["Mem_Usage"].apply(parse_mem)
            timeline = df.groupby("Seconds")["Mem_MiB"].sum().reset_index()

            # Plot
            avg_mem = timeline["Mem_MiB"].mean()
            plt.plot(
                timeline["Seconds"],
                timeline["Mem_MiB"],
                label=f"{name} (Avg: {avg_mem:.1f}MB)",
                linewidth=2,
            )
            files_found += 1
            print(f"Processed: {name}")

        except Exception as e:
            print(f"Could not process {file}: {e}")

if files_found > 0:
    plt.yscale("log")
    plt.title("Normalized Orchestrator Memory Footprint ($T=0$)", fontsize=16)
    plt.xlabel("Seconds from Start of Benchmark", fontsize=12)
    plt.ylabel("Total Stack RAM (MiB) - Log Scale", fontsize=12)
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("results/normalized_comparison.png")
    print(f"\n✅ Done! Generated chart from {files_found} sources.")
else:
    print("\n❌ No valid result files found.")

plt.show()
