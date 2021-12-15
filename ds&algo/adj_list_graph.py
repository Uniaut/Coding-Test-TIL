from collections import deque


class Vertex:
    '''
    vertex data using adjacency list
    '''
    def __init__(self, value, adj_list=None):
        self.value = value
        if adj_list is None:
            adj_list = []
        else:
            self.adj_list = adj_list


class Graph:   
    def __init__(self, vertices=None):
        if vertices is None:
            self.vertices = []
        else:
            self.vertices = vertices

    def insert(self, value, adj_list=None):
        self.vertices.append(Vertex(value, adj_list))
        for adj_vertex in adj_list:
            self.vertices[adj_vertex].adj_list.append(value)


    def dfs(self):
        check_order = []
        checked = [False] * len(self.vertices)
        to_check = deque([0])
        while to_check:
            v = to_check.pop()
            if checked[v]:
                continue
            else:
                checked[v] = True
                check_order.append(self.vertices[v].value)
                for next_v in self.vertices[v].adj_list:
                    to_check.append(next_v)
        else:
            return check_order

    def bfs(self):
        check_order = []
        checked = [False] * len(self.vertices)
        to_check = deque([0])
        while to_check:
            v = to_check.pop()
            if checked[v]:
                continue
            else:
                checked[v] = True
                check_order.append(self.vertices[v].value)
                for next_v in self.vertices[v].adj_list:
                    to_check.appendleft(next_v)
        else:
            return check_order

graph = Graph()
graph.insert(0, [])
graph.insert(1, [0])
graph.insert(2, [1])
graph.insert(3, [2])
graph.insert(4, [0, 2, 3])
print(graph.dfs())
print(graph.bfs())
