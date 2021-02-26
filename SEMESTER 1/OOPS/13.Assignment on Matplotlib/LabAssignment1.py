'''
Given a list of data containing name of Students, marks in 5 subjects.

Ms. Goofy wants to analyse the data. 
Think and help Ms. Goofy

'''

#Importing libraries
import matplotlib.pyplot as plt
import numpy as np

'''
Function to plot bar graph on number of student failed and passed in particular subjects
Arguments: ns: number of students,mylabels: label for student,marks: marks of each student,name: name of each student
Output: Plot bar graph
'''
def passedAndfailed(ns,mylabels,marks,name):
  #Maintaing studenfailed and studentpassed in different subjects
  studentfailed=[0 for i in range(5)]
  studentpassed=[0 for i in range(5)]

  #numpy array
  arr = np.array(marks)
  #Transpose
  arr = arr.transpose()

  #Traversing of marks of each subject of each student
  for i in range(5):
    for j in range(ns):
      if(arr[i][j]<33):
        #Student failed 
        studentfailed[i]+=1
      else:
        #Student passed
        studentpassed[i]+=1

  print("NUMBER OF STUDENT FAILED IN PARTICULAR SUBJECT")
  #Plotting bar for student failed subject wise
  plt.bar(mylabels,studentfailed)
  #Title
  plt.title("NUMBER OF STUDENT FAILED IN A SUBJECT")
  plt.show()

  print("NUMBER OF STUDENT PASSED IN PARTICULAR SUBJECT")
  #Plotting bar for studentpassed
  plt.bar(mylabels,studentpassed)
  #Title
  plt.title("NUMBER OF STUDENT PASSED IN A SUBJECT")
  plt.show()

'''
Function to plot line graph to plot subject wise topper
Arguments: mylabels: label for student,marks: marks of each student,name: name of each student
Output: Plot plot line graph
'''
def subjectTopper(marks,name,mylabels):
  print("SUBJECT WISE TOPPER")
  #SubjectWiseTopper 
  subjectWiseTopper=[0 for i in range(5)]
  #numpy array
  arr = np.array(marks)
  #Transpose
  arr = arr.transpose()
  #Fetching subject topper
  for i in range(5):
    subjectWiseTopper[i]=name[arr[i].argmax()]

  #Plotting
  plt.plot(subjectWiseTopper,mylabels)
  plt.show()

'''
Function to subplot of each student marks of different subject
Arguments: ns: number of studentsmarks: marks of each student,name: name of each student
Output: Plot subplot of each student
'''
def subPlotStudent(ns,marks,name):
  print("Trend of marks from subject 1 to subject n ")
  #Different subject number
  subject=[1,2,3,4,5]
  #Traversing different students
  for i in range(ns):
    #Subplotting for all the students 
    plt.subplot(ns,1,i+1)
    plt.plot(subject,marks[i])
    #Title
    plt.title(name[i])
    
  #Superiro Title
  plt.suptitle("STUDENS")
  plt.show()

'''
Function plot piechart of each student for subject wise partition
Arguments: ns: number of students,marks: marks of each student,name: name of each student
Output: Plot pie chart of each student
'''
def studentAnalysis(ns,marks,name,mylabels):
  print("DIFFERENT STUDENT PIE CHART ANALYSIS")
  #Traversing each student to do subject wise partition of total marks
  for i in range(ns):
    #Student name 
    print(name[i]," analysis---")
    #Label
    
    
    #Plotting pie chart
    plt.pie(marks[i],labels=mylabels,shadow=True)
    plt.legend(title="SUBJECTS")
    plt.show()

'''
Function to plot bar graph each student total marks and percentage scored
Arguments: ns: number of students,marks: marks of each student,name: name of each student
Output: Plot bar graph 
'''
def totAndPer(ns,marks,name):
  print("ANALYSIS OF TOTAL MARKS AND PERCENTAGE ")
  #Percentage of each student
  per=[0 for i in range(ns)]
  #Total marks of each student
  tot=[0 for i in range(ns)]
  #Calculating total marks and percentage
  for i in range(ns):
    tot[i]=sum(marks[i])
    per[i]=sum(marks[i])/5

  #Plotting bar for total marks
  plt.bar(name,tot)
  plt.title("SUM OF MARKS")
  plt.show()

  #Plotting bar for percentage
  plt.bar(name,per)
  plt.title("PERCENTAGE")
  plt.show()


'''
Main function i.e driver function to perform all the trivial tasks of the program
Taking user inputs and calling required functions
'''
def main():
  #Number of students
  ns = int(input("Enter number of students: "))
  #List to store student name
  name=[]

  #2D list containing marks of each subject for every student
  marks=[[0 for i in range(5)] for j in range(ns)]

  #Inputting marks and name of each student
  for i in range(ns):
    #Name
    name.append(input("Enter name of student: "))
    #Marks
    for j in range(5):
      marks[i][j]=(int(input("Enter marks for {} subject {} ".format(i+1,j+1))))
  
  #Label for different subjects
  mylabels=['Subject1','Subject2','Subject3','Subject4','Subject5']
  
  '''
  Analysis sequence:
  1.TotalMark and percentage
  2.Each student marks analysis
  3.Subplotting marks of each student
  4.Subject wise topper
  5.Number of student failed and passed
  '''
  totAndPer(ns,marks,name)
  studentAnalysis(ns,marks,name,mylabels)
  subPlotStudent(ns,marks,name)
  subjectTopper(marks,name,mylabels)
  passedAndfailed(ns,mylabels,marks,name)

#Making main() as the driver function
if __name__=='__main__':
  main()