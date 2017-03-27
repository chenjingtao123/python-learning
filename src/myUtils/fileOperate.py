import json

with open("/opt/json.txt", "r", encoding="utf-8") as f:
    obj = json.load(f)
    print(obj[0]['Title'])
