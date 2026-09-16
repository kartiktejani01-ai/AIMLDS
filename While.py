no = int(input("Enter number:"))
i = 1
sum = 0
while i <= no:
    sum = sum + i
    i = i + 1
print("Sum is:", sum)

# Fibonacci Series
n = int(input("Enter Number"))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a+b
    a = b
    b = c