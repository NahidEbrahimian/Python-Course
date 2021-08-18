import numpy as np

n = int(input("Enter number: "))
kh_pas = np.zeros([n, n], dtype= 'int')

for i in range(n):
    print('\n')
    for j in range(n):

        if j <= i:
            if i == j  or (j == 0 and i != 0) :
                kh_pas[i, j] = 1
                print(kh_pas[i, j], end =" ")

            else :
                kh_pas[i, j] = kh_pas[i-1, j-1] + kh_pas[i-1, j]
                print(kh_pas[i, j], end =" ")


print('\n\n', kh_pas)
