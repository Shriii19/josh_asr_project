import pandas as pd
from evaluate import load

df = pd.read_csv("data/predictions.csv")

# 🔥 Clean data
df = df.dropna()
df = df[df["prediction"] != ""]
df = df[df["text"] != ""]

# If still empty
if len(df) == 0:
    print("❌ No valid predictions found!")
    exit()

wer_metric = load("wer")

wer = wer_metric.compute(
    predictions=df["prediction"].astype(str).tolist(),
    references=df["text"].astype(str).tolist()
)

print("🔥 WER:", wer)