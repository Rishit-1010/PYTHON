n=int(input("Enter a number: "))
a=n
r=0
d=0
while (a>0):
    d=a%10
    r=(r*10)+d
    a //= 10
if n==r:
    print("Pallindrome")
else:
    print("Not Pallindrome")