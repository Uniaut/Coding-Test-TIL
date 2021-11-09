# BOARDCOVER
[Link](https://www.algospot.com/judge/problem/read/BOARDCOVER)

## 피드백
* 입출력 예제를 똑바로 확인하자.
* 주어진 예제가 제대로 풀리지 않을 때엔 더 쉬운 test case를 따라가며 오류를 찾아보자.

## 정답 코드
```python
read_line = lambda: list(map(int, input().strip().split(' ')))

cover_presets = [
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (1, 0)],
    [(0, 0), (1, 0), (1, -1)]
]

def count_cover(board):
    
    height, width = len(board), len(board[0])
    if not (True in [True in line for line in board]):
        return 1
    
    count = 0
    pos_height, pos_width = 0, 0
    for pos in range(0, (height - 1) * width):
        pos_height, pos_width = pos // width, pos % width
        if board[pos_height][pos_width]:
            break
        
    # case 0~2
    flag = True
    if pos_width == width - 1:
        flag = False
    if flag:
        for cover_preset in cover_presets[:3]:
            flag = True
            for cover_pad in cover_preset:
                if not board[pos_height + cover_pad[0]][pos_width + cover_pad[1]]:
                    flag = False
                    break
            if flag:
                new_board = [[ele for ele in line] for line in board]
                for cover_pad in cover_preset:
                    new_board[pos_height + cover_pad[0]][pos_width + cover_pad[1]] = False
                count += count_cover(new_board)
    # case 3
    cover_preset = cover_presets[3]
    flag = True
    if pos_width == 0:
        flag = False
    if flag:
        for cover_pad in cover_preset[1:]:
            if not board[pos_height + cover_pad[0]][pos_width + cover_pad[1]]:
                flag = False
                break
    if flag:
        new_board = [[ele for ele in line] for line in board]
        for cover_pad in cover_preset:
            new_board[pos_height + cover_pad[0]][pos_width + cover_pad[1]] = False
        count += count_cover(new_board)

    return count

n_case = read_line()[0]
for _ in range(n_case):
    temp = read_line()
    height, width= temp[0], temp[1]
    base_board = [[False for __ in range(width)] for _ in range(height)]
    for o_height in range(height):
        temp = list(input().strip())
        base_board[o_height] = [token == '.' for token in temp]
    
    print(count_cover(base_board))

```
