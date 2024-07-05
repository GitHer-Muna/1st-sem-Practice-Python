# Program to show the sum of total digit of number from user

Number = int(input('Please! Enter a number...\n'))

SumDigit = 0

for i in str(Number):
    SumDigit += int(i)
print("The sum is :",SumDigit)