'''
Implement Queue class, having following functions:
1. Enqueue: to insert an element, before insertion check queue is not full. 
2. Dequeue: to delete an element, before deletion, check queue should not be empty.
3. Display: to display elements of the list

'''
'''
Class Queue
Class methods:-
    __init__()     : constructor
    enQueue()      : to insert at the rear of the queue
    deQueue()      : to remove from the front of the queue
    displayQueue() : to display the queue

Class members:-
    size : fixed size of the queue , type: 'int'
    queue: our queue of size 'size' , type: 'list'
    front: pointer to removal end of the queue, type 'int'
    rear : pointer to insertion end of the queue, type 'int'


'''
class Queue:
    #Constructor
    def __init__(self,size):
        #Above defined members
        self.size = size
        #Initialising queue
        self.queue=["NONE"]*size
        self.front = -1
        self.rear = -1

    #Function to insert 'ele' at the rear of the queue    
    def enQueue(self,ele):
        #if queue isnt initialised
        if(self.rear==-1):
            #Initialising
            self.front=0
            self.rear=0
            #Adding ele to queue
            self.queue[self.rear]=ele
        
        #if queue is full    
        elif((self.rear==self.size-1 and self.front==0) or (self.rear == (self.front-1))):
            print("=>  Queue is full.")
            return

        #if rear crosses queue size then intialising again 
        elif(self.rear==self.size-1 and self.front!=0):
            self.rear=0
            self.queue[self.rear]=ele
        
        #normal insertion  
        else:
            self.rear+=1
            self.queue[self.rear]=ele
            
    #Function to remove element from front 
    def deQueue(self):
        #Queue empty condition
        if(self.front==-1):
            print("=>  Queue is Empty.")
            return
        #data to be removed
        data = self.queue[self.front]
        self.queue[self.front]="NONE"
        
        #if front and rear becomes equal 
        if(self.front == self.rear):
            self.front=-1
            self.rear=-1
        #if front reaches end of size of queue 
        elif(self.front == self.size-1):
            self.front=0
        #normal deletion
        else:
            self.front+=1
        #returning the removed data
        return data
    
    #Function to display queue 
    # From rear>=front then display from front -> rear
    # Else display from front -> size-1 and 0->rear
    def displayQueue(self):
        print("Queue is: ")
        #if queue is empty
        if(self.front == -1):
            print("=>  Queue is empty")
        #displaying queue
        elif(self.rear>=self.front):
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
            print('\n')
        else:
            for i in range(self.front,self.size):
                print(self.queue[i],end="")
            for i in range(0,self.rear+1):
                print(self.queue[i],end="")
            print('\n')

        
'''
Main function to perform trivial task of the program
Here menu driven function is provided
Enter
 1. Enqueue
 2. Dequeue
 3. Display
 Any other to exit:
'''

def main():
    #Input size of queue
    size = int(input("Enter the size of the queue: "))
    #Object of Queue class
    queue = Queue(size)
    while(True):
        print("------------------------")
        c = int(input("Enter\n 1. Enqueue\n 2. Dequeue\n 3. Display\n Any other to exit: "))
        
        if(c==1):
            #Element to insert
            ele = int(input("Enter element to enQueue: "))
            queue.enQueue(ele)
        elif(c==2):
            #Removed element details
            print("deQueue resulted in removal of: ",queue.deQueue())
        elif(c==3):
            #display queue
            queue.displayQueue()
        else:
            #Menu exit condition
            break
    

#making main() as driver function   
if __name__=="__main__":
    main()
