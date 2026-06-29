# Task — Display the list of users
# Make a GET request to https://jsonplaceholder.typicode.com/users, print the status code, then parse the JSON response
# and print each user in the format:
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

print(response.status_code)

data = response.json()

print(data)

# Format: number, name, username in parentheses, email after a dash.
# Hints:
#
# response.json() converts the JSON response into a Python list of dictionaries
# loop through the list, each user is a dictionary — access user["name"], user["username"], user["email"]
# use enumerate(data, start=1) for numbering
for index, user in enumerate(data, start=1):
    print(f"{index}. {user['name']} ({user['username']}) - {user['email']}")
