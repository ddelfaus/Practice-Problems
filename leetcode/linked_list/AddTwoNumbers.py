#plan first pass soultion
# is to go through each list node 
# create an array 
# add them togetheor and create a new node list for the soultion



class Solution(object):
     def addTwoNumbers(self, l1, l2, c = 0):
  
         
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret
        
        # list1 = []
        # list2 = []
        # dummy = ListNode(-1)
        # dummy.next = l1
    
        # current = dummy.next
        # # converting to list
        
        # while current:
        #     list1.append(current.val)
        #     current = current.next
            
        # dummy.next = l2
        # current = dummy.next
        # while current:
        #     list2.append(current.val)
        #     current = current.next
    
        # sum_list = 0
        # carry = 0
        # remander = 0
        # total = 0
        # print(list1)
        # print(list2)
        # sums2 = []
        # index = 0
        
        # for i in range(0, len(list1)):
        #     sum_list = list1[i] + list2[i]
        #     if sum_list >= 10:
        #         remander = (list1[i] + list2[i]) % 10
        #         carry = 1
        #         sums2.append(remander)
                
        #     else:
              
        #         total = list1[i] + list2[i] + carry
        #         sums2.append(total)
        #         carry = 0
     
       
        # current = dummy.next
        # for new_node in sums2:
        #     current.next = ListNode(new_node)
        #     current = current.next
            
        # current = dummy.next
        # return current.next
            
   
        