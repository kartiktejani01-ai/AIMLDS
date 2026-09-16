a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a > b :
    if a > c :
        largest = a
    else:
        largest = c
else :
    if b > c:
        largest = b
    else :
        largest = c

print("Largest number", largest)

#for loop
num  = int(input("Enter number"))

for i in range(1 , 11):
    print(num, "x", i, "=", num * i)

