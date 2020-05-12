    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        
        
        
#         for i in range(len(A) - 1):
#             if A[i] > A[i+1]:
#                 return i
            
#         return 0


#binary serach

        lower = 0
        higher = len(A) - 1
        
        while lower < higher:
            middle = (lower + higher) / 2
            
            if A[middle] > A[middle + 1]:
                lower = middle + 1
            
            else:
                higher = middle
            
            
        return lower