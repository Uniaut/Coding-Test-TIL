# k진수에서 소수 개수 구하기
문제 출처: KAKAO BLIND 2022 1차 2번

[Link](https://programmers.co.kr/learn/courses/30/lessons/92335)

## 풀이 과정
* k진수 변환 과정과 소수 판정 알고리즘을 활용한 문제.
* k진수 변환 과정은 간단하다.
```python
def to_base_k(n, k):
    l = []
    while n > 0:
        l.append(n % k)
        n //= k
    return ''.join(map(str, reversed(l)))
```
* 소수 판정 알고리즘을 이참에 정리해보자.
### 소수 판정법
1. 단순히 sqrt(N)까지 나누며 검사하는 법.
2. 소수의 목록이 주어진다면 O(sqrt(N) / log N) 안에 풀 수 있음 -> sqrt(N_LIMIT)까지의 모든 소수를 구하고 여러개의 정수를 판정한다면 훨씬 효율적이다.
3. 다만 이 경우 판정해야 할 정수의 자릿수 합에 상한선이 있으므로 sqrt(N)쪽이 더 편하고 빠르다.

## 피드백
* 처음엔 소수 목록을 구하는 방식으로 풀었는데, 소수 목록이 생각 별로 빠르지 않다는 사실을 인지했다면 시간 절약을 많이 했을 것 같다.

## 정답 코드
```python
def is_prime(n):
    if n == 1:
        return False
    border = int(n ** 0.5)
    for i in range(2, border + 1):
        if n % i == 0:
            return False
    
    return True


def to_base_k(n, k):
    l = []
    while n > 0:
        l.append(n % k)
        n //= k
    return ''.join(map(str, reversed(l)))

def solution(n, k):
    n_base_k = to_base_k(n, k)
    case_list = [int(e) for e in n_base_k.split('0') if e != '']
    answer = 0
    for c in case_list:
        if is_prime(c):
            answer += 1
    return answer
```
