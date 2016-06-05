#!/usr/bin/python3
LIST_COUNT = 1000
LOOP_COUNT = 1000
MAX_NUM = 10000


def data_generate():
    import random
    return [random.randint(1, MAX_NUM) for _ in range(LIST_COUNT)]


def selection_sort(data):
    for i in range(len(data) - 1):
        minimum = i

        for t in range(i + 1, len(data)):
            if data[minimum] > data[t]:
                  minimum = t

        data[i], data[minimum] = data[minimum], data[i]



def bubble_sort(data):
    for i in range(len(data)):
        for t in range(1, len(data) - 1):
            if data[t] < data[t - 1]:
                data[t], data[t - 1] = data[t - 1], data[t]



def insertion_sort(data):
    for i in range(1, len(data)):
        tmp = data[i]
        if data[i - 1] > tmp:
          j = i
          while j > 0 and data[j - 1] > tmp:
              data[j] = data[j - 1]
              j -= 1



def shell_sort(data):
    gap = len(data) // 2
    while gap > 0:
        for i in range(gap, len(data)):
            tmp = data[i]
            j = i - gap
            while j >= 0 and tmp < data[j]:
                data[j + gap] = data[j]
                j -= gap
            data[j + gap] = tmp
        gap //= 2

def merge_sort(data):
    mid = len(data)
    if mid == 1:
        return data

    left = merge_sort(data[:(mid//2)])
    right = merge_sort(data[(mid//2):])
    left = merge_sort(left)
    right = merge_sort(right)

    array = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            array.append(left.pop(0))
        else:
            array.append(right.pop(0))

    if len(left) !=0:
        array.extend(left)
    elif len(right) !=0:
        array.extend(right)

    return array


def quick_sort(data):
    if len(data) < 1:
        return data

    pivot = data [0]

    if len( data) > 2:
        pivot = data[ 0] if data[ 0] < data[ 1] else data[ 1]

    left = []
    right = []

    for x in range(1, len(data)):
        if data[x] <= pivot:
            left.append(data[x])
        else:
            right.append(data[x])

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right



if __name__=='__main__':
    import time
    import sys


    """
    start = time.time()

    for _ in range(LOOP_COUNT):
        data = data_generate()
        selection_sort(data)
        print('.', end='')
        sys.stdout.flush()

    end = time.time()
    print()
    print('経過時間:', (end-start))
    print('平均時間:', ((end-start) / LOOP_COUNT))
    """

    """
    start = time.time()

    for _ in range(LOOP_COUNT):
        data = data_generate()
        bubble_sort(data)
        [print('.', end='') if _ % 100 != 99 else print(int(_ / 100 + 1))]
        sys.stdout.flush()

    end = time.time()
    print()
    print('経過時間:', (end-start))
    """

    """
    start = time.time()

    for _ in range(LOOP_COUNT):
        data = data_generate()
        insertion_sort(data)
        [print('.', end='') if _ % 100 != 99 else print(int(_ / 100 + 1))]
        sys.stdout.flush()

    end = time.time()
    print()
    print('経過時間:', (end-start))
    """

    """
    start = time.time()

    for _ in range(LOOP_COUNT):
        data = data_generate()
        shell_sort(data)
        [print('.', end='') if _ % 100 != 99 else print(int(_ / 100 + 1))]
        sys.stdout.flush()

    end = time.time()
    print()
    print('経過時間:', (end-start))
    """

    """
    start = time.time()

    for _ in range(LOOP_COUNT):
        data = data_generate()
        merge_sort(data)
        [print('.', end='') if _ % 100 != 99 else print(int(_ / 100 + 1))]
        sys.stdout.flush()

    end = time.time()
    print()
    print('経過時間:', (end-start))
    """


    start = time.time()

    for _ in range(LOOP_COUNT):
        data = data_generate()
        quick_sort(data)
        [print('.', end='') if _ % 100 != 99 else print(int(_ / 100 + 1))]
        sys.stdout.flush()

    end = time.time()
    print()
    print('経過時間:', (end-start))
    print('平均時間:', ((end-start) / LOOP_COUNT))
