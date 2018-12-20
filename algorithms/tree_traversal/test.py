from dijkstra import dijkstra
from graph import Node

asdf = 'abcdefg'
a = []
for i in range(len(asdf)):
    a.append(Node(asdf[i]))

print(a)

def aa(iddx, idx, val):
    node = a[iddx]
    node.add_adjacent((a[idx], val))

aa(0,1,4)
aa(0,2,3)
aa(0,4,7)

aa(1,0,4)
aa(1,2,6)
aa(1,3,11)

aa(2,0,3)
aa(2,1,6)
aa(2, 3,4)
aa(2,4,8)

aa(3,1,5)
aa(3,2,11)
aa(3,4,2)
aa(3,5,2)
aa(3,6,10)

aa(4,0,7)
aa(4,2,8)
aa(4,3,2)
aa(4,6,5)

aa(6,3,2)
aa(5,6,5)

aa(6,3,10)
aa(6,4,5)
aa(6,5,5)
print(a[0].adjacents)

print(dijkstra(a[0]))
