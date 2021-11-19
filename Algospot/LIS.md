# LIS
[Link](https://www.algospot.com/judge/problem/read/LIS)

## 피드백
* 제출하기 전에 테스트 케이스를 더 만들어보면 좋을 것 같다.
* 

## 정답 코드
```python
read_line = lambda: [int(t) for t in input().split() if t]

def solve(seq, len_seq):
    data = [0 for _ in range(len_seq)]
    for i in range(len_seq, 0, -1):
        now = seq[i - 1]
        temp = [data[idx] for idx, ele in enumerate(seq) if now < ele and i - 1 < idx]
        if temp:
            data[i - 1] = max(temp) + 1
        else:
            data[i- 1] = 1
    return max(data)

if __name__ == '__main__':
    n_case = int(input())
    for _ in range(n_case):
        L = int(input())
        S = read_line()[:L]
        print(solve(S, L))
```
