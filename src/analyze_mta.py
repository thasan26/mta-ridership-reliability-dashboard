"""
MTA Ridership & Service Reliability Analytics Dashboard
Author: Tasfia Hasan

Purpose:
Analyze ridership, recovery percentage, delay minutes, and incident patterns
to support data analyst-style reporting for transit reliability.

Run:
    pip install -r requirements.txt
    python src/analyze_mta.py
"""

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "mta_ridership_reliability_sample.csv"
REPORT_DIR = ROOT / "reports"
REPORT_DIR.mkdir(exist_ok=True)

def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

def create_kpi_summary(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Mode").agg(
        Total_Ridership=("Daily_Ridership", "sum"),
        Average_Daily_Ridership=("Daily_Ridership", "mean"),
        Average_Recovery_Percentage=("Recovery_Percentage", "mean"),
        Total_Delay_Minutes=("Delay_Minutes", "sum"),
        Incident_Count=("Incident_Type", lambda s: (s != "No Incident").sum())
    ).reset_index()

def identify_high_delay_segments(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    incident_df = df[df["Incident_Type"] != "No Incident"]
    return (
        incident_df.groupby(["Mode", "Line_or_Route", "Borough_or_Region", "Incident_Type"])
        .agg(
            Total_Delay_Minutes=("Delay_Minutes", "sum"),
            Average_Recovery_Percentage=("Recovery_Percentage", "mean"),
            Incident_Count=("Incident_Type", "count")
        )
        .sort_values("Total_Delay_Minutes", ascending=False)
        .head(top_n)
        .reset_index()
    )

def main():
    df = load_data(DATA_PATH)
    summary = create_kpi_summary(df)
    high_delay = identify_high_delay_segments(df)

    summary.to_csv(REPORT_DIR / "mode_summary.csv", index=False)
    high_delay.to_csv(REPORT_DIR / "top_delay_segments.csv", index=False)

    print("KPI summary saved to reports/mode_summary.csv")
    print("Top delay segments saved to reports/top_delay_segments.csv")
    print("\nTop 5 high-delay findings:")
    print(high_delay.head().to_string(index=False))

if __name__ == "__main__":
    main()
