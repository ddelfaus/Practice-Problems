from collections import Counter

#Sherlock and Anagrams
#need to find all the pairs of characters in the word to count them
#I think this problem is beyond lambda school

#plan
#going to use counter to store all duplicates 
#




def sherlockAndAnagrams(s):

    count = 0
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        for j in b:
            count+=b[j]*(b[j]-1)/2
    return int(count)





print(sherlockAndAnagrams("abcdefghj"))