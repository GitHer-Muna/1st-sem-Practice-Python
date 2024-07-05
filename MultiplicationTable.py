# Program to display the multiplication table of number entered by user

Number = int(input('Please! Enter a number...\n'))

for i in range(1,11):
    print(Number, 'X', i, '=', Number*i)