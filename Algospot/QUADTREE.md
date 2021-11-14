# QUADTREE
[Link](https://www.algospot.com/judge/problem/read/QUADTREE)

## 피드백
* 경계 사례를 꼼꼼하게 확인하자
  * 이번 경우엔...
    1. decoding 할 때 xoooo로 끝날 경우
    2. w, b로만 구성된 경우
* 처음엔 [x, o, o, o]를 기본 구성요소로 두었으나 [o], [[], [], [], []]를 모두 기본 구성요소로 둔다면 코드 개선이 가능함
## 정답 코드
```python
read_line = lambda: input().strip()

def decode(s):
    if s[0] != 'x':
        return 0, s[0]
    tree = []
    size = 0
    s_iter = enumerate(s[1:])
    for index, token in s_iter:
        # if quad is full, return tree & how much to jump string 
        if size == 4:
            return index, tree
        # fill quad
        if token == 'x':
            n_jump, ele = decode(s[index + 1:])
            tree.append(ele)
            for _ in range(n_jump):
                s_iter.__next__()
        elif token == 'w':
            tree.append('w')
        elif token == 'b':
            tree.append('b')
        else:
            assert(False)
        size += 1
    return 0, tree

def encode_with_mod(tree):
    if len(tree) == 1:
        return tree[0]
    res = 'x'
    for index in [2, 3, 0, 1]:
        if type(tree[index]) != 'str':
            res += encode_with_mod(tree[index])
        else:
            res += tree[index]
    return res

if __name__ == '__main__':
    n_case = int(input())
    for _ in range(n_case):
        index, tree = decode(read_line())
        print(encode_with_mod(tree))
        
```

## 개선한 코드
```python
read_line = lambda: input().strip()

def decode(s):
    if s[0] != 'x':
        return 0, [s[0]]
    tree = []
    size = 0
    s_iter = enumerate(s)
    s_iter.__next__()
    for index, token in s_iter:
        # if quad is full, return tree & how much to jump string 
        if size == 4:
            return index - 1, tree
        # fill quad
        n_jump, ele = decode(s[index:])
        tree.append(ele)
        for _ in range(n_jump):
            s_iter.__next__()
        size += 1
    return 0, tree

def encode_with_mod(tree):
    if len(tree) == 1:
        return tree[0]
    # else: 
    res = 'x'
    for index in [2, 3, 0, 1]:
        res += encode_with_mod(tree[index])
    return res

if __name__ == '__main__':
    n_case = int(input())
    for _ in range(n_case):
        index, tree = decode(read_line())
        print(encode_with_mod(tree))
```
