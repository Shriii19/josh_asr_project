import pandas as pd

# Load predictions
df = pd.read_csv("data/predictions.csv")

# Remove empty rows
df = df.dropna()
df = df[df["prediction"] != ""]

# Take 25 samples
sample = df.head(25)

# Save file
sample.to_csv("data/error_samples.csv", index=False)

print("✅ error_samples.csv created!")