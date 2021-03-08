'''
Class 1:
Create a class employee with following attributes:
1. Name
2. EmpID
3. Designation: Worker/ Supervisor/Manager
4. Salary
5. Experience

Define all getter and setter methods + show method+__str__()

Calculate Salary according to Designation and experience
BaseSalary+AddSal+HRA

BaseSalary is
{10000, 15000, 20000} for Worker, Supervisor, Manager resp

AddSal=%age experience of BaseSalary

HRA=5% of BaseSalary


'''
'''
Class employee
Attributes -:
    name : name of the employee
    empId : emlpoyee id
    designation : worker/supervisor/manager
    experience : employee experience
    salary : employee salary

Member functions: 
    getter of all attributes
    setter of all attributes
    __str__ to return attributes details
    show() to print attributes details
'''
class employee():
    #constructor of class employee
    def __init__(self,name,empId,designation,experience):
        self.name = name
        self.empId = empId
        self.designation = designation
        self.experience = experience
        self.base = employee.baseSalary(self.designation)
        #Setting salary = base + additional salary + HRA
        self.salary = self.base + employee.addSalary(self.base,self.experience) + employee.hra(self.base)
        
    #Getter of all attributes
    def getter_name(self):
        return self.name
    def getter_empId(self):
        return self.empId
    def getter_designation(self):
        return self.designation
    def getter_salary(self):
        return self.salary
    def getter_experience(self):
        return self.experience

    #Setter of all attributes
    def setter_name(self,name):
        self.name = name
    def setter_empId(self,empId):
        self.empId = empId
    def setter_designation(self,designation):
        self.designation = designation
    def setter_salary(self,salary):
        self.salary = salary
    def setter_experience(self,experience):
        self.experience = experience

    #__str__ is to return the attributes details
    def __str__(self):
        return  'EmployeeClass( name={}, empId={}, designation={}, salary={}, experience={} )'.format(self.name,str(self.empId),self.designation,self.salary,self.experience)
    
    #To print all the attributes details
    def show(self): 
        print("Name : ",self.name)
        print("EmpId : ",self.empId)
        print("Designation : ",self.designation)
        print("Salary : ",self.salary)
        print("Experience : ",self.experience)
    
    #Base salary calculation according to the designation
    def baseSalary(designation):
        if designation == 'worker' :
            return 10000
        if designation == 'supervisor':
            return 15000
        if designation == 'manager':
            return 20000

    #Calculating additional salary
    def addSalary(base,experience):
        return experience*base/100
    #HRA calculation
    def hra(base):
        return 5*base/100
'''
Main function is the driver function
It creates the object of the class employee 
'''
def main():
    #Designations
    designationList=['worker','supervisor','manager']
    while(True):
        try:
            print("\n\n----Menu----")
            print("1.Create Object\n2.Call show()\n3.Call overriden __str__()\n")
            ch=int(input("INPUT: "))

            if ch==1:
                try:
                    #Creating object of class employee
                    name = input("Enter name: ")
                    empID = int(input("Enter empID: "))
                    designation = (input("Enter designation worker/supervisor/manager: ")).lower()
                    if designation not in designationList:
                        raise Exception("Not a valid designation.")
                    experience = int(input("Enter experience: "))
                    
                    employeeObj = employee(name,empID,designation,experience)
                    print("Object Created.")

                except Exception as e:
                    print(e)
                    print("Enter a valid input.")

            elif ch==2:
                #Calling show() to print attributes of the class
                l = locals()
                if 'employeeObj' in l:
                    employeeObj.show()
                else: 
                    print("Object doesn't exist.")
            elif ch==3:
                #Overriding __str__
                l = locals()
                if 'employeeObj' in l:
                    print(employeeObj)
                else: 
                    print("Object doesn't exist.")
        except:
            print("Enter only integer input.")

#Making main() as the driver function
if __name__ == '__main__':
    main()
      
