import math    #We will be using the math module for logarthimic functions
ch=1   
while ch!=0:
    print('(1)Power Function')           # A while loop whihc displays all the
    print('(2) Logarathimic Function')   # options you can chose from
    print('(0)Exit Menu')
    ch=int(input("Enter choice (1/2/0)"))
    if ch==1:
        base=float(input("Enter Base"))
        exponent=float(input("Enter exponent"))
        print("Power of the Number=",base**exponent)
    elif ch==2:
        base=''
        argument=float(input("Enter the Argument"))
        base=input("Enter the base(Leave it blank to take the base as e)")
        if len(base)==0:
            print("Log of",argument,"to the base e is",math.log(argument))
        else:
            print("Log of",argument,"to the base",base,"is",math.log(argument,int(base)))
