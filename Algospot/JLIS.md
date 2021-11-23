# JLIS
[Link](https://www.algospot.com/judge/problem/read/JLIS)

## 사족
* 이번에도 파이썬이라 당했다... 4일간 이것만 매달렸어...
* 테스트 예제들도 모두 통과했고 시간복잡도는 같은 관계로 정답 되기는 포기.
## 시간초과 코드
```python
read_line = lambda: [int(t) for t in input().split() if t]

def solve(seq1, seq2, l_s1, l_s2):
    data = [[None for __ in range(l_s2 + 1)] for _ in range(l_s1 + 1)]
    data[0][0] = 0

    # sole seq lis
    for idx_1 in range(l_s1):
        data[idx_1 + 1][0] = max([0] + [data[i + 1][0] for i in range(idx_1) if seq1[i] < seq1[idx_1]]) + 1
    for idx_2 in range(l_s2):
        data[0][idx_2 + 1] = max([0] + [data[0][i + 1] for i in range(idx_2) if seq2[i] < seq2[idx_2]]) + 1

    for idx_1 in range(l_s1):
        for idx_2 in range(l_s2):

            now_1 = seq1[idx_1]
            now_2 = seq2[idx_2]
            
            # condition of max: smaller then now seq, not same with other now
            condition_1 = [0] + [i + 1 for i, n in enumerate(seq1[:idx_1]) if n < now_1 and n != now_2]
            condition_2 = [0] + [i + 1 for i, n in enumerate(seq2[:idx_2]) if n < now_2 and n != now_1]
            temp = 0
            

            for _idx_1 in condition_1:
                for _idx_2 in condition_2:
                    temp = max(data[_idx_1][_idx_2], temp)
            
            data[idx_1 + 1][idx_2 + 1] = temp + (1 if seq1[idx_1] == seq2[idx_2] else 2)
    
    return max((max(each) for each in data))


if __name__ == '__main__':
    n_case = int(input())
    for _ in range(n_case):
        L = read_line()[:2]
        S1 = read_line()[:L[0]]
        S2 = read_line()[:L[1]]
        print(solve(S1, S2, L[0], L[1]))
```
