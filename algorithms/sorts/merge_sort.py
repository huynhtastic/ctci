from collections import deque

def merge_sort(A):
    if len(A) < 2:
        return A

    queue = deque([ deque([item]) for item in A ])
    while len(queue) > 1:
        queue.append(sort(queue.popleft(), queue.popleft()))

    return list(queue.pop())

def sort(a, b):
    sorted_queue = deque()
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            sorted_queue.append(a.popleft())
        else:
            sorted_queue.append(b.popleft())
    return sorted_queue + a + b
