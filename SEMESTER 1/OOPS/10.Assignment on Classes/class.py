'''
Creating Computer Class 
With attributes : Color,Brand,Processor,RAM
'''
class Computer:

    #Class variable
    count=0
    #Constructor to initialise the attributes
    def __init__(self,Color,Brand,Processor,RAM):
        self.Color = Color
        self.Brand = Brand
        self.Processor = Processor
        self.RAM = RAM
        Computer.count+=1
    
    #Printing the attributes of class Computer
    def setter_color(self, Color):
        self.Color = Color
    def setter_brand(self, Brand):
        self.Brand = Brand 
    def setter_processor(self, Processor):
        self.Processor = Processor     
    def setter_ram(self, RAM):
        self.RAM = RAM

    def getter_color(self):
        return self.Color
    def getter_brand(self):
        return self.Brand
    def getter_processor(self):
        return self.Processor
    def getter_ram(self):
        return self.RAM  
    def printDetails(self):
        return [self.Color,self.Brand,self.Processor,self.RAM]

    def getter_count(self):
        return Computer.count

    def compareObj(x,y):
        if(x.Color==y.Color and x.Brand==y.Brand and x.Processor==y.Processor and x.RAM==y.RAM):
            return "SAME"
        else:
            return "NOT SAME"
    
'''
Main function to input data from user 
and calling the desired functions
'''
def main():
    #Inputting data from user
    Color=input("Enter color: ")
    Brand=input("Enter brand: ")
    Processor=input("Enter processor: ")
    RAM=input("Enter ram: ")
    #Creating object of the class Computer
    obj = Computer(Color,Brand,Processor,RAM)
    obj.setter_ram("12GB")
    print("After setting computer 1 ram: ",obj.getter_ram())
    

    obj1 = Computer("Black","HP","i7","12GB")
    print("Computer: Fetching count- ",obj.getter_count())
    
    #Compare
    print("Comparison Result: ",Computer.compareObj(obj,obj1))

    #Calling printDetails() member function
    print("Computer 1 Details are: ",obj.printDetails())
    print("Computer 2 Details are: ",obj1.printDetails())
    
#Making main() as driver function  
if __name__=='__main__':
    main()

