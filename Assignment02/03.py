Seconds = int(input("Enter Seconds : "))

Hour = int(Seconds // 3600)
Minute = int((Seconds - (Hour * 3600)) // 60)
Second = ((Seconds - (Hour * 3600) - (Minute * 60)) % 60)

print(str(Hour).zfill(2), ':', str(Minute).zfill(2), ':', str(Second).zfill(2))