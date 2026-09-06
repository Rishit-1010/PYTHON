def triangle2(a):
    for i in range(1,a+1):
        for j in range(i,0,-1):
            print(j%2,end="")
        print()
a=int(input("Enter no. of rows:"))
triangle2(a)
# def triangle2(a):
#     for i in range(1,a+1):
#         print((a-i)*" ", end="")
#         for j in range(i,0,-1):
#             print(j%2,end="")
#         print()
# a=int(input("Enter no. of rows:"))
# triangle2(a)
