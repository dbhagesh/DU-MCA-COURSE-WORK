'''
Write a class named "Vector" having two components.
The class should have the following functions:
1. Add two vectors
2. Subtract two vectors
3. Multiply  two vectors (Dot product)
'''
'''
class Operations
Member function:
    addVectors- Function to add vectors
    subtractVectors- Function to subtract vectors
    dotVectors- Function to dot product of vectors

    Function return their output as a list.
'''
class Operations:
    #Member functions of the class

    #Input self1,self2 of object type
    #Returns the desired outputs as a list
    def addVectors(self1,self2):
        return [self1.x+self2.x,self1.y+self2.y]
    def subtractVectors(self1,self2):
        return [self1.x-self2.x,self1.y-self2.y]
    def dotVectors(self1,self2):
        return [self1.x*self2.x,self1.y*self2.y]
'''
class Vector Inherits class Operations
Constructor: 
    To intialise the vector in self
'''
class Vector(Operations):
    #Constructor
    def __init__(self,x,y):
        #Initialising the vectors
        self.x = x
        self.y = y
'''
Function to perform all the desired operations
Menu drivern program to call the desired operations from the class
Input: Nothing
Output: Prints the desired operation output
'''
def main():
    #Inputting the vector components from the user
    print("-----------")
    x1=int(input("Enter first vector x component:"))
    y1=int(input("Enter first vector y component:"))
    x2=int(input("Enter second vector x component:"))
    y2=int(input("Enter second vector y component:"))

    #Creating vector class to intialise the vectors
    v1=Vector(x1,y1) 
    v2=Vector(x2,y2)

    #Outputting the user inputted vector
    print("V1-> x component: ",v1.x)
    print("V1-> y component: ",v1.y)
    print("V2-> x component: ",v2.x)
    print("V2-> y component: ",v2.y)

    
    
    #Menu driven loop
    while(True):
        #Menu driven functionality
        choice = int(input("Enter '1':Add,'2':Subtract,'3':dot product or any other to exit."))
        #addVectors function
        if choice==1:
            print(Vector.addVectors(v1,v2))
        #subtractVectors function
        elif choice==2:
            print(Vector.subtractVectors(v1,v2))
        #dotVectors function
        elif choice==3:
            print(Vector.dotVectors(v1,v2))
        #Exiting the loop condition
        else:
            break

#Making main function as the driver function
if __name__=='__main__':
    main()