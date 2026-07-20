#Write a program to find the largest of three numbers. 
num1=float(input("Enter number1:"))
num2=float(input("Enter number2:"))
num3=float(input("Enter number3:"))

if num1>num2 and num1>num3:
    print(num1,"is greater")
elif num2>num1 and num2>num3:
    print(num2,"is greater")
else:
    print(num3,"is greater") 