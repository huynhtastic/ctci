class Node():
    def __init__(self, value=None, adjacents=None):
        self.value = value
        self.adjacents = [] if adjacents == None else adjacents

    def add_adjacent(self, node):
        self.adjacents.append(node)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

