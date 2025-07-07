
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == '+':
    print(f"{a} + {b} = {a + b}")
elif operation == '-':
    print(f"{a} - {b} = {a - b}")
elif operation == '*':
    print(f"{a} * {b} = {a * b}")
elif operation == '/':
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Error: Division by zero")
else:
    print("Sorry,Invalid operation")