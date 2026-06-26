# Task 1 — Basic inheritance
# Create a parent class Animal with name and method eat(). Create a child class Cat(Animal) that adds method meow().
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")


cat = Cat("Whiskers")
cat.eat()    # uses parent method
cat.meow()   # own method

print()
# Task 2 — super() basics
# Create a parent class Employee with name and position. Create a child class Manager(Employee) that adds team_size.
# Use super() in the constructor.
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Manager(Employee):
    def __init__(self, name, position, team_size):
        super().__init__(name, position)
        self.team_size = team_size


manager = Manager("Denis", "QA Lead", 5)
print(manager.name)
print(manager.position)
print(manager.team_size)

print()
# Task 3 — Inherited method uses child data
# Create parent Vehicle with brand and method info() that prints the brand. Create child Car(Vehicle) that adds model.
# Override info() to print both brand and model.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print(self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def info(self):
        print(f"{self.brand} {self.model}")


car = Car("Toyota", "Corolla")
car.info()

print()
# Task 4 — QA example
# Create a parent class BaseTest with name and method setup() that prints "Setting up {name}". Create a child
# LoginTest(BaseTest) that adds method run() printing "Running {name}".
class BaseTest:
    def __init__(self, name):
        self.name = name

    def setup(self):
        print(f"Setting up {self.name}")

class LoginTest(BaseTest):
    def run(self):
        print(f"Running {self.name}")


test = LoginTest("test_login")
test.setup()   # parent method
test.run()     # own method
