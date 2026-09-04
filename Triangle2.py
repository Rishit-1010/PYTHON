def triangle2(a):
    for i in range(1,a+1):
        for j in range(i,0,-1):
            if j%2==0:
                print(0,end="")
            else:
                print(1,end="")
        print()            
a=int(input("Enter no. of rows:"))    
triangle2(a)            