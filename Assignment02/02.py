
print("Enter time --> Hour:Minute:Second")

Time = list(input().split(':'))

Second = int(Time[0]) * 3600
Minute = int(Time[1]) * 60
Hour = int(Time[2])

second = Second + Minute + Hour

print("Seconds: ", second)
