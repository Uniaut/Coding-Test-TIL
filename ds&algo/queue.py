import array
import double_linked_list

class LinearQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.front = 0
        self.rear = 0
        self.data = array.array('l', [0] * self.max_size)

    def index_validation(self, prompt):
        if prompt == 'put':
            if self.max_size == self.rear:
                raise Exception('Overflow')
        elif prompt == 'get' or prompt == 'peek':
            if self.front == self.rear:
                raise Exception('Underflow')
            
        
    def put(self, value):
        self.index_validation('put')
        self.data[self.rear] = value
        self.rear += 1
    
    def get(self):
        self.index_validation('get')
        item = self.data[self.front]
        self.front += 1
        return item
    
    def peek(self):
        self.index_validation('peek')
        item = self.data[self.front]
        return item


class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.front = 0
        self.rear = 0
        self.data = array.array('l', [0] * self.max_size)


    def index_validation(self, prompt):
        if prompt == 'put':
            if self.front + self.max_size == self.rear:
                raise Exception('Overflow')
        elif prompt == 'get' or prompt == 'peek':
            if self.front == self.rear:
                raise Exception('Underflow')
            
        
    def put(self, value):
        self.index_validation('put')
        self.data[self.rear % self.max_size] = value
        self.rear += 1
    
    def get(self):
        self.index_validation('get')
        item = self.data[self.front % self.max_size]
        self.front += 1
        return item
    
    def peek(self):
        self.index_validation('peek')
        item = self.data[self.front % self.max_size]
        return item

class LinkedQueue:
    '''
    TODO:
    self.put()
    self.get()
    self.peek()
    '''
    def __init__(self):
        self.data = double_linked_list.DoubleLinkedList()
    
    def index_validation(self, prompt):
        if prompt == 'put':
            pass
        elif prompt == 'get' or prompt == 'peek':
            if self.data.is_empty():
                raise Exception('Underflow')
    
    def put(self, value):
        self.index_validation(self, 'put')
        self.data.append(value)
    
    def get(self, value):
        self.index_validation(self, 'get')
        return self.data.leftpop()
    
    def peek(self, value):
        self.index_validation(self, 'peek')
        return self.data.head.value