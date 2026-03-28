import os
import json
import pandas as pd

audio_dir = "data/audio"
transcript_dir = "data/transcripts"

data = []

for file in os.listdir(transcript_dir):
    if file.endswith(".json"):
        rid = file.replace(".json", "")

        transcript_path = os.path.join(transcript_dir, file)
        audio_path = os.path.join(audio_dir, f"{rid}.wav")

        # Skip if audio not found
       # if not os.path.exists(audio_path):
#     continue

        try:
            with open(transcript_path, "r", encoding="utf-8") as f:
                content = json.load(f)

            text = " ".join([seg.get("text", "") for seg in content]).strip()

            # Skip empty text
            if text == "":
                continue

            data.append({
                "audio_path": audio_path,
                "text": text
            })

        except Exception as e:
            print(f"Error processing {file}: {e}")

# Convert to DataFrame
df = pd.DataFrame(data)

# Save dataset
df.to_csv("data/dataset.csv", index=False, encoding="utf-8")

print("Dataset created successfully!")
print(df.head())