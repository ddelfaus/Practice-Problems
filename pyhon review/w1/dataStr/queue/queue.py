import sys

sys.path.append('../double_linked_list')

from double_linked_list import DoubleList



"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# array
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size
#     def __str__(self):
#        return f'{self.storage}'
#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1


#     def dequeue(self):
#         if self.size > 0 :
#             val = self.storage[0]
#             self.storage.pop(0)
#             self.size -= 1
#             return val
#         else:
#             return None



#Linked list

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoubleList()
    
    def __len__(self):
        return self.size
    def __str__(self):
       return f'{self.storage}'
    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1


    def dequeue(self):
        if self.size > 0 :
            val = self.storage[0]
            self.storage.pop(0)
            self.size -= 1
            return val
        else:
            return None


test = Queue()
test.dequeue()

test.enqueue(100)
test.enqueue(101)
test.enqueue(105)
test.dequeue()
print(len(test))

print(test)