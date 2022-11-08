a=float(input("nhập a= "))
b=float(input("nhập b= "))
c=float(input("nhập c= "))
if a == 0:
    if b == 0:
        if c == 0: 
            print("phtr vô số nghiệm")
        else: 
                print("phtr vo nghiệm")
    else:
        if c == 0: 
                    print("phtr có 1 nghiệm x=0")
        else: 
                        print("phtr có 1 nghiệm x=", -c/b)
else: 
    delta = b**2 - 4*a*c
    if delta < 0:
        print("phtr vo nghiệm ")
    elif  delta == 0: 
        print(" phtr có 1 nghiệm", -b/(2*a) )
    else:
            print("phtr có 2 nghiệm phân biệt")
            print("x1=", float((-b-(delta)/(2*a))))
            print("x2=",float((-b+(delta)/(2*a))))