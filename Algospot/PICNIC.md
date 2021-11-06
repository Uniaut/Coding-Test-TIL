# PICNIC
[Link](https://www.algospot.com/judge/problem/read/PICNIC)

## 나의 오답 유형
### 시간초과
* 그냥 비효율적인 방식에 너무 매달림
* 카운트 해야 할 대상이 친구 목록 뿐 아니라 가능한 짝의 경우의 수 등 다양함을 기억할 것.

### 런타임 에러
```python
temp = list(map(int, input().split(' ')))
```
위의 경우 마지막이 공백으로 끝나면 Runtime Error가 생김
```python
rl = lambda: list(map(int, input().strip().split(' ')))
```
strip을 이용해 해결.

## 정답 코드
```python
def total_methods(student_li, pair_li):
    if student_li == []:
        return 1
    
    sum = 0
    mate_x = student_li[0]
    for mate_y in student_li[1:]:
        if [mate_x, mate_y] in pair_li or [mate_y, mate_x] in pair_li:
            new_student_li = [i for i in student_li if (i != mate_x and i != mate_y)]
            sum += total_methods(new_student_li, pair_li)

    return sum

n_case = int(input())
rl = lambda: list(map(int, input().strip().split(' ')))
for _ in range(n_case):
    temp_input = rl()
    n_student, n_pair = temp_input[0], temp_input[1]

    if n_pair > 0:
        temp_input = rl()
        pair_li = [[temp_input[2 * i], temp_input[2 * i + 1]] for i in range(n_pair)]
        result = total_methods([i for i in range(n_student)], pair_li)
    else:
        input()
        result = 0

    print(result)
```
