print("---------------------Collatz Challenge---------------------")
a=int(input("Enter a number: "))
print("Sequence starts at:",a)
b=[]
while a>1:
    if a%2==0:
        a/=2
        b.append(a)
    elif a%2!=0:
        a=(a*3)+1
        b.append(a)
c=len(b)
d=max(b)
print("Sequence:",b)
print("Total Steps:",c)
print("Largest no. reached:",d)