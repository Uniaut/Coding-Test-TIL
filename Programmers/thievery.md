# 도둑질
[Link](https://programmers.co.kr/learn/courses/30/lessons/42897)

## 풀이 과정
* 원형으로 되어있으므로 마지막 것을 포함하는 경우 vs 처음 것을 포함하는 경우를 분리하여 계산해야 함
* 단순히 동적 계획법으로 풀 수 있는 문제인듯 함
* 나는 case 2개를 따로 돌리는 방식을 택함. 한번에 돌리는것 보다 직관적인듯

## 피드백
* 굉장히 더러운 코드가 되었는데 배열을 좀 효율적으로 썼다면 좋지 않았을까.

## 정답 코드
```python
def solution(money):
    arr1 = [None] * len(money)
    arr2 = [None] * len(money)
    
    arr1[0] = money[0]
    arr1[1] = money[0]
    arr2[0] = 0
    arr2[1] = money[1]
    for idx in range(2, len(arr1) - 1):
        arr1[idx] = max(arr1[idx - 1], arr1[idx - 2] + money[idx])
    for idx in range(2, len(arr1)):
        arr2[idx] = max(arr2[idx - 1], arr2[idx - 2] + money[idx])
    value1, value2 = arr1[-2], arr2[-1]
    return max(value1, value2)
```
