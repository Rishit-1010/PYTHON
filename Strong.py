a=int(input("Enter a number: "))
n=a
s=0
d=0
while n>0:
    d=n%10
    f=1
    for i in range(d,1,-1):
        f*=i
    s=s+f
    n=n//10
if a==s:
    print("Strong")
else:
    print("Not Strong")

#To print all strong numbers between 1 and 100000:
for a in range(1,100000):
    n=a
    s=0
    d=0
    while n>0:
        d=n%10
        f=1
        for i in range(d,1,-1):
            f*=i
        s=s+f
        n=n//10
    if a==s:
        print(s)