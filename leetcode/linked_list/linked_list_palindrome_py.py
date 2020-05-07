# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # helper function to count the length of the linked list 
    def count_list_len(self, head: ListNode) -> int:
        count = 0
        current = head
        
        while current:
            count += 1
            current = current.next
            
        return count
    
    def isPalindrome(self, head: ListNode) -> bool:
        len = self.count_list_len(head)
        
        # init ahead and behind pointers 
        ahead = head
        behind = None
        
        # reverse the first half of the linked list 
        for _ in range(len // 2):
            temp = ahead
            ahead = temp.next
            temp.next = behind
            behind = temp
            
        # if the linked list's length is odd, move ahead forward by one node
		# so that we skip the middle element
        if len % 2 == 1:
            ahead = ahead.next
            
        # ahead moves towards the end of the list, behind moves towards the front of the list 
        while ahead:
            if ahead.val != behind.val:
                return False
            
            ahead = ahead.next
            behind = behind.next
            
        return True