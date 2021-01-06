def flattenUsingRec(myList):
    
    for i in range(len(myList)):
        if(type(myList[i])==type(list())):
            return flattenUsingRec(myList[i])
        else:
            print(myList[i])
    #return newList

def main():
    #list1=[1,2,3,4,5]
    list2=[1,[2,3],4,[5,6]]
    #print(flattenUsingRec(list1))
    print(flattenUsingRec(list2))

if __name__ == "__main__":
    main()



