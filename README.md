# MTA Ridership & Service Reliability Analytics Dashboard

**Author:** Tasfia Hasan  
**Role alignment:** Data Analyst / Research Assistant / Transit Analytics  
**Tools:** Python, pandas, Excel-ready CSV, Power BI-ready dataset, data cleaning, KPI analysis, dashboard reporting

## Project Overview
This project analyzes transit ridership and service reliability patterns using a structured dataset designed for MTA-style analytics. The goal is to show how data can be cleaned, summarized, and turned into decision-support insights for ridership recovery, service reliability, and operational delays.

## Business / Research Questions
- Which transit modes have the highest ridership and strongest recovery percentage?
- Which incident categories contribute the most delay minutes?
- Which lines/routes and regions should be prioritized for deeper root-cause analysis?
- How can KPI tracking support leadership reporting and operational planning?

## Key Features
- Cleaned and structured a dataset with ridership, recovery percentage, delay minutes, incident type, route, region, and peak period fields.
- Built KPI summaries for total ridership, average daily ridership, average recovery percentage, total delay minutes, and incident counts.
- Identified high-delay route/region combinations to support root-cause analysis.
- Generated chart-ready outputs for Power BI, Excel Pivot Tables, and dashboard screenshots.

## Resume-Aligned Bullet Points
- Built a transit analytics dashboard using **Python, Excel, and Power BI-ready data** to track ridership, recovery percentage, delay minutes, and incident patterns across multiple transit modes.
- Cleaned and transformed structured ridership data into KPI summaries, reducing manual reporting work by creating reusable CSV outputs for dashboarding and leadership review.
- Identified high-delay route and incident patterns using grouped analysis, supporting root-cause analysis for service reliability improvement.

## Folder Structure
```text
mta-ridership-reliability-dashboard/
│
├── data/
│   └── mta_ridership_reliability_sample.csv
├── reports/
│   ├── mode_summary.csv
│   ├── top_delay_segments.csv
│   └── figures/
│       ├── subway_ridership_trend.png
│       ├── delay_by_incident_type.png
│       └── recovery_by_mode.png
├── src/
│   └── analyze_mta.py
├── requirements.txt
└── README.md
```

## How to Run
```bash
pip install -r requirements.txt
python src/analyze_mta.py
```

## Dashboard Suggestions for Power BI
Use the dataset in `data/mta_ridership_reliability_sample.csv`.

 visuals:
- KPI cards: Total Ridership, Average Recovery %, Total Delay Minutes, Incident Count
- Line chart: Date vs Daily Ridership
- Bar chart: Delay Minutes by Incident Type
- Matrix/table: Mode, Route, Region, Delay Minutes, Recovery %
- Slicer: Mode, Borough/Region, Incident Type, Peak Period

## Notes
This is a project using a public-analytics style sample dataset. It is designed to demonstrate data analyst skills, dashboard thinking, and transportation reliability analysis.
