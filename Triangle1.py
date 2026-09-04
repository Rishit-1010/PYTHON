a=int(input("Enter no. of rows required:"))
for i in range(1,a+1):
    print((a-i)*" ", end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()