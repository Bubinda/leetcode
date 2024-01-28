def solution(array, k):
    permutation = []
    index = 0

    while array: #O(n)
        index = (index + k-1) % len(array)
        permutation.append(array.pop(index)) # O(n)
    return permutation

#-> time complexity O(n^2)

import time
soldiers = 1000000
array = [s+1 for s in range(soldiers)]
k = 3
start = time.perf_counter()
perm = solution(array,k)
stop = time.perf_counter()
print(f'the list approach took :{stop-start}')
# very slow 




from collections import deque
def solution_2(array, k):
    d = deque(array)
    permutation = []

    while d:
        d.rotate(1-k)
        permutation.append(d.popleft())
    return permutation

import time
soldiers = 1000000
array = [s+1 for s in range(soldiers)]
k = 3
start = time.perf_counter()
perm = solution_2(array,k)
stop = time.perf_counter()
print(f'the deque approach took :{stop-start}')