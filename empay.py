def calculate_salary(basic, bonus, deduction):
    salary = basic + bonus - deduction
    return salary

name = input("Enter Name:")
basic = float(input("Enter basic:"))
bonus = float(input("Enter bonus:"))
deduction = float(input("Enter deduction:"))

net_salary = calculate_salary(basic, bonus, deduction)

print("Employee Name:",name)
print("net_salary:",net_salary)
