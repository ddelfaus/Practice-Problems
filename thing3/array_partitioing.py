#plan 
# record each item into the dictnary and its frequency 
#need to add 1 to the end so that max is never 1
#get the max from the dictnary
# compare max with remandier of len // k


# divide it by the length and make combinations 
# Each element in the array occurs in exactly one subsequence
# All the numbers in a subsequence are distinct
# Elements in the array having the same value must be in different subsequences

def partitionArray(k, numbers):
    # Write your code here
    print(numbers)
    

    # if len(numbers) % k != 0:
    #     return False
    freq = {}
    for i in numbers:
        freq[i] = freq.get(i,0) + 1
        print(freq, "first")
   

    #need to add to end to prevent false postivies
    freq[i] = freq.get(i,0) + 1
    print(freq, "second")

    print(freq.values())

    # max_l = max_l =  max([j for j in freq.values()]) if numbers != [] else  0
    max_l = max([nums for nums in freq.values()])
    print(max_l)
  
    if len(numbers) // k >= max_l:
        return True
    return False




print(partitionArray(3, [1, 2, 3, 4]))