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
Purpose:Function to make a synonym dictionary with recursive approach.
It will make the meanig as key and its values will be its synonyms.
Parameter: 'myDict'-original dictionary and 'synDict'-synonym dict both of type dictionary
Return:Returns nothing just the synonym dict is updated because of reference.
'''
import copy 

def makeSynDict(myDict,synDict):
    #If myDict gets empty i.e no more words are left to feed
    #Termination condition
    if not myDict:
        return 0
    else:
        #Taking out each pair of word/meaning at a time
        mytuple=myDict.popitem()
    #Checking if it already exists and then appending it in synonym dict
    if mytuple[1] in synDict:
        synDict[mytuple[1]].append(mytuple[0])
        return makeSynDict(myDict,synDict)
    #If it doesnt exist already then creating its existence in the synonym dict
    else:
        synDict[mytuple[1]]=[mytuple[0]]
        return makeSynDict(myDict,synDict)

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
    myDictcopy=copy.deepcopy(myDict)
    #Function to fill synonym dictionary
    makeSynDict(myDictcopy,synDict)
    print("Mr X synonym Dictionary is: ",synDict)
    
#Making main function as driver function

if __name__ == "__main__":
    main()