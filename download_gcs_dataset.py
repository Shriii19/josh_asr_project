import os
import requests

BASE_URL = "https://storage.googleapis.com/upload_goai/967179/"

audio_dir = "data/audio/"
transcripts_dir = "data/transcripts/"
metadata_dir = "data/metadata/"

os.makedirs(audio_dir, exist_ok=True)
os.makedirs(transcripts_dir, exist_ok=True)
os.makedirs(metadata_dir, exist_ok=True)


def download(url, dest):
    if os.path.exists(dest):
        print("already exists:", dest)
        return True
    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        with open(dest, "wb") as f:
            f.write(r.content)
        print("downloaded:", dest)
        return True
    else:
        print("failed:", url, r.status_code)
        return False


def process_id(rid):
    rid = str(rid)

    transcript_url = BASE_URL + rid + "_transcription.json"
    transcript_dest = transcripts_dir + rid + ".json"
    download(transcript_url, transcript_dest)

    metadata_url = BASE_URL + rid + "_metadata.json"
    metadata_dest = metadata_dir + rid + ".json"
    download(metadata_url, metadata_dest)

    audio_patterns = [rid + ".wav", rid + "_recording.wav", rid + ".mp3"]
    for pattern in audio_patterns:
        audio_url = BASE_URL + pattern
        ext = os.path.splitext(pattern)[1]
        audio_dest = audio_dir + rid + ext
        if download(audio_url, audio_dest):
            break


ids = [825780, 825781, 825782]

for rid in ids:
    print("processing", rid)
    process_id(rid)
