# 광고 삽입
2021 KAKAO BLIND RECRUITMENT 5번 문제 [Link](https://programmers.co.kr/learn/courses/30/lessons/72414)

## 풀이 과정
* 총 시청시간 수를 계산할 때, logs를 있는 그대로 활용한다면? => ```O(N^2) => 10^10```
  * logs를 i ~ i + 1 에 해당하는 시청자 수로 변형한다면? => T가 play_time일 때, ```O(T) = 3600 * 100```
    * 변형하는데 걸리는 시간은 => `O(T * n_logs) = 36 * 10^4 * 10^5` 는 좀 그러네
    * logs를 정렬한 다음 구간별 시청시간 수로 1차 변형, 이를 초단위 구간으로 변형하면 `O(N log N + T)` 시간에 변형 가능

## 피드백
* 초단위 구간 시간으로 변형하는 아이디어를 떠올리기가 힘들었다. 앞으로 계속해서 참고 가능한 아이디어일듯.
* 1차 변형은 다른 문제에서도 쓰일 수 있는 아이디어이므로 반드시 고려하자.

## 정답 코드
```python
def str2sec(_s: str):
    h, m, s = map(int, _s.split(':'))
    return h * 3600 + m * 60 + s


def log2tuple(_s: str):
    start, end = map(str2sec, _s.split('-'))
    return start, end


def sec2str(_s: int):
    h, m, s = _s // 3600, (_s // 60) % 60, _s % 60
    return f'{h:02d}:{m:02d}:{s:02d}'


def solution(play_time, adv_time, logs):
    '''
    for all splitted range, calculate n of user watching video
    '''
    play_time = str2sec(play_time)
    adv_time = str2sec(adv_time)

    logs = map(log2tuple, logs)
    start_logs, end_logs = [], []
    for start, end in logs:
        start_logs.append((start, 1))
        end_logs.append((end, -1))
    
    temp = sorted(start_logs + end_logs) + [(play_time, 0)]
    
    print(temp)

    temp2 = []
    prev_time = -1
    for timestamp, delta_count in temp:
        if prev_time != timestamp:
            temp2.append((timestamp, delta_count))
            prev_time = timestamp
        else:
            prev_time, prev_count = temp2[-1]
            temp2[-1] = (prev_time, prev_count + delta_count)


    print(temp2)

    mod_logs = []
    total_count = 0
    prev_time = 0
    for time, delta_count in temp2:
        mod_logs.append((prev_time, time - prev_time , total_count))
        total_count += delta_count
        prev_time = time

    print(mod_logs)
    
    sec_count = [0] * (str2sec("99:59:59") + 1)
    for time, length, count in mod_logs:
        for i in range(time, time + length):
            sec_count[i] = count
    
    print(sec_count[2395:2405])

    now_time = 0
    now_value = sum(sec_count[0:adv_time])
    best_time, best_value = now_time, now_value
    while True:
        if now_value > best_value:
            best_time = now_time
            best_value = now_value
        
        if now_time + adv_time == play_time:
            break

        now_value -= sec_count[now_time]
        now_value += sec_count[now_time + adv_time]
        now_time += 1

    result = best_time
    return sec2str(result)

```
