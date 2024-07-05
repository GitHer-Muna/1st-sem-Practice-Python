# Program to calculate actual salary of an employee with income tax..

Salary = int(input("Please! Enter the salary amount...\n"))

if Salary < 3000:
    print("Actual salary with 0% Income Tax is :", Salary)

elif Salary in range(3000,5000):
    Salary = Salary - Salary*6/100
    print("Actual salary with 6% Income Tax is :", Salary)

elif Salary in range(5000,7000):
    Salary = Salary - Salary*8/100
    print("Actual salary with 8% Income Tax is :", Salary)

elif Salary in range(7000,8000):
    Salary = Salary - Salary*12/100
    print("Actual Salary with 12% Income Tax is :", Salary)

elif Salary in range(8000,9000):
    Salary = Salary - Salary*16/100
    print("Actual salary with 16% Income Tax is :", Salary)

else:
    Salary = Salary - Salary*40/100
    print("Actual Salary with 40% Income Tax is :", Salary)