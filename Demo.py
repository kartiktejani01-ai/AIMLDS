#import keyword;
#print(keyword.kwlist)
no = 3

if no % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# Write a program using membership (in. not in) and identity (is. is not)
#operators on lists and variables.

number = [10,20,30,40,50] 

print("20 in number:",20 in number)
print("90 not in number:", 90 not in number)

a = 10
b = 20
c = 5

print("a is b", a is b)
print("a is not c", a is not c)

#Write a program to demonstrate operator precedence using colnplcx
#arithmetic expressions
result1 = a * b + c
result2 = a + b * 2
result3 = a / b + c
result4 = (a + c) * b - 2

print("Expression1",result1)
print("Expression2", result2)
print("Expression3", result3)
print("Expression4", result4)

# celsius convert fernhit to kelvin
C = 25
F = (C * 9 / 5)+ 32
K = C + 273.15

print("Temprature Celsius:", C)
print("Temprature Ferenhit:", F)
print("Temprature Kelvin:", K)
