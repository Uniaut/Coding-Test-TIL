# TRIANGLEPATH
[Link](https://www.algospot.com/judge/problem/read/TRIANGLEPATH)

## 피드백
* 제발 디버깅용 print 지우고 제출하자^^

## 정답 코드
```python
read_line = lambda: [int(t) for t in input().split(' ') if t]

def solve(base_board, len_board):
    max_board = [[0 for _ in range(len_board)] for __ in range(len_board)]
    for idx_line in range(len_board):
        for idx_col in range(idx_line + 1):
            now = base_board[idx_line][idx_col]
            temp1 = max_board[idx_line - 1][idx_col - 1] if idx_col > 0 else 0
            temp2 = max_board[idx_line - 1][idx_col] if idx_col < idx_line else 0
            max_board[idx_line][idx_col] = now + max(temp1, temp2)
    return max(max_board[-1])


if __name__ == '__main__':
    n_case = int(input())
    for _ in range(n_case):
        len_board = int(input())
        board = []
        for __ in range(len_board):
            board.append(read_line())
        print(solve(board, len_board))

```
