# Task 1 — Assert status code
# Make a GET request to user 1, then assert the status code is 200. Print a success message if it passes.
import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

assert response.status_code == 200, f"Expected 200, got {response.status_code}"

print("Status code check passed!")

print()
# Task 2 — Assert response body
# For the same user, assert that: id equals 1, name equals "Leanne Graham", and the email field exists.
response = requests.get(url)
data = response.json()

assert data["id"] == 1, f"Expected id 1, got {data['id']}"
assert data["name"] == "Leanne Graham", f"Expected Leanne Graham, got {data['name']}"
assert "email" in data, "Email field is missing"

print("All body checks passed!")

print()
# Task 3 — Assert list length
# Get all users, assert that exactly 10 were returned.
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

assert len(response.json()) == 10, f"Expected 10, got {len(response.json())}"

print("Count check passed: 10 users")

print()
# Task 4 — Full API test
# Write a complete test for creating a user via POST. Check: status code is 201, the response contains the name
# you sent, and an id was assigned.
url = "https://jsonplaceholder.typicode.com/users"
new_user = {"name": "Denis", "job": "QA"}

response = requests.post(url, json=new_user)
data = response.json()

assert response.status_code == 201, f"Expected 201, got {response.status_code}"
assert data["name"] == "Denis", f"Expected 'Denis', got {data['name']}"
assert "id" in data, "No id was assigned"

print(f"All checks passed! Created user with id: {data['id']}")
