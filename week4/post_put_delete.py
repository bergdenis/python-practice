# Task 1 — POST (create)
# Send a POST request to https://jsonplaceholder.typicode.com/users to create a new user. Print the status code and
# the response body.
import requests

url = "https://jsonplaceholder.typicode.com/users"

new_user = {"name": "Denis", "job": "QA Engineer"}

response = requests.post(url, json=new_user)

print(f"status code: {response.status_code}")
print(response.json())

print()
# Task 2 — PUT (update)
# Send a PUT request to update user with id 1 at https://jsonplaceholder.typicode.com/users/1. Print status code
# and response.
url = "https://jsonplaceholder.typicode.com/users/1"

updated_user = {"name": "Denis Berg", "job": "QA Automation Engineer"}

response = requests.put(url, json=updated_user)

print(f"status code: {response.status_code}")
print(response.json())

print()
# Task 3 — DELETE / Удалить
# Send a DELETE request to remove user with id 1. Print the status code.
url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.delete(url)

print(f"status code: {response.status_code}")
