# FENCE
[Link](https://www.algospot.com/judge/problem/read/FENCE)

## 실마리
* 단순히 start ~ end 의 모든 케이스를 추적한다면: O(n^2) -> 애매하다.
* 경우의 수가 겹치지 않게 모든 범위에서 분할 가능함.
* 가장 낮은 것에서 바로 다음 높은 것, 그 다음엔 다시 분할하는 식으로...

## 피드백
* 내가 만든 코드 또한 최악의 경우 O(n^2)이므로 이진분할의 형태로 문제를 다시 만드는게 나음
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
## 개선한 코드

TODO
