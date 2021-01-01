def main():
    print(" a: ORDER \n b: CHANGEABILITY\n c: DENOTION\n d: DUPLICACY\n e: EMPTY DATATYPE DENOTION\n f: exit the program")
    
    while(True):
        inp=input("Enter:")
        while(True):
            if(inp=="a"):
                order()
                break
            if(inp=="b"):
                changeability()
                break
            if(inp=="c"):
                denotion()
                break
            if(inp=="d"):
                duplicate()
                break
            if(inp=="e"):
                emptyData()
                break
            if(inp=="f"):
                print("---EXIT---")
                exit()
def order():
    print("----ORDER----")
    print("ORDER MEANS THAT IF THE DATA IS ARRANGED IN SOME ORDER")
    print("List  : Ordered ")
    print("Tuple : Ordered ")
    print("Set   : Unordered ")
    print("Dict  : Unordered ")

def changeability():
    print("----CHANGEABILITY----")
    print("IF THE DATA CAN BE CHANGED OR MODIEFIED IN SOME WAY OR NOT")
    print("List  : Changeable ")
    print("Tuple : Unchangeable ")
    print("Set   : Unchangeable ")
    print("Dict  : Changeable ")

def denotion():
    print("----DENOTION----")
    print("HOW THE DATA TYPES ARE DENOTED")
    print("List  : mylist = [1,2,3] ")
    print("Tuple : mytuple = (1,2,3)") 
    print("Set   : myset = {1,2,3} ")
    print("Dict  : thisdict = {1:'a','2':'b'} ")

def duplicate():
    print("----DUPLICATE VALUES----")
    print("IF DUPLICACY OF ELEMENTS IS ALLOWED OR NOT")
    print("List  : ALLOWED ")
    print("Tuple : ALLOWED ")
    print("Set   : NOT ALLOWED ")
    print("Dict  : NOT ALLOWED ")

def emptyData():
    print("----EMPTY DATA TYPE DENOTION----")
    print("HOW THE EMPTY DATA TYPES ARE DENOTED")
    print("List  : [] ")
    print("Tuple : () ")
    print("Set   : set() ")
    print("Dict  : {} ")
if __name__ == "__main__":
    main()