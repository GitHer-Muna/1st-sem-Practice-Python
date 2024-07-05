# Program to check leap year

Year = int(input("Enter the year...\n"))

if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
    print("This is Leap Year.")
else:
    print("This is not Leap Year.")