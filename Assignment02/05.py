from random import randint

while True:

    Dice_Number = randint(1, 6)

    if Dice_Number == 6:

        print("Dice number is : ", Dice_Number)
        print("****You won an award****")

    else:

        print("Dice number is : ", Dice_Number)
        Play = input("If you want to continue enter 'y' : ")

        if Play != 'y':
            break

print("Ended")