'''
This program take a integer inputs 'n', a string 'inp' to print the desired figure
'n':  any number
'inp': 'a' to 'n' character
e.g:
I/P:
Enter number of rows: 5
Figures from 'a'-'n' are available
Enter the figure to print: a
O/P:
--------------------------
1
1  2
1  2  3
1  2  3  4
1  2  3  4  5

--------------------------
'''

'''
Driver function 
It contains a menu driver code to print any figure from 'a' - 'n'
Purpose: to print the desired figure
Parameter: none
'''

def main():
    n=int(input("Enter number of rows: "))
    print("Figures from 'a'-'n' are available")
    inp=input("Enter the figure to print: ")
    #Menu Driven
    while True:
        if inp=='a': 
            print("\n--------------------------")
            patterna(n)
            print("\n--------------------------")
            break
        if inp=='b': 
            print("\n--------------------------")
            patternb(n)
            print("\n--------------------------")
            break
        if inp=='c': 
            print("\n--------------------------")
            patternc(n)
            print("\n--------------------------")
            break
        if inp=='d': 
            print("\n--------------------------")
            patternd(n)
            print("\n--------------------------")
            break        
        if inp=='e': 
            print("\n--------------------------")
            patterne(n)
            print("\n--------------------------")
            break
        if inp=='f': 
            print("\n--------------------------")
            patternf(n)
            print("\n--------------------------")
            break
        if inp=='g': 
            print("\n--------------------------")
            patterng(n)
            print("\n--------------------------")
            break
        if inp=='h': 
            print("\n--------------------------")
            patternh(n)
            print("\n--------------------------")
            break
        if inp=='i': 
            print("\n--------------------------")
            patterni(n)
            print("\n--------------------------")
            break
        if inp=='j': 
            print("\n--------------------------")
            patternj(n)
            print("\n--------------------------")
            break
        if inp=='k': 
            print("\n--------------------------")
            patternk(n)
            print("\n--------------------------")
            break
        if inp=='l': 
            print("\n--------------------------")
            patternl(n)
            print("\n--------------------------")
            break
        if inp=='m': 
            print("\n--------------------------")
            patternm(n)
            print("\n--------------------------")
            break
        if inp=='n': 
            print("\n--------------------------")
            patternn(n)
            print("\n--------------------------")
            break
        else:
            print("Enter input from a-n only.")
            break
    
'''
Purpose: Function to print Fig a)
Parameter: Inputted integer 'n'
Return: Nothing, but prints the given figure

1
1  2
1  2  3
1  2  3  4
1  2  3  4  5

'''
def patterna(n):
    for i in range(1,n+1):
        for j in range(0,i):
            print(j+1," ",end="")
        print("")


'''
Purpose: Function to print Fig b)
Parameter: Inputted integer 'n'
Return: Nothing, but prints the given figure

      1
    1 2 1
  1 2 3 1 2
1 2 3 4 1 2 3

'''
def patternb(n):
    for i in range(1,n+1):
        if(i==n):
            print((int(n-i-1/2))*"  ",end="")
        else:
            print((int(n-i-1/2)+1)*"  ",end="")
        for j in range(0,int((2*i-1)/2)):
            print(j+1 ,end=" ")
        for j in range(0,int((2*i-1)/2)-1):
            print(j+1 ,end=" ")
        print((int(n-i-2/2)+1)*"  ")

'''
Purpose: Function to print Fig c)
Parameter: Inputted integer 'n'
Return: Nothing, but prints the given figure

5  4  3  2  1
4  3  2  1
3  2  1
2  1
1

'''
def patternc(n):
    for i in range(1,n+1):
        for j in range(n+1-i,0,-1):
            print(j," ",end="")
        print("")

'''
Purpose: Function to print Fig d)
Parameter: Inputted integer 'n'
Return: Nothing, but prints the given figure

1
2  2
3  3  3
4  4  4  4
5  5  5  5  5

'''
def patternd(n):
    for i in range(1,n+1):
        for j in range(0,i):
            print(i," ",end="")
        print("")

'''
Purpose: Function to print Fig e)
Parameter: Inputted integer 'n'
Return: Nothing, but prints the given figure

1  2  3  4  5
   2  3  4  5
      3  4  5
         4  5
            5

'''
def patterne(n):
    for i in range(1,n+1):
        print((i-1)*"   ",end="")
        for j in range(0+i,n+1):
            
            print(j," ",end="")
        print("")

'''
Purpose: Function to print Fig f)
Parameter: Inputted integer 'n'
Return: Nothing, but prints the given figure

* * * * *
*       *
*       *
*       *
* * * * *

'''
def patternf(n):
    for i in range(0,n):
        for j in range(0,n):
            if(i==0)and(j==0):
                print("*",end=" ")
            elif(i==n-1)and(j==n-1):
                print("* ",end=" ")
            elif(i==0):
                print("* ",end="")
            elif(j==0):
                print("* ",end="")
            elif(i==n-1):
                print("* ",end="")
            elif(j==n-1):
                print((n)*" ","*",end="")
        print("")
        
