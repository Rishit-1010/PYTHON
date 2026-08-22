flag=True
while flag:
    print("------------------------MENU------------------------")
    print("1. Calculate Simple Interest")
    print("2. Calculate Compund Interest")
    print("3. Currency conversion(rupees to US dollar)")
    print("4. Exit")
    a=int(input("Enter: "))
    if a==1:
        p=int(input("Enter Principle: "))
        r=int(input("Enter Rate of Interest: "))
        t=int(input("Enter Time: "))
        si=(p*r*t)/100
        print("Simple Interest is ₹",si)
    elif a==2:
        p=int(input("Enter Principle: "))
        r=int(input("Enter Rate of Interest: "))
        t=int(input("Enter Time: "))
        ci=p*((1+(r/100))**t)
        print("Compound Interest is ₹",ci)
    elif a==3:
        r=int(input("Enter currency in ₹: "))
        d=r/83
        print("Currency in US dollar is $",d)
    elif a==4:
        print("Exiting....")
        flag=False
        import keyboard
        import time
        time.sleep(0.5)
        keyboard.send("ctrl+`")