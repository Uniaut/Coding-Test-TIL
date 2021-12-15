class DualNode:
    '''
    DualNode members:
        self.value -> value.
        self.next -> ref to next node
        self.prev -> ref to prev node
        
    methods:
        self.__init__(self, value) -> constructor
    '''
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    @staticmethod
    def connect(prev_node, next_node):
        prev_node.next = next_node
        next_node.prev = prev_node


class DoubleLinkedList:
    '''
    member:
        self.head: head node
        self.tail: tail node
        self.length: length of list

    methods:
        self.__init__() : constructor, make empty list
        self.is_empty() : is list empty
        self.prepend(value) : head append
        self.append(value) : tail append
        self.pop(): tail pop
        self.leftpop() : head pop
        self.__getitem__(index) : indexing
        self.insert_after(value, index) : insert after item
        self.remove(value, index) : insert after item
    '''

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def __getitem__(self, key):
        item = self.index(key)
        return item.value

    def index(self, index):
        if index > 0:
            item = self.head
            while index:
                index -= 1
                item = item.next
        elif index < 0:
            item = self.tail
            while index + 1:
                index += 1
                item = item.prev
        else:
            item = self.head
        return item

    def is_empty(self) -> bool:
        if self.length:
            return True
        else:
            return False
    
    def prepend(self, value):
        new_node = DualNode(value)
        if self.length == 0:
            self.head, self.tail = new_node, new_node
        else:
            old_head = self.head
            DualNode.connect(new_node, old_head)
            self.head = new_node
        self.length += 1

    def append(self, value):
        new_node = DualNode(value)
        if self.length == 0:
            self.head, self.tail = new_node, new_node
        else:
            old_tail = self.tail
            DualNode.connect(old_tail, new_node)
            self.tail = new_node
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            pass
        elif self.length == 1:
            self.length = 0
            self.head, self.tail = None, None
        else:
            self.length -= 1
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail  = new_tail
    
    def leftpop(self):
        if self.length == 0:
            raise Exception('Underflow')
        elif self.length == 1:
            old_head = self.head

            self.length = 0
            self.head, self.tail = None, None
        else:
            old_head = self.head

            self.length -= 1
            new_head = self.head.next
            new_head.prev = None
            self.tail  = new_head
        return old_head.value

    def insert_after(self, value, index):
        prev_node = self.index(index)
        if prev_node is self.tail:
            self.append(value)
        else:
            new_node = DualNode(value)
            DualNode.connect(prev_node, new_node)
            next_node = prev_node.next
            DualNode.connect(new_node, next_node)
    
    def remove(self, index):
        remove_node = self.index(index)
        if remove_node is self.head:
            self.leftpop()
        elif remove_node is self.tail:
            self.pop()
        else:
            prev_node = remove_node.prev
            next_node = remove_node.next
            DualNode.connect(prev_node, next_node)