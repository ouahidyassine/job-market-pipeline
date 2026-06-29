import requests
import json

API_BASE = "https://data.gov.ma/data/api/3/action"

def get_hcp_emploi_datasets():
    url = f"{API_BASE}/package_search"
    params = {
        "fq": "groups:emploi AND organization:haut-commissariat-au-plan",
        "rows": 100
    }
    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()
    data = response.json()

    if not data["success"]:
        raise Exception("Echec de la requete API CKAN")

    datasets = data["result"]["results"]
    print(f"Total datasets HCP emploi trouves: {len(datasets)}")
    return datasets

if __name__ == "__main__":
    datasets = get_hcp_emploi_datasets()

    catalog = []
    for ds in datasets:
        catalog.append({
            "name": ds["name"],
            "title": ds["title"],
            "notes": ds.get("notes", ""),
            "resources": [
                {"url": r["url"], "format": r["format"], "name": r["name"]}
                for r in ds.get("resources", [])
            ]
        })

    with open("data/bronze/hcp_catalog.json", "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    print("Catalogue sauvegarde: data/bronze/hcp_catalog.json")