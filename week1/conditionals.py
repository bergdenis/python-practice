# Task 1 — Basic if/elif/else
# Given:
test_status = "FAILED"

# Print a message based on the status: if PASSED — "Test passed, all good", if FAILED — "Test failed, check the logs",
# if SKIPPED — "Test skipped", anything else — "Unknown status".
if test_status == "PASSED":
    print("Test passed, all good")
elif test_status == "FAILED":
    print("Test failed, check the logs")
elif test_status == "SKIPPED":
    print("Test skipped")
else:
    print("Unknown status")

print()
# Task 2 — Comparison operators
# Given:
response_time = 850

# If response time is under 200 — "Fast", 200 to 500 — "Acceptable", 500 to 1000 — "Slow",
# over 1000 — "Critical, SLA breached".
if response_time < 200:
    print("Fast")
elif response_time <= 500:
    print("Acceptable")
elif response_time <= 1000:
    print("Slow")
else:
    print("Critical, SLA breached")

print()
# Task 3 — and / or / not
# Given:
status_code = 200
has_body = True

# Print "Valid response" only if status code is 200 AND body is present. Print "Invalid response" otherwise.
# Then separately: print "No content" if body is NOT present.
if status_code == 200 and has_body:
    print("Valid response")
else: print('Invalid response')

if not has_body:
    print("No content")

print()
# Task 4 — in operator
# Given:
allowed_methods = ["GET", "POST", "PUT", "DELETE"]
method = "PATCH"

# Check if the method is allowed and print the result.
if method in allowed_methods:
    print(f"Method {method} is allowed")
else:
    print(f"Method {method} is not allowed")

print()
# Task 5 — Nested conditions
# Given:
is_authenticated = True
role = "viewer"

# Logic:
#
# Not authenticated → "Access denied"
# Authenticated + role "admin" → "Full access"
# Authenticated + role "editor" → "Can edit"
# Authenticated + any other role → "Read only"
if not is_authenticated:
    print("Access denied")
elif role == "admin":
    print("Full access")
elif role == "editor":
    print("Can edit")
else:
    print("Read only")

print()
# Task 6 — Ternary operator
status_code = 404

# In a single line using a ternary operator print "Success" if status code is 200, otherwise "Failure".
result = "Success" if status_code == 200 else "Failure"
print(result)
