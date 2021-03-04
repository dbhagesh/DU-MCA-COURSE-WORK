'''
Applications of stack:
1. Evaluate Postfix expression
2. Parenthesis checking (consider all three types of parenthesis)
3. Conversion of infix to postfix

A menu driver program to perform any of the above operations on the stack.

Input: 
1. Any proper postfix expression
2. An expression
3. An infix expression
Output:
1. Evaluated expressin
2. Paranthesis checking result
3. Converted postfix expression
'''

#Importing stack class from my stack.py
from stack import Stack

'''
Function to evaluate the postfix expression
Input: Inputs the postfix expression
Output: Evaluated Expression
'''
def evaluatePostfix():
    #Input
    print("Input expression with numeric value and opertors.")
    exp = str(input("Enter the postfix expression to evaluate: "))
    #Creating stack of expression size
    stack = Stack(len(exp))
    #Traversing expression
    for i in exp:
        #push if alphanumeric
        if(i.isalnum()):
            stack.push(i)
        #if operator pop two var from stack and perform operation and push to the stack
        elif(i=='+' or i=='-' or i=='*' or i=='/' or i=='%' or i=='**' ):
            a=int(stack.pop())
            b=int(stack.pop())
            stack.push(str(eval('a'+i+'b')))
    #Evaluated expression 
    print("Evaluated expression resulted into :",stack.pop())
'''
Function to perform parenthesis matching
Input: Expression
Ouput: Result of parenthesis matching
'''
def parenthesisCheck():
    #Input
    exp = str(input("Enter the postfix expression to evaluate: "))
    #Creating stack of the expression size
    stack = Stack(len(exp))
    #Storing different parenthesis
    oParen = ['(','{','[']
    cParen = [')','}',']']

    #Pair of parenthesis
    paren ={')':'(','}':'{',']':'['}
    
    #Traversing expression
    for i in exp:
        #if opening braces
        if(i in oParen):
            stack.push(i)
        #if closing braces
        if(i in cParen):
            #if stack empty
            if(len(stack)==0):
                print("Not Balanced. Missing {}.".format(paren[i]))
                return

            #if braces present then pop else print message
            if i==')':
                if(stack.front()=='('):
                    stack.pop()
                else:
                    print("Not Balanced. Missing {}.".format(paren['(']))
                    return
            if i=='}':
                if(stack.front()=='{'):
                    stack.pop()
                else:
                    print("Not Balanced. Missing {}.".format(paren['{']))
                    return
            if i==']':
                if(stack.front()=='['):
                    stack.pop()
                else:
                    print("Not Balanced. Missing {}.".format(paren['[']))
                    return
    #if braces still present in the stack then unbalanced else balanced        
    if(len(stack)==0):
        print("Blanced")
    else:
        print("Not Balanced. Missing pair of {}".format(stack.front()))

    return
'''
Function to convert Infix to Postfix expression
Input: Infix expression
Ouput: Postfix expression
'''

def conversionInfixtoPostfix():
    #Input
    exp = str(input("Enter the infix expression. "))
    #Creating stack
    stack = Stack(len(exp))
    #Precedence Dictionary
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3,'(':-1,')':-1}
    #Output string
    s = ""
    #Traversing the expression
    for i in exp:
        #If alpha numeric
        if i.isalnum():
            #Append to output
            s+=i
        #if opening braces
        elif i=='(':
            stack.push(i)
        #If closing braces
        elif i==')':
            #until stack is non empty and no opening braces on top of stack 
            while(len(stack)!=0 and stack.front()!='('):
                s+=stack.front()
                stack.pop()
            #Safety condition
            if(len(stack)!=0 and stack.front()!='('):
                return -1
            #Popping the top of stack
            else:
                stack.pop()
            
        #If operator
        else:
            #If stack is non empty and expression opertor precedence is less the than the top of stack preference
            while(len(stack)!=0 and precedence[i]<=precedence[stack.front()]):
                #Appending in output
                s+=stack.front()
                stack.pop()
            #Pushing the new operator
            stack.push(i)
    #Appending the left over things into the stack
    while(len(stack)!=0):
        #Appending in output
        s+=stack.front()
        stack.pop()

    #prting output              
    print("Postfix expression is: ",s)
        
'''
Main function to perform the specified tast
It contains the menu driven function to perform the required operations 
onto the expression.
Input: Choice for the menu function
'''

def main():
    '''
    MENU:
    1:Evaluate Postfix 
    2.Parenthesis checking 
    3.Conversion of infix to postfix
    
    '''
    print("-----------------Menu---------------")
    print("1:Evaluate Postfix \n2.Parenthesis checking \n3.Conversion of infix to postfix\n")
    print("Anything else to terminate from menu.")
    #Loops until exiting condition is encountered
    while(True):
        #Input for menu
        try:
            n = int(input("Enter choice: "))
            if(n==1):
                evaluatePostfix()
            elif(n==2):
                parenthesisCheck()
            elif(n==3):
                conversionInfixtoPostfix()
            else:
                #Terminating condition
                print("Exiting program...")
                break
        except:
            print("Enter a valid input.")
#Making main() as the driver function
if __name__=='__main__':
    main()
