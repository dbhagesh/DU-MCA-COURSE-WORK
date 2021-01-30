def flattenUsingRec(myList):
    
    for i in range(len(myList)):
        if(type(myList[i])==type(list())):
            return flattenUsingRec(myList[i])
        else:
            print(myList[i])

def main():
    
    list1=[1,[2,3],4,[5,6]]
    print(flattenUsingRec(list1))
    
#Making main() as driver function
if __name__ == "__main__":
    main()



