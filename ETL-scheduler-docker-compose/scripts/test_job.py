import datetime
import sys


def main():
    now = datetime.datetime.now()
    print(f"--- ETL Job Started at {now} ---")
    print("Processing data...")
    print("Job completed successfully!")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
