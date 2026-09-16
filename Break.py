# Break Statement
for i in range(1 , 6):
    if i == 3:
        break
    print(i)
print("Break Statement")

# continue Statement
for i in range(1 , 6):
    if i == 3:
        continue
    print(i)
print("Continur Statement")

#Pass Statement
for i in range(1 , 6):
    if i == 3:
        pass
    print(i)

# even number Generate
even = [i for i in range(1 , 50) if i % 2 == 0]
print("even", even)