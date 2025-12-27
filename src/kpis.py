import pandas as pd

def compute_kpis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns KPI table with:
    Total transactions, Total value, Avg value, Fraud Rate, Flagged Fraud Rate
    """
    kpiTotalTxns = len(df)
    kpiTotalValue = df["amount"].sum()
    kpiAvgValue = df["amount"].mean()
    kpiFraudRate =df['isFraud'].mean()
    kpiFlaggedRate = df['isFlaggedFraud'].mean()

    kpis = pd.DataFrame({
    "KPI": [
        "Total transactions",
        "Total value",
        "Average value",
        "Fraud Rate",
        "Flagged Fraud Rate",
    ],
    "Value": [
        kpiTotalTxns,
        kpiTotalValue,
        kpiAvgValue,
        kpiFraudRate,
        kpiFlaggedRate,
    ],
    })

    return kpis
