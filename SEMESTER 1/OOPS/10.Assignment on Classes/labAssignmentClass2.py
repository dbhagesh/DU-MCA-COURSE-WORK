'''
Class 2:
Define all getter and setter methods + __str__()

LAPTOP
Attributes:

Brand
Processor
RAM
Color


show()
'''
'''
Creating Laptop Class 
    With attributes : Color,Brand,Processor,RAM

    Member functions: 
        __init__ : constructor
        getter and setter of all attributes
        __str__ : return all attributes
        getter_count : count number of objects
        compareobj : compare object 
'''
class Laptop():

    #Class variable
    count=0
    #Constructor to initialise the attributes
    def __init__(self,Color,Brand,Processor,RAM):
        self.Color = Color
        self.Brand = Brand
        self.Processor = Processor
        self.RAM = RAM
        #Count of objects of the class
        Laptop.count+=1
    
    #Setter functions of the attributes of class Laptop
    def setter_color(self, Color):
        self.Color = Color
    def setter_brand(self, Brand):
        self.Brand = Brand 
    def setter_processor(self, Processor):
        self.Processor = Processor     
    def setter_ram(self, RAM):
        self.RAM = RAM

    #Getter functions of the attributes of the class Laptop
    def getter_color(self):
        return self.Color
    def getter_brand(self):
        return self.Brand
    def getter_processor(self):
        return self.Processor
    def getter_ram(self):
        return self.RAM 

    #__str__ function to return the attributes of the class 
    def __str__(self):
        return 'Laptop Class-> Color: {}, Brand: {}, Processor: {}, Ram: {} '.format(self.Color,self.Brand,self.Processor,self.RAM)
    #Getter function to get the count number of objects of the class
    def getter_count(self):
        return Laptop.count
    #Function to compare attributes of two objects, if attributes are equal then return "SAME" else "NOT SAME"
    def compareObj(x,y):
        #Comparing the attributes of the class
        if(x.Color==y.Color and x.Brand==y.Brand and x.Processor==y.Processor and x.RAM==y.RAM):
            return "SAME"
        else:
            return "NOT SAME"

    
'''
Main function to input data from user 
and calling the desired functions
'''
def main():
    '''
    #Inputting data from user
    Color=input("Enter color: ")
    Brand=input("Enter brand: ")
    Processor=input("Enter processor: ")
    RAM=input("Enter ram: ")
    #Creating object of the class Laptop
    obj = Laptop(Color,Brand,Processor,RAM)
    obj.setter_ram("12GB")
    print("After setting Laptop 1 ram: ",obj.getter_ram())
    
    #Creating another object
    obj1 = Laptop("Black","HP","i7","12GB")
    print("Laptop: Fetching count- ",obj.getter_count())
    
    #Comparing the objects
    print("Comparison Result: ",Laptop.compareObj(obj,obj1))

    #Calling printDetails() member function
    print("Laptop 1 Details are: ",obj.__str__())
    print("Laptop 2 Details are: ",obj1.__str__())
    '''

    while(True):
        print("\n\n---MENU---")
        print("1.Create objects\n2.show method\n3.Compare objects\n4.str method")
        try:
            ch=int(input("INPUT: "))

            if ch==1:
                print("Enter Object1: ")
                #Inputting data from user
                Color=input("Enter color: ")
                Brand=input("Enter brand: ")
                Processor=input("Enter processor: ")
                RAM=input("Enter ram: ")
                #Creating object of the class Laptop
                obj1 = Laptop(Color,Brand,Processor,RAM)
            elif ch==2:

            elif ch==3:

            elif ch==4:

            else:
                print("Exiting program...")
                break
        except:
            print("Enter a valid input.")
#Making main() as driver function  
if __name__=='__main__':
    main()

