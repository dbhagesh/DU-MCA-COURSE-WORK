'''
Class student
Attributes:
rollnum- Roll Number 
name- Name of Student
marklist- Marks of student
Class- Class of student
grade- Grade obtained by student
percentage- Percentage obtained by the student

Member Functions:
Getter and setter of every attributes
getter of count: To count number of student objects
'''

class Student: 
    #Student var to count
    count=0

    #Constructor of Student Class
    def __init__(self,rollnum,name,marklist,Class,grade,percentage):
        self.rollnum = rollnum
        self.name = name
        self.marklist = marklist
        self.Class = Class
        self.grade = grade
        self.percentage = percentage
        Student.count+=1
    #Getter of every attribute
    def getter_rollnum(self):
        return self.rollnum
    def getter_name(self):
        return self.name
    def getter_marklist(self):
        return self.marklist
    def getter_Class(self):
        return self.Class
    def getter_grade(self):
        return self.grade
    def getter_percentage(self):
        return self.percentage
    
    #Getter of student count
    def getter_count(self):
        return Student.count

    #Setter of every Attribute
    def setter_rollnum(self,rollnum):
        self.rollnum = rollnum
    def setter_name(self,name):
        self.name = name
    def setter_marklist(self,marklist):
        self.marklist = marklist
    def setter_Class(self,Class):
        self.Class = Class 
    def setter_grade(self,grade):
        self.grade = grade
    def setter_percentage(self,percentage):
        self.percentage = percentage

    #Printing details of student
    def printDetails(self):
        print("Rollnum: ",self.rollnum)
        print("Name: ",self.name)
        print("Marklist: ",self.marklist)
        print("Class: ",self.Class)
        print("Grade: ",self.grade)
        print("Percentage: ",self.percentage)
      
'''
Main function to call take input from the user
And perform the desired and required functions and output
'''
def main():
    print("Enter student details->")
    #Student details
    rollnum = input("Enter rollnum: ")
    name = input("Enter name: ")
    #Number of subjects
    n = int(input("Enter number of subject: "))
    #Empty marklist
    marklist=[]
    print("Enter marks out of 100: ")
    #Inputting the marklist
    for i in range(n):
        marklist.append(int(input("Enter marks of subject :")))
    #Inputting the class
    Class = input("Enter Class: ")
    #Calculating the student percentage
    percentage = (sum(marklist)/n)

    #Calculating the grade according to the student percentage
    if percentage>90:
        grade="A+"
    elif percentage>75:
        grade="A"
    elif percentage>60:
        grade="B+"
    elif percentage>50:
        grade="B"
    elif percentage>40:
        grade="C"
    else:
        grade="FAIL"
    
    #Initialising the object
    obj = Student(rollnum, name, marklist, Class, grade, percentage)
    #Printing details of the student object
    obj.printDetails()

#Making main() as driver function
if __name__=='__main__':
    main()