from collections import deque
import collections


class BNode:
    '''
    self.value
    self.left
    self.right
    '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BTree:
    def __init__(self, values):
        node_list = [None]
        for v in values:
            node_list.append(BNode(v))
        
        for idx, n in enumerate(node_list):
            if n is None:
                continue

            left_idx = idx * 2
            right_idx = idx * 2 + 1
            if left_idx < len(node_list):
                n.left = node_list[left_idx]
            if right_idx < len(node_list):
                n.right = node_list[right_idx]
            
        self.head = node_list[1]
    
    def __traversal(self, node, order, level=0):
        left = node.left
        right = node.right

        if order == 'pre':
            print('*' * level, node.value)

        if left is not None:
            self.__traversal(left, order, level + 1)
        
        if order == 'in':
            print('*' * level, node.value)
        
        if right is not None:
            self.__traversal(right, order, level + 1)
        
        if order == 'post':
            print('*' * level, node.value)
    
    def preorder(self):
        self.__traversal(self.head, 'pre')

    def inorder(self):
        self.__traversal(self.head, 'in')

    def postorder(self):
        self.__traversal(self.head, 'post')
    
    def bfs_in(self, value):
        to_check = deque([self.head])
        while to_check:
            node = to_check.pop()
            if node.value == value:
                return True
            else:
                left = node.left
                right = node.right
                if left is not None:
                    to_check.appendleft(left)
                if right is not None:
                    to_check.appendleft(right)
        else:
            return False

    def dfs_in(self, value):
        to_check = deque([self.head])
        while to_check:
            node = to_check.pop()
            if node.value == value:
                return True
            else:
                left = node.left
                right = node.right
                if right is not None:
                    to_check.append(right)
                if left is not None:
                    to_check.append(left)
        else:
            return False


a = BTree([i for i in range(1, 10)])
a.inorder()
print(a.bfs_in(8))