class Node:
    '''
    left, right, comparison builtin
    '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BiSearchTree:
    '''
    add, remove, search
    '''
    def __init__(self):
        self.head = None
    

    def __search(self, value, up_node, node, dir=None):
        if node is None:
            result = (up_node, None, dir)
        elif value < node.value:
            result = self.__search(value, node, node.left, 'left')
        elif value > node.value:
            result = self.__search(value, node, node.right, 'right')
        else:
            result = (up_node, node, dir)
        
        return result

    def __traversal(self, node, level=0):
        if node is None:
            return
        else:
            print(' *' * level, node.value)
            self.__traversal(node.left, level + 1)
            self.__traversal(node.right, level + 1)

    def traversal(self):
        self.__traversal(self.head)


    def search(self, value):
        up, down, dir = self.__search(value, None, self.head)
        if down is None:
            return False
        else:
            return True

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            up, down, dir = self.__search(value, None, self.head)
            if down is not None:
                raise Exception('double item')
            else:
                new = Node(value)
                if dir == 'left':
                    up.left = new
                else:
                    up.right = new

    def remove(self, value):
        up, center, dir = self.__search(value, None, self.head)
        if center is None:
            raise Exception('no item')
        else:
            left, right = center.left, center.right
            if left is None and right is None:
                if up is None:
                    self.head = None
                elif dir == 'left':
                    up.left = None
                else:
                    up.right = None
            elif left is None or right is None:
                child = right if left is None else left
                if dir == 'left':
                    up.left = child
                else:
                    up.right = child
            else:
                prev = center
                curr = center.left
                
                while curr.right:
                    prev = curr
                    curr = curr.right

                if prev is not center:
                    prev.right = curr.left
                else:
                    prev.left = curr.left
                
                curr.left = center.left
                curr.right = center.right

                if up is None:
                    self.head = curr
                elif dir == 'left':
                    up.left = curr
                else:
                    up.right = curr


bst = BiSearchTree()
import random
x = list(range(20))
random.shuffle(x)
for el in x:
    bst.add(el)
bst.traversal()

bst.remove(6)
bst.traversal()

bst.remove(10)
bst.traversal()