    
    
from collections import Counter 
    
    
def makeAnagram(a, b):
    
    
    
    
    # make dictionaries from both strings 
        c1 = Counter(a) 
        c2 = Counter(b) 
        # print(c1)
        # finding the common elements from both dictonary 
        common = c1&c2 
        print(common, "common")
        value = 0
    
        # adding up the key from common dictionary in order  
        # to get the total number of common elements 
        for key in common: 
            value = value + common[key] 
            
        # returning the number of elements to be  
        # removed to form an anagram 
        print(value)
        print(len(a)- 2*value, "waaa")
        return (len(a)-2*value+ len(b))          
    


print(makeAnagram("waaaaa", "waaaaas"))






#failed
#go string a to check if in string b
#if there is a match delete
#count the length of both and add to gether to get delecitons 

# def makeAnagram(a, b):
    
    
#     l1 = list(a)
 
#     l2 = list(b)
    
#     for letter in l1:
#         if letter in l2:
#             l1.remove(letter)
#             l2.remove(letter)

#     for letter2 in l2:
#         if letter2 in l1:
           
#             l1.remove(letter2)
#             l2.remove(letter2)


#     print(l1)
#     print(l2)
#     return len(l1) + len(l2)












# print(makeAnagram("showman", "woman"))



#failed plan
#go through string a and check for same letters 
#if it is add to a new list
#using the legth of that list subtract it from each list to get the total deletions


# def makeAnagram(a, b):

#     contains_letter =[]


#     deletes = 0
#     for letter in a:
#         if letter in b:
#             contains_letter.append(letter)


#     deletes_a = len(a) - len(contains_letter)
#     deletes_b = len(b) - len(contains_letter)

#     deletes = deletes_a + deletes_b

#     print(contains_letter)
#     return deletes


# print(makeAnagram("aaaaaaaaddd", "aaaaaadd"))


#falied plan
#we have to delete characters to make both strings match?

#go through string a and check matches. 
# If there is a match add it to the set
# no match dont add and increase delete count by 1







# def makeAnagram(a, b):
    
#     contains_letter = set()
#     deletes = 0
#     for letter in a:
#         print(letter)
#         if letter in b:
#             contains_letter.add(letter)

#         else:
#             deletes += 1

#     for letter in a:
#         if letter not in contains_letter:
#             deletes +=1 

    
    
#     return deletes


# print(makeAnagram("ade", "fga"))



