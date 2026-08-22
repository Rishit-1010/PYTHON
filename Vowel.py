a=str(input("Enter a word/s: "))
b=[]
for i in a:
    if i=="a" or i=="A":
        b.append("a")
    elif i=="e" or i=="E":
        b.append("b")
    elif i=="i" or i=="I":
        b.append("i")
    elif i=="o" or i=="O":
        b.append("o")
    elif i=="u" or i=="U":
        b.append("u")
c=len(b)
print("No. of vowels in the word/s are",c)