# DAX Measures

These measures were designed for the `pediatric_encounters_gold` table in the Power BI semantic model.

## Total Encounters

```DAX
Total Encounters =
COUNTROWS(pediatric_encounters_gold)
```

## Average LOS

```DAX
Average LOS =
AVERAGE(pediatric_encounters_gold[Length_of_Stay_Days])
```

## Emergency Admissions

```DAX
Emergency Admissions =
CALCULATE(
    [Total Encounters],
    pediatric_encounters_gold[Admission_Type] = "Emergency"
)
```

## Emergency Admission %

```DAX
Emergency Admission % =
DIVIDE(
    [Emergency Admissions],
    [Total Encounters]
)
```

## Long Stay Encounters

```DAX
Long Stay Encounters =
CALCULATE(
    [Total Encounters],
    pediatric_encounters_gold[Length_of_Stay_Days] >= 4
)
```

## Long Stay Rate

```DAX
Long Stay Rate =
DIVIDE(
    [Long Stay Encounters],
    [Total Encounters]
)
```

## 30-Day Readmissions

```DAX
30-Day Readmissions =
CALCULATE(
    [Total Encounters],
    pediatric_encounters_gold[Readmit_30_Day_Flag] = 1
)
```

## 30-Day Readmission Rate

```DAX
30-Day Readmission Rate =
DIVIDE(
    [30-Day Readmissions],
    [Total Encounters]
)
```

## Average LOS by Department

Use the `Average LOS` measure with `Department` on the visual axis.

## Encounter Volume by Month

Use the `Total Encounters` measure with `Admit_Month` on the visual axis.
