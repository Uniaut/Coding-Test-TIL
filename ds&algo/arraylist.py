import array

class ArrayList:
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.size = 1
        self.data = array.array('l', [0])
    
    def __call__(self, idx):
        return self.data[self.head + idx]

    def __repr__(self):
        return str(self.data[self.head:self.tail])

    def append(self, n):
        self.tail += 1
        if self.tail > self.size:
            self.size *= 2
            new_data = array.array('l', [0] * self.size)
            for idx, num in enumerate(self.data):
                new_data[idx] = num
            self.data = new_data
        self.data[self.tail - 1] = n

    def isempty(self):
        if self.tail - self.head:
            return False
        else:
            return True
    
    def prepend(self, n):
        self.append(0)
        for idx in range(self.tail - 2, self.head - 1, -1):
            self.data[idx + 1] = self.data[idx]
        self.data[self.head] = n

    def sethead(self, idx):
        self.head += idx

    def insert(self, n, idx):
        self.sethead(idx)
        self.prepend(n)
        self.sethead(-idx)

    def remove(self, idx):
        self.tail -= 1
        for idx in range(self.head + idx, self.tail):
            self.data[idx] = self.data[idx + 1]


s = ArrayList()
for i in range(20):
    s.prepend(i)
    print(s)
s.sethead(3)
print(s)
s.prepend(100)
print(s)
s.insert(200, 3)
print(s)
s.remove(7)
print(s)
print(s(4))