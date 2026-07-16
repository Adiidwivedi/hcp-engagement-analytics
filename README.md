# HCP Engagement Analytics: Optimizing Pharma Sales Rep Targeting

## Business Problem
Pharma sales reps visit doctors (HCPs) to promote medicines, but without
data-driven prioritization, visit effort is often misallocated — high-potential
doctors get overlooked while low-potential doctors receive repeat visits.
This project analyzes rep-doctor engagement data to identify high-potential
doctors, evaluate rep effectiveness, and recommend optimized visit allocation.

## Objective
- Segment doctors by prescription growth potential (High / Medium / Low)
- Rank sales reps by effectiveness (prescription lift per visit)
- Identify at-risk doctors with declining engagement
- Quantify visit-allocation gaps and recommend fixes

## Dataset
Synthetically generated dataset (Python + Faker) simulating real pharma
sales operations:
- 500 doctors across 5 regions and 5 specialties
- 25 sales reps with varying experience levels
- 3,904 visit records over 12 months, each with pre/post prescription counts

Real HCP-level prescription data is not publicly available due to
healthcare data privacy regulations, so a realistic synthetic dataset with
built-in statistical relationships (rep experience → prescription lift) was
generated to simulate authentic business patterns.

## Tech Stack
- **SQL (SQLite)** — ETL pipeline, view creation, KPI calculation using
  window functions (RANK, LAG)
- **Python (pandas, Faker)** — synthetic data generation
- **Power BI** — interactive dashboard (visuals also available as static
  charts in this repo; `.pbix` file can be rebuilt using `sql/analysis_queries.sql`
  outputs as source data)

## Approach
1. Generated a realistic synthetic pharma engagement dataset
2. Loaded data into SQLite and built an ETL pipeline: cleaned records,
   checked for duplicates/nulls, created analytical views
3. Calculated prescription lift (after − before) per visit as the core metric
4. Used SQL window functions to rank reps by effectiveness and track
   month-over-month visit trends
5. Segmented doctors into High/Medium/Low potential tiers based on average
   prescription lift
6. Built dashboard visuals to surface actionable insights

## Key Insights (from actual query results)
- **Coverage gap identified:** High-Potential doctors (2.6% of total) receive
  only **4.8 average visits**, while Low and Medium potential doctors receive
  **7.7–8.2 average visits** — meaning the highest-impact doctors are
  currently under-served relative to their potential.
- **Rep performance spread:** Top-ranked rep achieves **4.85 avg prescription
  lift per visit** vs a much lower spread among bottom-ranked reps —
  indicating a training/technique gap worth closing.
- **Regional variance:** South and Central regions show the highest average
  prescription lift (2.58 and 2.56), while West lags at 1.79 — suggesting
  region-specific engagement strategies are needed.
- **19 doctors** flagged as "at-risk" — showing negative average prescription
  lift, signaling declining engagement that needs intervention.

## Business Recommendation
Reallocate visit frequency toward the High-Potential segment (currently
under-visited relative to impact), replicate top-performing reps' engagement
approach across low-ranked reps via targeted coaching, and prioritize
outreach to the 19 at-risk doctors before they fully disengage.

## Dashboard Preview
![Dashboard](dashboard/dashboard_screenshot.png)

## Repository Structure
```
hcp-engagement-analytics/
├── data/                    # doctors.csv, reps.csv, visits.csv
├── scripts/generate_data.py # synthetic dataset generator
├── sql/
│   ├── schema.sql           # table definitions
│   ├── etl_transform.sql    # cleaning + view creation
│   └── analysis_queries.sql # KPI extraction queries
├── dashboard/
│   └── dashboard_screenshot.png
└── README.md
```

## How to Run
1. `pip install pandas numpy faker`
2. `python scripts/generate_data.py` → generates CSVs in `data/`
3. Load CSVs into a SQLite database (or run via pandas `to_sql`)
4. Run `sql/etl_transform.sql` to build views
5. Run `sql/analysis_queries.sql` to extract KPIs
6. Import views/query results into Power BI for interactive dashboard
