import random

Num = int(input("Enter a number: "))

Array = random.sample(range(0, Num * 10), Num)

print(Array)