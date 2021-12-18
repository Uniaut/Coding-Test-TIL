from itertools import combinations, product

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
        if a == b:
            pass
        elif a < 0 or self.n < a or b < 0 or self.n < b:
            raise Exception(str((a, b)) + ' is out of index')
        else:
            self.table[a][b] = value


def f_w(g: Graph) -> Graph:
    new_g = Graph(g.n)
    for start, end in combinations(range(g.n), r=2):
        new_g[start, end] = g[start, end]

    for mid, start, end in product(range(g.n), repeat=3):
        if new_g[start, end] > new_g[start, mid] + new_g[mid, end]:
            min_dist = new_g[start, mid] + new_g[mid, end]
        else:
            min_dist = new_g[start, end]
        new_g[start, end] = min_dist

    return new_g

graph = Graph(20)
for i in range(20):
    for j in range(i):
        graph[i, j] = (i - (j * 2)) ** 2 + 1

print('\n'.join([str(each) for each in graph.table]))
print('\n'.join([str(each) for each in f_w(graph).table]))