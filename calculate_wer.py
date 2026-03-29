import pandas as pd
from evaluate import load

df = pd.read_csv("data/predictions.csv")
df = df.dropna()
df = df[df["prediction"] != ""]
df = df[df["text"] != ""]

if len(df) == 0:
    print("no valid predictions found")
    exit()

wer_metric = load("wer")

wer = wer_metric.compute(
    predictions=df["prediction"].astype(str).tolist(),
    references=df["text"].astype(str).tolist()
)

print("WER:", round(wer, 4))