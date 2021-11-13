# Karatsuba 알고리즘
## 개요
* 매우 큰 자리수의 곱셈을 할 때에는 vector * vector 형식의 연산이 이루어지게 됨
* 단순 곱셈 알고리즘 (초등학생 알고리즘이라고 부름)의 경우, L(x)가 vector의 길이일 때  L(n1) * L(n2)의 시간복잡도를 지닌다.
  * 즉, L(n1) = L(n2)일때 이 알고리즘의 시간복잡도는 O(n^2)이다
* Karatsuba 알고리즘은 a * b를 (a0 * m^*len* + a1) * (b1 * m^*len* + b1)으로 변환하여
* a0 * b0, a0 * b1 + a1 * b0, a1 * b1의 3가지 문제로 분할한다. 문제가 3개로 분할될 때 마다 len은 n으로부터 2배씩 줄어든다.
  * 즉, 시간복잡도는 3^*log n* = n^*log 3*이고, log 3 < 2 (밑 2일 때)이기 때문에 초등학생 알고리즘보다 빠르다!

## 피드백
* 코드를 작성하는 과정에서 재사용성을 늘린답시고 너무 복잡하게 코딩하면 느려진다...

## 코드
```python
from random import random

from sys import getsizeof
from time import time
from typing import List

INT_MAX = 10
SIZE = 2049
x = [int(random()*INT_MAX) for _ in range(SIZE)]
y = [int(random()*INT_MAX) for _ in range(SIZE)]

def regulated(a: List):
    roof_up = 0
    i_a = 0
    while i_a < len(a) or roof_up > 0:
        if roof_up > 0:
            if i_a == len(a):
                a.append(roof_up)
            else:
                a[i_a] += roof_up
            roof_up = 0
        if a[i_a] >= INT_MAX:
            roof_up, a[i_a] = a[i_a] // INT_MAX, a[i_a] % INT_MAX
        i_a += 1
    return a

def added(a: List, b: List):
    return [e_a + e_b for e_a, e_b in zip(a, b)]

def slow_multiplied(a: List, b: List):
    res = [0 for _ in range(len(a) + len(b))]
    for i_a, e_a in enumerate(a):
        for i_b, e_b in enumerate(b):
            res[i_a + i_b] += e_a * e_b
    return res

def karatsuba_multiplied(a: List, b: List):
    if len(a) == 1:
        return [a[0] * b[0]]
    else:
        # 2 power n is fastest.
        length = 1 << (len(a) - 1).bit_length()
        if length != len(a):
            a = [a[i] if i < len(a) else 0 for i in range(length)]
            b = [b[i] if i < len(b) else 0 for i in range(length)]
        res_length = length << 1
        i_mid = length >> 1
        a_0, a_1 = a[:i_mid], a[i_mid:]
        b_0, b_1 = b[:i_mid], b[i_mid:]
        # recursion: using z_1, z_2, z_3 to get original
        z_0 = karatsuba_multiplied(added(a_0, a_1), added(b_0, b_1))
        z_1 = karatsuba_multiplied(a_0, b_0)
        z_2 = karatsuba_multiplied(a_1, b_1)
        z_3 = added(z_0, [-e1 - e2 for e1, e2 in zip(z_1, z_2)])

        res = []
        res.extend(z_1)
        res.extend(z_3)
        res.extend(z_2)
        return res


def multiply1(a, b):
    return regulated(karatsuba_multiplied(a, b))
def multiply2(a, b):
    return regulated(slow_multiplied(a, b))

if __name__ == '__main__':
    if False:
        x = [1, 1]
        y = [1, 1]

    start_time = time()
    res = multiply1(x, y)
    end_time = time()
    print('K:', end_time - start_time)
    start_time = time()
    res = multiply2(x, y)
    end_time = time()
    print('S:', end_time - start_time)
    
    if False:
        print('x:', x, 'y:', y)
        print(res)
        
```
