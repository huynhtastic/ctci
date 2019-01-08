from collections import deque

def merge_sort(A):
    # return any list under the length of 2
    if len(A) < 2:
        return A

    # create a queue of queues for each element
    queue = deque([ deque([item]) for item in A ])

    # cycle through pairs of queues until one queue is left in the queue
    while len(queue) > 1:
        queue.append(sort(queue.popleft(), queue.popleft()))

    return list(queue.pop())

def sort(a, b):
    # make a new queue containing all of the elements sorted from a and b
    sorted_queue = deque()

    # make comparisons from elements in each queue until one queue runs out
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            sorted_queue.append(a.popleft())
        else:
            sorted_queue.append(b.popleft())
    # add all queues as either a or b will be empty and the other queue will
    # contain only elements bigger than the sorted queue
    return sorted_queue + a + b
