Num = int(input("Enter a number: "))

Fibo_Series = []

for i in range(Num):

    if i < 2:
        Fibo_Series.append(1)

    else:
        Fibo_Series.append(Fibo_Series[i-1] + Fibo_Series[i-2])


print("Fibo Series: ", Fibo_Series)