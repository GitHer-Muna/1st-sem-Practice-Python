#Fibonacci_Series

n = int(input("Please! Enter the maximum number...\n"))
a = 0 
b = 1
print(a)
print(b)

for i in range(2,n):
    c = a + b
    a = b
    b = c
    print(a + b)