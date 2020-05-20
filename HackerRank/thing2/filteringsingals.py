#plan
#need to go through the frequencise and pass through the filters which is a list in a list
#need to figure out way to check with each fiter range and return a count

from collections import Counter


def countSignals(frequencies, filterRanges):
    # Write your code here
    store_nums = []
    for ranges in filterRanges:
        for number in frequencies:
            if number in range(ranges[0], ranges[1]):
                
                store_nums.append(number)

    
  
    counted_dict= dict(Counter(store_nums))
    
    amount = 0
    
    counted_dict = dict((k, v) for k, v in counted_dict.items() if v == len(filterRanges))
    return (len(counted_dict))
    # if len(filterRanges) in counted_dict.values():
    #     print("")

    # for freq in counted_dict:
    #     print(freq, "test")
    #     if freq.get() == len(filterRanges):
           
    #         amount += 1
    
    # print(amount)