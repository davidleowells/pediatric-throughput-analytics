import pandas as pd
from pathlib import Path

BRONZE = Path("data/pediatric_encounters_bronze.csv")
GOLD = Path("data/pediatric_encounters_gold.csv")

def pct(n, d):
    return 0 if d == 0 else 100 * n / d

def main():
    bronze = pd.read_csv(BRONZE)
    gold = pd.read_csv(GOLD)
    print("Row count validation")
    print(f"Bronze rows: {len(bronze):,}")
    print(f"Gold rows:   {len(gold):,}")
    print(f"Difference:  {len(gold) - len(bronze):,}")
    print()

    print("Identifier validation")
    print(f"Unique Encounter_ID values: {gold['Encounter_ID'].nunique():,}")
    print(f"Duplicate Encounter_ID values: {gold['Encounter_ID'].duplicated().sum():,}")
    print()

    print("KPI validation")
    total = len(gold)
    print(f"Total Encounters: {total:,}")
    print(f"Average LOS: {gold['Length_of_Stay_Days'].mean():.2f}")
    print(f"Emergency Admission %: {pct((gold['Admission_Type'] == 'Emergency').sum(), total):.1f}%")
    print(f"Long Stay Rate: {pct((gold['Length_of_Stay_Days'] >= 4).sum(), total):.1f}%")
    print(f"30-Day Readmission Rate: {pct(gold['Readmit_30_Day_Flag'].sum(), total):.1f}%")

if __name__ == "__main__":
    main()
