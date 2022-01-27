# 신고 결과 받기
**문제 출처: KAKAO 2022 BLIND 1차 1번**

[Link](https://programmers.co.kr/learn/courses/30/lessons/92334)

## 풀이 과정
* A가 B를 신고했음을 나타내는 N * N 테이블에 report 기록을 저장한다. (A와 B가 같다면 한번의 신고로 간주하므로 element는 boolean으로 해도 좋다.)
* banned 리스트를 만들어 k회 이상 신고된 아이디를 정지한다.
* 모든 계정 (A, B)에 대해 A가 B를 신고했고 B가 정지당했다면 결과 받기 카운트를 추가한다.
* id만 주어지고 index가 없기 때문에 string -> intager 의 역할을 하는 dict인 str_to_id를 만듦.

## 피드백
* 그냥 dict[id:set]으로 하는 경우도 봤는데, 작성 속도는 그쪽이 더 빠를지도 모르겠다.

## 정답 코드
```python
def solution(id_list, report, k):
    str_to_id = {id_str:idx for idx, id_str in enumerate(id_list)}
    size = len(id_list)
    table = [[False] * size for _ in range(size)]
    for r in report:
        reporter, reported = map(lambda s: str_to_id[s], r.split(' '))
        table[reporter][reported] = True
    
    banned = [False] * size
    for reported in range(size):
        count = 0
        for reporter in range(size):
            if table[reporter][reported]:
                count += 1
        if count >= k:
            banned[reported] = True
    
    answer = [0] * size
    for reporter in range(size):
        for reported in range(size):
            if table[reporter][reported] and banned[reported]:
                answer[reporter] += 1
    
    return answer
```
