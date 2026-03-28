import os
import requests
from typing import List

BASE_URL = "https://storage.googleapis.com/upload_goai/967179/"
AUDIO_PATTERNS = ["{id}.wav", "{id}_recording.wav", "{id}.mp3"]

# Output directories
AUDIO_DIR = "data/audio/"
TRANSCRIPTS_DIR = "data/transcripts/"
METADATA_DIR = "data/metadata/"

# Ensure directories exist
def ensure_dirs():
    for d in [AUDIO_DIR, TRANSCRIPTS_DIR, METADATA_DIR]:
        os.makedirs(d, exist_ok=True)

def file_exists(path: str) -> bool:
    return os.path.isfile(path)

def download_file(url: str, dest: str) -> bool:
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            with open(dest, "wb") as f:
                f.write(r.content)
            print(f"Downloaded: {dest}")
            return True
        else:
            print(f"Failed to download (status {r.status_code}): {url}")
            return False
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def process_id(recording_id: str):
    # Download transcription
    transcript_url = f"{BASE_URL}{recording_id}_transcription.json"
    transcript_dest = os.path.join(TRANSCRIPTS_DIR, f"{recording_id}.json")
    if not file_exists(transcript_dest):
        download_file(transcript_url, transcript_dest)
    else:
        print(f"Exists, skipping: {transcript_dest}")

    # Download metadata
    metadata_url = f"{BASE_URL}{recording_id}_metadata.json"
    metadata_dest = os.path.join(METADATA_DIR, f"{recording_id}.json")
    if not file_exists(metadata_dest):
        download_file(metadata_url, metadata_dest)
    else:
        print(f"Exists, skipping: {metadata_dest}")

    # Download audio (try all patterns)
    audio_downloaded = False
    for pattern in AUDIO_PATTERNS:
        audio_url = f"{BASE_URL}" + pattern.format(id=recording_id)
        ext = os.path.splitext(pattern)[1]
        audio_dest = os.path.join(AUDIO_DIR, f"{recording_id}{ext}")
        if file_exists(audio_dest):
            print(f"Exists, skipping: {audio_dest}")
            audio_downloaded = True
            break
        if download_file(audio_url, audio_dest):
            audio_downloaded = True
            break
    if not audio_downloaded:
        print(f"Audio not found for ID {recording_id}")

def main(ids: List[str]):
    ensure_dirs()
    for rid in ids:
        print(f"\nProcessing ID: {rid}")
        process_id(str(rid))

if __name__ == "__main__":
    # Example: replace with your list or range
    ids = [825780, 825781, 825782]
    main(ids)
