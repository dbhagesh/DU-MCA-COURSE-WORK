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
        if designation == 'Worker':
            return 10000
        if designation == 'Supervisor':
            return 15000
        if designation == 'Manager':
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
    #Creating object of class employee
    employeeObj = employee('bhagesh',10,'Worker',10)
    #Calling show() to print attributes of the class
    employeeObj.show()

#Making main() as the driver function
if __name__ == '__main__':
    main()
      
