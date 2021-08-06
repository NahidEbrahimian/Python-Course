num = int(input("Enter number of students: "))

Max_number = 0
Min_number = 20
Sum_numbers = 0


for i in range(num):
    Score = float(input("Enter the programming score: "))

    if Score > Max_number:
        Max_number = Score

    if Score < Min_number:
        Min_number = Score

    Sum_numbers = Sum_numbers + Score

Average = Sum_numbers / num

print("Max_number: ", Max_number, ", Min_number: ", Min_number, ", Average: ", Average)