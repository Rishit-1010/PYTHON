def check_speed():
    s=int(input("Enter your speed(in km/hr): "))
    if s<=70:
        print("OK")
    if s>70:
        d=0
        for i in range(71,s+1,5):
            d+=1
        if d>5:
            print("WARNING!")
        if d>10:
            print("Lisence Suspended!!")
    print("Demerit Points: ",d)
check_speed()
