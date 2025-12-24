import pandas as pd

def compute_kpis(df: pd.DataFrame) -> dict:
    return {
        "kpiTotalTxns": len(df),
        "kpiTotalValue": df["amount"].sum(),
        "kpiAvgValue": df["amount"].mean(),
        "kpiFraudRate": df["isFraud"].mean(),
        "kpiFlaggedRate": df["isFlaggedFraud"].mean(),
    }

def test_compute_kpis_basic():
    df = pd.DataFrame(
        {
            "amount": [10.0, 20.0, 30.0],
            "isFraud": [0, 1, 0],
            "isFlaggedFraud": [0, 0, 1],
        }
    )

    k = compute_kpis(df)

    assert k["kpiTotalTxns"] == 3
    assert k["kpiTotalValue"] == 60.0
    assert k["kpiAvgValue"] == 20.0
    assert abs(k["kpiFraudRate"] - (1 / 3)) < 1e-9
    assert abs(k["kpiFlaggedRate"] - (1 / 3)) < 1e-9

