'''
This program will help Mr. X to populate his synonym Dictionary with the help of his Dictionary.
It will ask for more word meanings to add from the user. If yes it will first populate his dictionary 
and then make his synonym dictionary.
Note: It will be good approach if words and there meanings are taken as single word.
Example:
I/P:
This is the dictionary program. It will help Mr. X to populate his synonym dictionary.
MR. X dictionary:  {'multiple': 'different', 'several': 'different', 'opera': 'play',
'show': 'play', 'effort': 'work', 'endeavor': 'work', 'travel': 'movement', 'trip': 'movement', 'aid': 'help'}
Enter 'yes' if you want to add more word meaning to the dictionary.Else enter anything: yes
Enter word to add in Dictionary: hibernation
Enter meaning of above word: sleep
Enter 'stop' to stop adding words else writing anything : stop
O/P:
Mr X synonym Dictionary is:  {'different': ['multiple', 'several'],
'play': ['opera', 'show'], 'work': ['effort', 'endeavor'], 'movement': 
['travel', 'trip'], 'help': ['aid'], 'sleep': ['hibernation']}
'''

'''
Purpose:Function to make a synonym dictionary with iterative approach.
It will make the meanig as key and its values will be its synonyms.
Parameter: 'myDict'-original dictionary and 'synDict'-synonym dict both of type dictionary
Return:Returns nothing just the synonym dict is updated because of reference.
'''

def makeSynDict(myDict,synDict):
    #Traversing through myDict
    for i in myDict:
        #If key already present in synDict then append the value to synDict value
        if(myDict[i] in synDict):
            synDict[myDict[i]].append(i)
        #If key is not present then create a new entry in synDict
        else:
            #Values are created of list type so that late values can be appended in the list
            synDict[myDict[i]]=[i]

'''
Purpose: Main function i.e driver function. It handles the program initialisation.
Like inputing new word/meaning pairs to the dictionary. And calling the required function for required task.

'''
def main():
    print("This is the dictionary program. It will help Mr. X to populate his synonym dictionary. ")
    #Original Dict of MR.X with word meaning pairs
    myDict={"multiple":"different","several":"different","opera":"play","show":"play","effort":"work","endeavor":"work","travel":"movement","trip":"movement","aid":"help"}
    print("MR. X dictionary: ",myDict)
    #Input 'yes' to feed more word/meaning to myDict
    inp=(input("Enter 'yes' if you want to add more word meaning to the dictionary.Else enter anything: "))
    if(inp=='yes'):
        #Will stop feeding when 'stop' is entered
        while(True):
            word=(input("Enter word to add in Dictionary: "))
            meaning=(input("Enter meaning of above word: "))
            #Creating a new pair
            myDict[word]=meaning
            #Input 'stop' to stop
            inp=input("Enter 'stop' to stop adding words else writing anything : ")
            if(inp=='stop'):
                break

    #Synonym Dictionary will be filled by makeSynDict() function
    synDict={}
    #Function to fill synonym dictionary
    makeSynDict(myDict,synDict)
    print("Mr X synonym Dictionary is: ",synDict)

#Making main function as driver function
if __name__ == "__main__":
    main()