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
    
    kpiTotalTxnsStr = f"{kpiTotalTxns:,}"
    kpiTotalValueStr = f"{kpiTotalValue:,.2f}"
    kpiAvgValueStr = f"{kpiAvgValue:,.2f}"
    kpiFraudRateStr = f"{kpiFraudRate:.4%}"
    kpiFlaggedRateStr = f"{kpiFlaggedRate:.4%}"


    kpis = pd.DataFrame({
    "KPI": [
        "Total transactions",
        "Total value",
        "Average value",
        "Fraud Rate",
        "Flagged Fraud Rate",
    ],
    "Value": [
        kpiTotalTxnsStr,
        kpiTotalValueStr,
        kpiAvgValueStr,
        kpiFraudRateStr,
        kpiFlaggedRateStr,
    ],
    })

    return kpis
