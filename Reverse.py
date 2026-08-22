a=int(input("Enter a number: "))
r=0
n=0
while (a>0):
    n=a%10
    r=(r*10)+n
    a //= 10
print("Reverse is",r)