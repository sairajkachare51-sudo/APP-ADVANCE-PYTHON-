#Write a program to find the greatest among three numbers using nested if
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b:
    if a > c:
        print("Greatest number is:", a)
    else:
        print("Greatest number is:", c)
else:
    if b > c:
        print("Greatest number is:", b)
    else:
        print("Greatest number is:", c)