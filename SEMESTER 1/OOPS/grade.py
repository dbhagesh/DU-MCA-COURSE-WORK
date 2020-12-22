def main():
    marks=int(input("Enter marks for printing grade:"))
    gradeCalc(marks)
    
def gradeCalc(marks):
    if(marks>=90):
        print("A")
    if(marks>=80):
        print("A-")
    if(marks>=70):
        print("B")
    if(marks>=60):
        print("B-")
    if(marks>=50):
        print("C")
    if(marks>=40):
        print("C-")
    else:
        print("FAIL")

if (__name__=='__main__'):
    main()
