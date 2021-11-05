# BOGGLE
[Link](https://www.algospot.com/judge/problem/read/BOGGLE)

## 나의 오답 유형
### 시간초과
* Dynamic Programming 기법이 거의 강제됨(시간 초과로 인해)
* 시간초과가 날 법한 알고리즘 인지 짐작해보는 능력 필요

### python상 list 구조에 대한 몰이해
```python
impossible_data = []
temp = []
for _ in range(5):
    temp.append([])
for _ in range(5):
    impossible_data.append(temp) # 이렇게 append 된 temp끼리는 서로 동기화되어 생각대로 동작하지 않는다.
```

## 정답 코드
```python
import copy


impossible_data = []
for _ in range(5): 
    temp = []
    for _ in range(5):
        temp.append([])
    impossible_data.append(temp)
def _hasWord(board, word, ln, col):
    if word == '':
        return True

    if len(word) in impossible_data[ln][col]:
        return False

    pads = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for pad in pads:
        new_ln = ln + pad[0]
        new_col = col + pad[1]
        if (new_ln < 0) or (new_ln > 4) or (new_col < 0) or (new_col > 4):
            continue
        if board[new_ln][new_col] == word[0]:
            if _hasWord(board, word[1:], new_ln, new_col):
                return True

    impossible_data[ln][col].append(len(word))
    return False
def hasWord(board, word):
    for ln in range(5):
        for col in range(5):
            if board[ln][col] == word[0]:
                if _hasWord(board, word[1:], ln, col):
                    return True
    return False
if __name__ == '__main__':
    n_case = int(input())
    for _ in range(n_case):
        board = []
        for __ in range(5):
            str_input = input()
            board_subline = []
            for ele in str_input:
                board_subline.append(ele)
            board.append(board_subline)

        n_words = int(input())
        for __ in range(n_words):
            word = input()

            for ele_1 in impossible_data:
                for ele_2 in ele_1:
                    ele_2.clear()

            result = 'YES' if hasWord(board, word) else 'NO'

            print(word + ' ' + result)
```
