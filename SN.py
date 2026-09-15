Student_Name = (input("Enter Student_Name:"))
Rollno = int(input("Enter Rollno:"))

English = float(input("Enter English Mark:"))
Math = float(input("Enter Math Mark:"))
Python = float(input("Enter Python Mark:"))

total = English + Math + Python 

percentage = total / 3
if percentage >= 90:
    Grade = "A"
elif percentage >=70:
    Grade = "B"
else:
    Grade = "C"


print("English:",+English)
print("Math:",+Math)
print("Python:",+Python)
print("total:",+total)
print(f"percentage:{percentage:.2f}%")
print("Grade:",Grade)