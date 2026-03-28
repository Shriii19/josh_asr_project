def download_file(url, path):
    if os.path.exists(path):
        print(f"Skipped: {path}")
        return

    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            
            # Validate JSON
            if path.endswith(".json"):
                try:
                    json.loads(r.content)
                except:
                    print(f"Invalid JSON: {url}")
                    return

            with open(path, "wb") as f:
                f.write(r.content)

            print(f"Downloaded: {path}")
        else:
            print(f"Failed: {url}")

    except Exception as e:
        print(f"Error: {url} -> {e}")