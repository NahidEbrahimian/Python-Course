import math

op = input("Enter selected operator between: +, -, *, /, Radical, sin, cot, cos, tan, factorial : ")

if op == '+' or op == '-' or op == '*' or op == '/':

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if op == '+':
        print("a + b = ", a+b)

    if op == '-':
        print("a + b = ", a - b)

    if op == '*':
        print("a + b = ", a * b)

    if op == '/':
        if b == 0:
            print("Second number cannot be zero")

        else:
            print("a / b = ", a / b)

elif op == 'Radical' or op == 'sin' or op == 'cot' or op == 'cos' or op == 'tan' or op == 'factorial':

    a = float(input("Enter number: "))

    if op == 'Radical':
        if a < 0:
            print("i")

        else:
            print("Radical = ", math.sqrt(a))

    if op == 'sin':
        print("sin = ", math.sin(math.radians(a)))

    if op == 'cot':

        sin = math.sin(math.radians(a))
        cos = math.cos(math.radians(a))
        print("cot = ", cos/sin)

    if op == 'cos':
        print("cos = ", math.cos(math.radians(a)))

    if op == 'tan':
        print("tan = ", math.tan(math.radians(a)))
        print("tan = ", sin/cos)

    if op == 'factorial':
        print("factorial = ", math.factorial(int(a)))