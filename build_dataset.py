import os
import json
import pandas as pd

audio_dir = "data/audio"
transcript_dir = "data/transcripts"

data = []

for file in os.listdir(transcript_dir):
    if not file.endswith(".json"):
        continue

    rid = file.replace(".json", "")
    transcript_path = os.path.join(transcript_dir, file)
    audio_path = os.path.join(audio_dir, rid + ".wav")

    with open(transcript_path, "r", encoding="utf-8") as f:
        content = json.load(f)

    parts = []
    for seg in content:
        if seg.get("text", ""):
            parts.append(seg["text"])

    text = " ".join(parts).strip()

    if text == "":
        continue

    data.append({"audio_path": audio_path, "text": text})

df = pd.DataFrame(data)
df.to_csv("data/dataset.csv", index=False, encoding="utf-8")
print("saved", len(df), "rows to data/dataset.csv")