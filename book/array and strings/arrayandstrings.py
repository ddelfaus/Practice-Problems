#checking unique characters in string
#for each letter add it to a list
#check letter in list to determind if unique


def check (word):
    letters = []
    for x in word:
        if x not in letters:
            letters.append(x)
            print(letters)
        else:
            return False
    
    return True




#1.2 check Permutation
#arrays must have the same number of characters only order can be different
#get lengths and check if same
#sort both strings and check if same
def perm(string1, string2):
    len1= len(string1)
    len2 = len(string2)

    if len1 != len2:
        return False
    
    if sorted(string1) == sorted(string2):
        return True
    
    else:
        return False
    

    



print(perm("eef", "ecf"))



#1.3 
# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith
# ", 13
# Output: "Mr%20John%20Smith"


def url(string):
    new_string =string.replace(" ", "%20")
    return new_string


print(url("the a f e   aea"))



#1.4
