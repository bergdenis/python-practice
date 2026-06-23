import json

# Task 1 — Word counter
# First create a file text.txt with this content (write it via code):
text = ["QA engineer tests software", "Automation saves time", "Python is a powerful tool"]

# Then read the file and print:
# total number of lines / общее количество строк
# total number of words / общее количество слов
# the longest word / самое длинное слово
with open("text.txt", "w") as file:
    for line in text:
        file.write(f"{line}\n")

line_count = 0
word_count = 0
longest_word = ""

with open("text.txt", "r") as file:
    for line in file:
        line_count += 1

        words_in_line = line.split()
        word_count += len(words_in_line)

        for word in words_in_line:
            if len(word) > len(longest_word):
                longest_word = word

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Longest word: {longest_word}")

print()
# Task 2 — Safe JSON reader
# Write a function read_json_safe(filename) that:
# tries to open and parse a JSON file
# if file doesn't exist — returns "File not found"
# if file has invalid JSON — returns "Invalid JSON"
# if all good — returns the parsed dict
#
# Test on three cases:
def read_json_safe(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return "File not found"
    except json.JSONDecodeError:
        return "Invalid JSON"

print(read_json_safe("config.json"))         # existing valid file from Thursday
print(read_json_safe("missing.json"))        # doesn't exist
print(read_json_safe("text.txt"))            # exists but not valid JSON

print()
# Task 3 — User filter
# Step 1 — create users.json via code with this data:
users = [
    {"name": "Denis", "role": "admin", "active": True},
    {"name": "Anna", "role": "editor", "active": True},
    {"name": "Pavel", "role": "viewer", "active": False},
    {"name": "Elena", "role": "admin", "active": True},
    {"name": "Igor", "role": "viewer", "active": False},
]
# Step 2 — read users.json, filter only active users, and write them to a new file active_users.json.
#
# Step 3 — print how many active users were saved.
#
# Then open active_users.json to verify it contains only Denis, Anna, Elena.
with open("users.json", "w") as file:
    json.dump(users, file, indent=2)

with open("users.json", "r") as file:
    users_data = json.load(file)

active_users = []

for user in users_data:
    if user["active"]:
        active_users.append(user)

with open("active_users.json", "w") as file:
    json.dump(active_users, file, indent=2)

print(f"Active users saved: {len(active_users)}")
