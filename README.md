# HCP Engagement Analytics: Optimizing Pharma Sales Rep Targeting
`Repository Name: hcp-engagement-analytics`

## 💼 Business Problem
Pharmaceutical medical representatives frequently visit Healthcare Professionals (HCPs) to drive brand adoption. However, without analytical territory planning, visit frequencies are routinely misallocated—leaving high-potential clinicians underserved while low-potential accounts receive redundant engagement loops. 

This project engineers an end-to-end data processing pipeline and business intelligence framework to segment clinicians by value, rank field force effectiveness, identify churn risks, and optimize commercial resource allocation.

## 🎯 Strategic Objectives
* **HCP Segmentation:** Classify doctors into actionable strategic tiers (High / Medium / Low potential) based on historical adoption capacity.
* **Sales Force Effectiveness Index:** Compute strict regional performance benchmarks to rank representatives by incremental value generated per engagement.
* **Attrition Risk Inversion:** Systematically isolate at-risk accounts showing declining post-visit brand engagement.
* **Operational Gap Analysis:** Quantify current territory coverage inefficiencies and formulate targeted corrective field action plans.

## 📊 Dataset Ingestion & Architecture
Real HCP-level prescription behavior data is heavily protected under global healthcare privacy standards (e.g., HIPAA). To model real-world complexities, this framework utilizes a synthetically compiled, statistically correlated dataset engineered to simulate multi-layered pharma operations:
* **500 Doctors Master Registry:** Distributed across 5 geographic regions and 5 core medical therapeutic specialties.
* **25 Field Sales Representatives:** Mapped dynamically by tenure, experience metrics, and territory distribution rules.
* **3,904 Transactional Interaction Records:** Longitudinal data captured across a 12-month period, mapping absolute baseline, pre-visit, and post-visit volumetric performance shifts.

## 🛠️ Production Tech Stack
* **Python (pandas, NumPy):** Powers the core Extract-Transform-Load (ETL) pipeline, data generation protocols, and preliminary structural validations.
* **SQL (SQLite Engine):** Serves as the high-performance storage and analytical engine—utilizing complex table constraints, optimized staging views, and execution-ready **Window Functions (`LAG`, `DENSE_RANK`)**.
* **Power BI Desktop:** Delivers the interactive executive business intelligence workspace driving cross-filtering dashboard diagnostics, territory reviews, and action triggers.

## ⚙️ Core Analytical Approach
1. **ETL Pipeline & Ingestion:** Ingest raw relational attributes into an optimized SQLite staging layer while asserting data integrity, strict null-value pruning, and primary-foreign key relationships.
2. **Back-End Metrics Optimization:** Rather than forcing rendering lag on the BI front-end, complex metric processing—specifically "Prescription Lift" ($Post-Visit\ Volume - Pre-Visit\ Volume$)—is computed directly at the database view level.
3. **Advanced Window Querying:** Longitudinal drift is derived via SQL `LAG` arrays to trace chronological drop alerts per account, while `DENSE_RANK` partitions absolute rep performance across regional bounds.
4. **BI Cross-Filtering Mapping:** Establish a low-latency relational data model (Star Schema) in Power BI Desktop to translate analytical data arrays into responsive executive cockpits.

## 🚀 Key Data-Driven Insights
* **Territory Coverage Discrepancy:** High-Potential clinicians (2.6% of the overall registry) average only **4.8 interactions annually**, contrasted against an over-indexed **7.7 to 8.2 average visits** targeting Low/Medium potential segments—exposing a massive strategic misallocation of commercial resources.
* **Performance Variance & Technique Gap:** The top-ranked field representative secures an exceptional **4.85 average prescription lift per visit**, highlighting a substantial execution spread over bottom-quartile performers that indicates clear training deficits.
* **Geographic Market Dynamics:** The South and Central operational zones lead aggregate velocity with strong regional metrics (2.58 and 2.56 average lift), while the West territory drops sharply to 1.79, signaling a need for instant localized pricing or positioning re-evaluation.
* **Proactive Risk Intervention:** Isolated **19 high-risk clinicians** exhibiting net-negative sequential prescription deltas, providing field managers with an immediate target list for churn prevention outreach.

## 💡 Business Recommendations
* **Commercial Realignment:** Shift field representative visit targets immediately toward the High-Potential clinician cohort to convert untapped high-margin value.
* **Field Force Standardization:** Code and institutionalize the engagement framework used by the top-quartile reps into centralized playbooks, scaling peak execution across lower-ranked reps through structured field coaching.
* **Targeted Churn Preemption:** Deploy priority outreach schedules focusing on the 19 identified at-risk clinicians to rebuild disengaging accounts before complete conversion loss occurs.

## 📂 Repository Blueprint
```text
hcp-engagement-analytics/
├── data/                    # Ingested entities: doctors.csv, reps.csv, visits.csv
├── sql_queries/
│   ├── 01_schema_and_views.sql  # Database DDL structure, constraints, and optimization views
│   └── 02_kpi_analysis.sql      # Production window execution (LAG, DENSE_RANK, Tiering)
├── setup_pharma.py          # Central automated ingestion & pipeline initialization script
├── pharma_analytics.pbix    # Production Power BI Dashboard analytical file
└── README.md                # System documentation
