# PI
[Link](https://www.algospot.com/judge/problem/read/PI)

## 피드백
* 처음엔 (start, end)를 기준으로 하는 n by n cache를 만들었는데, 시간초과가 나서 점화식 형태로 깔끔하게 나타낼 수 있는 모습이다.
* n-dimension vector 하나로 충분함.

## 사족
* 분명 O(n) 알고리즘인데 왜 아직도 시간초과가 나는지 아직도 모르겠고... 나는 포기했고...

## 코드
```python
def condition(start: int, end: int) -> int:
    if len(set(seq[start:end])) == 1:
        return 1

    x: int = end - start
    diff: int = seq[start] - seq[start + 1]

    res1, res2 = [], []
    for i in range(1, x):
        res1_diff: int = seq[start + i] - seq[start + i + 1]

        if i < x - 1:
            res1.append(res1_diff == diff)

        if i > 1:
            res2.append(seq[start + i % 2] == seq[start + i])
    
    if all(res1):
        return 2 if diff == 1 or diff == -1 else 5

    if all(res2):
        return 4

    return 10


def n_solve(seq):
    lseq: int = len(seq)
    cache = [None] * (lseq + 1)

    for idx in (3, 4, 5):
        if idx > lseq:
            break

        cache[idx] = condition(0, idx)

    for idx in range(6, lseq + 1):
        b_start: int = max(3, idx - 5)
        b_end: int = idx - 3 + 1
        cache[idx] = min([cache[border] + condition(border, idx) for border in range(b_start, b_end)])

    return cache[lseq]


n_case: int = int(input())
for _ in range(n_case):
    seq = [int(token) for token in input().strip()]
    print(n_solve(seq))

```
