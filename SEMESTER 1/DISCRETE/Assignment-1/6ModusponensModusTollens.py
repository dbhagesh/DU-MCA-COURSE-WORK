from tabulate import tabulate
'''
6. Write a program to implement Modus ponens and Modus Tollens.
a: Modus ponens
b: Modus tollens
'''

def ponens():
    print("Modus Ponens")
   
    print("((P -> Q) ∧ P ) ->Q")
    print(tabulate([[0,0,1,0,1], [0,1,1,0,1], [1,0,0,0,1], [1,1,1,1,1]], headers=['P', 'Q','(P->Q)',"(P -> Q) ∧ P )","((P -> Q) ∧ P ) ->Q"]))

def tollens():
    print("Modus Ponens")
   
    print("((P -> Q) ∧ ~Q ) ->~P")
    print(tabulate([[0,0,1,1,1], [0,1,1,0,1], [1,0,0,0,1], [1,1,1,0,1]], headers=['P', 'Q','(P->Q)',"((P -> Q) ∧ ~Q )","((P -> Q) ∧ ~Q ) ->~P"]))
    
def main():
    print("Enter a,b for the implemtation of the Modus Ponens and Modus Tollens.\nAnd anyother to exit.")

    while(True):
        inp=input("Enter input: ")
        if(inp=='a'):
            ponens()
        if(inp=='b'):
            tollens()
        else:
            break

if __name__=='__main__':
    main()
            