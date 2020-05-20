#plan
#go through the array and delete items until everything is equal
#find the number with the highest amount of duplicates
# delete everything else
# return the minimal deletes

from collections import Counter

def equalizeArray(arr):

    # Write your code here
    counted_dict= dict(Counter(arr))
    print(counted_dict)

    highest_freq = max(counted_dict, key = counted_dict.get)
    print(highest_freq)
   

    return len(arr) - counted_dict.get(highest_freq)


print(equalizeArray([3, 3, 2, 1]))

