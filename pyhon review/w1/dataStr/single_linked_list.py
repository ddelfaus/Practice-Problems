# node


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_data(self):
        return self.value


    def get_next(self):
        return self.next

    def set_next(self, value):
        self.next = value



#Linked list

class LinkedList:
    def __init__(self, head=None):
        self.head = head


    def insert(self,value):
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head= new_node


    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()

        return count


    def search(self, value):

        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == value:
                found =True

            else:
                current = current.get_next()
        
        if current is None:
            print("not in list")




    def delete(self, value):
        current = self.head
        previous = None
        found = False

        while current and found is False:
            if current.get_data() == value:
                found = True
            else:
                previous = current
                current = current.get_next()

            if current is None:
                print("not in list")

            if previous is None:
                self.head = current.get_next()
            
            else: previous.set_next(current.get.Next())

    def get_list(self):
        current = self.head

        while current:
            print(current.get_data())


            current = current.get_next()







new_list = LinkedList().insert(5)

new_list.head.get_list()