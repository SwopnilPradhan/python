a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))


if a > b and a > c :
    print(a, "is the largest of three numbers.")
elif b > c and b > a :
    print(b, "is the largest of three numbers.")
elif c > a and c > b :
    print(c, "is the largest of three numbers.")
else :
    print("The numbers are equal")