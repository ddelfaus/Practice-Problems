class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #the majority element is the element that appears more than floor(n/2) times
        # we dont need to worry about there not being a majority element
        
        # is there a pssibility of multiple majority elements
        #how many times each number shows up
        # hash map with keys athe numbers and values as the counts
        
        #1. popuiulate a hash map with the counts of each of the numbers in the input list
        majority = len(nums)// 2
    
        counts = {}
        
        for n in nums:
            if n in counts:
                counts[n] += 1
                
            else:
                counts[n] = 1
        
            if counts[n] > majority:
                return n
                
                
        # #2. look through our hash map to see which number a value > n //2
        
        # for key, values in counts.items():
        #     if values > majority:
        #         return key