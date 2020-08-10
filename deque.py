class Deque:
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data)==0
    
    def first(self):
        if self.is_empty():
            raise exception('Deque is empty')
        else:
            return self._data[0]
    
    def last(self):
        if self.is_empty():
            raise exception('Deque is empty')
        else:
            return self._data[-1]
    
    def add_first(self,data):
        self._data.insert(0,data)
        
    def add_last(self,data):
        self._data.append(data)
        
    def delete_first(self):
        if self.is_empty():
            raise exception('Deque is empty')
        value = self._data.pop(0)
        return value
    
    def delete_last(self):
        if self.is_empty():
            raise exception('Deque is empty')
        value = self._data.pop()
        return value


d=Deque()
d.add_last(10)
d.add_last(20)
d.add_last(30)
d.add_last(40)
d.add_last(50)
print('Deque: ',d._data)
print('First: ',d.first())
print('Delete first: ',d.delete_first())
print('Deque: ',d._data)
print('Last: ',d.last())
print('Delete last: ',d.delete_last())
print('Deque: ',d._data)
d.add_first(50)
print('Add First')
print('Deque: ',d._data)
d.add_last(60)
print('Add Last')
print('Deque: ',d._data)
print('Length: ',len(d))
