Name = input("Enter your name: ")
Score1 = float(input("Enter Score1: "))
Score2 = float(input("Enter Score2: "))
Score3 = float(input("Enter Score3: "))

Avg = (Score1 + Score2 + Score3) / 3

if Avg >= 17:
    print("Educational_Evaluation is Great")

if 17 > Avg >= 12:
    print("Educational_Evaluation is Normal")

if Avg < 12:
    print("Educational_Evaluation is Fail")