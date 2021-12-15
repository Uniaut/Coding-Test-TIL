class SingleNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def index(self, n):
        if n == 0:
            return self
        else:
            return self.next.index(n - 1)

    def tail(self):
        if self.next is None:
            return self
        else:
            return self.next.tail()



class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def prepend(self, value):
        old_head = self.head
        new_head = SingleNode(value)

        new_head.next = old_head
        self.head = new_head
    
    def append(self, value):
        old_tail = self.head.tail()
        new_tail = SingleNode(value)

        old_tail.next = new_tail
    
    def set_head(self, idx):
        self.head = self.head.index(idx)

    def __getitem__(self, key):
        return self.head.index(key)

    def insert(self, value, idx):
        prev_ele = self.head.index(idx)
        next_ele = prev_ele.next
        new_ele = SingleNode(value)

        prev_ele.next = new_ele
        new_ele.next = next_ele

    def remove(self, value, idx):
        if idx == 0:
            self.head = self.head.next
        else:
            prev_ele = self.head.index(idx - 1)
            remove_ele = prev_ele.next
            next_ele = remove_ele.next

            prev_ele.next = next_ele