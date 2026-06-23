# Task 1 — Simplest function
# Write a function say_hello() that prints "Hello, QA!". Call it.
def say_hello():
    print("Hello, QA!")

say_hello()

print()
# Task 2 — Function with one argument
# Write a function greet(name) that prints "Hello, {name}!". Call it twice with different names.
def greet(name):
    print(f"Hello, {name}!")

greet("Denis")
greet("Anna")

print()
# Task 3 — return instead of print
# Write a function add(a, b) that returns the sum of two numbers. Save the result in a variable and print it.
def add(a, b):
    return a + b

result = add(5, 10)
print(result)

print()
# Task 4 — Function with a condition
# Write a function is_passed(status) that returns True if status equals "passed", otherwise False. Test it on two values.
def is_passed(status):
    if status == "passed":
        return True
    else:
        return False

print(is_passed("passed"))
print(is_passed("failed"))

print()
# Task 5 — Function that calculates something useful
# Write a function success_rate(passed, total) that returns the percentage of successful tests rounded to 1 decimal.
# Call it with passed=7, total=10.
def success_rate(passed, total):
    return round((passed / total) * 100, 1)

print(success_rate(7, 10))
