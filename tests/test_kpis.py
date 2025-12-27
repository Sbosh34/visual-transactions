import pandas as pd
from src.kpis import compute_kpis

def test_compute_kpis_basic_numbers():
    df = pd.DataFrame({
        'amount': [100.0, 50.0, 50.0], 'isFraud':[0, 1, 0], 'isFlaggedFraud':[0, 0, 1],
        })

    kpis = compute_kpis(df)

    d = dict(zip(kpis['KPI'], kpis['Value']))

    assert d["Total transactions"] == 3
    assert d["Total value"] == 200.0
    assert d["Average value"] == (200.0 / 3.0)
    assert d["Fraud Rate"] == (1.0 / 3.0)
    assert d["Flagged Fraud Rate"] == (1.0 / 3.0)
