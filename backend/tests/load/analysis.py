#!/usr/bin/env python3
"""
Quick post-run report: finds _stats_history.csv & spits out Markdown.
"""
import csv
import os
import sys

def main():
    csv_path = next(p for p in os.listdir() if p.endswith("_stats_history.csv"))
    reqs = []
    times = []
    with open(csv_path) as f:
        rd = csv.DictReader(f)
        for row in rd:
            reqs.append(int(row["Total Request Count"]))
            times.append(float(row["Average Response Time"]))
    avg_t = sum(times[-5:]) / 5          # last 5 samples
    lat95 = sorted(times)[int(len(times) * .95)]
    print("### Load-test summary")
    print(f"- Peak **{max(reqs)}** requests.")
    print(f"- Final 5-samples Avg RT ≈ **{avg_t:.2f} ms**.")
    print(f"- 95th percentile latency ≈ **{lat95:.2f} ms**.")
    return 0 if avg_t < 500 else 1

if __name__ == "__main__":
    sys.exit(main())
