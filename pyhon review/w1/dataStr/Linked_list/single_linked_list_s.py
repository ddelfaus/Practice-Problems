#linked list
# collection of nodes
 
# build node class
#has a pointer to the next node
#has a value
#functions
#get data
#get next
#set next

#build single list class
#has a head or start or first node
#insert 
#size 
#search
#delete
#get list


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


    def get_data(self):
        return self.value = value

    def get_next(self):
        return self.next = next

    def set_next(self, value):
        self.next = value



class LinkedList:
    def __init__(self, head = None):
        self.head = head


    def insert(self, value):
        #needs to add a value to the end of list
        




