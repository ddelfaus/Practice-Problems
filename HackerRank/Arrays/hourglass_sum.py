
    #2d array
    #need to go through the 2d array in hourglass pattern
    #111 [0,0][0,1][0,2]
    #010 [N][1,1][N]
    #111 [2,0][2,1][2,2]
    #need to create an array of list of sums to use max on
def hourglassSum(arr):
    sums = []
    for r in range(len(arr)- 2):
        for c in range(len(arr)-2):
            hour_sum = 0
            hour_sum += arr[r][c] + arr[r][c + 1]+ arr[r][c + 2] + arr[r + 1][c + 1] + arr[r+2][c] + arr[r+2][c + 1] + arr[r + 2][c + 2]

            sums.append(hour_sum)

    return max(sums)