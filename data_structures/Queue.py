from collections import deque
# import deque since python has no apparent way to implement a queue with 
# constant time dequeues

class Queue():
    def __init__(self):
        self._queue = deque()

    def add(self, item):
        self._queue.append(item)

    def remove(self):
        if not self.is_empty():
            return self._queue.popleft()
        raise ValueError('The queue is empty.')

    def peek(self):
        if not self.is_empty():
            return self._queue[0]
        raise ValueError('The queue is empty.')

    def is_empty(self):
        return not bool(self._queue)
