import random


def bubble_sort(shuffled_list):
    length = len(shuffled_list)
    for i in range(length):
        for j in range(i):
            if shuffled_list[i] < shuffled_list[j]:
                shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]
    return shuffled_list


def selection_sort(shuffled_list):
    length = len(shuffled_list)
    for i in range(length):
        min_idx = i
        for j in range(min_idx + 1, length):
            if shuffled_list[min_idx] > shuffled_list[j]:
                min_idx = j
        else:
            shuffled_list[i], shuffled_list[min_idx] = shuffled_list[min_idx], shuffled_list[i]
    return shuffled_list

def insertion_sort(shuffled_list):
    length = len(shuffled_list)
    for i in range(length - 1):
        for j in reversed(range(i + 1)):
            if shuffled_list[j] > shuffled_list[j + 1]:
                shuffled_list[j], shuffled_list[j + 1] = shuffled_list[j + 1], shuffled_list[j]
            else:
                break
    return shuffled_list


def merge(li1, li2):
    result = []
    length1, length2 = len(li1), len(li2)
    idx1, idx2 = 0, 0
    while True:
        if idx1 == length1 and idx2 == length2:
            break
        elif idx1 == length1:
            result.append(li2[idx2])
            idx2 += 1
        elif idx2 == length2:
            result.append(li1[idx1])
            idx1 += 1
        else:
            if li1[idx1] < li2[idx2]:
                result.append(li1[idx1])
                idx1 += 1
            else:
                result.append(li2[idx2])
                idx2 += 1
    return result

def merge_sort(li, is_sorted=False):
    length = len(li)
    if length == 1:
        return li
    # split
    li1, li2 = li[:length // 2], li[length // 2:]

    a = merge_sort(li1)
    b = merge_sort(li2)
    result = merge(a, b)

    return result


def quick_sort(li, range=None):

    if range is None:
        range = (0, len(li))
    start, end = range


    if end - start <= 1:
        return

    pivot = start
    low, high = start + 1, end - 1
    while True:
        while low < end and li[pivot] > li[low]:
            low += 1
        
        while li[pivot] < li[high] and start < high:
            high -= 1

        if low < high:
            li[low], li[high] = li[high], li[low]
            low += 1
            high -= 1
        else:
            break
        

    li[pivot], li[high] = li[high], li[pivot]
    mid = low
    
    quick_sort(li, (start, mid))
    quick_sort(li, (mid, end))
    return li
        



if __name__ == '__main__':
    for _ in range(100):
        shuffled = [i for i in range(30)]
        random.shuffle(shuffled)
        print('*', shuffled)
        sort_func = quick_sort
        print('>', sort_func(shuffled))
