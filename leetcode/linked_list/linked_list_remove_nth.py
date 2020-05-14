#plan 
#go through node list and count
#remove it by setting current.next.next over it


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
    
        start = ListNode(-1)
        start.next = head
        
        length = 0
        
        current = start
        
        while current is not None:
         
            length += 1
            current = current.next
            
        
     
        changed_n = length - n - 1
        length = 0
        
        start.next = head
        current = start
        while current is not None:
          
            if length == changed_n:
             
                length += 1
                current.next = current.next.next
                
            else:
                length += 1
                current = current.next
                
        return start.next
                
        