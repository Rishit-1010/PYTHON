n=int(input("Enter a number: "))
if n==2:
    print("Prime")
else:
    for i in range(1,n+1):
        if 1<i<n:
            if n%i!=0:
                a="Prime"
            elif n%i==0:
                a="Not Prime"
                break
    print(a)