def calculate_salary(basic):
    hra=(20/100)*basic
    da=(10/100)*basic
    if basic>=50000:
        bonus=(10/100)*basic
    else:
        bonus=(5/100)*basic
    gross=hra+da+bonus+basic
    print("HRA:",hra)
    print("DA:",da)
    print("Bonus:",bonus)
    return gross
salary=int(input("Enter basic salary: "))
print("Gross Salary:",calculate_salary(salary))