-- Create Doctors Master Dimension Table
CREATE TABLE IF NOT EXISTS doctors (
    doctor_id INTEGER PRIMARY KEY,
    doctor_name TEXT NOT NULL,
    specialty TEXT NOT NULL,
    region TEXT NOT NULL,
    hospital_type TEXT NOT NULL,
    baseline_prescriptions INTEGER NOT NULL
);

-- Create Sales Representatives Dimension Table
CREATE TABLE IF NOT EXISTS reps (
    rep_id INTEGER PRIMARY KEY,
    rep_name TEXT NOT NULL,
    region TEXT NOT NULL,
    experience_years INTEGER NOT NULL
);

-- Create Sales Visits Fact Table
CREATE TABLE IF NOT EXISTS visits (
    visit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INTEGER,
    rep_id INTEGER,
    visit_date TEXT NOT NULL,
    prescriptions_before INTEGER NOT NULL,
    prescriptions_after INTEGER NOT NULL,
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id),
    FOREIGN KEY (rep_id) REFERENCES reps(rep_id)
);

-- Analytical View
CREATE VIEW IF NOT EXISTS view_visit_impact_summary AS
SELECT 
    v.visit_id, v.visit_date, d.doctor_name, d.specialty, d.region AS doctor_region,
    d.baseline_prescriptions, r.rep_name, r.experience_years,
    v.prescriptions_before, v.prescriptions_after,
    (v.prescriptions_after - v.prescriptions_before) AS prescription_lift
FROM visits v
JOIN doctors d ON v.doctor_id = d.doctor_id
JOIN reps r ON v.rep_id = r.rep_id;
