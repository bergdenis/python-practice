# Task 1 — Variables and print
# Create variables: your name, age, city, salary (with decimals), are you currently employed (True/False). Print each
# one with a label.
name = 'Denis'
age = 38
city = 'Prague'
salary = 85000.5
employed = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Salary: {salary}")
print(f"Employed: {employed}")

print()
# Task 2 — Data types
# Create one variable of each type: str, int, float, bool. Print both the value and its type using type().
name = 'Denis'
age = 38
salary = 85000.5
employed = True

print(name, type(name))
print(age, type(age))
print(salary, type(salary))
print(employed, type(employed))

print()
# Task 3 — Arithmetic
# Given two variables: price = 1500 and quantity = 7.
# Calculate and print: the total amount, the remainder of total divided by 4, the price doubled, and the integer part
# of total divided by 100.

price = 1500
quantity = 7

total = price * quantity

print("Total amount:", total)
print("Remainder of total divided by 4:", total % 4)
print("Price doubled:", price * 2)
print("Integer part of total divided by 100:", total // 100)

print()
# Task 4 — Strings and f-strings
# Create variables first_name, last_name, position. Combine and print them in a single line using an f-string:
# QA Engineer Denis Berg is ready to automate.

first_name = "Denis"
last_name = "Berg"
position = "QA Engineer"

print(f"{position} {first_name} {last_name} is ready to automate.")

print()
# Task 5 — Type conversion
# Given variables age = "38" (a string!) and bonus = 5000 (an integer). Add them together and print the result.
# Without conversion you'll get an error — your task is to fix it and understand why it happens.

age = "38"
bonus = 5000

print(int(age) + bonus)
