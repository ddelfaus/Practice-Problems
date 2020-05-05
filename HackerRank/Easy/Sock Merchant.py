#Plan
# Create a set()
#go through arr 
#add to set if nothing in it
#if there is something increase the count by 1
# remove it from set
#return count

def sockMerchant(n, ar):
    socks = set()
    pairs = 0
    for x in ar:
 
        if x not in socks:
            socks.add(x)

        else: 
            socks.remove(x)
            pairs = pairs + 1

    return pairs
             




print(sockMerchant(5, [10, 20,20, 10, 10, 30, 50, 10, 20]))