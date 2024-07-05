#Program to Count total digit

Number = int(input('Please! Enter a number...\n'))
count = len(str(abs(Number)))

print("The total number of digit is :",count)

#Another way

count = 0
while Number > 0 :
    count = count + 1
    Number = Number // 10
print("Total number of digit is :", count)