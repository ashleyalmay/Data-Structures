"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #this makes new node
        new_Node = ListNode(value)
        #tells it where to go
        new_Node.next = self.head
        #prev nothing is there
        new_Node.prev = None

        if self.head is not None:
            self.head.prev = new_Node
        #something there added it 
        self.head = new_Node
        #adds 1 to the counter in memory
        self.length +=1
        
        if self.tail is None:
            #order matters move things right to left
            self.tail = self.head
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return
        else:
            x = self.head.value
            #more then 1 in the list
            if self.head is not self.tail:
                self.head = self.head.next
                self.head.prev = None
            #just one element in the list    
            else:
                self.head = None
                self.tail = None
        #counter
        self.length -=1       
        return x   
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            self.head = new_node
        self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.#
    """
    def remove_from_tail(self):
        current_tail = self.tail
        if self.tail.prev is None:
            self.head = None
            self.tail = self.tail.prev
        #counter
        self.length -=1
        return current_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head == node:
            return
        if self.tail == node:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        node.prev.next = node.next
        node.prev = None
        node.next = self.head
        self.head = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.#
    """
    def move_to_end(self, node):
        # delete the node
        self.delete(node)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.#
    """
    def delete(self, node):
        if self.tail == node and self.head == node:
            #checks tail and head
            self.head = None
            self.tail = None
            return
        if self.tail == node:
            self.tail = node.prev
            node.prev.next = None
            return
        if self.head == node:
            self.head = node.next
            node.next.prev = None
            return
        x = self.head
        while x.next is not None:
            if x.value == x:
                break
            x = x.next
        if x.next is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            if x.value == x:
                x.value = None
            #counter
            self.length -=1    
            return
            
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return
        else:
            #set a max node to None
            current_max = None
            #set current node to current head
            current_node = self.head
            #loop over the nodelist while the current_node is not None
            while current_node is not None:
                # check if current max is none or if current node is greater than current max
                if current_max is None or current_node.value > current_max:
                    # overwrites current_max to the current_node.value
                    current_max = current_node.value
                current_node = current_node.next
            return current_max