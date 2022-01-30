# 양궁대회
**문제 출처: KAKAO BLIND 2022 1차 4번**

[Link](https://programmers.co.kr/learn/courses/30/lessons/92342)

## 풀이 과정
* 특정 점수를 얻기 위한 화살의 수는 O(1)시간 내에 쉽게 구할 수 있다.
* 얻을 수 있는 점수의 조합은 1024개(2^10)이고, 다음의 조건으로 최선의 조합인지 여부를 판정할 수 있다
  1. 점수격차가 최고인지
  2. 점수격차가 같다면 0점에 더 많이 쏘았는지 
  3. 앞이 같다면 1점에 더 많이 쏘았는지
  4. ...

## 피드백
* 비트마스킹이 큰 의미가 없어보이는데, 그냥 itertools.product를 쓰는 쪽이 읽기 좋은 코드였을 것 같다.

## 정답 코드
```python
def case(goal, info, n):    
    delta_score = 0
    result = [0] * 11
    for i in range(10):
        if goal[i]:
            result[i] = info[i] + 1
            n -= result[i]
            delta_score += (10 - i)
        elif info[i] > 0:
            delta_score -= (10 - i)
    else:
        result[10] = n
    return delta_score, n, result

def solution(n, info):
    best = (0, [0] * 11)
    for i in range(1 << 10):
        goal = [1 if i & (1 << bit_idx) else 0 for bit_idx in range(10)]
        delta_score, left_arrow, result = case(goal, info, n)
        if left_arrow >= 0 and delta_score >= best[0]:
            best_result = best[1]
            if delta_score > best[0]:
                best = (delta_score, result)
            elif tuple(reversed(best_result)) < tuple(reversed(result)):
                best = (delta_score, result)
    if best[0] == 0:
        return [-1]
    else:
        return best[1]
```
