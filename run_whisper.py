import pandas as pd
import torch
import librosa
import os
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# Load dataset
df = pd.read_csv("data/dataset.csv")

# 🔥 Limit for testing (IMPORTANT)
df = df.head(10)

# Load model
processor = WhisperProcessor.from_pretrained("openai/whisper-small")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")

model.eval()

predictions = []

for i, row in df.iterrows():
    audio_path = row["audio_path"]

    # Skip if audio missing
    if not os.path.exists(audio_path):
        print(f"Missing audio: {audio_path}")
        predictions.append("यह एक डमी प्रेडिक्शन है")
        continue

    try:
        # Load audio
        audio, sr = librosa.load(audio_path, sr=16000)

        # Convert to input features
        input_features = processor(audio, sampling_rate=16000, return_tensors="pt").input_features

        # Generate output
        with torch.no_grad():
            predicted_ids = model.generate(input_features)

        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

        predictions.append(transcription)

        print(f"Done {i}")

    except Exception as e:
        print(f"Error: {e}")
        predictions.append("")

# Save results
df["prediction"] = predictions
df.to_csv("data/predictions.csv", index=False)

print("✅ Predictions saved!")