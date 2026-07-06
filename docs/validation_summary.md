# Validation Summary

This summary documents basic source-to-report validation checks for the synthetic pediatric encounter dataset.

## Row Counts

| Check | Result |
|---|---:|
| Bronze row count | 1,000 |
| Gold row count | 1,000 |
| Difference | 0 |

## Missing Values

No missing values were found in the source dataset across the core encounter fields.

## Unique Identifiers

| Field | Unique Count |
|---|---:|
| Patient_ID | 1,000 |
| Encounter_ID | 1,000 |

## Department Counts and Average LOS

| Department           |   Total_Encounters |   Average_LOS |
|:---------------------|-------------------:|--------------:|
| Emergency Department |                553 |          0.28 |
| General Pediatrics   |                194 |          2.85 |
| PICU                 |                138 |         11.53 |
| NICU                 |                115 |         17.17 |

## Monthly Encounter Volume

| Admit_Month   |   Total_Encounters |
|:--------------|-------------------:|
| 2025-01       |                179 |
| 2025-02       |                178 |
| 2025-03       |                223 |
| 2025-04       |                211 |
| 2025-05       |                209 |

## LOS Category Distribution

| LOS_Category             |   Percent_of_Encounters |
|:-------------------------|------------------------:|
| Same-day                 |                    39.9 |
| Short stay (1-3 days)    |                    28.2 |
| Extended stay (8+ days)  |                    22.7 |
| Moderate stay (4-7 days) |                     9.2 |

## KPI Reconciliation

| KPI | Value |
|---|---:|
| Total Encounters | 1,000 |
| Average LOS | 4.27 |
| Emergency Admission % | 76.2% |
| Long Stay Rate | 31.9% |
| 30-Day Readmission Rate | 5.7% |
