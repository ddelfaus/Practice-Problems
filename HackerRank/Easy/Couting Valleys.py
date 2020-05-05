#plan
# go through arr and check if it is below start
#if it is below start then continue going though arr until it goes back at sea level
#when it does incrase valley by 1


def countingValleys(n, s):
    altitude = 0
    valleys = 0
    for x in s:
        if x == 'U':
            altitude = altitude + 1
        else:
            altitude = altitude - 1
        
        if x == 'U' and altitude == 0:
            valleys = valleys + 1
    
    return valleys                


print(countingValleys(5,'UDDDUDUU'))