import math
def myRoot(a,b,c):
    if((b**2-4*a*c)>=0):
        print("Root1",(-b+(math.sqrt(b**2-4*a*c)))/(2*a))
        print("Root2",(-b-(math.sqrt(b**2-4*a*c)))/(2*a))
    else:
        print("Imaginary Roots")

myRoot(1,2,1)
myRoot(2,1,1)

