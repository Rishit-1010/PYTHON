# a=int(input("Enter the no. of rows required: "))
# s=int(input("Enter the no. you want to print: "))
# for i in range(1,a+1):
#     x=str(s)
#     print(i*x)
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
