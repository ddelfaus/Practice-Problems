
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

        while current:
            print(current.value)
            current = current.next

    
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



new_list = LinkedList()
new_list.insert(5)
new_list.insert(2)
new_list.insert(1)
new_list.insert(10)
new_list.insert(13)
new_list.insert(25)
new_list.insert(35)
# new_list.print_list()
# new_list.delete_dups()

new_list.print_at_n_to_end(4)