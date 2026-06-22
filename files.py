# Task 1 — Write to file
# Write a list of test names to a file tests.txt, each on a new line.
tests = ["test_login", "test_logout", "test_search"]

# Then open the file manually in PyCharm to check it worked.
# File content:
# test_login
# test_logout
# test_search

with open("tests.txt", "w") as file:
    for test in tests:
        file.write(f"{test}\n")

print()
# Task 2 — Read whole file
# Read the entire tests.txt you just created and print its content.
with open("tests.txt", "r") as file:
    content = file.read()
print(content)

print()
# Task 3 — Read line by line
# Read tests.txt line by line, print each line with a number. Use strip() to remove extra newlines.
with open("tests.txt", "r") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number}. {line.strip()}")

print()
# Task 4 — Append to file
# Append "test_checkout" to the existing tests.txt without erasing it. Then read and print the whole file.
with open("tests.txt", "a") as file:
    file.write("test_checkout\n")

with open("tests.txt", "r") as file:
    content = file.read()
    print(content)

print()
# Task 5 — Count lines
# Read tests.txt and count how many lines (tests) it contains. Print the count.
with open("tests.txt", "r") as file:
    line_count = 0
    for line in file:
        line_count += 1

print(f"Total tests: {line_count}")
