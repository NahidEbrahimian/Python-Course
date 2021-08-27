class time:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def sum(self, time2):
        result = time(None, None, None)
        result.s = (self.second + time2.second)
        result.m = (self.minute + time2.minute)
        result.h = (self.hour + time2.hour)
        if result.s >= 60:
            result.s -= 60
            result.m += 1
        if result.m >= 60:
            result.m -= 60
            result.h += 1

        return result

    def sub(self, time2):
        result = time(None, None, None)
        result.s = (self.second - time2.second)
        result.m = (self.minute - time2.minute)
        result.h = (self.hour - time2.hour)
        if result.s <= 0:
            result.s += 60
            result.m -= 1
        if result.m <= 0:
            result.m += 60
            result.h -= 1

        return result

    def convert_time_to_second(self):
        h = self.hour * 3600
        m = self.minute * 60
        seconds = h + m + self.second
        return seconds

    def convert_second_to_time(self, Seconds):
        result = time(None, None, None)
        result.h = int(Seconds // 3600)
        result.m = int((Seconds - (result.h * 3600)) // 60)
        result.s = ((Seconds - (self.hour * 3600) - (self.minute * 60)) % 60)
        return result


def show_Op():
    print('1- sum')
    print('2- sub')
    print('3- convert_time_to_second')
    print('4- convert_second_to_time')
    print('5- exit')

while True:
    show_Op()
    op = int(input("Please select operator: "))

    if op == 1 or op == 2:
        print("Please enter first time --> Hour : Minute : Second")
        time1 = list(input().split(':'))
        time1 = time(int(time1[0]), int(time1[1]), int(time1[2]))

        print("Please enter second time --> Hour : Minute : Second")
        time2 = list(input().split(':'))
        time2 = time(int(time2[0]), int(time2[1]), int(time2[2]))

        if op == 1:
            sum = time1.sum(time2)
            print(str(sum.h).zfill(2), ':', str(sum.m).zfill(2), ':', str(sum.s).zfill(2))

        if op == 2:
            sub = time1.sub(time2)
            print(str(sub.h).zfill(2), ':', str(sub.m).zfill(2), ':', str(sub.s).zfill(2))

    elif op == 3:
        print("Please enter first time --> Hour : Minute : Second")
        time1 = list(input().split(':'))
        time1 = time(int(time1[0]), int(time1[1]), int(time1[2]))
        seconds = time1.convert_time_to_second()
        print(seconds)

    elif op == 4:
        second = int(input("Enter seconds : "))
        hour = time(0, 0, 0)
        hour = hour.convert_second_to_time(second)
        print(str(hour.h).zfill(2), ':', str(hour.m).zfill(2), ':', str(hour.s).zfill(2))

    elif op == 5:
        break

    choice = input("If you want to continue enter 'y' : ")
    if choice == 'y':
        continue
    else:
        break





