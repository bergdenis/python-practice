# Task 1 — Basic property (getter)
# Create a class Circle with radius. Add a property called area that returns the area (3.14 × radius × radius).
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius * self.radius


circle = Circle(5)
print(circle.area)     # note: no () — it's a property

print()
# Task 2 — Property as computed field
# Create a class Person with first_name and last_name. Add a property full_name that returns them combined.
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


person = Person("Denis", "Berg")
print(person.full_name)

print()
# Task 3 — Getter and setter with validation
# Create a class Account with _balance. Add:
# a property balance (getter) that returns _balance
# a setter that prevents negative values (prints "Cannot be negative" if value < 0)
class Account:
    def __init__(self, balance):
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Cannot be negative")
        else:
            self._balance = value


account = Account(100)
print(account.balance)
account.balance = 200
print(account.balance)
account.balance = -50
print(account.balance)

# 100
# 200
# Cannot be negative
# 200
