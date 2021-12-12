# 신규 아이디 추천
2021 KAKAO BLIND RECRUITMENT 1번 문제
[[Link]](https://programmers.co.kr/learn/courses/30/lessons/72410)

## 풀이 과정
* 문제에서 제시하는 내용을 그대로 따라가면 통과임

## 피드백
* str.lower 등 built-in method를 제대로 활용하지 못하고 기괴한 코드를 짠 것이 가장 아쉽다.
* 정규식을 다시 공부해야 할 것 같다.

## 정답처리된 코드
```python
def step1(new_id):
    Atoa = {
        'A': 'a',
        'B': 'b',
        'C': 'c',
        'D': 'd',
        'E': 'e',
        'F': 'f',
        'G': 'g',
        'H': 'h',
        'I': 'i',
        'J': 'j',
        'K': 'k',
        'L': 'l',
        'M': 'm',
        'N': 'n',
        'O': 'o',
        'P': 'p',
        'Q': 'q',
        'R': 'r',
        'S': 's',
        'T': 't',
        'U': 'u',
        'V': 'v',
        'W': 'w',
        'X': 'x',
        'Y': 'y',
        'Z': 'z',
    }
    result = [Atoa.setdefault(token, token) for token in new_id]
    return result

def step2(new_id):
    return [token for token in new_id if token in [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '0',
        '-',
        '_',
        '.'
    ]]

def step3(new_id):
    result = []
    prev_dot = False
    for token in new_id:
        if (not prev_dot) or token != '.':
            result.append(token)
        if token == '.':
            prev_dot = True
        else:
            prev_dot = False
    return result

def step4(new_id):
    result = []
    for idx, token in enumerate(new_id):
        if idx > 0 and idx < len(new_id) - 1:
            result.append(token)
        elif token != '.':
            result.append(token)
        else:
            continue

    return result

def step5(new_id):
    if new_id:
        return new_id
    else:
        return ['a']

def step6(new_id):
    if len(new_id) >= 16:
        return step4(new_id[:15])
    else:
        return new_id

def step7(new_id):
    if len(new_id) <= 2:
        return new_id + [new_id[-1]] * (3 - len(new_id))
    else:
        return new_id

def solution(new_id):
    for idx, func in enumerate([step1, step2, step3, step4, step5, step6, step7]):
        new_id = func(new_id)
        print(idx, new_id)
    return ''.join(new_id)
```

## 개선된 코드
```python
def step1(new_id):
    result = [token.lower() for token in new_id]
    return result

def step2(new_id):
    return [token for token in new_id if 
            token.islower() or token.isdecimal() or token in '.-_']

def step3(new_id):
    result = []
    prev_dot = False
    for token in new_id:
        if token != '.':
            result.append(token)
            prev_dot = False
        else:
            if not prev_dot:
                prev_dot = True
                result.append(token)
            else:
                pass
    return result

def step4(new_id):
    result = []
    for idx, token in enumerate(new_id):
        if idx > 0 and idx < len(new_id) - 1:
            result.append(token)
        elif token != '.':
            result.append(token)
        else:
            continue

    return result

def step5(new_id):
    if new_id:
        return new_id
    else:
        return ['a']

def step6(new_id):
    if len(new_id) >= 16:
        return step4(new_id[:15])
    else:
        return new_id

def step7(new_id):
    if len(new_id) <= 2:
        return new_id + [new_id[-1]] * (3 - len(new_id))
    else:
        return new_id

def solution(new_id):
    for idx, func in enumerate([step1, step2, step3, step4, step5, step6, step7]):
        new_id = func(new_id)
        print(idx, new_id)
    return ''.join(new_id)
```
