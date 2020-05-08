#Plan

#u
#find all triplets in the array that sum up to the target sum and return 2d array of all the triplets
#each inner array containing a single triplet should have all three of its elements ordered in ascending order
#the triplets themselves should be ordered in ascending order by the first triplet element.
#if two triplet elements have the same first element, then they should be ordered such that smaller second element comes first.
# if two triplet elements have the same first and second elements, then they should be ordered such that the smaller thrid element comes firts

#if no triplets can be found then return empty array

#so basically find 3 values that add up to the target?
#going to loop with each of the possible values that add up to the sun. 3 for loops
#going to check for the target and then return the triplet 

def threeNumberSum(arr, target):
    solutions = []
    for num_1 in range(len(arr) -2):
        for num_2 in range(len(arr) -1):
            for num_3 in range(len(arr)):
                if(arr[num_1] + arr[num_2] + arr[num_3] == target):
                    solution = [arr[num_1],arr[num_2], arr[num_3]]
                    solution.sort()
                    if solution not in solutions:
                        solutions.append(solution)
                   
  
    return solutions






print(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 30))

