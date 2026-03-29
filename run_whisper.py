import pandas as pd
import torch
import librosa
import os
from transformers import WhisperProcessor, WhisperForConditionalGeneration

df = pd.read_csv("data/dataset.csv")

processor = WhisperProcessor.from_pretrained("openai/whisper-small")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")
model.eval()

predictions = []

for i, row in df.iterrows():
    audio_path = row["audio_path"]

    if not os.path.exists(audio_path):
        print("missing audio:", audio_path)
        predictions.append("")
        continue

    audio, sr = librosa.load(audio_path, sr=16000)
    input_features = processor(audio, sampling_rate=16000, return_tensors="pt").input_features

    with torch.no_grad():
        predicted_ids = model.generate(input_features)

    text = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    predictions.append(text)
    print(i, text)

df["prediction"] = predictions
df.to_csv("data/predictions.csv", index=False)
print("done")