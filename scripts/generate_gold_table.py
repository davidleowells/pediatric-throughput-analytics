import pandas as pd
from pathlib import Path

INPUT = Path("data/pediatric_encounters_bronze.csv")
OUTPUT = Path("data/pediatric_encounters_gold.csv")

def age_group(age):
    if age == 0:
        return "Infant"
    if 1 <= age <= 12:
        return "Child"
    return "Adolescent"

def los_category(days):
    if days == 0:
        return "Same-day"
    if 1 <= days <= 3:
        return "Short stay (1-3 days)"
    if 4 <= days <= 7:
        return "Moderate stay (4-7 days)"
    return "Extended stay (8+ days)"

def main():
    df = pd.read_csv(INPUT)
    df["Admit_Date"] = pd.to_datetime(df["Admit_Date"], errors="coerce")
    df["Admit_Month"] = df["Admit_Date"].dt.strftime("%Y-%m")
    df["Age_Group"] = df["Age"].apply(age_group)
    df["LOS_Category"] = df["Length_of_Stay_Days"].apply(los_category)
    df["Long_Stay_Flag"] = (df["Length_of_Stay_Days"] >= 4).astype(int)
    df["Readmit_Status"] = df["Readmit_30_Day_Flag"].map({1: "Readmitted within 30 days", 0: "Not readmitted"})
    df["Admission_Type"] = df["Admission_Type"].str.strip().str.title()
    df["Department"] = df["Department"].str.strip()
    df["Discharge_Status"] = df["Discharge_Status"].str.strip()
    df["Admit_Date"] = df["Admit_Date"].dt.strftime("%Y-%m-%d")
    df.to_csv(OUTPUT, index=False)
    print(f"Wrote {OUTPUT} with {len(df):,} rows")

if __name__ == "__main__":
    main()
