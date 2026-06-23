# Task 1 — Basic while
# Given:
count = 1

# Print numbers from 1 to 10 using while loop.
while count <= 10:
    print(count, end=" ")
    count += 1


print()
print()
# Task 2 — Retry logic
# Given
retry_count = 0
max_retries = 5

# Simulate retry logic — print "Attempt X" until max retries reached, then print "Max retries reached".
while retry_count < 5:
    print(f"Attempt {retry_count + 1}")
    retry_count += 1

print("Max retries reached")

print()
# Task 3 — while with break
# Given
attempts = 0
correct_password = "qa123"
entered_password = ""

# Simulate password attempts — on each iteration set password = "qa123" on attempt 3 (use attempts == 3 to change it).
# Break when correct password entered, print " X attempts".
while entered_password != correct_password:
    attempts += 1
    if attempts == 3:
        entered_password = correct_password
        print(f"Access granted after {attempts} attempts")
    else:
        entered_password = "123"
        print(f"Wrong password, attempt: {attempts}")

print()
# Task 4 — while with continue
# Given
number = 0

# Print only odd numbers from 1 to 15 using continue to skip even ones.
while number <= 15:
    if number % 2 == 0:
        number += 1
        continue
    print(number, end=" ")
    number += 1

print()
# Task 5 — Accumulator
# Given
response_times = [120, 340, 89, 456, 210, 78, 534]
index = 0
total = 0

# Using while loop calculate total and average response time.
while index < len(response_times):
    total += response_times[index]
    index += 1
average = total / len(response_times)

print(f"Total: {total}ms")
print(f"Average: {average}ms")
