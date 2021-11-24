# PI
[Link](https://www.algospot.com/judge/problem/read/PI)

## 피드백
* 처음엔 (start, end)를 기준으로 하는 n by n cache를 만들었는데, 시간초과가 나서 점화식 형태로 깔끔하게 나타낼 수 있는 모습이다.
* n-dimension vector 하나로 충분함.

## 사족
* 분명 O(n) 알고리즘인데 왜 아직도 시간초과가 나는지 아직도 모르겠고... 나는 포기했고...

## 코드
```python
def read_line():
    return [int(token) for token in input().strip()]


def n_solve(seq):
    def condition(start, end):
        x = end - start
        if len(set(seq[start:end])) == 1:
            return 1
        else:
            dif = seq[start] - seq[start + 1]
            if False not in [dif == seq[start + i] - seq[start + i + 1] for i in range(1, x - 1)]:
                if dif == 1 or dif == -1:
                    return 2
                else:
                    return 5
            elif False not in [seq[start + i % 2] == seq[start + i] for i in range(2, x)]:
                return 4
            else:
                return 10
    lseq = len(seq)
    cache = [None for _ in range(lseq + 1)] # cache[idx] = minpoint of seq[:idx]
    for idx in [3, 4, 5]:  # [:3] to [:5] -> c[3] to c[5]
        if idx > lseq:
            break
        cache[idx] = condition(0, idx)
    for idx in range(6, lseq + 1):  # [:6] to [:lseq] -> min([:3 or idx - 5] ~ [:idx - 3] + )
        b_start = max(3, idx - 5)
        b_end = idx - 3 + 1
        cache[idx] = min([cache[border] + condition(border, idx) for border in range(b_start, b_end)])

    return cache[lseq]


n_case = int(input())
for _ in range(n_case):
    seq = read_line()
    print(n_solve(seq))

```
