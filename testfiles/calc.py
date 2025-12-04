# Simple Calculator

def calculator():
    print("Operations: +  -  *  /")
    op = input("Enter operator: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero")
    else:
        print("Invalid operator")

# Run
calculator()
