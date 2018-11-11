class Node():
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            tail = Node(data)
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = tail

    def pop(self, data):
        if self.head == None:
            raise ValueError('This LinkedList has no nodes.')
        cur_node = self.head
        if self.head.data == data:
            self.head = None
            return cur_node
        while cur_node.next != None:
            if cur_node.next.data == data:
                node = cur_node.next
                cur_node.next = cur_node.next.next
                return node
            cur_node = cur_node.next
        raise ValueError('"{}" not found in LinkedList.'.format(data))
