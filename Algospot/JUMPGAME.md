# JUMPGAME
[Link](https://www.algospot.com/judge/problem/read/JUMPGAME)

## 피드백
* 전역변수 처리를 까먹지 말자
* 문제를 잘 읽고...풀자... 
  * 출력이 true / false가 아니라 YES / NO 잖아...

## 정답 코드
```python
read_line = lambda: [int(e) for e in input().strip().split(' ')]

cache = None # explored pos: True
board = None
l_b = None
def _solve(line, col):
    if board[line][col] == 0:
        return True
    elif cache[line][col]:
        return False
    else:
        n_jump = board[line][col]
        if line + n_jump < l_b:
            if _solve(line + n_jump, col):
                return True
        if col + n_jump < l_b:
            if _solve(line, col + n_jump):
                return True
        cache[line][col] = True
        return False

def solve(base_board, len_board):
    global cache, board, l_b
    cache = [[False for _ in range(len_board)] for _ in range(len_board)]
    board = base_board
    l_b = len_board
    return _solve(0, 0)

if __name__ == '__main__':
    n_case = int(input())
    for _ in range(n_case):
        len_board = int(input())
        base_board = []
        for __ in range(len_board):
            base_board.append(read_line()[:len_board])
        print('YES' if solve(base_board, len_board) else 'NO')
```
