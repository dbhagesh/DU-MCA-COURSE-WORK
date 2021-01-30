from tabulate import tabulate
'''
5. Write a program to implement the tautology, Contradiction/Absurdity and Contingency.
a: tautology
b: contradiction
c: contigency
'''
'''
A tautology is a formula which is "always true" --- that is, it is true for every assignment
of truth values to its simple components. You can think of a tautology as a rule of logic.

The opposite of a tautology is a contradiction, a formula which is "always false". In other
words, a contradiction is false for every assignment of truth values to its simple components.

A statement that can be either true or false depending on the truth values of its variables
is called a contingency.

'''
def tautology():
    print("Tautology Example")
    print("A tautology is a formula which is 'always true'")
    print("(P->Q) v (Q->P)")
    print(tabulate([[0,0,1,1,1], [0,1,1,0,1], [1,0,0,1,1], [1,1,1,1,1]], headers=['P', 'Q','(P->Q)',"(Q->P)","(P->Q) v (Q->P)"]))

def contradiction():
    print("Contradiction Example")
    print("A contradiction is a formula which is 'always false'")
    print("(P∧∼P")
    print(tabulate([[1,0,0], [0,1,0]], headers=['P','~P',"P ∧∼P"]))

def contigency():
    print("Contigency Example")
    print("A contigency is a formula which is either 'true' or 'false'.")
    print("(P→Q)⟶ (P∧Q)")
    print(tabulate([[0,0,1,0,0], [0,1,1,0,0], [1,0,0,0,1], [1,1,1,1,1]], headers=['P', 'Q','(P->Q)',"(P∧Q)","(P→Q)⟶ (P∧Q)"]))
    
def main():
    print("Enter a,b,c,d,e for the implemtation of the particular law.\nAnd anyother to exit.")

    while(True):
        inp=input("Enter input: ")
        if(inp=='a'):
            tautology()
        if(inp=='b'):
            contradiction()
        if(inp=='c'):
            contigency()
        else:
            break

if __name__=='__main__':
    main()
        