import math
# 2.1 R�mov� Dups! Write code to remove duplicates from an unsorted linked list.
#plan store each node value in a list if in list already remove it


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def get_data(self):
        return self.value

    def set_next(self, value):
        self.next = value

class LinkedList:
    def __init__(self,head =None, ):
        self.head = head
  
    def get_head(self):
        return self.head
    def insert_as_new_head(self, value):
        new_node =Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert(self, value):
        #set value and create node
        new_node = Node(value)
        #check for head node
        if self.head is None:
            self.head = new_node
        
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            
            current.next = new_node
     
    def print_list(self):

        current =self.head
        print("start")
        while current:
            print(current.value)
            current = current.next
        print("end")
    
    def delete_dups(self):
        current = self.head
        nodes = []
        while current:
            if current.value not in nodes:
                nodes.append(current.value)

                prev = current
                current = current.next
            else:
                
                prev.next = current.next

                current = current.next

#2.2 return nth to end of single linked list

# go through the list to the n and print values from n to last node 
    #go through list
    #keep track of length
    #check 

    def print_at_n_to_end(self,n):
        current = self.head
        count = 0
       
        while current:
            count +=1

            if count >= n:
                print(current.value)
                current = current.next
            else:
                current = current.next

#2.3 delete the middle node
    def delete_mid(self):
    #get length of linked list
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next

        print(count)
        if count <=2:
            print("list too small")
            return
        #find midpoint and round up
        midpoint = math.ceil(count/2)
        print(midpoint)

        #go through linked list again and remove the midpoint
        current = self.head
        count = 0

        while current:
            count +=1 
            if count != midpoint:
                
                prev = current
                current = current.next
            
            else:
                prev.next = current.next
                current = None
    

# 2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.

#need two pointers and listnodes  using a dummy list
#before head and after head
#depening on x we add to each listnode
#combine them
   
#    *****
    def partx(self,head, x):
        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_head = Node(0)
        after = after_head = Node(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next



# 2.5 You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.

#go through first node list and the second one with 2 while loops
#add values of each and the go to next node
#add a carry varible to carry over

def sum(self,x, y)
   
        result = ListNode(0)
        result_head = result
        
        y = l2.val
        xy = []
        carry = 0
        while l1 and l2:
            x = l1.val
            y = l2.val
            total = x + y
            if carry == 1:
                total += 1
                
            if total >= 10:
                carry = 1
                total = 0
            else:
                carry = 0
            
            result_head.next = ListNode(total)
            result_head = result_head.next
        
            l1 = l1.next
            l2 = l2.next
        return result.next
         
new_list = LinkedList()
new_list.insert(5)
new_list.insert(2)
new_list.insert(1)
new_list.insert(13)
new_list.insert(25)
new_list.insert(35)
# new_list.print_list()
# new_list.delete_dups()
# new_list.print_at_n_to_end(4)
new_list.print_list()
new_list.delete_mid()




