#multiply table by for loop
print ("Multiplication table printing by for loop")
a = int(input("enter first number:  \n"))            #Taking input
for n in range(1,11):                      #Condition
    print(a,"X", n, "=", n*a)                #Output
    