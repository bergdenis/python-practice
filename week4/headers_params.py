# Task 1 — Query params
# Get posts for user with id 1 using params. Print status code and how many posts were returned.
import requests

url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}

response = requests.get(url, params=params)

print(f"status {response.status_code}")
print(f"Posts found: {len(response.json())}")

print()
# Task 2 — Check the built URL
# After the request from Task 1, print the actual URL that was formed.

response = requests.get(url, params=params)

print(response.url)

print()
# Task 3 — Multiple params
# Get todos that belong to user 1 AND are completed. Print how many were found.
url = "https://jsonplaceholder.typicode.com/todos"
params = {"userId": 1, "completed": "true"}

response = requests.get(url, params=params)
print(f"status {response.status_code}")
print(f"Todos found: {len(response.json())}")

print()
# Task 4 — Headers
# Send a GET request with custom headers. Print the request headers that were actually sent.
url = "https://jsonplaceholder.typicode.com/users/1"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
response = requests.get(url, headers=headers)
print(response.request.headers)