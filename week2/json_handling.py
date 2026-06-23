import json

# Task 1 — Parse JSON string
# Parse this JSON string into a dict and print status and code.
json_text = '{"status": "ok", "code": 200}'

data = json.loads(json_text)

print(f"Status: {data['status']}")
print(f"Code: {data['code']}")

print()
# Task 2 — Dict to JSON string
# Convert this dict to a JSON string and print it.
data = {"name": "Denis", "role": "QA", "active": True}

json_text = json.dumps(data)

print(json_text)

print()
# Task 3 — Nested JSON
# Parse this JSON and print the username from the nested object.
json_text = '{"status": 200, "data": {"user_id": 42, "username": "denis"}}'

parsed_data = json.loads(json_text)

username = parsed_data["data"]["username"]

print(f"Username: {username}")

print()
# Task 4 — Write JSON to file
# Write this dict to config.json with indent=2. Then open it in PyCharm to check formatting.
config = {
    "env": "staging",
    "timeout": 30,
    "retries": 3
}

with open("../config.json", "w") as file:
    json.dump(config, file, indent=2)

print()
# Task 5 — Read JSON from file
# Read config.json you just created and print each key-value pair.
with open("../config.json", "r") as file:
    config_data = json.load(file)
    for key, value in config_data.items():
        print(f"{key}: {value}")
