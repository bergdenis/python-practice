# Task 1 — Catch division by zero
# Write code that tries to divide 10 by 0 and catches the ZeroDivisionError, printing "Cannot divide by zero".
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

print()
# Task 2 — Catch ValueError
# Try to convert "abc" to an integer. Catch the ValueError and print "Invalid number".
try:
    number = int("abc")
except ValueError:
    print("Invalid number")

print()
# Task 3 — Catch KeyError
# Given a dict, try to access a missing key. Catch the KeyError and print "Key not found".
data = {"name": "Denis", "role": "QA"}

# Try to access data["age"].
try:
    user_age = data["age"]
except KeyError:
    print("Key not found")

print()
# Task 4 — Get error message
# Try to convert "hello" to int. Catch the error using as e and print the actual error message.
try:
    number = int("hello")
except ValueError as e:
    print(f"Error: {e}")

print()
# Task 5 — try/except/else/finally
# Write code that divides 10 by 2. Use all four blocks: try, except, else, finally.
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")
    print("Division successful")
finally:
    print("Operation complete")

print()
# Task 6 — Function with error handling
# Write a function safe_divide(a, b) that returns the division result, or returns "Error: division by zero" if b is 0.
# Test:
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: division by zero"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
