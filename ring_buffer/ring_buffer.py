from doubly_linked_list import DoublyLinkedList
'''
A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

Implement this behavior in the RingBuffer class. RingBuffer has two methods, append and get. The append method adds elements to the buffer. The get method, which is provided, returns all of the elements in the buffer in a list in their given order. It should not return any None values in the list even if they are present in the ring buffer.
buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']
'''

'''
if storage len < capacity
    add to
    set head = current
if storage len = cap
    if current = head
    remove head
    add to head
    curr = curr.next
if curr.next is not none
    add to head
    prev and next change
    curr = head
    remove head
    move curr to curr.next
'''

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()                

    def append(self, item):
        #if self len < cap
        if self.storage.length < self.capacity:
            #add to tail
            self.storage.add_to_tail(item)
            # curr = head
            self.current = self.storage.head
            return
        #if self.len = cap
        if self.storage.length == self.capacity:
            #if current = head
            if self.current == self.storage.head:
                #remove head
                self.storage.remove_from_head()
                #make the item the head
                self.storage.add_to_head(item)
                #update the current to next
                self.current = self.current.next
                return
            #if curr.next is not none
            if self.current.next:
                #add to head
                self.storage.add_to_head(item)
                new_node = self.storage.head
                #prev and next change
                temp = self.current.next
                self.storage.head = self.storage.head.next
                self.current.next = new_node
                new_node.prev = self.current
                new_node.next = temp
                temp.prev = new_node
                
                if self.current.next.next:
                    self.current = self.current.next.next
                    # curr goes to front
                    self.storage.move_to_front(self.current.prev.prev)
                    # remove head
                    old_head = self.storage.remove_from_head()
            else:
                self.current = self.storage.head
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item) 

    def get(self):
        list_buffer_contents = []
        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next
        return list_buffer_contents
