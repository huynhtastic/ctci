class Stack():
    def __init__(self):
        self.stack = []

    def pop(self):
        if not self.stack.is_empty():
            return self.stack.pop()
        raise ValueError('The stack is empty.')

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        if not self.stack.is_empty():
            return self.stack[-1]
        raise ValueError('The stack is empty.')

    def is_empty(self):
        return not bool(self.stack)
