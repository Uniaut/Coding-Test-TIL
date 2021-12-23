# 가사 검색
2021 KAKAO BLIND RECRUITMENT 3번 문제
[[Link]](https://programmers.co.kr/learn/courses/30/lessons/72412)

## 풀이 과정
* 쿼리 수가 q, 지원자 수가 n이라면 naive linear search의 경우 O(qn) => `5 * 10 ^ 10` (시간 초과)
* **중요한 고려사항**: 턱걸이 점수를 받은 지원자가 2명 이상 있을 경우 그 지원자가 포함되도록 코드를 짤 필요가 있다.
  * 해결책: 기준이 `이상` 이므로 점수를 오름차순으로 정렬했다면 cut = score일 경우 start ~ mid에서 search해야 함
* 옵션 필터링은 단순한 구현부니까 언급 패스

## 피드백
* 쿼리상에서 option을 구분하는 과정이 굉장히 더럽게 풀었다. itertools.product를 쓰거나 했다면 좋았을 것 같음.
* binary search에서 애먹었는데 좀 메모하면서 풀었다면 좋았을 것 같음
## 정답처리된 코드
```python
from itertools import product


lang = ['cpp', 'java', 'python']
side = ['frontend', 'backend']
career = ['junior', 'senior']
food = ['chicken', 'pizza']

def bi_search(li, num, start, end):
    if end - start == 1:
        if num <= li[start]:
            return start - 1
        else:
            return start
    else:
        mid = (start + end) // 2
        if num <= li[mid]:
            return bi_search(li, num, start, mid)
        else:
            return bi_search(li, num, mid, end)


def info2info(i):
    i = i.split(' ')
    return tuple(i[:4]), int(i[4])

def querytoquery(q):
    q = q.replace(' and ', ' ').split(' ')
    q[4] = int(q[4])
    return tuple(q[:4]), int(q[4])


def solution(info, query):
    info = [info2info(i) for i in info]
    info.sort(key=lambda i: i[1])
    # todo: split info for tag
    info_tagged = []
    # index: i(l) s c f + i(s) c f + i(c) f + i(f)
    for l in lang:
        for s in side:
            for c in career:
                for f in food:
                    scores = []
                    for i in info:
                        if i[0] == (l,s,c,f):
                            scores.append(i[1])
                    else:
                        info_tagged.append(scores)
    # print(info_tagged)
    
    query = [querytoquery(q) for q in query]
    
    answer = []
    # todo: bi_search
    for q in query:
        idx = -1
        count = 0
        for l in lang:
            for s in side:
                for c in career:
                    for f in food:
                        idx += 1
                        for q_filter, i_item in zip(q[0], (l,s,c,f)):
                            if q_filter == '-':
                                continue
                            elif i_item != q_filter:
                                break
                        else:
                            scores = info_tagged[idx]
                            if scores:
                                result = bi_search(scores, q[1], 0, len(scores))
                                count += (len(scores) - result - 1)
        else:
            answer.append(count)
    
    
    return answer
  ```
## 개선된 코드
```python
from itertools import product


def modify_info_item(item:str):
    splitted = item.split(' ')
    tag = splitted[0:4]
    score = int(splitted[4])
    return tag, score

def modify_query_item(item:str):
    splitted = item.replace(' and ', ' ').split(' ')
    tag = splitted[0:4]
    score = int(splitted[4])
    return tag, score


def bi_search(score_list, score_cut, start, end):
    if start + 1 == end:
        if score_list[start] >= score_cut:
            return start + 1
        else:
            return start
    
    mid = (start + end) // 2
    if score_list[mid] < score_cut:
        return bi_search(score_list, score_cut, start, mid)
    else:
        return bi_search(score_list, score_cut, mid, end)



def solution(info, query):
    info = [modify_info_item(each) for each in info]
    info.sort(key=lambda item: -item[1])
    query = [modify_query_item(each) for each in query]
    
    tag_list = (
        ['cpp', 'java', 'python'],
        ['backend', 'frontend'],
        ['junior', 'senior'],
        ['chicken','pizza']
    )
    filtered_info = {tag:[] for tag in product(*tag_list)}
    # print(filtered_info)
    for info_item in info:
        info_tag, info_score = info_item
        filtered_info[tuple(info_tag)].append(info_score)

    
    answer = []
    for query_item in query:
        query_tag, query_score = query_item
        query_count = 0
        for tag_composition in product(*tag_list):
            for q_tag, c_tag in zip(query_tag, tag_composition):
                if q_tag != '-' and q_tag != c_tag:
                    break
            else:
                to_search = filtered_info[tuple(tag_composition)]
                if to_search:
                    count = bi_search(to_search, query_score, 0, len(to_search))
                else:
                    count = 0
                query_count += count
        else:
            answer.append(query_count)
    return answer
```
