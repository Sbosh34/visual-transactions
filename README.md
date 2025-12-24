# Payments Insights (PaySim)
[![CI](https://github.com/Sbosh34/visual-transactions/actions/workflows/ci.yml/badge.svg)](https://github.com/Sbosh34/visual-transactions/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.x-informational)
![Pandas](https://img.shields.io/badge/pandas-ready-informational)

> A small analytics project that turns transaction-level data into clear, consulting-style insights using reproducible Python notebooks.

## What this project does
Using a **sample** of the PaySim synthetic transactions dataset:
- Computes core transaction KPIs (volume, value, average ticket)
- Measures fraud and flagged-fraud rates
- Visualises portfolio mix (transactions by type)
- Visualises fraud behaviour over time
- Produces a short written “insights + recommendations” snapshot

## Dataset
This project uses the **PaySim** synthetic financial transactions dataset (mobile-money style). The dataset is distributed on Kaggle and is generated from the PaySim simulator. :contentReference[oaicite:0]{index=0}  
Background on PaySim as a simulator (how synthetic datasets are generated to resemble real transaction behaviour) is discussed in the PaySim paper/proceedings. :contentReference[oaicite:1]{index=1}

> Note: I did **not** commit the full raw dataset into Git. Only a small, reproducible sample is used for quick runs.

1) Create and activate a virtual environment and Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

2) Put the raw paysim dataset(From Kaggle) here
```text
data/raw/paysim.csv
```

3)Generate a small dataset(Optional and this will save you a lot of time trusssst me) and name it paysim_sample.csv
Save it here
```text
data/sample/paysim_sample.csv
```

4) Run the notebook in the environment
```bash
jupyter lab
```

## Outputs
- Snapshot report: `reports/kpi_snapshot.md`


