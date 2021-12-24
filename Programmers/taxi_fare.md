# 합승 택시 요금
2021 KAKAO BLIND RECRUITMENT 4번 문제 [[Link]](https://programmers.co.kr/learn/courses/30/lessons/72413)

## 풀이 과정
* 합승 요금은 적절한 vertex가 주어졌을 때, fare[start ~ vertex] + fare[vertex ~ a] + fare[vertex ~ b]이다
* start, a, b에 대해 각각 최단거리를 계산하는 dijkstra 알고리즘을 적용할 수 있음
* node 200개면 floyd-warshall 써도 되지 않나... 왜 시간초과가 나왔을까

## 피드백
* floyd-warshall과 djikstra 알고리즘을 다시 복습하자.

## 정답 코드
```python
class Graph:
    def __init__(self, n):
        self.n_vertex = n
        self.table = [[10000000] * i for i in range(n)]

    def __getitem__(self, key):
        a, b = key
        if a < b:
            a, b = b, a
        
        if a == b:
            return 0
        else:
            return self.table[a][b]
    
    def __setitem__(self, key, value):
        a, b = key
        if a < b:
            a, b = b, a
        
        if a == b:
            pass
        else:
            self.table[a][b] = value
    
    def update(self, vertices):
        for start in vertices:
            visited = [False] * self.n_vertex
            for _ in range(self.n_vertex):
                to_visit = [i for i in range(self.n_vertex) if not visited[i]]
                mid = min(to_visit, key=lambda i: self[start, i])
                visited[mid] = True
                for end in range(self.n_vertex):
                    if self[start, mid] + self[mid, end] < self[start, end]:
                        self[start, end] = self[start, mid] + self[mid, end]



def solution(n, s, a, b, fares):
    g = Graph(n)
    s -= 1
    a -= 1
    b -= 1
    for each in fares:
        vertex1, vertex2, cost = each
        vertex1 -= 1
        vertex2 -= 1
        g[vertex1, vertex2] = cost

    g.update((s, a, b))

    return min(g[s, mid] + g[mid, a] + g[mid, b] for mid in range(n))

```
