print("First Function Program\n")
def greet():
	print("Hello! Welcome to Python.")
greet()
print("\n")

############# Addition #############
print("Addition Example:")
def add(a, b):
    return a + b
result = add(5, 3)
print(result)
print("\n")

############# Variable Scope #############
print("Variable Scope Example:")
x=10
def show_scope():
    x=5
    print(x)
show_scope()
print(x)
print("\n")

############# Modules #############
print("Modules Example:")
import math
import random
print(math.sqrt(16))
print(random.randint(-10, -1))






