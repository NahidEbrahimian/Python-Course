print("***triangle***")
a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))

if a+b > c and a+c > b and b+c > a:
    print("Ok")
else:
    print("Error")