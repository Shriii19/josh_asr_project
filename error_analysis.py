import pandas as pd

df = pd.read_csv("data/predictions.csv")
df = df.dropna()
df = df[df["prediction"] != ""]
df = df[df["text"] != ""]

# keep only rows where prediction differs from reference
errors = df[df["prediction"] != df["text"]]

# take every Nth row so we get a spread across the dataset, not just the start
step = max(1, len(errors) // 25)
sample = errors.iloc[::step].head(25)

sample.to_csv("data/error_samples.csv", index=False)
print("saved", len(sample), "error samples")