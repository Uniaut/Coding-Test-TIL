import array

class Stack:
    def __init__(self, max_size=10):
        self.index = 0
        self.max_size = max_size
        self.data = array.array('l', [0] * max_size)
    
    def append(self, value):
        self.index += 1
        if self.index < self.max_size:
            raise Exception('the stack is full')
        else:
            self.data[self.index - 1] = value

    def peek(self):
        if self.index == 0:
            raise Exception('the stack is empty')
        else:
            value = self.data[self.index - 1]
            return value
    
    def pop(self):
        if self.index == 0:
            raise Exception('the stack is empty')
        else:
            value = self.data[self.index - 1]
            self.index -= 1
            return value

    def is_empty(self):
        if self.index == 0:
            return True
        else:
            return False

a = Stack(2)
a.append(1)
a.append(2)
a.append(3)
