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
    per - percentage obtained by student

'''
class Student:
    #Constructor
    def __init__(self,name,rollno,tmarks,per):
        #Initialising
        self.name = name
        self.rollno = rollno
        self.tmarks = tmarks
        self.per = per

    #Overriding __str__ to return the student data
    def __str__(self):
        return "(NAME: {},ROLLNO: {},TMARKS: {},PER: {} )".format(self.name,self.rollno,self.tmarks,self.per)
'''
Class Stack - 
Methods : 
    push() - push element to the stack top
    pop() - pop the topmost element from the stack
    peek() - peek the topmost element of the stack
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
    peek()
    To return the topmost element
    Arguments: self
    Returns : topmost element on the stack
    '''
    def peek(self):
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
    #size of the stack 
    size=0
    while(size<=0):
        print("Enter size greater than 0")
        size = int(input("Enter the stack size: "))
    
    #Exception handling
    try:
        #Number of subjects
        subj = int(input("Enter number of subjects: "))
        #Maximum marks
        MM = int(input("Enter maximum marks for each subjects: "))
    
    

        #Creating object of Stack class 
        #Passing 'size' of the stack as input to intialise the stack in the class
        obj= Stack(size)

        #Menu
        '''
        1.Insert
        2.Pop
        3.peek
        4.Length

        '''
        print("---MENU---")
        print("\n1.Insert\n2.Pop\n3.peek\n4.Length\n")
        #Menu Driven functionality
        while(True):
            #Choice
            try:
                ch = int(input("Enter choice: "))
                if(ch==1):
                    name = input("Enter name: ")
                    rollno = int(input("Enter roll no: "))
                    tmarks = int(input("Enter total marks: "))
                    per = (tmarks/(subj*MM))*100
                    student1=Student(name,rollno,tmarks,per)
                    print("Pushed ",obj.push(student1))

                elif(ch==2):
                    print("Popped: ",obj.pop())
                elif(ch==3):
                    print("peek ele is : ",obj.peek())
                elif(ch==4):
                    print("Number of Elements in the stack",len(obj))
                else:
                    print("Exiting Program...")
                    break
            except:
                print("Enter a valid input.")
    except:
        print("Enter valid value.")


#Making main() as driver function 
if __name__=='__main__':
    main()
