from tkinter import Y


def BiggestNum():
    x=int(input("Num1:"))
    y=int(input("Num2:"))
    z=int(input("Num32:"))
    if (x>y) and (x>z):
        print("Largest no is ",x)
    if (y>x) and (y>z):
        print("Largest no is ",y)
    if (z>x) and (z>y):
        print("Largest no is ",z)

def ArmstrongNo():
    num = int(input("Enter a number: "))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")

def ReverseNum():
    number = int(input("Enter the integer number: "))  
    revs_number = 0  
    while (number > 0):   
        remainder = number % 10  
        revs_number = (revs_number * 10) + remainder  
        number = number // 10  
    print("The reverse number is : {}".format(revs_number))

def Sumofdigit():  
    n=int(input("Enter the Number:"))
    sum = 0
    while (n != 0):  
        sum = sum + (n % 10)
        n = n//10       
    print("The sum of digits is",sum)
    
def hcf():  
    x = int(input("Enter first number: "))  
    y = int(input("Enter second number: "))
    if x > y:  
        smaller =y  
    else:  
        smaller = x  
    for i in range(1,smaller + 1):  
        if((x % i == 0) and (y % i == 0)):  
            hcf = i  
    print("The H.C.F. of", x,"and", y,"is", hcf)

def compute_lcm():
    x = 54
    y = 24
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    print("The L.C.M. is",lcm)

def leapyear():
    year = int(input("Enter a year: "))
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))

def typesoftriangle():
    print("Input lengths of the triangle sides: ")
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))

    if x == y == z:
	    print("Equilateral triangle")
    elif x==y or y==z or z==x:
	    print("isosceles triangle")
    else:
	    print("Scalene triangle")

def quadroots():
    import cmath  
    a = float(input('Enter a: '))  
    b = float(input('Enter b: '))  
    c = float(input('Enter c: '))    
    d = (b**2) - (4*a*c)  
    sol1 = (-b-cmath.sqrt(d))/(2*a)  
    sol2 = (-b+cmath.sqrt(d))/(2*a)  
    print('The solution are {0} and {1}'.format(sol1,sol2))

def quadrant():
    X= int(input('Enter value for X-axis :'))
    Y= int(input('Enter value for Y-axis :'))
    if X > 0 and Y > 0:
        print('X and Y lie at First quadrant')
    elif X < 0 and Y > 0:
        print('X and Y lie at Second quadrant')
    elif X < 0 and Y < 0:
        print('X and Y lie at Third quadrant')
    elif X > 0 and Y < 0:
        print('X and Y lie at Fourth quadrant')
    else: 
        print('X and Y lie at Origin')

