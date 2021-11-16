# FENCE
[Link](https://www.algospot.com/judge/problem/read/FENCE)

## 실마리
* 단순히 start ~ end 의 모든 케이스를 추적한다면: O(n^2) -> 애매하다.
* 경우의 수가 겹치지 않게 모든 범위에서 분할 가능함.
* 가장 낮은 것에서 바로 다음 높은 것, 그 다음엔 다시 분할하는 식으로...

## 피드백
* 내가 만든 코드 또한 Worst case에서 O(n^2)이므로 이진분할의 형태로 문제를 다시 만드는게 낫다.
    * `worst_case = [20000 - (1 - i % 2 + i // 2) for i in range(20000))]`
* 이진분할도 비슷하다 -> 빈틈없이 채우는건 똑같기 때문에...
* 느렸던 것은 indice가 아니라 deep copy한 list가 계속해서 생겨나서 그렇다 

## 정답 코드
```python
read_int = lambda: int(input())
read_line = lambda: [int(e) for e in input().strip().split(' ')]

c_list = None
def case_list(board, board_len):
    # print(board)
    if board_len == 1:
        c_list.append(board[0])
    else:
        board_min = min(board)
        c_list.append(board_len * board_min)
        # find all other case
        start, end = 0, 0
        while end < board_len:
            if board[end] == board_min:
                if end - start > 0:
                    case_list(board[start:end], end - start)
                start = end + 1
            end += 1
        if end - start > 0:
            case_list(board[start:end], end - start)

if __name__ == '__main__':
    n_case = read_int()
    for _ in range(n_case):
        board_len = read_int()
        board = read_line()
        c_list = []
        case_list(board, board_len)
        print(max(c_list))
```
## 개선한 코드(라고는 하지만 Algospot Test case 다양성의 문제로 더 느리게 판별된다)
```python
read_int = lambda: int(input())
read_line = lambda: [int(e) for e in input().strip().split(' ')]

def bin_solve(board):
    len_board = len(board)
    board.append(-1)
    max_rect = 0
    stack = []
    stack.append((0, len_board))
    while stack:
        start, end = stack.pop()
        if end == start:
            continue
        elif end == start + 1:
            if max_rect < board[start]:
                max_rect = board[start]
        else:
            len_subboard = end - start
            border = (len_subboard >> 1) + start
            stack.append((start, border))
            stack.append((border, end))
            # print(len_subboard, start, end, border)
            # print(stack[-2:])

            # border case
            ex_start, ex_end = border - 1, border
            min_range = min(board[ex_start], board[ex_end])
            
            # prepare edge trick: edge is -1
            save_start_edge, save_end_edge = board[start - 1], board[end]
            board[start - 1], board[end] = -1, -1

            while min_range + 1:
                # extend to case-max
                while board[ex_start - 1] >= min_range:
                    ex_start -= 1
                while board[ex_end + 1] >= min_range:
                    ex_end += 1

                # comp case
                comp_rect = (ex_end - ex_start + 1) * min_range
                if max_rect < comp_rect:
                    max_rect = comp_rect
                
                #next min = bigger outside
                min_range = max(board[ex_start - 1], board[ex_end + 1])
            
            # recover before edge trick
            board[start - 1], board[end] = save_start_edge, save_end_edge

    return max_rect

if __name__ == '__main__':
    c = read_int()
    for _ in range(c):
        n = read_int()
        board = read_line()[:n]
        print(bin_solve(board))
```
