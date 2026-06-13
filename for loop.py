# Task 1 — Basic for
# Given
test_cases = ["login", "logout", "register", "password_reset"]

# Print each test case with its number starting from 1.
i = 1
for test in test_cases:
    print(f"{i}. {test}")
    i += 1

print()
# Task 2 — for with range()
# Without a list, using range() only:
#
# print numbers from 1 to 10
# print even numbers from 2 to 20
# print numbers from 10 to 1 in reverse order
for i in range(1, 11):
    print(i, end=" ")
print()

for i in range(2, 21, 2):
    print(i, end=" ")
print()

for i in range(10, 0, -1):
    print(i, end=" ")

print()
# Task 3 — for with break and continue
# Given
status_codes = [200, 201, 200, 404, 200, 500, 200]

# если код 404 — выведи "Not found, skipping" и пропусти
# если код 500 — выведи "Server error, stopping" и останови цикл
# иначе выведи "OK: {код}"
for code in status_codes:
    if code == 404:
        print("Not found, skipping")
        continue
    elif code == 500:
        print("Server error, stopping")
        break
    else:
        print(f"OK: {code}")

print()
# Task 4 — enumerate and zip
# Given
endpoints = ["/login", "/users", "/orders"]
methods = ["POST", "GET", "GET"]

# Using zip() and enumerate() print pairs with number.
for i, (endpoint, method) in enumerate(zip(endpoints, methods)):
    print(f"{i+1}. {method} {endpoint}")

print()
# Task 5 — for with accumulator
# Given
response_times = [120, 340, 89, 456, 210, 78, 534]
fast_requests = 0
slow_requests = 0
total = 0
# Calculate and print using for loop:
#
# fast requests under 200ms
# slow requests over 400ms
# average response time

for time in response_times:
    total += time

    if time < 200:
        fast_requests += 1
    elif time > 400:
        slow_requests += 1

average = total / len(response_times)

print(f"Fast requests (< 200ms): {fast_requests}")
print(f"Slow requests (> 400ms): {slow_requests}")
print(f"Average response time: {average}ms")
