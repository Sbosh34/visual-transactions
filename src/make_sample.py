from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw/paysim.csv")
OUT_PATH = Path("data/sample/paysim_sample.csv")
NROWS_TO_HEAD = 200000
SAMPLE_SIZE = 10000

if not RAW_PATH.exists():
    raise FileNotFoundError(f"Could not find: {RAW_PATH}. Put paysim.csv in data/raw")

df = pd.read_csv(RAW_PATH, nrows = NROWS_TO_HEAD)
df_sample = df.sample(n = min(SAMPLE_SIZE, len(df)), random_state = 1)
df_sample.to_csv(OUT_PATH, index = False)

print("Sample created:", OUT_PATH)
print("Sample size:", df_sample.shape) #(rows, columns)
print("Columns", list(df_sample.columns)) #Column names
