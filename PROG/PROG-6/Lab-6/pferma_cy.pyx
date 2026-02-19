from math import isqrt
import threading

def is_perfect_square(int n):
    cdef int root = isqrt(n)
    return root * root == n

def fermat_factorization(N):
    if N % 2 == 0:
        return 2, N // 2
    x = isqrt(N) + 1
    while True:
        y2 = x * x - N
        y = isqrt(y2)
        if y * y == y2:
            return x - y, x + y
        x += 1

def process_batch(list nums, list output, int offset):
    for i in range(len(nums)):
        output[offset + i] = fermat_factorization(nums[i])

def parallel_factorization(list numbers, int num_threads=4):
    cdef int total = len(numbers)
    cdef int batch_size = (total + num_threads - 1) // num_threads

    output = [None] * total
    threads = []

    for i in range(num_threads):
        start = i * batch_size
        end = min(start + batch_size, total)
        if start >= end:
            break
        batch = numbers[start:end]
        t = threading.Thread(target=process_batch, args=(batch, output, start))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return output
