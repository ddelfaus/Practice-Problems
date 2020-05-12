  def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
	     # create a new linked list with 0
        
        current = ListNode(0)
        # create the pointer at started at first postion
        pointer = current
       
        #while True: (I am going to use breaks to stop the loop)
        
        while True:
            
            #check for empty list
            if l1 is None and l2 is None:
                break
            #check for one list to be empty and set the pointer
            elif l1 == None:
                pointer.next = l2
                break
            elif l2 == None:
                pointer.next = l1
                break 
             # else: check for smallest value between both list   
            else:
                smaller_value = 0
                if l1.val < l2.val:
                    smaller_value = l1.val
                    #move to the next val in list
                    l1 = l1.next
                    
                #it will handle >= 
                else:
                    smaller_value = l2.val
                    #move to the next val in list
                    l2 = l2.next
                
                #create new node with smallest value
                new_node = ListNode(smaller_value)
                #set the pointer.next to the new node
                pointer.next = new_node
                pointer = pointer.next
            
        #return value 
        
        return current.next
    
    
    
    "recursive"
    
    #base case
    if l2 is None:
        return l1
    
    if l1 is None:
        return l2
    
    if l1.val <= l2.val
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    
    else:
        l2.next = self.mergeTwoLists(l2.next, l1)
        return l2
    
    
    