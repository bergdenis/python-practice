# Test 1 — GET single user
# GET user with id 2. Assert: status 200, id equals 2, email field exists.
import requests

url = "https://jsonplaceholder.typicode.com/users/2"

response = requests.get(url)
user_data = response.json()

assert response.status_code == 200, f"Expected 200, got {response.status_code}"
assert user_data["id"] == 2, f"Expected id 2, got {user_data['id']}"
assert "email" in user_data, "Email field is missing"

print(f"Test 1 passed: got {user_data['name']}")

print()
# Test 2 — GET list count
# GET all posts. Assert: status 200, exactly 100 posts returned.
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
posts = response.json()

assert response.status_code == 200, f"Expected 200, got {response.status_code}"
assert len(posts) == 100, f"Expected 100, got {len(posts)}"

print(f"Test 2 passed: {len(posts)} posts found")

print()
# Test 3 — POST create
# POST a new post. Assert: status 201, response contains the title you sent, id was assigned.
url = "https://jsonplaceholder.typicode.com/posts"

new_post = {"title": "My test post", "body": "test content", "userId": 1}

response = requests.post(url, json=new_post)
data = response.json()

assert response.status_code == 201, f"Expected 201, got {response.status_code}"
assert data["title"] == "My test post", f"Expected 'My test post', got {data['title']}"
assert "id" in data, "No id was assigned"

print(f"Test 3 passed: created post with id {data['id']}")

print()
# Test 4 — PUT update
# PUT update post id 1. Assert: status 200, title matches what you sent.
url = "https://jsonplaceholder.typicode.com/posts/1"

updated_post = {"title": "Updated title", "body": "updated", "userId": 1}
response = requests.put(url, json=updated_post)
data = response.json()

assert response.status_code == 200, f"Expected 200, got {response.status_code}"
assert data["title"] == "Updated title", f"Expected 'Updated title', got {data['title']}"

print(f"Test 4 passed: title updated")

print()
# Test 5 — Chain (filter with params)
# GET posts filtered by userId=1 using params. Assert: status 200, all returned posts belong to userId 1.
url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}

response = requests.get(url, params=params)
data = response.json()

assert response.status_code == 200, f"Expected 200, got {response.status_code}"
for post in data:
    assert post["userId"] == 1, f"Expected id 1, got {post['userId']}"

print(f"Test 5 passed: all 10 posts belong to user {params['userId']}")
