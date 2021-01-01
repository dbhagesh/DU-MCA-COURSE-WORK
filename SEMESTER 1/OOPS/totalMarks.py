'''
Function to input marks of both subject of each student and then printing the total marks of each student

I/P:
Enter Total Number of students:3
Enter Marks for 1st subject
Enter marks for student 1:1
Enter marks for student 2:2
Enter marks for student 3:3
Enter Marks for 2nd subject
Enter marks for student 1:4
Enter marks for student 2:5
Enter marks for student 3:6

O/P:
[5, 7, 9]
'''

#Function to take input marks of students in list ‘marksList’ with total strength ‘numStudent’
def inputMarks(numStudent):
    marksList=list() 
    for i in range(numStudent):
        m1=int(input("Enter marks for student "+str(i+1)+":"))
        #Input is taken as string so converting the input as int
        #STATEMENT 1
        #Appending the inputted element in the list
        #Filling the list respected postions with m1
        marksList.append(m1)  
    return marksList


#Function to validate the input marks i.e. marks should be between 0 to 100.
#returns TRUE if list of marks is valid otherwise returns FALSE
def validateMarks(marks):
    # Traverse each element 
    for i in marks:
        #STATEMENT 2
        #Checking if the marks are out of bound
        if i>100 or i<0:
            return False
        return True


#Main Script
TotalMarks=[]
numStudents=int(input("Enter Total Number of students:"))
print("Enter Marks for 1st subject")
marks1=inputMarks(numStudents)
print("Enter Marks for 2nd subject")
marks2=inputMarks(numStudents)
#STATEMENT 3
#Validating both subject marks if they are invalid then execute if statement
if not(validateMarks(marks1) and validateMarks(marks2)): 
	print("Invalid Marks")
else: 
    #STATEMENT 4
    #Traversing the list till numStudents
    for i in range(numStudents):
        #STATEMENT 5
        #Adding the marks of both subject of each student and then appending in total marks
        TotalMarks.append(marks1[i]+marks2[i])
print(TotalMarks)