#plan
#can jump up to 2

#go through inputs when jumpint more than 1 stop it at 2 and jump again
#

def jumpingOnClouds(c):
    
    jump = 0
    i = 0
    # for c[i] in range(len(c)-2):
      
    
    #     if c[i] == 0 and c[i +1] == 0:
    #         jump += 1
    #         i += 2
    #     elif c[i] == 1:
    #         jump +=1 
    #         i +=1
    #     else:
    #         jump +=1
    #         i += 1
        
    # return jump - 1


    while i < len(c) - 1:
        if i + 2 == len(c) or c[i +2 ] == 1:
            i +=1
            jump += 1
        
        else:
            i +=2
            jump += 1

    return jump


c =  [0, 0, 1, 0, 0, 1, 0]

print(jumpingOnClouds(c))