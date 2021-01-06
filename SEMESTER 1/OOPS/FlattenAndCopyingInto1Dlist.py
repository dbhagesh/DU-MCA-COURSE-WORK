def copyList(myList,copiedList):
    for i in range(len(myList)):
        if(type(myList[i])==type(list())):
            print(myList[i])
            copyList(myList[i],copiedList)
        else:
            print(myList[i])
            copiedList.append(myList[i])

def main():
    list1=[1,2,3,4,5]
    copiedList=[]
    copyList(list1,copiedList)
    print("Final COPIED list",copiedList)
    list1[1]=9
    print(list1)
    print(copiedList)

if __name__ == "__main__":
    main()