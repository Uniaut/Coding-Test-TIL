import heapq
import itertools

class Graph:
    def __init__(self, n):
        self.n = n
        self.table = [[None]*i for i in range(n)]

    @staticmethod
    def align_index(a, b):
        if a < b:
            return (b, a)
        else:
            return (a, b)

    def __getitem__(self, key):
        a, b = Graph.align_index(*key)
        if a == b:
            return 0
        else:
            item = self.table[a][b]
            return item

    def __setitem__(self, key, value):
        a, b = Graph.align_index(*key)
        if a == b or a < 0 or self.n < a or b < 0 or self.n < b:
            raise IndexError(str((a, b)) + ' is out of index')
        else:
            self.table[a][b] = value


def find_root(root_list, node):
    if root_list[node] == node:
        return node
    else:
        result = find_root(root_list, root_list[node])
        root_list[node] = result
        return result


def prim(g: Graph) -> Graph:
    edge_to_check = []
    for i in range(g.n):
        heapq.heappush(edge_to_check, (g[0, i], (0, i)))
    
    new_g = Graph(g.n)
    connected = [False] * g.n
    connected[0] = True
    while not all(connected):
        value, edge = heapq.heappop(edge_to_check)
        print(value, edge)
        i, j = edge
        if connected[j]:
            pass
        else:
            connected[j] = True, True
            new_g[i, j] = value
            for k in range(g.n):
                heapq.heappush(edge_to_check, (g[j, k], (j, k)))
        
    return new_g

graph = Graph(20)
for i in range(20):
    for j in range(i):
        graph[i, j] = (i - (j * 2)) ** 2 + 1

print('\n'.join([str(each) for each in prim(graph).table]))