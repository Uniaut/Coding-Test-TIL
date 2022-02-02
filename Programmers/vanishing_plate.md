# 사라지는 
**문제 출처: KAKAO BLIND 2022 1차 7번**

[Link](https://programmers.co.kr/learn/courses/30/lessons/92345)

## 풀이 과정
* minimax 문제의 변형으로, A와 B의 턴이 바뀔때 함수의 목적이 변함을 인식하면 풀릴 것이다.
* minimax 함수의 리턴 값은 (A의 기댓값, B의 기댓값)이고, turn이 A라면 A에게 최선인, B라면 B에게 최선인 기댓값을 리턴한다.

## 피드백
* 미니맥스 관련 문제들을 더 풀어보고, 추가로 alpha beta pruning에 대해 알아보면 좋을 것 같다.

## 정답 코드
```python
def minimax(board, aloc, bloc, turn, count):
    '''
    turn = 'A' or 'B'
    '''
    if False:
        for b in board:
            print(b)
        else:
            print('=>', aloc, bloc, turn, count)

    row_size = len(board)
    col_size = len(board[0])

    if turn == 'A':
        ar, ac = aloc
        if board[ar][ac] == 0:
            return (-100 + count, 100 - count)
        case = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_ar, new_ac = ar + dr, ac + dc
            if all((0 <= new_ar, new_ar < row_size, 0 <= new_ac, new_ac < col_size)):
                if board[new_ar][new_ac] == 1:
                    board[ar][ac] = 0
                    case.append(minimax(board, [new_ar, new_ac], bloc, 'B', count + 1)[0])
                    board[ar][ac] = 1
        if len(case) == 0:
            return (-100 + count, 100 - count)
        else:
            best = max(case)
            return (best, -best)
    else:
        br, bc = bloc
        if board[br][bc] == 0:
            return (100 - count, -100 + count)
        case = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_br, new_bc = br + dr, bc + dc
            if all((0 <= new_br, new_br < row_size, 0 <= new_bc, new_bc < col_size)):
                if board[new_br][new_bc] == 1:
                    board[br][bc] = 0
                    case.append(minimax(board, aloc, [new_br, new_bc], 'A', count + 1)[1])
                    board[br][bc] = 1
        if len(case) == 0:
            return (100 - count, -100 + count)
        else:
            best = max(case)
            return (-best, best)


def solution(board, aloc, bloc):
    answer = minimax(board, aloc, bloc, 'A', 0)
    answer = 100 - abs(answer[0])
    return answer
```
