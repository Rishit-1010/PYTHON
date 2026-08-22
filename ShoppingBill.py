def shopping_bill():
    a=int(input("Enter the shopping amount: "))
    if a>=5000:
        bill=a*(1-(20/100))
    elif 3000<=a<=4999:
        bill=a*(1-(15/100))
    elif 1500<=a<=2999:
        bill=a*(1-(10/100))
    elif a<1500:
        bill=a
    if bill>=3000:
        de=0
    elif bill<3000:
        de=100
    f=bill+de
    print("Discount: ₹",a-bill)
    print("Delivery Charge: ₹",de)
    print("Final Amount: ₹",f)
shopping_bill()