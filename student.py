print("student Marksheet")

name = input("Enter student Name:")
rollno = input("Enter student rollno:")
CollageName = input("Enter CollageName:")

maths = float(input("Enter maths mark:"))
English = float(input("Enter English mark:"))
science = float(input("Enter Science marks:"))
Hindi = float(input("Enter Hindi mark:"))
Gujrati = float(input("Enter Gujrati mark:"))

total = maths + English + science + Hindi + Gujrati
persentage = total / 5

print("\n Marksheet ")
print("Name:",name)
print("maths:",maths)
print("English:",English)
print("Science:",science)
print("Hindi:",Hindi)
print("Gujrati:",Gujrati)

