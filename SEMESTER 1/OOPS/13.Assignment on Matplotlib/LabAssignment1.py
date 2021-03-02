'''
Given a list of data containing name of Students, marks in 5 subjects.

Ms. Goofy wants to analyse the data. 
Think and help Ms. Goofy

'''

#Importing libraries
import matplotlib.pyplot as plt
import numpy as np

'''
Class Analysis
Members:
    ns - number of students
    name - name of students
    marks - marks of each student 
    arr - numpy array of marks
    MM - maximum marks
    passMarks - passing marks
  Member functions:
    passedAndfailed - number of student passed and failed
    subjectTopper - topper of each subject
    subPlotStudent - trend of marks of each student
    studentAnalysis - marks analysis of each student and highest marks indicator
    totAndPer - total and percentage of each student marks
'''

class Analysis:
  
  '''
  Constructor of class Analysis
  '''
  def __init__(self,ns,mylabels,marks,name,MM):
    self.ns = ns
    self.mylabels = mylabels
    self.name = name
    self.marks = marks
    self.arr = np.array(marks)
    self.MM = MM
    self.passMarks = 0.333 * MM
  '''
  Function to plot bar graph on number of student failed and passed in particular subjects
  Arguments: ns: number of students,mylabels: label for student,marks: marks of each student,name: name of each student
  Output: Plot bar graph
  '''

  def passedAndfailed(self):
    #Maintaing studenfailed and studentpassed in different subjects
    studentfailed=[0 for i in range(5)]
    studentpassed=[0 for i in range(5)]

    #Transpose
    arr = self.arr.transpose()
    #Traversing of marks of each subject of each student
    
    for i in range(5):
      y=(arr[i]<self.passMarks)
      studentfailed[i]=len(arr[i][y])
      studentpassed[i]=self.ns-len(arr[i][y])
    
    print("NUMBER OF STUDENT FAILED IN PARTICULAR SUBJECT")
    #Plotting bar for student failed subject wise
    plt.bar(self.mylabels,studentfailed,color=['black', 'red', 'green', 'blue', 'cyan'])
    #Title
    plt.title("NUMBER OF STUDENT FAILED IN A SUBJECT")
    plt.show()

    print("NUMBER OF STUDENT PASSED IN PARTICULAR SUBJECT")
    #Plotting bar for studentpassed
    plt.bar(self.mylabels,studentpassed,color=['black', 'red', 'green', 'blue', 'cyan'])
    #Title
    plt.title("NUMBER OF STUDENT PASSED IN A SUBJECT")
    plt.show()

  '''
  Function to plot line graph to plot subject wise topper
  Arguments: mylabels: label for student,marks: marks of each student,name: name of each student
  Output: Plot scatter point graph
  '''
  def subjectTopper(self):
    print("SUBJECT WISE TOPPER")
    print("Each point indicates the name of topper of the subject.")
    #SubjectWiseTopper 
    subjectWiseTopper=[0 for i in range(5)]
    
    #Transpose
    arr = self.arr.transpose()
    #Fetching subject topper
    for i in range(5):
      subjectWiseTopper[i]=self.name[arr[i].argmax()]

    #Plotting
    plt.scatter(subjectWiseTopper,self.mylabels)
    plt.title("SUBJECTWISE TOPPER")
    plt.show()

  '''
  Function to subplot of each student marks of different subject
  Arguments: ns: number of studentsmarks: marks of each student,name: name of each student
  Output: Plot subplot of each student
  '''
  def subPlotStudent(self):
    print("Trend of marks from subject 1 to subject n ")
    
    #Traversing different students
    for i in range(self.ns):
      #Subplotting for all the students 
      plt.subplot(self.ns,1,i+1)
      plt.plot(self.mylabels,self.marks[i],marker='o')
      #Title
      plt.title(self.name[i])
      
    #Super Title
    plt.suptitle("TREND OF MARKS OF EACH STUDENT")
    plt.show()

  '''
  Function plot piechart of each student for subject wise partition
  Arguments: ns: number of students,marks: marks of each student,name: name of each student
  Output: Plot pie chart of each student
  '''
  def studentAnalysis(self):
    print("DIFFERENT STUDENT PIE CHART ANALYSIS")
    #Traversing each student to do subject wise partition of total marks
    for i in range(self.ns):
      #Plotting pie chart
      explode = [0.02,0.02,0.02,0.02,0.02]
      #Highlighting highest marks subject
      explode[self.marks[i].index(max(self.marks[i]))]=0.09
      plt.pie(self.marks[i],explode=explode,labels=self.mylabels,shadow=True,autopct='%1.1f%%')
      plt.title("STUDENT : {}".format(self.name[i]))
      plt.legend(title="SUBJECTS")
      plt.show()

  '''
  Function to plot bar graph each student total marks and percentage scored
  Arguments: ns: number of students,marks: marks of each student,name: name of each student
  Output: Plot bar graph 
  '''
  def totAndPer(self):
    print("ANALYSIS OF TOTAL MARKS AND PERCENTAGE ")
    #Percentage of each student
    per=[0 for i in range(self.ns)]
    #Total marks of each student
    tot=[0 for i in range(self.ns)]
    #Calculating total marks and percentage
    tot = np.sum(self.arr,axis=1)
    per = (np.sum(self.arr,axis=1))*100/(5*self.MM)

    #Plotting bar for total marks
    plt.bar(self.name,tot,color=(0.2, 0.4, 0.6, 0.6))
    plt.title("SUM OF MARKS")
    plt.show()

    #Plotting bar for percentage
    plt.bar(self.name,per,color=(0.2, 0.4, 0.6, 0.6))
    plt.title("PERCENTAGE")
    plt.show()


'''
Main function i.e driver function to perform all the trivial tasks of the program
Taking user inputs and calling required functions
'''
def main():
  #Number of students
  ns = int(input("Enter number of students: "))
  MM = int(input("Enter maximum marks."))
  #List to store student name
  name=[]
  #Label for different subjects
  mylabels=['OOPS','MTCS','TC','CSA','DM']
  #2D list containing marks of each subject for every student
  marks=[[0 for i in range(5)] for j in range(ns)]

  #Inputting marks and name of each student
  for i in range(ns):
    #Name
    name.append(input("Enter name of student: "))
    #Marks
    for j in range(5):
      try:
        marks[i][j]=(int(input("Enter marks for {} subject {} ".format(i+1,mylabels[j]))))
        if marks[i][j]<0:
          raise Exception("Sorry, no numbers below zero.")
        if marks[i][j]>MM:
          raise Exception("Sorry, enter marks in valid range.")
      except Exception as e:
        print(e)
        
        

  obj = Analysis(ns,mylabels,marks,name,MM)
  '''
  Analysis sequence:
  1.TotalMark and percentage
  2.Each student marks analysis
  3.Subplotting marks of each student
  4.Subject wise topper
  5.Number of student failed and passed
  '''
  while(True):
    print("\n\n----MENU----")
    print("1.TotalMark and percentage\n2.Each student marks analysis\n3.Subplotting marks of each student\n4.Subject wise topper\n5.Number of student failed and passed\n")
    print("Anything else to exit\n")
    ch = int(input("Enter the choice: "))

    if(ch==1):
      obj.totAndPer()
    elif(ch==2):
      obj.studentAnalysis()
    elif(ch==3):
      obj.subPlotStudent()
    elif(ch==4):
      obj.subjectTopper()
    elif(ch==5):
      obj.passedAndfailed()
    else:
      print("Exiting program....")
      break
  
#Making main() as the driver function
if __name__=='__main__':
  main()