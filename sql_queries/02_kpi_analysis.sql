-- KPI 1: Prescription Growth Trends Using LAG
SELECT visit_id, doctor_name, rep_name, visit_date, prescriptions_after,
    LAG(prescriptions_after, 1, 0) OVER (PARTITION BY doctor_name ORDER BY visit_date) AS previous_visit_prescriptions,
    (prescriptions_after - LAG(prescriptions_after, 1, prescriptions_before) OVER (PARTITION BY doctor_name ORDER BY visit_date)) AS sequential_growth_lift
FROM view_visit_impact_summary ORDER BY doctor_name, visit_date;

-- KPI 2: Sales Representative Performance Ranking Using DENSE_RANK()
SELECT rep_name, doctor_region, SUM(prescription_lift) AS total_prescription_gain,
    DENSE_RANK() OVER (PARTITION BY doctor_region ORDER BY SUM(prescription_lift) DESC) as regional_rep_rank
FROM view_visit_impact_summary GROUP BY rep_name, doctor_region;
