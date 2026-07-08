# Task 1 — Variable between requests
# Step 1: Create a user via POST, save the returned id in a variable.
# Step 2: Print a message using that id.
import requests

url = "https://jsonplaceholder.typicode.com/users"
new_user = {"name": "Denis", "job": "QA"}

response = requests.post(url, json=new_user)

user_id = response.json()["id"]

print(f"Created user with id: {user_id}")
print(f"Now using id {user_id} for the next request")

print()
# Task 2 — Chain: create then fetch
# Step 1: Get post with id 1.
# Step 2: Take the userId from that post, then fetch that user's data.
post_url = "https://jsonplaceholder.typicode.com/posts/1"
users_url = "https://jsonplaceholder.typicode.com/users"

post_response = requests.get(post_url)
post = post_response.json()
user_id = post["userId"]
print(f"Post belongs to user id: {user_id}")

user_response = requests.get(f"{users_url}/{user_id}")
user = user_response.json()
print(f"User name: {user['name']}")

print()
# Task 3 — Session with shared headers
# Create a Session, set a common header on it, then make two GET requests through the session. Print the status code
# of each.
url1 = "https://jsonplaceholder.typicode.com/users/1"
url2 = "https://jsonplaceholder.typicode.com/users/2"

session = requests.Session()
session.headers.update({"Accept": "application/json"})

response1 = session.get(url1)
response2 = session.get(url2)

print(f"Request 1 status: {response1.status_code}")
print(f"Request 2 status: {response2.status_code}")
