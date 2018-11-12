def dfs(root):
    if root == None:
        return
    print('visited {}'.format(root.value))
    root.visited = True
    for child in root.children:
        if child.visited != True:
            dfs(child)
