# 파괴되지 않은 건물
**문제 출처: KAKAO BLIND 2022 1차 6번**

[Link](https://programmers.co.kr/learn/courses/30/lessons/92344)

## 풀이 과정
* 누적합을 2차원으로 확장할 수 있는지를 묻는 문제이다.
* `(r1, c1), (r1, c2), (r2, c1), (r2, c2)`에 각각 `deg, -deg, -deg, deg`를 넣으면 row, column 순서에 상관 없이 풀어 낼 수 있다.

## 피드백
* 누적합 문제인건 어렴풋이 느꼈지만 도저히 2차원으로 확장할 생각을 못함. 누적합에 대한 개념이 정립이 안되어서 그런 것 같다.
  * 배웠으면 알차게 써먹을 수 있겠다는 마인드 *^^*


## 정답 코드
```python
def solution(board, skill):
    row_size, col_size = len(board), len(board[0])
    delta_board = [[0] * (col_size + 1) for _ in range(row_size + 1)]
    for s in skill:
        type_skill, r1, c1, r2, c2, degree = s
        if type_skill == 1:
            degree *= -1
        r2 += 1
        c2 += 1
        
        delta_board[r1][c1] += degree
        delta_board[r2][c1] += -degree
        delta_board[r1][c2] += -degree
        delta_board[r2][c2] += degree
    
    for row_idx in range(row_size + 1):
        now_value = 0
        for col_idx in range(col_size + 1):
            now_value += delta_board[row_idx][col_idx]
            delta_board[row_idx][col_idx] = now_value
    for col_idx in range(col_size + 1):
        now_value = 0
        for row_idx in range(row_size + 1):
            now_value += delta_board[row_idx][col_idx]
            delta_board[row_idx][col_idx] = now_value
    
    answer = 0
    for row_idx in range(row_size):
        for col_idx in range(col_size):
            if board[row_idx][col_idx] + delta_board[row_idx][col_idx] > 0:
                answer += 1

    return answer
```
