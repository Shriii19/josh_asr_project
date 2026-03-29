import os
import json
import requests


def download_file(url, path):
    if os.path.exists(path):
        print("skipped:", path)
        return

    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        if path.endswith(".json"):
            try:
                json.loads(r.content)
            except:
                print("invalid json:", url)
                return

        with open(path, "wb") as f:
            f.write(r.content)
        print("downloaded:", path)
    else:
        print("failed:", url)