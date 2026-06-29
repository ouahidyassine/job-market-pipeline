import requests
import json
import os
import time

def download_resources():
    with open("data/bronze/hcp_catalog.json", "r", encoding="utf-8") as f:
        catalog = json.load(f)

    out_dir = "data/bronze/hcp_xlsx"
    os.makedirs(out_dir, exist_ok=True)

    success_count = 0
    for ds in catalog:
        name = ds["name"]
        for resource in ds["resources"]:
            if resource["format"].upper() != "XLSX":
                continue

            filepath = os.path.join(out_dir, f"{name}.xlsx")
            try:
                r = requests.get(resource["url"], timeout=20)
                r.raise_for_status()
                with open(filepath, "wb") as out:
                    out.write(r.content)
                print(f"OK: {name}.xlsx")
                success_count += 1
            except Exception as e:
                print(f"ERREUR sur {name}: {e}")

            time.sleep(1)

    print(f"\nTotal telecharge: {success_count} fichiers")

if __name__ == "__main__":
    download_resources()
