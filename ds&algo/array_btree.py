import array

class BTree:
    '''
    TODO:
    __init__()
    preorder()
    inorder()
    postorder()
    bfs()
    dfs()
    '''
    @staticmethod
    def left(n):
        return (n + 1) * 2 - 1

    @staticmethod
    def right(n):
        return (n + 1) * 2
    
    @staticmethod
    def up(n):
        return (n + 1) // 2 - 1

    def __init__(self, value):
        self.data = array.array('l', value)
        self.length = len(value)
    
    def __traversal(self, idx, order):
        if idx >= self.length:
            return
        
        if order == 'pre':
            print(self.data[idx])
            self.__traversal(BTree.left(idx), order)
            self.__traversal(BTree.right(idx), order)
        elif order == 'in':
            self.__traversal(BTree.left(idx), order)
            print(self.data[idx])
            self.__traversal(BTree.right(idx), order)
        elif order == 'post':
            self.__traversal(BTree.left(idx), order)
            self.__traversal(BTree.right(idx), order)
            print(self.data[idx])
        else:
            raise Exception('invalid order data')

    def preorder(self):
        self.__traversal(0, 'pre')

    def inorder(self):
        self.__traversal(0, 'in')

    def postorder(self):
        self.__traversal(0, 'post')

    def bfs(self, value):
        for idx in range(self.length):
            if self.data[idx] == value:
                return idx
        else:
            return None

    def dfs(self, value):
        to_check = [0]
        while to_check:
            idx = to_check.pop()
            if idx >= self.length:
                continue
            elif self.data[idx] == value:
                return idx
            else:
                to_check.append(BTree.left(idx))
                to_check.append(BTree.right(idx))
        else:
            return None

t = BTree([i*2 for i in range(10)])
print(t.dfs(8))
t.preorder()