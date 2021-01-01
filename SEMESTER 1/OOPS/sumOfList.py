'''
I/P:
Enter list size: 5
Enter list elements -
Enter 1 : 1
Enter 2 : 2
Enter 3 : 3
Enter 4 : 4
Enter 5 : 5
Enter list elements -
Enter 1 : 2
Enter 2 : 3
Enter 3 : 4
Enter 4 : 5
Enter 5 : 6
O/P:
[3, 5, 7, 9, 11]
'''
#Main Function
def main():
    #Inputing list size n
    n=int(input("Enter list size: "))
    #Defining the list of size n with zeros
    list1=[0]*n
    list2=[0]*n
    #filling lists
    fillList(list1,n)
    fillList(list2,n)
    #Finding sum of lists
    print(sunList(list1,list2,n))

#Function to sum two numbers
#Parameter: integer: x,y
#Returns : A summed integer z
def sumTwoNum(x,y):
    z=x+y
    return z
#Function to sum two lists using sumTwoNum
#Parameter: Lists -list1,list2 and integer: n
#Returns : A summed list3 with the sum of list1 and list2
def sunList(list1,list2,n):
    #code to sum respective elements of these list
    #return list
    #Initialising a list3 with 'n' zeros
    list3=[0]*n
    #filling summed values of respective elements of list1 and list2 into list3
    for i in range(n):
        list3[i]= sumTwoNum(list1[i],list2[i])
    return list3


#Function to fillList
#Parameter: List -listN and integer: n
#Returns : filling the lists with the user input

def fillList(listN,n):
    print("Enter list elements - ")
    #inputing user filled elements into the list
    for i in range(n):
        listN[i]=int(input("Enter {} : ".format(i+1)))
    return listN
#Making main function as driver function
if __name__ == "__main__":
    main()
