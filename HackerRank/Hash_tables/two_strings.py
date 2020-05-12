# two strings and see if there is a substring
# go through each word and see if that letter is in the second word


def twoStrings(s1, s2):
    for x in s1:
        if x in s2:

            return "yes"

    
    return "no"


print(twoStrings("yer", "waaa"))