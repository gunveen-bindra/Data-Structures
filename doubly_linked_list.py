class Node:
    def __init__(self,element,prev,next):
        self.element=element
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    
    def __init__(self):
        self._head = Node(None,None,None)
        self._tail = Node(None,None,None)
        self._head.next=self._tail
        self._tail.prev=self._head
        self._size = 0
        
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def display(self):
        newest = self._head
        while newest:
            print(newest.element,end='-->')
            newest = newest.next
        print()
        
    def add_head(self,e):
        temp = self._head
        if self.is_empty():
            self._head=temp
            self._tail=temp
        else:
            self._head = Node(e,None,None)
            self._head.next = temp
            self._size += 1
        
    def add_tail(self,e):
        temp = Node(e,None,None)
        if self.is_empty():
            self._head=temp
            self._tail=temp
        else:
            self._tail.next = temp
            temp.prev=self._tail
        self._tail=temp
        self._size += 1
    
    def remove_head(self):
        if self.is_empty():
            print("List is empty")
        value = self._head.element
        self._head = self._head.next
        self._head.prev = None
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return value
    
    def remove_tail(self):
        if self.is_empty():
            print("List is empty")
        newest = self._head
        i = 0
        while i<len(self)-2:
            newest=newest.next
            i+=1
        self._tail =newest 
        newest = newest.next
        value = newest.element
        self._tail.next = None
        self._size -= 1
        return value

    def back_traverse(self):
        first = self._head
        second = first.next
        first.next=None
        first.prev=second
        while second is not None:
            second.prev = second.next
            second.next = first
            first = second
            second = second.prev
        self._head=first
    
l = DoublyLinkedList()
l.add_tail(10)
l.add_tail(20)
l.add_tail(30)
l.add_tail(40)
l.display()
print('Delete',l.remove_head())
l.display()
print('Delete',l.remove_tail())
l.display()
l.add_head(70)
l.add_head(80)
l.add_head(90)
l.add_head(100)
l.display()
l.back_traverse()
l.display()
