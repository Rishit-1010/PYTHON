def floyd(a):
    k=1
    for i in range(1,a+1):
        for j in range(1,i+1):
            print(k, end=" ")
            k+=1
        print()
a=int(input("Enter no. of rows: "))
floyd(a)