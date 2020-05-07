        # think about how do this same problem with an array
        # [1, 2, 2, 1]
            ^        ^
        
        # with an array, we'll have two pointers, one at each end
        # have the pointers move in towards the middle of the array in unison
        # at each iteration step, we check that their elements match
        # when we get to the middle of the array, do we have an old element out or not
        # so if there isn't an odd element, then we stop at the two middle 
        # if there is an odd element out, we dont actually need to check it; it can be anything
        
        # doing this with a linked list
        # we don't have access directly to the end
        # moving backwards is not something we can easilyt do with a singly linked list
        # dont know the length
        
        
        # reverse the last half of the linked list
        # have a pointer at the end and a pointer at the head
        # traverse both pointers towards the middle
        
        # let's migrate the data to a different data structure that is easier  to do the check on
        # traverse the linked list and create an array with the elements of the list
        #check if the array is palindrome
        
        fast = head
        slow = head
        