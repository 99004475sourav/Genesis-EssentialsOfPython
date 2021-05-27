def choiceArith(num1, num2, choice):
    #num1= float(input(" Please Enter the First Value Number 1: "))
    #num2= float(input(" Please Enter the Second Value Number 2: "))
    #choice= int(input("Enter your choice:-\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n"))
    if choice==1:
        print("Sum is",(num1+num2))
    elif choice==2:
        print("Diff is",(num1-num2))
    elif choice==3:
        print("Product is",(num1*num2))
    elif choice==4:
        print("Division is",(num1/num2))

num1= float(input(" Please Enter the First Value Number 1: "))
num2= float(input(" Please Enter the Second Value Number 2: "))
choice= int(input("Enter your choice:-\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n"))
choiceArith(num1, num2, choice)