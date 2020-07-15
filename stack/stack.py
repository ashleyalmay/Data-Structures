"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
       return len(self.storage)
    
    def push(self, value):
        self.storage.append(value)

    def pop(self):
        try: 
            return self.storage.pop()
        except:      
            return None
        
class Stack2LL:
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

#stack 2 wasnt working I thought it was the naming I had size before but put apple i had to check on pop if 0 was true and add on push. 