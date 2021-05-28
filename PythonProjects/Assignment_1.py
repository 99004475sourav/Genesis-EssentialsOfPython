from tkinter import Y


def BiggestNum(x,y,z):
    #x=int(input("Num1:"))
    #y=int(input("Num2:"))
    #z=int(input("Num3:"))
    if (x>y) and (x>z):
        print("Largest no is ",x)
        return x
    if (y>x) and (y>z):
        print("Largest no is ",y)
        return y
    if (z>x) and (z>y):
        print("Largest no is ",z)
        return z

def ArmstrongNo(num):
    #num = int(input("Enter a number: "))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num,"is an Armstrong number")
        return 1
    else:
        print(num,"is not an Armstrong number")
        return 0

def ReverseNum(number):
    #number = int(input("Enter the integer number: "))  
    revs_number = 0  
    while (number > 0):   
        remainder = number % 10  
        revs_number = (revs_number * 10) + remainder  
        number = number // 10  
    print("The reverse number is : {}".format(revs_number))
    return revs_number

def Sumofdigit(n):  
    #n=int(input("Enter the Number:"))
    sum = 0
    while (n != 0):  
        sum = sum + (n % 10)
        n = n//10       
    print("The sum of digits is",sum)
    return sum
    
def myhcf(x,y):  
    #x = int(input("Enter first number: "))  
    #y = int(input("Enter second number: "))
    if x > y:  
        smaller =y  
    else:  
        smaller = x  
    for i in range(1,smaller + 1):  
        if((x % i == 0) and (y % i == 0)):  
            hcf = i  
    print("The H.C.F. of", x,"and", y,"is", hcf)
    return hcf

def compute_lcm(x,y):
    #x = 54
    #y = 24
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
    return lcm

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

def choiceArith():
    num1= float(input(" Please Enter the First Value Number 1: "))
    num2= float(input(" Please Enter the Second Value Number 2: "))
    choice= int(input("Enter your choice:-\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n"))
    if choice==1:
        print("Sum is",(num1+num2))
    elif choice==2:
        print("Diff is",(num1-num2))
    elif choice==3:
        print("Product is",(num1*num2))
    elif choice==4:
        print("Division is",(num1/num2))    

def fibonacci():
    nterms = int(input("How many terms? "))
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
    else:
        print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

def factorial(num):
    #num = int(input("Enter a number: "))
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
    print("The factorial of",num,"is",factorial)
    return factorial

def sumoffactors():
    import math 
    n=int(input("Enter the Number"))
    if(n == 1):
        return 1
    result = 0
    for i in range(2,(int)(math.sqrt(n))+1) :
        if (n % i == 0) :
            if (i == (n/i)) :
                result = result + i
            else :
                result = result + (i + n//i)
    print(result+n+1)

def isvowel():
    ch = input("Enter a character: ")

    if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        print(ch, "is a Vowel")
    else:
        print(ch, "is a Consonant")
 
def primerange(upper):
    #lower = int(input("Enter lower range: "))  
    #upper = int(input("Enter upper range: "))  
    c=0
    for num in range(1,upper + 1):  
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:  
                    break  
            else:  
                print(num)
                c=c+1
    print(c)
    return c
        
def triangularsum(n): 
    sum = 0
    for i in range(1, n + 1):
        sum += i * (i + 1) / 2
    print(sum)
    return sum
    

def SieveOfEratosthenes(n,isPrime):
    isPrime[0] = isPrime[1] = False
    for i in range(2,n+1):
        isPrime[i] = True
    
    for p in range(2,n+1):
        if (p*p<=n and isPrime[p] == True):
            for i in range(p*2,n+1,p):
                isPrime[i] = False
                p += 1
def superprime(n):
    isPrime = [1 for i in range(n+1)]
    SieveOfEratosthenes(n, isPrime)
    primes = [0 for i in range(2,n+1)]
    j = 0
    for p in range(2,n+1):
        if (isPrime[p]):
            primes[j] = p
            j += 1
    for k in range(j):
        if (isPrime[k+1]):
            print(primes[k])

def nCr(n, r):
    
    res=(factorial(n) / ((factorial(r))*(factorial(n - r))))
    print (res)
    return res

def trianglepyramid(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")

def pascalstri(n):
    for line in range(0, n) :
        for i in range(0, line + 1) :
            print(binomialCoeff(line, i),
                " ", end = "")
        print()
def binomialCoeff(n, k) :
    res = 1
    if (k > n - k) :
        k = n - k
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)
     
    return res

BiggestNum(4,5,6)
ArmstrongNo(153)
ReverseNum(345)
Sumofdigit(123)
myhcf(8,4)
compute_lcm(6,9)
primerange(10)
triangularsum(7)
superprime(241)
nCr(5,3)
trianglepyramid(5)
pascalstri(5)