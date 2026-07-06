# Data Dictionary

## Source Table: pediatric_encounters_bronze

| Field | Type | Description |
|---|---|---|
| Patient_ID | Text | Synthetic patient identifier |
| Encounter_ID | Text | Unique synthetic encounter identifier |
| Age | Integer | Patient age in years |
| Admit_Date | Date | Encounter admission date |
| Admission_Type | Text | Elective, Emergency, or Urgent |
| Department | Text | Emergency Department, General Pediatrics, PICU, or NICU |
| Length_of_Stay_Days | Integer | Length of stay in days |
| Discharge_Status | Text | Discharged Home, Transferred, or Observation/Follow-up |
| Readmit_30_Day_Flag | Integer | 1 if readmitted within 30 days; otherwise 0 |

## Curated Table: pediatric_encounters_gold

The gold table contains all source fields plus derived fields used for reporting.

| Field | Type | Description |
|---|---|---|
| Admit_Month | Text | Year-month value derived from Admit_Date |
| Age_Group | Text | Infant, Child, or Adolescent |
| LOS_Category | Text | Same-day, Short stay, Moderate stay, or Extended stay |
| Long_Stay_Flag | Integer | 1 if Length_of_Stay_Days >= 4; otherwise 0 |
| Readmit_Status | Text | Readmitted within 30 days or Not readmitted |

## Transformation Notes

- Age group logic: age 0 = Infant; ages 1-12 = Child; ages 13+ = Adolescent.
- LOS category logic: 0 days = Same-day; 1-3 days = Short stay; 4-7 days = Moderate stay; 8+ days = Extended stay.
- Long stay logic: encounters with LOS >= 4 days are flagged as long stays.
