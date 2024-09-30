import math

print("-------------------------Choose Triangle-------------------------")
print("1. Scalene Triangle")
print("2. Isosceles Triangle")
print("3. Equilateral triangle")

t = int(input("Enter your choice (in number)     \n"))
if t == 1 :
  s1 = int(input("Enter first side     \n"))
  s2 = int(input("Enter second side     \n"))
  s3 = int(input("Enter third side     \n"))
  s = float((s1 + s2 + s3)/2)
  a = float(s*(s-s1)*(s-s2)*(s-s3))
  print("Area of scalene triangle")
  print(math.sqrt(a)) 
elif t == 2 :
  h = int(input("Enter measure of height   \n"))
  sd2 = int(input("Enter base side     \n"))
  
  a = float(0.5*(h*sd2))
  print("Area of isosceles triangle is ", a)
elif t == 3 :
   si2 = int(input("Enter side     \n"))
   f = math.sqrt(3)
   print("Area of Equilateral triangle is ", f/4 * si2 * si2)
else :
    print("Number between 1-3")