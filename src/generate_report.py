import argparse
import pandas as pd

from src.kpis import compute_kpis


def main():
    parser = argparse.ArgumentParser(description="Generate KPI snapshot report from a CSV.")
    parser.add_argument("--input", required=True, help="Path to input CSV (e.g. data/sample/paysim_sample.csv)")
    parser.add_argument("--output", default="reports/kpi_snapshot.md", help="Path to output markdown report")
    args = parser.parse_args()

    df = pd.read_csv(args.input)

    kpis = compute_kpis(df)

    lines = []
    lines.append("# KPI Snapshot\n")
    lines.append(f"Source file: `{args.input}`\n")
    lines.append("\n## KPIs\n\n")

    # Markdown table
    lines.append("| KPI | Value |\n")
    lines.append("|---|---|\n")
    for _, row in kpis.iterrows():
        lines.append(f"| {row['KPI']} | {row['Value']} |\n")

    with open(args.output, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"Wrote report to {args.output}")


if __name__ == "__main__":
    main()

