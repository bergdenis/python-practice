# What we're building
# A mini test-reporting system.
# test_models.py — classes (data models)
# report_data.json — test data
# run_report.py — main file, reads JSON and prints report
#
# Step 1 — create folder
# In the project root create a folder week3_project/. All three files go inside.
#
# Step 2 — test_models.py (classes)
# Create a file with two classes.
# Class TestCase:
#
# __init__ takes name, status, duration
# method is_passed() — returns True if status == "passed"
#
# Class TestReport:
#
# __init__ takes suite_name, creates empty list test_cases
# method add_test(test_case) — adds a TestCase to the list
# method passed_count() — returns number of passed tests
# method failed_count() — returns number of failed tests
# method total_duration() — returns sum of all durations
# method print_summary() — prints the final report
#
# Hints:
# passed_count() — loop through self.test_cases, count those where is_passed() is True
# total_duration() — accumulate test.duration in a loop
# Start with test_models.py only — write both classes. This is the biggest part, take your time.
# When done — show me, I'll check. Then I'll give Step 3 (JSON) and Step 4 (run).
class TestCase:
    def __init__(self, name, status, duration):
        self.name = name
        self.status = status
        self.duration = duration

    def is_passed(self):
        return self.status == "passed"

class TestReport:
    def __init__(self, suite_name):
        self.suite_name = suite_name
        self.test_cases = []

    def add_test(self, test_case):
        self.test_cases.append(test_case)

    def passed_count(self):
        count = 0
        for test in self.test_cases:
            if test.is_passed():
                count += 1
        return count

    def failed_count(self):
        count = 0
        for test in self.test_cases:
            if test.status == "failed":
                count += 1
        return count

    def total_duration(self):
        total = 0
        for test in self.test_cases:
            total += test.duration
        return total

    def print_summary(self):
        print(f"=== {self.suite_name} ===")
        print(f"Passed: {self.passed_count()}")
        print(f"Failed: {self.failed_count()}")
        print(f"Total duration: {self.total_duration()}ms")

# Step 3 — Data in JSON
# Create a file report_data.json in the week3_project/ folder with the following content:
# This is just a data file — no Python. Create it, paste the content, save.