def check_speed():
    s=int(input("Enter your speed(in km/hr): "))
    if s<=70:
        print("OK")
    if s>70:
        d=0
        for i in range(71,s+1,5):
            d+=1
        if 5<d<11:
            print("Demerit Points:",d)
            print("WARNING!")
        elif d>10:
            print("Demerit Points:",d)
            print("Lisence Suspended!")
check_speed()