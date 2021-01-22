# checking unique characters in string
# for each letter add it to a list
# check letter in list to determind if unique


def check(word):
    letters = []
    for x in word:
        if x not in letters:
            letters.append(x)
            print(letters)
        else:
            return False

    return True


# 1.2 check Permutation
# arrays must have the same number of characters only order can be different
# get lengths and check if same
# sort both strings and check if same
def perm(string1, string2):
    len1 = len(string1)
    len2 = len(string2)

    if len1 != len2:
        return False

    if sorted(string1) == sorted(string2):
        return True

    else:
        return False


print(perm("eef", "ecf"))


# 1.3
# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith
# ", 13
# Output: "Mr%20John%20Smith"


def url(string):
    new_string = string.replace(" ", "%20")
    return new_string


print(url("the a f e   aea"))


# 1.4
# Palindrome Permutation
# get rid of spaces and lowercase everything
# go through string a count and store each letter
# need to use dict
# at most only 1 letter can have an odd occurrence
#

def pp(string):
    new_string = string.replace(" ", "")
    new_string = new_string.lower()

    d = {}

    for i in new_string:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
# check for 1 odd count
    odd_count = 0
    for k, v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

# print(pp("dog godeers"))


# 1.5 one away

def one(string1, string2):
    # sort both words
    word1 = sorted(string1)
    word2 = sorted(string2)

# check if one word is smaller than the other
# store the larger word first or if they are the same store the first one
    stored_word = []
    compared_word = []
    if len(word1) >= len(word2):
        stored_word = word1
        compared_word = word2
    else:
        stored_word = word2
        compared_word = word1
    #check if difference is greater than 1
    count = 0
    if len(stored_word) > len(compared_word):
        diff = len(stored_word) - len(compared_word)
        if diff > 1:
            return False

        else:
            count = 1

    # compare the smaller or the second one to the word that is stored
    # have a count that counts when the characters are not the same if its is greater than 1 return false
    for i in range(0, len(compared_word)):
        print(i)
        if stored_word[i] != compared_word[i]:
            count += 1

    if count <= 1:
        return True

    else:
        return False
#
print(one("effs", "dogs"))

#1.6

# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (


#go through string and store the letter and a count with a object or dictnary 
#if count greater than 1 return false

def sc(string):

    new_string = string.lower()
    d= {}
    return_string= True

    for i in string:
        if i in d:
            d[i] += 1
            return_string = False
        else:
            d[i] = 1

    if return_string is True:
        print(string)
    else:
        l = []
        for key, value in d.items():
            l.append(key)
            if value > 1 :
                l.append(str(value))

        

        l = ''.join(l)
        print(l)
        
sc("")


#1.7
# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?



    #     # transpose matrix
    #     for i in range(n):
    #         for j in range(i, n):
    #             matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    #     # reverse each row
    #     for i in range(n):
    #         matrix[i].reverse()

def flip(matrix): 
    n = len(matrix[0])
    for r in range(n):
        print(r, "row")
        for c in range(r, n):
            print(c, "col")
            matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]
            

    for r in range(n):
        matrix[r].reverse()
    


# flip([[1,2,3],[4,5,6],[7,8,9]])



# 1.8 zero matrix Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0. 

# go through matrix and if element = o then set the row and col to zero
# use matrix traversal 
# check for 0
# if 0 than set mark in a set



def zero(matrix): 
    print(matrix)
    R = len(matrix)
    C = len(matrix[0])
    #create a place to store marks
    rows = []
    cols = []
    #loop through and mark
    for r in range(R):
        for c in range(C):
            if matrix[r][c] == 0:
                rows.append(r)
                cols.append(c)

    #set matrix to zero if mark
    for r in range(R):
        for c in range(C):
            if r in rows or c in cols:
                matrix[r][c] = 0


    print(matrix)


# zero([[0,1,2,0],[3,4,5,2],[1,3,1,5]])

#1.9
# String Rotation:Assumeyou have a method isSubstringwhich checks if oneword is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

#plan

#stort each word and check if same

def strroate(s1, s2):
    string1 = ''.join(sorted(s1))
    string2 = ''.join(sorted(s2))

    if string1 == string2:
        return True
    else:
        return False



print(strroate("test","estt"))
