# 메뉴 리뉴얼
2021 KAKAO BLIND RECRUITMENT 2번 문제
[[Link]](https://programmers.co.kr/learn/courses/30/lessons/72411)

## 풀이 과정
* time complexity를 잘 계산해야 하는 문제.
  * 겹치는지 여부를 확인하는 연산이 굉장히 많은데 bit masking을 사용해 시간을 단축할 수 있다
* 처음 풀었을 당시엔 어찌저찌 풀었는데 두번째 풀때 되니까 안풀림. 결국 처음 봤던 코드에서 착안하여 해결
* 모든 가능한 메뉴를 계산할 때는 최악의 경우 `sigma i: 2 to 10, 26_C_i`개의 경우의 수를 다 계산해야 하므로 시간 초과될 가능성이 높음
* 'ABCD'가 8번 나온다면 같은 주문에서 'ABC'도 8번 등장한다는 것을 이용해서 로직을 최적화할 수 있음
  * 풀었던 당시엔 order가 20개 이하임을 이용해 orders 내의 모든 조합을 시도해 최대 빈도인 메뉴 구성을 찾음
  * 두번째 풀면서는  같은 order가 2회 이상 등장해야 하기 때문에 중복으로 등장하는 조합만 possible_cases에 넣어 후보군을 좁혔는데 자꾸 오답이 나와서 포기함
    * ㅠㅠ


## 피드백
* chr()과 ord()를 알았다면 atoi같은 우스운 코드는 짜지 않았을텐데 ㅋㅋㅋ
* 무작정 키보드에 손부터 올리는 문제풀이 습관은 확실히 도움이 되지 않는다. 최대한 많이 생각하고 코딩하기 시작할 것.

## 정답처리된 코드
```python
from itertools import combinations

atoi = dict({(token, idx) for idx, token in 
        enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')})
itoa = dict({(idx, token) for idx, token in 
        enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')})

def tobit(order):
    l = [atoi[token] for token in order]
    num = 0
    for each in l:
        num |= 1 << each
    return num


def tolist(num):
    li = []
    count = 0
    while num:
        if num & 1:
            li.append(itoa[count])
        count += 1
        num >>= 1
    return li
            



def solution(orders, course):
    orders = [tobit(each) for each in orders]
    print(orders)
    
    # dict of n_item -> max repeat course
    course_max = [{
        'list': [],
        'repeat': 0
    } for n_item in course]
    for i in range(1, len(orders)): # i: repeat of order
        i += 1
        for order_combi in combinations(orders, r=i):
            x = (1 << 26) - 1
            for num in order_combi:
                x &= num
            # x: common orders
            len_common = len(tolist(x))

            for idx, n_item in enumerate(course):
                if n_item > len_common:
                    continue
                if i > course_max[idx]['repeat']:
                    course_max[idx]['repeat'] = i
                    course_max[idx]['list'] = [x]
                elif i == course_max[idx]['repeat']:
                    course_max[idx]['list'].append(x)
    
    print(course_max)
    answer = []
    
    for idx, n_item in enumerate(course):
        num_li = course_max[idx]['list']
        for num in num_li:
            for li in combinations(tolist(num), r=n_item):
                s = ''.join(li)
                answer.append(s)
        
    
    '''
    ABCDEFGHIJK/X
    ABCDEFGHIJK/Y
    ABCDEFGHIJK/Z
    ABCDEFGHIJK/W
    '''
    
    answer.sort()
    return answer
```

## 개선된 코드
```python
from itertools import combinations


def to_bit(order):
    n = 0
    for token in order:
        n += 1 << (ord(token) - ord('A'))
    return n


def to_str(n):
    order = ''
    for i in range(26):
        if (1 << i) & n:
            order += chr(i + ord('A'))
    return order


def solution(orders, course):
    bit_orders = [to_bit(each) for each in orders]
    
    # dict of n_item -> max repeat course
    course_max = {n_item:(2, set()) for n_item in course}

    for repeat_order in range(2, len(orders) + 1): # i: repeat of order
        for order_combi in combinations(bit_orders, r=repeat_order):
            x = (1 << 26) - 1
            for num in order_combi:
                x &= num
            
            # x: common orders
            len_common = len(to_str(x))

            for n_item in course:
                if n_item > len_common:
                    continue
                
                best_count, best_set = course_max[n_item]
                if repeat_order > best_count:
                    course_max[n_item] = (repeat_order, set([x]))
                elif repeat_order == best_count:
                    best_set.add(x)
    
    print(course_max)
    answer = []
    
    for n_item in course:
        _,  best_set = course_max[n_item]
        for num in best_set:
            for li in combinations(to_str(num), r=n_item):
                s = ''.join(li)
                answer.append(s)
    
    answer.sort()
    return answer
```
