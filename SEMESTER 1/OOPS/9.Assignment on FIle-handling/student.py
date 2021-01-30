'''
1. Create a file containing records of the students marks in each subject. 
2. Read the file created in step 1, generate the marksheets of individual student and save it in a file named <studentName_rollno>.
3. Also generate a file containing name of students scoring highest marks subject-wise. 


Ex:
I/P:

O/P:

'''
#Importing pickle library
import pickle
'''
Purpose: Function to create each marksheet and write data into it 
Inputs: String-> 'filename':name of the file of format <student_rollno>,'sname':name of student,
        Integer->'sroll':roll number of student,
        List->'marks':marks of student

Output: Write the data to the marksheet of each student
'''
def create_file_marksheet(filename,sname,sroll,smarks):
    #try expect for error handling
    try: 
        #Creating marksheet of student and opeining that 
        f = open(str(filename)+".txt","wt") 
        #Writing the given information into the file
        f.write("---UNIVERSITY OF STUDENTS---\n")
        f.write("---Student Marksheet--\n") 
        f.write("Name: ")
        f.write(sname)
        f.write("\n")
        f.write("Roll Number: ")
        f.write(str(sroll))
        f.write("\n")
        #Writing the marks
        for i in range(len(smarks)):
            f.write("Subject {} Marks are: ".format(i+1))
            f.write(str(smarks[i]))   
            f.write("\n") 
        #Closing the file
        #Closing the file
        f.close() 
    #When an error is encountered
    except: 
        print("Unable to write to create_file_marksheet")
'''
Purpose: Function to create binary file 'marks' and storing 'dictionary' into it  
Inputs: Strings->'name':name of file,'mode':mode of file opening
        Dictionary->'dictionary': dictionary containing student data
Output: Write the 'dictionary' to the file 'name'
'''
def create_file(name,mode,dictionary):
    #Try except to handle errors
    try: 
        #Opening the file in write in binary mode
        f = open(name, mode) 
        #Using pickle to dumb dictionary into the file
        pickle.dump(dictionary,f)
        #Closing the file
        f.close() 
    #If errors are encountered
    except: 
        print("Unable to write to create_file")
'''
Purpose: Function to create file for marksheet of each student 
        Filename of marksheets - <studentname_rollno>
Inputs: Strings->'name':name of file in filename format
Output: Creates the file of marksheet and calls the function 'create_file_marksheet'
        which will enter the records of each stundent
'''
def generate_marksheets(name):
    #student dictionary which contains the record of each student
    dictionary={}
    #try except to handle errors
    try: 
        #Opening the 'marks' file 
        f = open(name,"rb") 
        #Loading the dictionary from 'marks'
        dictionary=pickle.load(f) 
        #Closing the file
        f.close()
    #When an error is encountered
    except: 
        print("Unable to write to generate_marksheets")
    #For each student forming his/her marksheet
    for i in dictionary:
        #filename of format <name_rollno>
        filename=str(dictionary[i][0])+"_"+str(i)
        #Calling create_file_marsheet to create each marksheet
        create_file_marksheet(filename,dictionary[i][0],i,dictionary[i][1:])
'''
Purpose: Function to create text file 'highest_marks.txt' which contains 
Inputs: list->'hmarks': hmarks contains highest mark holder details
Output: write the highest mark details in the file.
'''   
def highest_marks(hmarks):
    #Exception handling
    try:
        #Creating the file and opening it in writing in text mode
        f=open("highest_marks.txt","wt")
        #Writing the details of highest marks hoolder
        f.write("---Highest marks in each subject---\n")
        #For traversing through each subject
        subject=0
        #Writing the details from hmarks
        #hmarks structure
        #[[max marks, roll number of student with highest marks, name of student scored maximum][..]..]
        for i in hmarks:
            f.write("Subject: ")
            f.write(str(subject+1))
            f.write("\n")
            f.write("Roll Number: ")
            f.write(str(i[1]))
            f.write("\n")
            f.write("Student Name : ")
            f.write(str(i[2]))
            f.write("\n")
            f.write("Highest Marks: ")
            f.write(str(i[0]))
            f.write("\n")
            f.write("---------------------\n")
            subject+=1
        #Closing the file
        f.close()
    #When exception occurs
    except:
        print("Unable to write to highest_marks")
    


'''
Main function is the driver function.
Makes the calls to the relevant functions
Takes the required inputs from the user
Input: Number of students: 'n', Number of subjects: 'sn'
Returs: Returns nothing, but write the desired outputs to the files
'''        
        

def main():
    #Inputting number of students 
    n=int(input("Enter number of students: "))
    #Inputting number of subjects
    sn=int(input("Enter number of subjects: "))
    #Structure of dictionary- To store student details
    #{Roll number:['Student name','Marks of subject 1','Marks of subject 2',...]...}
    dictionary={}
    #Storing data of students in the dictionary in the above format
    for i in range(0,n):
        #Name of the student
        sname=input("Enter the name of student with roll number {}: ".format(i+1))
        #List to store marks and name
        mlist=[]
        mlist.append(sname) 
        #Inputting marks of the subjects
        for j in range(0,sn):
            marks=int(input("Enter marks for subject {}: ".format(j+1)))
            mlist.append(marks)
        #Inputting the list of marks and name to the dictionary where key is the roll number 
        dictionary[i+1]=mlist
    #List to store marks of each student where rows are student traversed with roll number
    #and colums are the subjects
    # Structure of marks is
    # [[student1MarksOfSubject1,student2MarksOfSubject1...][student1MarksOfSubject2,student2MarksOfSubject2..]...]     
    marks = [[] for j in range(sn)]
    #Highest marks of each subject is stored here
    #Structure of hmarks list is
    #[[max marks, roll number of student with highest marks, name of student scored maximum][..]..]
    hmarks = [[] for j in range(sn)]
    #Traversing the dictionary
    for i in dictionary:
        #Subject reference
        subject=0
        #Traversing the marks of each student 
        for j in dictionary[i][1:]:
            #appending marks to the marks list
            marks[subject].append(j)
            subject+=1
    #Subject traversing variable
    subject=0
    #Structure of hmarks list is
    #[[max marks, roll number of student with highest marks, name of student scored maximum][..]..]
    for i in marks:
        #Appending max marks
        hmarks[subject].append(max(i))
        #Appending roll number of student
        hmarks[subject].append(i.index(max(i))+1)
        #Appending name of student
        hmarks[subject].append(dictionary[i.index(max(i))+1][0])
        subject=subject+1

    #Function to create binary file 'marks' and storing 'dictionary' into it        
    create_file("marks","wb",dictionary)
    #Function to create marksheet of each student
    generate_marksheets("marks")
    #Function to create file which contains highest marks of each subject
    highest_marks(hmarks)

    
#Making main function as the driver function
if __name__ == "__main__":
    main()