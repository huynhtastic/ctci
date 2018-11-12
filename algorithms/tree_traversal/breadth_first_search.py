def bfs(root):
    queue = Queue()
    root.marked = True
    queue.enqueue(root)

    while not queue.is_empty():
        node = queue.dequeue()
        node.visited = True
        for neighbor in node.adjacent:
            if neighbor.marked != True:
                neighbor.marked = True
                queue.enqueue(neighbor)
