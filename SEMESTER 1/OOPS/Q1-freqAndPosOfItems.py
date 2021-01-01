def main():
    n=int(input("Enter the size of list: "))
    myList=inputList(n)
    freqAndPos(myList)

#Function to input values in the list
#Parameters: Length of list:int value
def inputList(n):
    myList=[0]*n
    for i in range(n):
        myList[i]=int(input("Enter {} element:".format(i+1)))
    return myList

def freqAndPos(myList):
    freqDict={}
    posDict={}
    for i in myList:
        if i not in freqDict.keys():
            freqDict[i]=1
        else:
            freqDict=freqDict[i]+1
    print(freqDict)

if __name__ == "__main__":
    main()


