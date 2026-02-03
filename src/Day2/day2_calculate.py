a=input("Enter first number: ")
b=input("Enter second number: ")

operation = input("Enter operation (+, -, *, /, %): ")
if operation == '+':
    print("Addition: ", float(a)+float(b))
elif operation == '-':
    print("Subtraction: ", float(a)-float(b))
elif operation == '*':
    print("Multiplication: ", float(a)*float(b))
elif operation == '/':
    if float(b) != 0:
        print("Division: ", float(a)/float(b))
    else:
        print("Error: Division by zero")
elif operation == '%':
    print("Modulus: ", float(a)%float(b))
else:
    print("Invalid operation")
