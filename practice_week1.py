# Final Task Week 1 — Test Report Analyzer
# Given
test_run = [
    {"name": "test_login", "status": "passed", "duration": 120},
    {"name": "test_logout", "status": "passed", "duration": 85},
    {"name": "test_register", "status": "failed", "duration": 340},
    {"name": "test_search", "status": "passed", "duration": 560},
    {"name": "test_checkout", "status": "failed", "duration": 890},
    {"name": "test_payment", "status": "skipped", "duration": 0},
    {"name": "test_profile", "status": "passed", "duration": 210},
]

# What to do:
#
# Count and print how many tests passed, failed, skipped
#
# Print the success rate (passed out of total), rounded to 1 decimal
#
# Print total and average duration (average only for tests that actually ran — not skipped)
#
# Print names of all failed tests
#
# Print the name of the slowest test
#
# Print the verdict: if success rate >= 70% — "BUILD STABLE", otherwise "BUILD UNSTABLE"
status_counts = {"passed": 0,"failed": 0,"skipped": 0,}

for test in test_run:
    status = test["status"]
    status_counts[status] += 1

print(f"Passed: {status_counts['passed']}")
print(f"Failed: {status_counts['failed']}")
print(f"Skipped: {status_counts['skipped']}")

passed_count = 0
total_count = len(test_run)

for test in test_run:
    if test["status"] == "passed":
        passed_count += 1

success_rate = (passed_count / total_count) * 100
print(f"Success rate: {success_rate:.1f}%")

total_duration = 0
ran_count = 0

for test in test_run:
    if test["status"] != "skipped":
        total_duration = total_duration + test["duration"]
        ran_count = ran_count + 1

if ran_count > 0:
    average_duration = total_duration / ran_count
else:
    average_duration = 0

print(f"Total duration: {total_duration}ms")
print(f"Average duration: {average_duration:.1f}ms")

failed_test_names = []

for test in test_run:
    if test["status"] == "failed":
        failed_test_names.append(test["name"])

print(f"Failed tests: {failed_test_names}")

max_duration = -1
slowest_test_name = ""

for test in test_run:
    if test["duration"] > max_duration:
        max_duration = test["duration"]
        slowest_test_name = test["name"]

print(f"Slowest test: {slowest_test_name}")

if success_rate >= 70:
    print("Verdict: BUILD STABLE")
else:
    print("Verdict: BUILD UNSTABLE")
