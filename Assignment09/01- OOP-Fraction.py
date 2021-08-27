class fraction:

    def __init__(self, s, m):
        self.numerator = s
        self.denominator = m

    def sum(self, second_number):
        result = fraction(None, None)
        result.numerator = (self.numerator * second_number.denominator) + (second_number.numerator * self.denominator)
        result.denominator = self.denominator * second_number.denominator
        return result

    def mul(self, second_number):
        result = fraction(None, None)
        result.numerator = self.numerator * second_number.numerator
        result.denominator = self.denominator * second_number.denominator
        return result

    def sub(self, second_number):
        result = fraction(None, None)
        result.numerator = (self.numerator * second_number.denominator) - (second_number.numerator * self.denominator)
        result.denominator = self.denominator * second_number.denominator
        return result

    def div(self, second_number):
        result = fraction(None, None)
        result.numerator = self.numerator * second_number.denominator
        result.denominator = self.denominator * second_number.numerator
        return result

    def show(self):
        print(self.numerator, '/', self.denominator)


def show_Op():
    print('1- mul')
    print('2- div')
    print('3- sum')
    print('4- sub')
    print('5- exit')

while True:
    show_Op()
    op = int(input("Please select operator: "))

    print("Please enter first fraction --> numerator / denominator ")
    fraction1 = list(input().split('/'))
    fraction1 = fraction(int(fraction1[0]), int(fraction1[1]))

    print("Please enter second fraction --> numerator / denominator ")
    fraction2 = list(input().split('/'))
    fraction2 = fraction(int(fraction2[0]), int(fraction2[1]))

    if op == 1:
        m = fraction1.mul(fraction2)
        print("\nmul of two fraction : ")
        m.show()

    elif op == 2:
        d = fraction1.div(fraction2)
        print("\ndiv of two fraction : ")
        d.show()

    elif op == 3:
        sum = fraction1.sum(fraction2)
        print("\nSum of two fraction : ")
        sum.show()

    elif op == 4:
        sub = fraction1.sub(fraction2)
        print("\nSub of two fraction : ")
        sub.show()

    elif op == 5:
        break

    choice = input("If you want to continue enter 'y' : ")
    if choice == 'y':
        continue
    else:
        break
