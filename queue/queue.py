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

from singly_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)
#add has to always be  in the 1st postion
    def enqueue(self, value):
        self.storage.insert(0,value)
#yeet out
    def dequeue(self):
        try: 
            return self.storage.pop()
        except:      
            return None


class Queue2LL:#still working on this 
    def __init__(self):
        self.apple = 0
        self.storage = LinkedList()
       
    def __len__(self):
        print(self.apple)
        return self.apple
         
         
    def push(self, value):
        self.storage.add_to_tail(value)
        self.apple +=1

    def pop(self):
        try:
            if self.apple == 0:
                return None
            self.apple -=1
            return self.storage.remove_tail()
        except:      
            return None
