#plan
#create a dummy node for the new list
#go through the linked list
#if node.next reaches the kth value change the .next to .next.next to skip it

# return the list


# def removeKthLinkedListNode(head, k):
#     # Write your code here
#     #creating dummy node
#     start = SinglyLinkedListNode(-1)
#     start.next = head
#     length = 0
#     current = start
#     while current is not None:
       
#         length += 1
#         current = current.next
    
#     change_k = length - k -1
#     length = 0

#     start.next = head
#     current = start        
#     while current is not None:
#         if length == change_k:
#             length += 1
#             current.next = current.next.next
#         else:    
#             length += 1
#             current = current.next
#     return start.next