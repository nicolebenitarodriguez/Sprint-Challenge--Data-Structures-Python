class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        #pass
        if node == None:
            return
        if node.next_node == None:
            self.head = node
            return
        self.reverse_list(node.next_node, node)
        node.next_node.set_next(node)
'''
the base case is when reach the end of the LL
test if node is at end, then the node becomes head. 

self in the case is the original LL being called in test file
self.list.reverse_list(node=self.list.head, None)
first time it is called above it is given the list head as the first node
so basically starting at the head if statement will pass else will run

the else state will take the node of the next value and the current node
then it will set the next node , next node value to the current node (reversing order) the last step is reversing the head in base case 
'''
