# Task 1 — List basics
# Given
test_results = ["passed", "failed", "passed", "skipped", "failed", "passed"]

# Print:
#
# total number of tests
# number of "passed"
# first and last element
# list without first and last element (slice)
print(f"Total tests: {len(test_results)}")
print(f"Passed: {test_results.count("passed")}")
print(f"First: {test_results[0]}")
print(f"Last: {test_results[-1]}")
print(f"Middle: {test_results[1:-1]}")

print()
# Task 2 — List methods
# Given
bugs = ["login_bug", "timeout_bug", "ui_bug"]

# add "api_bug" to the end
# add "critical_bug" at index 0
# remove "ui_bug"
# print sorted list
# print number of elements
bugs.append("api_bug")
bugs.insert(0, "critical_bug")
bugs.remove("ui_bug")

print(sorted(bugs))
print(len(bugs))

print()
# Task 3 — Dictionary basics
# Given
response = {
    "status_code": 200,
    "message": "OK",
    "data": {"user_id": 42, "username": "denis"}
}

# Print:
#
# status_code
# message
# username from nested dictionary
# all keys
# all values
print(f"Status: {response["status_code"]}")
print(f"Message: {response["message"]}")
print(f"Username: {response["data"]["username"]}")
print(f"Keys: {response.keys()}")
print(f"Values: {response.values()}")

print()
# Task 4 — Dictionary methods
# Given
test_stats = {
    "passed": 45,
    "failed": 5,
    "skipped": 2
}

# add key "total" with sum of all tests
# update "failed" to 3
# remove "skipped"
# print final dictionary
# print value by key "blocked" — if missing print 0 using .get()
test_stats["total"] = sum(test_stats.values())
test_stats["failed"] = 3
del test_stats["skipped"]
print(test_stats)
print(f"Blocked: {test_stats.get("blocked", 0)}")

print()
# Task 5 — Tuple / Кортеж
# Given
http_methods = ("GET", "POST", "PUT", "DELETE", "PATCH")
coordinates = (55.7558, 37.6173)

# print length of http_methods
# check if "DELETE" exists
# print first three methods using slice
# try to change first element and explain what happened
print(f"Methods count: {len(http_methods)}")
print(f"DELETE exists: {"DELETE" in http_methods}")
print(f"First three: {http_methods[:3]}")
# http_methods[0] = "HEAD"  # TypeError: 'tuple' object does not support item assignment

# Methods count: 5
# DELETE exists: True
# First three: ('GET', 'POST', 'PUT')
# TypeError: 'tuple' object does not support item assignment

print()
# Task 6 — Trap
# What will this print — answer in text without running
data = {"status": "active", "role": "admin"}

# value1 = data["blocked"]  # KeyError: 'blocked'
print(value2)  # None
print(value3)  # not found

print(value1)
print(value2)
print(value3)

# KeyError: 'blocked'