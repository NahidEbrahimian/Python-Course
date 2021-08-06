Sum = 0

while True:

    x = input("If you want to continue enter a number else type 'exit': ")

    if x == 'exit':
        break

    else:
        Sum = Sum + int(x)

print("Sum = ", Sum)