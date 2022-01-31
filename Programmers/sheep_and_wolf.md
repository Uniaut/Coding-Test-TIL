# 양과 늑대
문제 출처: KAKAO BLIND 2022 1차 5번

[Link](https://programmers.co.kr/learn/courses/30/lessons/92343)

## 풀이 과정
* binary tree 구현 및 dfs를 이용한 노드 방문 순서 탐색
* 노드의 최대 갯수: 17개, 최악의 경우 방문 경우의 수는 (8!)^2이므로 dp + 비트마스킹 해야 풀리지만 프로그래머스는 제한시간이 널널해서 풀린듯.

## 피드백
* dp + 비트마스킹을 적용한 풀이는 시간나면 시도해보자.

## 정답 코드
```python
def best(sheep, wolf, tree, tree_size, nodes):
    if sheep <= wolf:
        return -1
    
    best_case = sheep
    for node in filter(lambda i: nodes[i], range(tree_size)):
        next_sheep, next_wolf = sheep, wolf
        if tree[node][0] == 0:
            next_sheep += 1
        else:
            next_wolf += 1
        
        next_nodes = [n for n in nodes]
        next_nodes[node] = False
        for child in tree[node][1:]:
            if child != -1:
                next_nodes[child] = True
        best_case = max(best_case, best(next_sheep, next_wolf, tree, tree_size, next_nodes))

    return best_case

def solution(info, edges):
    tree_size = len(info)
    tree = [[0, -1, -1] for _ in range(tree_size)]
    for idx, i in enumerate(info):
        tree[idx][0] = i
    
    for e in edges:
        parent, child = e
        if tree[parent][1] == -1:
            tree[parent][1] = child
        else:
            tree[parent][2] = child
        
    nodes = [False] * tree_size
    for child in tree[0][1:]:
        if child != -1:
            nodes[child] = True
    return best(1, 0, tree, tree_size, nodes)
```
