from tabulate import tabulate
'''
4. Write a program to implement the following laws:
    a. Identity laws
    b. Domination laws
    c. Double negation laws
    d. Demorgan’s laws
    e. Associative laws
'''
def identityLaw():
    print("Laws->")
    print("X+0=X")
    print("X*1=X")
    print("-Truth Table-")
    print(tabulate([[1, 1], [0, 0]], headers=['Input', 'Output']))
'''
Domination laws
F ∧ x = F: If the first thing in an AND expression is false, then it doesn't matter whether the second thing is true or false; the AND expression is going to be false either way.

T ∨ x = T: If the first thing in an OR expression is true, then it doesn't matter whether the second thing is true or false; the OR expression is going to be true either way.

Idempotent laws
T ∧ x = x: If the first thing in an AND expression is true, then the value of the AND expression will be true if x is true, or false if x is false. In other words, the AND expression will have the same truth value as x does.

F ∨ x = x: If the first thing in an OR expression is false, then the value of the OR expression will be true if x is true, or false if x is false. In other words, the OR expression will have the same truth value as x does.
'''
def dominationLaw():
    print("Laws->")
    print("F ∧ x = F")
    print("T ∨ x = T")
    print("-Truth Table-")
    print(tabulate([[1,0], [0,0]], headers=['Input', 'Output']))
    print("----------------------------")
    print(tabulate([[1,1], [0,1]], headers=['Input', 'Output']))
def doubleNegationLaw():
    print("Law->")
    print("~(~X) = X")
    print("-Truth Table-")
    print(tabulate([[1,1], [0,0]], headers=['Input', 'Output']))

def demorganLaw():
    print("Laws->")
    print("(X.Y)' =(X'+Y') ")
    print("(X+Y)' = (X'.Y')")
    print("-Truth Table-")
    print(tabulate([[0,0,0,0], [0,1,1,1], [1,0,1,1], [1,1,1,1]], headers=['X', 'Y',"(X.Y)'","(X'+Y')"]))
    print("----------------------------")
    print(tabulate([[0,0,1,1], [0,1,0,0], [1,0,0,0], [1,1,0,0]], headers=['X', 'Y',"(X+Y)'","(X'.Y')"]))
def associativeLaw():
    print("Laws->")
    print("(X+Y)+Z = X+(Y+Z) ")
    print("(X.Y).Z = X.(Y.Z) ")
    print("-Truth Table-")
    print(tabulate([[0,0,0,0,0], [0,0,1,1,1], [0,1,0,1,1], [0,1,1,1,1],[1,0,0,1,1], [1,0,1,1,1], [1,1,0,1,1], [1,1,1,1,1]], headers=['X', 'Y','Z',"LHS","RHS"]))
    print("----------------------------")
    print(tabulate([[0,0,0,0,0], [0,0,1,0,0], [0,1,0,0,0], [0,1,1,0,0],[1,0,0,0,0], [1,0,1,0,0], [1,1,0,0,0], [1,1,1,1,1]], headers=['X', 'Y','Z',"LHS","RHS"]))

def main():
    print("Enter a,b,c,d,e for the implemtation of the particular law.\n And anyother to exit.")
    while(True):
        inp=input("Enter input: ")
        if(inp=='a'):
            identityLaw()
        if(inp=='b'):
            dominationLaw()
        if(inp=='c'):
            doubleNegationLaw()
        if(inp=='d'):
            demorganLaw()
        if(inp=='e'):
            associativeLaw()
        else:
            break

if __name__=='__main__':
    main()
        