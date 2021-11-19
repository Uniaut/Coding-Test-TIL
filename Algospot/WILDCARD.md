# WILDCARD
[Link](https://www.algospot.com/judge/problem/read/WILDCARD)

## 피드백
* 경우의 수를 꼼꼼하게 따져가며 계산할 것.
* 애매한 경우엔 테스트를 돌려가면서 코딩하자.
* 알고스팟 judge는 책의 내용을 이행하는 것에만 초점이 맞춰져 있으니 그 외의 것들에 연연하지 말자.

## 주목할 만한 것
* string indexing
```python
a = 'hi'
print([a[i:] for i in range(len(a) + 1)])
```
의 결과는 `['hi', 'i', '']`
## 정답 코드
```python
cache = None # tested impossible list
def __solve(keyword, word, idx_key, idx_word):
    if not keyword: # key is ''
        return not word # word is ''
    elif keyword[0] == '*': # first token is '*'
        for i in range(len(word) + 1): # 'key' & ['word', 'ord', 'rd', 'd', '']
            if _solve(keyword[1:], word[i:], idx_key + 1, idx_word + i):
                return True
        else:
            return False
    else: # key token is ? or default
        if not word: # word is ''
            return False
        elif keyword[0] == '?' or keyword[0] == word[0]: # compare
            return _solve(keyword[1:], word[1:], idx_key + 1, idx_word + 1) # then next level
        else:
            return False

def _solve(keyword,word, idx_key, idx_word):
    if cache[idx_key][idx_word]:
        return False
    elif __solve(keyword, word, idx_key, idx_word):
        return True
    else:
        cache[idx_key][idx_word] = True
        return False

def solve(keyword, word):
    global cache
    cache = [[False for _ in range(len(word) + 1)] for _ in range(len(keyword) + 1)]
    return _solve(keyword, word, 0, 0)

if __name__ == '__main__':
    n_case = int(input())
    for _ in range(n_case):
        keyword = input().strip()
        n_word_list = int(input())
        result = []
        for __ in range(n_word_list):
            word = input().strip()
            if solve(keyword, word):
                result.append(word)
        result.sort()
        for each in result:
            print(each)
```
