from collections import Counter

#plan
#For the magazine separate the string and put each word in a list
#same thing for the note
#check each word in the note with the magazine
#how to handle duplicates
#I guess I am going to use a dictionary to store the word and the howmany word, amount

def checkMagazine(magazine, note):
    #to store words from magazine
    word_bank = {}

    for word in magazine:
        
        if word not in word_bank:
        
           
            word_bank[word] = 1
        else: 
            word_bank[word] = word_bank[word] + 1
 

    #check if words available 

    for word in note:

        if word in word_bank and word_bank[word] > 0:

            word_bank[word] = word_bank[word] - 1
        else:
            return False

    return True



print(checkMagazine(['dog', 'cat', 'bird', 'bird'],['dog', 'cat', 'bird', 'bird', 'cat']))
