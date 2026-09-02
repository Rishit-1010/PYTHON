def check_loan(age, salary, creditscore):
    flag=False
    if 21<=age<=60:
        if 30000<=salary:
            if 700<=creditscore:
                flag=True
    return flag
age=int(input("Enter your age: "))
salary=int(input("Enter monthly salary: "))
creditscore=int(input("Enter credit score: "))
print("Loan Approved!" * check_loan(age, salary, creditscore) or "Loan Denied!")