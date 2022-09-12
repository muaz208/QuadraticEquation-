import math
def quadratic():

    try:

        a=int(input("Please enter the a value: "))
        b=int(input("Please enter the a value: "))
        c=int(input("Please enter the a value: "))
    except:
        print("Not a valid entry, please try again")
        quadratic()
        return None

    discrim=(b*b)-(4*a*c)

    if(discrim>0):
        x1=((-1*b)+math.sqrt(discrim))//(2*a)
        x2=((-1*b)-math.sqrt(discrim))//(2*a)
        print("\nThe two roots are x1=", x1, "and x2=",x2)
        return x1,x2

    elif(discrim==0)://only one root
        x=(-1*b)//(2*a);
        print("The only root is x=",x)
        return x

    elif(discrim<0)://discriminent is less than 0 meaning complex roots
        print("There are no real roots!")
        return None

quadratic()
