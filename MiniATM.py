with open("pin.txt","r") as file:
    pin=file.read()
with open("balance.txt") as file:
    b=file.read()
flag=True
print("----------------------ATM----------------------")
p=input("Enter your PIN: ")
if p!=pin:
    p=input("Incorrect PIN! Try again: ")
    if p!=pin:
        p=input("Incorrect PIN! Try again: ")
        if p!=pin:
            print("Incorrect PIN! Account is locked.")
            import keyboard
            import time
            time.sleep(0.5)
            keyboard.send("Ctrl+`")
        else:
            pass
    else:
        pass
else:
    pass
while flag:
    with open("balance.txt","r") as file:
        b=int(file.read())
    print("1. Check balance.")
    print("2. Deposit money.")
    print("3. Withdraw money.")
    print("4. Change PIN.")
    print("5. Exit")
    c=int(input("Enter your choice: "))
    if c==1:
        print("Current balance is ₹",b)
    elif c==2:
        d=int(input("Deposit Amount(in ₹): "))
        print("Amount deposited!")
        b+=d
        with open("balance.txt","w") as file:
            file.write(str(b))
    elif c==3:
        w=int(input("Enter Withdrawal Amount(in ₹): "))
        if w<=b:
            print("Withdrawal Successfull!")
            b-=w
            with open("balance.txt","w") as file:
                file.write(str(b))
        elif w>b:
            print("Withdrawal Failed: Insufficient Balance")
    elif c==4:
        p=input("Enter your current pin: ")
        if p!=pin:
            p=input("Incorrect PIN! Try again: ")
            if p!=pin:
                p=input("Incorrect PIN! Try again: ")
                if p!=pin:
                    print("Incorrect PIN! Account is locked.")
                    flag=False
                    import keyboard
                    import time
                    time.sleep(0.5)
                    keyboard.send("Ctrl+`")
                else:
                    pass
            else:
                pass
        else:
            pass
        pin=input("Enter new pin: ")
        with open("pin.txt","w") as file:
            file.write(pin)
        print("PIN was changed successfully.")
    elif c==5:
        print("Exiting...")
        flag=False
        import keyboard
        import time
        time.sleep(0.5)
        keyboard.send("Ctrl+`")