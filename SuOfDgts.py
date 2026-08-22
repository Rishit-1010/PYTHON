n=int(input("Enter a no.: "))
a=n
s=0
d=0
while a>0:
    d=a%10
    s=s+d
    a=a//10
print("Sum of all digits is",s)
#Sum of even digits:
d2=0
s2=0
while n>0:
    d2=n%10
    if d2%2==0:
        s2=s2+d2
    n=n//10
print("Sum of even digits is",s2)
print("Sum of odd digits is",s-s2)