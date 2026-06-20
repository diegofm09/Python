import json
from pathlib import Path

main_p = Path(__file__).resolve().parent

catalog_path = main_p/"catalog.json"

with open(catalog_path, "r") as file:
    catalog = json.load(file)

n= -1
for i in catalog["products"]:
    n +=1
    print(catalog["products"][n])

catalog["products"][0].get("sizes").append("XXL")
catalog["products"][1].get("sizes").append("XXL")

with open(catalog_path, "w") as file:
    json.dump(catalog, file, indent=2)