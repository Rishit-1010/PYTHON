def sum_digits(a):
    s=0
    while a>0:
        d=a%10
        s=s+d
        a=a//10
    return s
def is_prime(a):
    flag=False
    i=2
    while(i<a):
        if a%i==0:
            flag=True
            break
        i+=1
    if flag:
        return False
    else:
        return True
def is_pallindrome(a):
    n=a
    rev=0
    while n>0:
        d=n%10
        rev=(rev*10)+d
        n//=10
    if rev==a:
        return True
    else: 
        return False
a=int(input("Enter a no.: "))
print("Sum of digits:",sum_digits(a))
print("Prime" * is_prime(a) or "Not Prime")
print("Pallindrome" * is_pallindrome(a) or "Not Pallindrome")