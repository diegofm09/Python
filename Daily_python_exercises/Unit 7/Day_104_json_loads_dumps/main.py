import json
from pathlib import Path

json_string = '''
    {
        "students": [
            {
                "id": 1,
                "name": "Josh",
                "age": 19,
                "full-time": true
            },
            {
                "id": 2,
                "name": "Jessica",
                "age": 23,
                "full-time": false
            }
        ]
    }
'''
json_path = Path(__file__).resolve().parent / "students.json"

data = json.loads(json_string)
print(data)
print(data["students"][0]["name"])

data["test"] = [{"name": "Josh", "mark": "A"}, {"name": "Jessica", "mark": "C"}]
print(type(data))
print(data)
new_data_json = json.dumps(data, indent=2, sort_keys=True)
print(type(new_data_json))
print(new_data_json)
