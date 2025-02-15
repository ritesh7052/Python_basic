import json
json_string = '{"name": "Alice", "age": 25}'
obj = json.loads(json_string)
print(obj["name"])
