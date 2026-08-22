x=int(input("Enter a no.: "))
n=x
c=len(str(n))
s=0
d=0
while n>0:
    d=n%10
    s=s+(d**c)
    n//=10
if x==s:
    print("Armstrong")
else:
    print("Not Armstrong")

#To print all armstrong numbers between 1 and 100000:
for x in range(1,100000):
    n=x
    c=len(str(n))
    s=0
    d=0
    while n>0:
        d=n%10
        s=s+(d**c)
        n//=10
    if x==s:
        print(x)