# CLOCKSYNC
[Link](https://www.algospot.com/judge/problem/read/CLOCKSYNC)

## 실마리
* 스위치 갯수는 10개이고 상태는 4개이므로 4^10 = 1024^2, 대략 1,000,000 = 10^6개의 경우의 수가 있다.
* bruteforce로 직접 풀어보면 시간초과가 나옴. (test case가 최대 30개 -> 10^8까지는 여유롭지 않다는 뜻)
* 스위치별 시계 데이터를 시계별 스위치 데이터로 바꾼 후 스위치 순서를 강제함. 강제하지 않은 버전이 강제한 버전보다 스위치를 적게 누를 가능성은 없음.

## 피드백
* 코드가 길어지면 지치는 경향이 있음 -> 간단하게라도 주석을 달아서 뇌가 과부하되지 않도록 하자.
* 근데 책에서는 bruteforce로 푸네;; 내가 과하게 비효율적으로 짜나보다.
* 느리지만 빨리 짜지고 유효한 코드가 있는지 생각해보자.
* 빠르게 짤 수 있는데 멀리 돌아가는 구문이 있는지 생각해보자. (굳이 함수화 할 필요 없는걸 함수로 만들거나, 등등)

## 정답 코드
```python
read_line = lambda: [int(e) for e in input().strip().split(' ')]

clock_by_switch_data = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]
]
switch_by_clock_data = [[] for _ in range(16)]
switch_order = []
next_status = lambda i: i % 12 + 3


if __name__ == '__main__':
    for index_clock, each_clock in enumerate(switch_by_clock_data):
        for index_switch, each_switch in enumerate(clock_by_switch_data):
            if index_clock in each_switch:
                each_clock.append(index_switch)
    # print(switch_by_clock_data)

    temp_data = [[each for each in each_list] for each_list in switch_by_clock_data]
    while True in [len(each_list) > 0 for each_list in temp_data]:
        for index_clock, each_clock in enumerate(temp_data):
            if len(each_clock) == 1:
                num_switch = each_clock[0]
                switch_order.append((num_switch, index_clock))
                temp_data = [[each for each in each_list if each != num_switch] for each_list in temp_data]
                break
        # print(switch_order)

    num_case = read_line()[0]
    for _ in range(num_case):
        count = 0
        board = read_line()
        for n_switch, n_clock in switch_order:
            while board[n_clock] != 12:
                # press switch
                count += 1
                clock_list = clock_by_switch_data[n_switch]
                board = [next_status(status) if i_clock in clock_list else status for i_clock, status in enumerate(board)]
        if True in [status != 12 for status in board]:
            count = -1
        print(count)

```
