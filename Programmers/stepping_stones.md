# 징검다리
[Link](https://programmers.co.kr/learn/courses/30/lessons/43236)

## 바람직한 풀이 과정(이분탐색 문제인 것을 모른다는 전제 하에)
* naive하게 모든 케이스를 고려한다면 O(N^N).... (이유: n_C_n/2)
* 처음 생각했던 접근: 당장 제일 작은 간격을 합치는 방식으로 하자!
  * 문제점: 같은 간격이 여러개라면 무엇부터 합쳐야 할지, 어떤 방향으로 합쳐야 할지 계산하기 힘들다 => 최종적으로 정답이 아닐 확률이 높음
* answer는 0 <= x < distance + 1 인데, 이분탐색을 사용할 수 있을까?
  * distance가 1,000,000,000이라면 충분히 가능함( 50,000 * log dist = 5 * 10^3)
* mid를 기준으로 n이 충분하다면 mid <= answer < end
* 부족하다면 start <= answer < mid
  * 이렇게 두면 목표 간격을 위한 최소 삭제 돌의 수가 n으로 딱 맞아떨어지는 경우가 아니어도 cover 가능

## 피드백
* 이분탐색이 아닌 해결에 삘이 꽂혀서 힘을 너무 뺀 것 같다. 효율적인 공부는 아니었다 싶음

## 정답 코드
```python
def solution(distance, rocks, n):
    rocks.sort()

    dist_s, dist_e = 0, distance + 1
    # assert: start <= answer < end
    while dist_e - dist_s > 1:
        dist_mid = (dist_s + dist_e) // 2

        # compute least n
        r_to_remove = 0
        start_pos = 0
        for pos in rocks:
            if pos - start_pos < dist_mid:
                r_to_remove += 1
            else:
                start_pos = pos
        else:
            if distance - start_pos < dist_mid:
                r_to_remove += 1

        # next search
        if r_to_remove > n:
            dist_s, dist_e = dist_s, dist_mid
        else:
            result = dist_mid
            dist_s, dist_e = dist_mid, dist_e

    return result
```
