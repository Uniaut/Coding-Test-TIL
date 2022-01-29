# 주차 요금 계산
문제 출처: KAKAO BLIND 2022 1차 3번

[Link](https://programmers.co.kr/learn/courses/30/lessons/92341)

## 풀이 과정
* 시간순으로 records가 주어지니까 그냥 자동차 status 등록하고, 마감 시간에 정산해서 결과 출력

## 피드백
* 자동차 종류가 10000면 dict로 안해도 될 것 같은데? list로 했다면 더 편했을듯

## 정답 코드
```python
import math

def time_str2min(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def solution(fees, records):
    dt, df, at, af = fees
    status = dict()
    for r in records:
        '''
        preprocessing
        '''
        time_str, car_id, io_status = r.split(' ')
        time_min = time_str2min(time_str)
        car_id = int(car_id)

        # (total_used, status, option:start time)
        if io_status == 'IN':
            total_used, _ = status.setdefault(car_id, (0, -1))
            status[car_id] = (total_used, time_min)
        else:
            total_used, start_time = status[car_id]
            status[car_id] = (total_used + (time_min - start_time), -1)

    result = []
    for item in status.items():
        car_id, v = item
        total_used, start_time = v
        if start_time != -1:
            total_used += time_str2min('23:59') - start_time
        
        result.append((car_id, total_used))

    answer = []
    result.sort()
    for r in result:
        _, used = r
        if used > dt:
            cost = df + af * math.ceil((used - dt) / at)
            answer.append(cost)
        else:
            answer.append(df)
    return answer
```
