from stack import Stack

def evaluatePostfix():
    exp = str(input("Enter the postfix expression to evaluate: "))
    stack = Stack(len(exp))
    for i in exp:
        if(i.isalnum()):
            stack.push(i)
        elif(i=='+' or i=='-' or i=='*' or i=='/' or i=='%' or i=='**' ):
            a=int(stack.pop())
            b=int(stack.pop())
            stack.push(str(eval('a'+i+'b')))
        
    print("Evaluated expression resulted into :",stack.pop())

def parenthesisCheck():
    exp = str(input("Enter the postfix expression to evaluate: "))
    stack = Stack(len(exp))
    oParen = ['(','{','[']
    cParen = [')','}',']']
    paren ={')':'(','}':'{',']':'['}
    

    for i in exp:
        if(i in oParen):
            stack.push(i)
        if(i in cParen):
            if(len(stack)==0):
                print("Not Balanced")
                return
            
            if i==')':
                if(stack.front()=='('):
                    stack.pop()
                else:
                    print("Not Balanced")
                    return
            if i=='}':
                if(stack.front()=='{'):
                    stack.pop()
                else:
                    print("Not Balanced")
                    return
            if i==']':
                if(stack.front()=='['):
                    stack.pop()
                else:
                    print("Not Balanced")
                    return
            
    if(len(stack)==0):
        print("Blanced")
    else:
        print("Not Balanced")

    return

def conversionInfixtoPostfix():
    exp = str(input("Enter the postfix expression to evaluate: "))
    stack = Stack(len(exp))
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3,'(':-1,')':-1}
    for i in exp:

        if i.isalnum():
            
            print(i,end='')
        else:
            if(len(stack)==0 or stack.front()=='(' or precedence[i]>precedence[stack.front()] ):
                stack.push(i)      
            elif i=='(':
                stack.push(i)
            elif i==')':
                while(len(stack)!=0 and stack.front!='('):
                    '''
                    if(len(stack)!=0 and stack.front()!='('):
                        break
                    else:
                    '''

                    print(stack.pop(),end='')
            else:
            
                while(len(stack)!=0 and precedence[stack.front()]>=precedence[i]):
                    print(stack.pop(),end="")
                stack.push(i)

    while(len(stack)!=0):
        print(stack.pop(),end="")
                    
    print('\n')
    
        


def main():
    print("-----------------Menu---------------")
    print("1:Evaluate Postfix \n2.Parenthesis checking \n3.Conversion of infix to postfix\n")
    print("Anything else to terminate from menu.")

    while(True):
        n = int(input("Enter choice: "))
        if(n==1):
            evaluatePostfix()
        if(n==2):
            parenthesisCheck()
        if(n==3):
            conversionInfixtoPostfix()
        else:
            break
if __name__=='__main__':
    main()
