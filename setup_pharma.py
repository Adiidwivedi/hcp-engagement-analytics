import pandas as pd
import numpy as np
from faker import Faker
import random
import sqlite3  # SQL export ke liye add kiya

fake = Faker('en_IN')
np.random.seed(42)
random.seed(42)

# ---- 1. Doctors Table (500 doctors) ----
specialties = ['Cardiology', 'Oncology', 'Neurology', 'Endocrinology', 'General Physician']
regions = ['North', 'South', 'East', 'West', 'Central']

doctors = []
for i in range(1, 501):
    doctors.append({
        'doctor_id': f'D{i:04d}',
        'doctor_name': fake.name(),
        'specialty': random.choice(specialties),
        'region': random.choice(regions),
        'hospital_type': random.choice(['Private', 'Government', 'Clinic']),
        'baseline_prescriptions': np.random.randint(5, 100)  # monthly avg before any visits
    })
doctors_df = pd.DataFrame(doctors)

# ---- 2. Reps Table (25 sales reps) ----
reps = []
for i in range(1, 26):
    reps.append({
        'rep_id': f'R{i:03d}',
        'rep_name': fake.name(),
        'region': random.choice(regions),
        'experience_years': np.random.randint(1, 15)
    })
reps_df = pd.DataFrame(reps)

# ---- 3. Visits Table (5000 visit records over 12 months) ----
visits = []
visit_id = 1
for _, doc in doctors_df.iterrows():
    num_visits = np.random.randint(2, 15)  # kitni baar visit hui saal bhar mein
    matching_reps = reps_df[reps_df['region'] == doc['region']]
    if len(matching_reps) == 0:
        matching_reps = reps_df
    for v in range(num_visits):
        rep = matching_reps.sample(1).iloc[0]
        visit_date = fake.date_between(start_date='-365d', end_date='today')
        
        # Safe Date Conversion (SQLite compatibility)
        visit_date_str = visit_date.strftime('%Y-%m-%d')
        
        # Effective rep + good doctor engagement -> better prescription lift
        rep_skill = rep['experience_years'] / 15
        lift_factor = np.random.normal(loc=rep_skill * 5, scale=3)
        prescriptions_after = max(0, doc['baseline_prescriptions'] + lift_factor)
        
        visits.append({
            'visit_id': visit_id,
            'doctor_id': doc['doctor_id'],
            'rep_id': rep['rep_id'],
            'visit_date': visit_date_str,  # Saved as clean string
            'prescriptions_before': doc['baseline_prescriptions'],
            'prescriptions_after': round(prescriptions_after, 1)
        })
        visit_id += 1

visits_df = pd.DataFrame(visits)

# ---- Save as CSV ----
doctors_df.to_csv('doctors.csv', index=False)
reps_df.to_csv('reps.csv', index=False)
visits_df.to_csv('visits.csv', index=False)

# ---- AUTOMATIC SQL EXPORT (Added for ETL step) ----
db_name = "pharma_data.db"
conn = sqlite3.connect(db_name)

# Tables ko database me write kar rahe hain
doctors_df.to_sql('doctors', conn, if_exists='replace', index=False)
reps_df.to_sql('reps', conn, if_exists='replace', index=False)
visits_df.to_sql('visits', conn, if_exists='replace', index=False)

conn.close()

print("Files created: doctors.csv, reps.csv, visits.csv")
print(f"Database created: '{db_name}' with 3 tables loaded successfully!")
print(f"Doctors: {len(doctors_df)}, Reps: {len(reps_df)}, Visits: {len(visits_df)}")