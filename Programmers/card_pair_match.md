# 광고 삽입
2021 KAKAO BLIND RECRUITMENT 6번 문제 [[Link]](https://programmers.co.kr/learn/courses/30/lessons/72415)

## 풀이 과정
* BFS의 경우 가능한 조작의 수를 따라가다 보면 `9^32`개를 탐색해야 함
* A* 알고리즘으로 경우의 수를 충분히 줄일 수 있음
  * heuristic value = 이미 조작한 횟수 + 남은 카드 수 * 2 - 3
* 이렇게만 하면 다른 조작, 같은 결과인 가짓수가 너무 많아짐
* status와 조작한 횟수가 같은 경우엔 우선순위 큐에 넣지 않고, 이미 있는 녀석이 heap에서 나오길 기다림
* class에 넣었으니까 같은 녀석인지 판단을 위해 eq와 hash 정의

## 피드백
* BFS만 써도 충분했을 것 같음. 단순히 방문한 상태인지 점검할 필요가 있었던 것 같다.
* 단순히 게임을 구현하는 것이 제일 어려웠던 문제.... 너무 복잡하게 생각한 것 같다.

## 정답 코드
```python
import heapq


class Status:
    def __init__(self, board, cursor_r, cursor_c, selected, n_action):
        board = tuple(tuple(l) for l in board)
        self.board = board
        self.cursor_r = cursor_r
        self.cursor_c = cursor_c
        self.selected = selected
        self.n_action = n_action

        self.heuristic_value = None
        self.heuristic()

    def heuristic(self):
        if self.heuristic_value is None:
            count = 0
            for l in self.board:
                for i in l:
                    if i:
                        count += 1
            
            self.heuristic_value = self.n_action + (count) * 2 - 3
        
        return self.heuristic_value
    
    def __eq__(self, __o) -> bool:
        return all([(self.board == __o.board),
            (self.cursor_c == __o.cursor_c),
            (self.cursor_r == __o.cursor_r),
            (self.selected == __o.selected),
            (self.n_action == __o.n_action)
        ])
    
    def __hash__(self) -> int:
        return hash((self.board, self.cursor_r, self.cursor_c, self.n_action, self.selected))


    def __call__(self):
        return self.heuristic(), self.n_action
    
    def l(self):
        if self.cursor_c > 0:
            new_cursor_c = self.cursor_c - 1
        else:
            new_cursor_c = 0
        
        return Status(self.board, self.cursor_r, new_cursor_c, self.selected, self.n_action + 1)
    
    def r(self):
        if self.cursor_c < 3:
            new_cursor_c = self.cursor_c + 1
        else:
            new_cursor_c = 3
        
        return Status(self.board, self.cursor_r, new_cursor_c, self.selected, self.n_action + 1)
    
    def u(self):
        if self.cursor_r > 0:
            new_cursor_r = self.cursor_r - 1
        else:
            new_cursor_r = 0
        
        return Status(self.board, new_cursor_r, self.cursor_c, self.selected, self.n_action + 1)
    
    def d(self):
        if self.cursor_r < 3:
            new_cursor_r = self.cursor_r + 1
        else:
            new_cursor_r = 3

        return Status(self.board, new_cursor_r, self.cursor_c, self.selected, self.n_action + 1)


    def cl(self):
        new_cursor_c = self.cursor_c
        while new_cursor_c > 0:
            new_cursor_c -= 1
            if self.board[self.cursor_r][new_cursor_c]:
                break
        
        return Status(self.board, self.cursor_r, new_cursor_c, self.selected, self.n_action + 1)
    
    def cr(self):
        new_cursor_c = self.cursor_c
        while new_cursor_c < 3:
            new_cursor_c += 1
            if self.board[self.cursor_r][new_cursor_c]:
                break
        
        return Status(self.board, self.cursor_r, new_cursor_c, self.selected, self.n_action + 1)
    
    def cu(self):
        new_cursor_r = self.cursor_r
        while new_cursor_r > 0:
            new_cursor_r -= 1
            if self.board[new_cursor_r][self.cursor_c]:
                break
        
        return Status(self.board, new_cursor_r, self.cursor_c, self.selected, self.n_action + 1)
    
    def cd(self):
        new_cursor_r = self.cursor_r
        while new_cursor_r < 3:
            new_cursor_r += 1
            if self.board[new_cursor_r][self.cursor_c]:
                break
        
        return Status(self.board, new_cursor_r, self.cursor_c, self.selected, self.n_action + 1)

    def en(self):
        if self.board[self.cursor_r][self.cursor_c]:
            if self.selected is None:
                new_selected = (self.cursor_r, self.cursor_c)
                new_status = Status(self.board, self.cursor_r, self.cursor_c, new_selected, self.n_action + 1)
            elif self.selected == (self.cursor_r, self.cursor_c):
                new_status = Status(self.board, self.cursor_r, self.cursor_c, None, self.n_action + 1)
            else:
                selected_r, selected_c = self.selected
                if self.board[selected_r][selected_c] == self.board[self.cursor_r][self.cursor_c]:
                    new_board = [[i for i in r] for r in self.board]
                    new_board[selected_r][selected_c] = 0
                    new_board[self.cursor_r][self.cursor_c] = 0
                    
                    new_status = Status(new_board, self.cursor_r, self.cursor_c, None, self.n_action + 1)
                else:
                    new_status = Status(self.board, self.cursor_r, self.cursor_c, None, self.n_action + 1)
        else:
            new_status = Status(self.board, self.cursor_r, self.cursor_c, self.selected, self.n_action + 1)

        return new_status


def solution(board, r, c):
    zero_status = Status(board, r, c, None, 0)
    v_heap = []
    st_set = set()
    heapq.heappush(v_heap, (zero_status(), id(zero_status), zero_status))
    while True:
        _, __, st = heapq.heappop(v_heap)
        if len(v_heap) % 10000 == 0:
            print(len(v_heap), st.board, st.cursor_r, st.cursor_c, st.selected, st())
        if not any([any(each) for each in st.board]):
            return st.n_action
        
        for action in ['l', 'r', 'u', 'd', 'cl', 'cr', 'cu', 'cd', 'en']:
            new_st = getattr(st, action)()
            if new_st in st_set:
                pass
            else:
                st_set.add(new_st)
                heapq.heappush(v_heap, (new_st(), id(new_st), new_st))

```
