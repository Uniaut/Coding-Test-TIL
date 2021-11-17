# FANMEETING
[Link](https://www.algospot.com/judge/problem/read/FANMEETING)

## 분석
N = 200k이므로 단순 반복문보다 빠른 method를 쓰는게 좋다 (bit mask, karatsuba multiply 등)

## 피드백
* 결국 algospot에서 python으로는 풀기 힘들어 보인다. python builtin 함수가 느려서 라이브러리 없이는 ㅇㅇ...
* python에서는 너무 시간에 연연하지 말고 구현 자체에 의미를 두는게 좋을듯.

```python
read_line = lambda: input().strip()

def slow_solve(mem, fan):
    n_mem, n_fan = len(mem), len(fan)
    count = 0
    for i in range(n_fan - n_mem + 1):
        flag = True
        for j in range(n_mem):
            # if fan & mem are all Male -> no count
            if fan[i + j] and mem[j]:
                flag = False
        if flag:
            count += 1
            
    return count

def add(a, b):
    return [i + j for i, j in zip(a, b)]
def sub(a, b, c):
    return [i - j - k for i, j, k in zip(a, b, c)]
def mult(a, b):
    # print(len(a))
    if len(a) == 2:
        return [a[0] * b[0], a[0] * b[1] + a[1] * b[0], a[1] * b[1], 0]
    else:
        border = len(a) >> 1
        a1, a0 = a[:border], a[border:] # a = a0 * 2^k + a1
        b1, b0 = b[:border], b[border:] # b = b0 * 2^k + b1
        z0 = mult(a0, b0)
        z2 = mult(a1, b1)
        z1 = sub(mult(add(a0, a1), add(b0, b1)), z0, z2)
        
        # z = z2 + z1 * 2^k + z0 * 2^2k
        # z = z2[:border] + add(z2[border:], z1[:border]) + add(z1[border:], z0[:border]) + z0[border:]
        z = z2 + z0
        for i in range(border * 2):
            z[border + i] += z1[i]
        return z
def mult_solve(mem, fan):
    n_mem, n_fan = len(mem), len(fan)
    
    # reverse member to multiply
    mem.reverse()
    # extend for mult
    mult_len = 1<<(n_fan-1).bit_length()
    # mult_len = n_fan
    mem += [0 for _ in range(mult_len - n_mem)]
    fan += [0 for _ in range(mult_len - n_fan)]

    c = mult(fan, mem)

    # print(c[n_mem - 1:n_fan])
    count = sum((1 for each in c[n_mem - 1:n_fan] if not each))
    return count

if __name__ == '__main__':
    n_case = int(input())
    for _ in range(n_case):
        str_mem = read_line()
        str_fan = read_line()
        mem = [1 if token=='M' else 0 for token in str_mem]
        fan = [1 if token=='M' else 0 for token in str_fan]
        # print(slow_solve(mem, fan))
        print(mult_solve(mem, fan))
```