'''
Purpose: Function to print Fig g)
Parameter: Inputted integer 'n'
Return: Nothing, but prints the given figure

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

'''
def patterng(n):
    for i in range(0,n):
        for j in range(0,n):
            print("* ",end="")
        print("")

'''
Purpose: Function to print Fig h)
Parameter: Inputted integer 'n'
Return: Nothing, but prints the given figure

     *
    * * *
  * * * * *
* * * * * * *

'''
def patternh(n):    
    for i in range(1,n+1):
        if(i==n):
            print((int(n-i-1/2))*"  ",end="")
        else:
            print((int(n-i-1/2)+1)*"  ",end="")
        for j in range(0,int((2*i-1)/2)):
            print("* ",end="")
        for j in range(0,int((2*i-1)/2)-1):
            print("* ",end="")
        print((int(n-i-2/2)+1)*"  ")

'''
Purpose: Function to print Fig i)
Parameter: Inputted integer 'n'
Return: Nothing, but prints the given figure

* * * * * * *
  *       *
    *   *
      *

'''
def patterni(n):
    for i in range(1,n+1):
        if(i==n):
            print((int(n-i-1/2))*"  ",end="")
        else:
            print((i-1)*"  ",end="")
        for j in range(1,n+1-i):
            if(i==1)or(j==1):
                print("* ",end="")
            else:
                print("  ",end="")

        for j in range(1,n-i):
            if(i==1)or(j==n-1-i):
                print("* ",end="")
            else:
                print("  ",end="")
        print((i-1)*"  ")


'''
Purpose: Function to print Fig j)
Parameter: Inputted integer 'n'
Return: Nothing, but prints the given figure

* * * * * * *
  * * * * *
    * * *
      *

'''
def patternj(n):
    for i in range(1,n+1):
        if(i==n):
            print((int(n-i-1/2))*"  ",end="")
        else:
            print((i-1)*"  ",end="")
        for j in range(1,n+1-i):
            print("* ",end="")
        for j in range(1,n-i):
            print("* ",end="")
        print((i-1)*"  ")

'''
Purpose: Function to print Fig k)
Parameter: Inputted integer 'n'
Return: Nothing, but prints the given figure

    *
  * * *
* * * * *
  * * *
    *

'''
def patternk(n):
    for i in range(0,int(n/2)+1):
        print("  "*(int(n/2)-i),end="")
        for j in range(0,i+1):
            print("* ",end="")
        for j in range(0,i):
            print("* ",end="")
        print("  "*(int(n/2)-i))
    for i in range(0,int(n/2)):
        print("  "*(i+1),end="")
        for j in range(0,(int(n/2)-i)):
            print("* ",end="")
        for j in range(0,(int(n/2)-i-1)):
            print("* ",end="")
        print("  "*(i+1))


'''
Purpose: Function to print Fig l)
Parameter: Inputted integer 'n'
Return: Nothing, but prints the given figure

    *
  *   *
*       *
  *   *
    *

'''
def patternl(n):
    #Upper fig
    for i in range(0,int(n/2)+1):
        print("  "*(int(n/2)-i),end="")
        for j in range(0,i+1):
            if(j==0):
                print("* ",end="")
            else:
                print("  ",end="")

        for j in range(0,i):
            if(j==i-1):
                print("* ",end="")
            else:
                print("  ",end="")
        print("  "*(int(n/2)-i))
    #Lower Fig
    for i in range(0,int(n/2)):
        print("  "*(i+1),end="")
        for j in range(0,(int(n/2)-i)):
            if(j==0):
                print("* ",end="")
            else:
                print("  ",end="")
        for j in range(0,(int(n/2)-i-1)):
            if(j==(int(n/2)-i-1-1)):
                print("* ",end="")
            else:
                print("  ",end="")
        print("  "*(i+1))


'''
Purpose: Function to print Fig m)
Parameter: Inputted integer 'n'
Return: Nothing, but prints the given figure

  $ $ $ $ $
    $ $ $ $
      $ $ $
        $ $
          $

'''
def patternm(n):
        
    for i in range(1,n+1):
        for j in range(0,i):
            print(end="  ")
        for j in range(0,n+1-i):
            print("$",end=" ")
        print("")
'''
Purpose: Function to print Fig n)
Parameter: Inputted integer 'n'
Return: Nothing, but prints the given figure

          #
        # #
      # # #
    # # # #
  # # # # #

'''
def patternn(n):
    for i in range(1,n+1):
        for j in range(0,n+1-i):
            print(end="  ")
        for j in range(0,i):
            print("#",end=" ")
        print("")

#Making main() as driver function
if __name__ == "__main__":
    main()