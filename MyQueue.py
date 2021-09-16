from MyNode import Node

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0 
    def enqueue(self, value):
        if self.has_space():
            node_to_add = Node(value)
            if self.is_empty():
                self.head = node_to_add
                self.tail = node_to_add
            else:
                self.tail.set_next_node(node_to_add)
                self.tail = node_to_add
            self.size += 1
        else:
            return None
    def dequeue(self):
        if self.get_size > 0:
            node_to_remove = self.head
            if self.get_size == 0:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
                self.size -= 1
                return node_to_remove.get_value()
        else:
            return None
    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            return None 
    def get_size(self):
        return self.size
    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()
    def is_empty(self):
        return self.size == 0
        

