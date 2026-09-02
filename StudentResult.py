def calculate_result():
    m1=int(input("Enter marks obtained in Maths: "))
    m2=int(input("Enter marks obtained in Physics: "))
    m3=int(input("Enter marks obtained in Chemistry: "))
    a=((m1+m2+m3)/150)*100
    if a>=90:
        grade=("A+")
    elif 90>a>=75:
        grade=("A")
    elif 85>a>=60:
        grade=("B")
    elif 60>a>=40:
        grade=("C")
    elif 40>a:
        grade=("Fail")
    print("Percentage =",a)
    print("Grade=",grade)
calculate_result()