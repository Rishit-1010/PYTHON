def rectangle(a):
    for i in range(0,a+1):
        if i%a==0:
                print((a+1)*"* ")
        else:        
                for j in range(0,a+1):
                    print("* "*(j%a==0) or "  ", end="")
                print()
a=int(input("Enter Size of Box: "))
rectangle(a)