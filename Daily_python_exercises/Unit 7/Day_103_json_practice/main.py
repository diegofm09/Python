import json

#exercise 1
with open("Daily_python_exercises/Unit 7/Day_103_json_practice/books.json", "r") as file:
    catalog = json.load(file)

for i in catalog["books"]:
    print(f'{i.get("title")} is {"available" if i.get("available") else "not available"} and has a {i.get("rating")} rating')


#exercise 2
catalog["books"].append({"title": "Spain History", "available": True, "rating": 6.4})

with open("Daily_python_exercises/Unit 7/Day_103_json_practice/books.json", "w") as file:
    json.dump(catalog, file, indent=2)
