# Way 1 — import the whole module
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))

# Way 2 — import specific functions
from calculator import multiply

print(multiply(10, 5))
