def calculate_bill():
    u=int(input("Enter units consumed: "))
    if u<101:
        c=u*4
    elif 100<u<201:
        u-=100
        c=400+(u*6)
    elif u>200:
        u-=200
        c=1000+(u*8)
    c+=100
    if c>2000:
        c=c*(1+(5/100))
    print("Final Bill is ₹",c)
calculate_bill()