# 가사 검색
2020 KAKAO BLIND RECRUITMENT 4번 문제
[[Link]](https://programmers.co.kr/learn/courses/30/lessons/60060)

## 풀이 과정
* 단순 선형 검색의 경우 O(n_queries * n_words * len_word&query) = 10^13이므로 다른 방법을 찾아야 함
* Trie를 쓰되, 물음표의 개수가 많은 경우 O(n_words)가 되므로 prefix, postfix의 특징을 활용한 count dict를 만들어 '?'에 진입하는 순간 count로 넘기기
  * 이것을 수행하기 위해 Trie를 두개 만들어 prefix가 ?인 경우 reversed word를 저장하고 reversed query를 쏘는 방식으로 구현

## 피드백
* recursion을 쓰기 전에 제한 조건을 확인했다면 삽질 할 필요가 없었을 것... stack이나 queue를 활용한 재귀함수 대체도 연습할 필요가 있을 것 같다.

## 정답처리된 코드
```python
import sys


sys.setrecursionlimit(1000000)

class AlphaNode:
    def __init__(self):
        self.end_node = False
        self.children = [None] * 26
        self.count = {}
    
    def better_search(self, string, start=0):
        if len(string) == start:
            if self.end_node:
                return 1
            else:
                return 0
        else:
            token = string[start] 
            if token == '?':
                return self.count.setdefault(len(string), 0)
            else:
                idx = ord(token) - ord('a')
                next_node = self.children[idx]
                if next_node is not None:
                    return next_node.better_search(string, start + 1)
                else:
                    return 0

    def add(self, string, start=0):
        if len(string) == start:
            if self.end_node:
                pass
            else:
                self.end_node = True
        else:
            idx = ord(string[start]) - ord('a')
            next_node = self.children[idx]
            if next_node is None:
                next_node = AlphaNode()
                self.children[idx] = next_node
            
            next_node.add(string, start + 1)
        self.count[len(string)] = self.count.setdefault(len(string), 0) + 1


class Trie:
    def __init__(self) -> None:
        self.root = AlphaNode()
    
    def better_search(self, string):
        return self.root.better_search(string)

    def add(self, string):
        self.root.add(string)

        
def solution(words, queries):
    a = Trie()
    b = Trie()
    for w in words:
        a.add(w)
        b.add(''.join(reversed(w)))

    print('start')
    answer = []
    for q in queries:
        if q[0] == '?':
            answer.append(b.better_search(''.join(reversed(q))))
        else:
            answer.append(a.better_search(q))
    
    return answer
```
