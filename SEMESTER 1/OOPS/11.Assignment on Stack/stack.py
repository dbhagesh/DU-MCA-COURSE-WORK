'''
Create a class Stack, to hold records of Student class, having following methods:
1. To push an element on the top of the stack
2. Pop element and display the popped element
3. Peek the top element of the stack 
4. Total elements in the stack

Note: 
1. Push is possible only when stack is not full
2. Pop operation can be performed when stack is not empty

Input:- Please specify the stack size in the object call
Output:- Class operation outputs defined below
'''


'''
class Student to hold record of the student
Methods: 
    contructor- to initiliase the object
    __str__-to return the data of the object
Instance:
    name-name of the students
    rollno- roll no of the student
    tmarks - total marks of the students

'''
class Student:
    #Constructor
    def __init__(self,name,rollno,tmarks):
        #Initialising
        self.name = name
        self.rollno = rollno
        self.tmarks = tmarks
    #Overriding __str__ to return the student data
    def __str__(self):
        return "{},{},{}".format(self.name,self.rollno,self.tmarks)
'''
Class Stack - 
Methods : 
    push() - push element to the stack top
    pop() - pop the topmost element from the stack
    front() - peek the topmost element of the stack
    __len__() - overriden len method to find total elements in the stack

Instance variables
    myStack - type 'list': to store the stack
    size - type 'int': size of the stack 
'''
class Stack:
    #Constructor
    def __init__(self,size):
        #Storing Stack
        self.myStack = []
        #Size of the stack
        self.size = size

    '''
    push()
    To push element on top of stack taking care of overflow condition
    Arguments: self, integer type 'ele'
    '''
    def push(self,ele):
        if(len(self.myStack)==self.size):
            print("Overflow Occured")
            return
        self.myStack.append(ele)
        return "Successful"
        
    
    '''
    pop()
    To pop element from top of stack taking care of stack empty condition
    Arguments: self
    Return: returns the topmost element which is popped up
    '''
    def pop(self):
        if(len(self.myStack)==0):
            return "Stack Empty"
        pele = self.myStack[-1]
        self.myStack = self.myStack[:len(self.myStack)-1]
        return pele

    '''
    front()
    To return the topmost element
    Arguments: self
    Returns : topmost element on the stack
    '''
    def front(self):
        if(len(self.myStack)==0):
            return "Stack Empty, nothing on top"
        return self.myStack[-1]
    '''
    __len__()
    Overriding len() for objects, it returns the stack size
    Arguments: self
    Returns: number of elements in the stack
    '''
    def __len__(self):
        return len(self.myStack)
        
'''
main() is the driver function here, it calls the required functions and
make the desired input outputs according to the need.

Here class object is created and relevent methods are called

'''
def main():
    size = int(input("Enter the stack size: "))
    #Creating object of Stack class 
    #Passing 'size' of the stack as input to intialise the stack in the class
    obj= Stack(size)
    student1 = Student("BHAGESH",1,50)
    student2 = Student("ANKIT",2,40)
    #Pushing to the stack
    print("Pushed ",obj.push(student1))
    print("Front ele is : ",obj.front())
    #Popping fron the stack
    print("Popped: ",obj.pop())
    print("Popped: ",obj.pop())

    #Again push
    print("Pushed ",obj.push(student2))

    print("Popped: ",obj.pop())

    #Front()
    print("Front ele is : ",obj.front())

    #Overriden len() 
    print("Pushed ",obj.push(student1))
    print("Pushed ",obj.push(student2))
    print("Number of Elements in the stack",len(obj))
    
#Making main() as driver function 
if __name__=='__main__':
    main()
