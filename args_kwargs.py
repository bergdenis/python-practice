# Task 1 — Default value
# Write a function greet(name, greeting="Hello") that prints "{greeting}, {name}!". Call it once with default
# greeting, once with custom.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Denis")
greet("Anna", "Hi")

print()
# Task 2 — Default value with number
# Write a function connect(host, port=8080) that prints "Connecting to {host}:{port}". Call once with default port,
# once with port 3000.
def connect(host, port=8080):
    print(f"Connecting to {host}:{port}")

connect("localhost")
connect("api.example.com", 3000)

print()
# Task 3 — args basics
# Write a function add_all(*args) that returns the sum of all numbers passed.
# Test:
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3))
print(add_all(10, 20, 30, 40))

print()
# Task 4 — args with loop
# Write a function print_tests(*args) that prints each test name on a new line with its number.
# Test:
def print_tests(*args):
    for number, test_name in enumerate(args, start=1):
        print(f"{number}. {test_name}")

print_tests("test_login", "test_logout", "test_search")

print()
# **Task 5 — **kwargs basics
# Write a function show_config(**kwargs) that prints each key-value pair.
# Test:
def show_config(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_config(env="staging", timeout=30, retries=3)
