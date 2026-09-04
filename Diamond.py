def print_diamond_nested(a):
    for i in range(1, a + 1):
        print((a-i)*" ",end="")
        print((2*i-1)*"*",end="")
        print()
    for i in range(a - 1, 0, -1):
        print((a-i)*" ",end="")
        print((2*i-1)*"*",end="")
        print()
a=int(input("Enter size:"))
print_diamond_nested(a)