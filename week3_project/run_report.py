# Claude responded: Step 4 — Main file run_report.Step 4 — Main file run_report.py
# This is where everything comes together: import classes, read JSON, create objects, print the report. Create
# run_report.py in week3_project/.
# Part 1 — Imports and reading JSON
#
# import json
# import your TestCase and TestReport classes from test_models
# read report_data.json into a variable
import json
from test_models import TestCase, TestReport

with open("report_data.json", "r") as file:
    data = json.load(file)

# Part 2 — Create objects from data
#
# Create a TestReport object, passing it the suite_name from the data
# Loop through the tests list — for each one, create a TestCase and add it to the report via add_test()
# Call report.print_summary() to output the report
report = TestReport(data["suite_name"])

for test in data["tests"]:
    test_case = TestCase(test["name"], test["status"], test["duration"])
    report.add_test(test_case)

report.print_summary()
