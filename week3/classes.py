# Task 1 — Your first class
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def greet(self):
        print(f"Hi, I'm {self.name} from {self.city}")

person = Person("Denis", 38, "Prague")
person2 = Person("Daniel", 40, "Prague")
person.greet()
person2.greet()

print("-------")
print(person.name)
print(person.age)
print(person.city)
print("-------")
print(person2.name)
print(person2.age)
print(person2.city)

print()
# Task 2 — Class with a method that returns
# Create a class Rectangle with width and height. Add a method area() that returns the area (width × height).
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print(rect.area())

print()
# Task 3 — Method using object data
# Create a class BankAccount with owner and balance. Add a method deposit(amount) that adds to the balance,
# and show_balance() that prints the current balance.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")


account = BankAccount("Denis", 100)
account.deposit(50)
account.show_balance()

print()
# Task 4 — Default value in init
# Create a class TestCase with name and status (default "not run"). Add a method run() that sets status to "passed".
class TestCase:
    def __init__(self, name, status="not run"):
        self.name = name
        self.status = status

    def run(self):
        self.status = "passed"

test = TestCase("test_login")
print(test.status)
test.run()
print(test.status)

print()
# Task 5 — Counter inside object
# Create a class TestRunner with a passed counter starting at 0. Add methods add_pass() (increases counter)
# and report() (prints total passed).
class TestRunner:
    def __init__(self):
        self.passed = 0

    def add_pass(self):
        self.passed += 1

    def report(self):
        print(f"Total passed: {self.passed}")

runner = TestRunner()
runner.add_pass()
runner.add_pass()
runner.add_pass()
runner.report()
