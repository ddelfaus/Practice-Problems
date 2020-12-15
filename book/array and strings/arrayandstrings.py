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