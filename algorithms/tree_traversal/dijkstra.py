"""
class Node():
    value = something
    adjacents = [(b,4), (c,3), (7,e)]
    """

def dijkstra(root):
    # set a table of shortest paths and previous nodes
    to_visit = [(root, root, 0)]
    visited = {}
    visited_edges = []

    travelled_dist = 0
    while to_visit:
        # extract current node info
        cur_node, prev_node, travelled_dist = to_visit.pop()
        #print(visited_edges)
        visited_edges.append({cur_node, prev_node})  # travelled this edge
        # check if we've been to this node before from a different route
        if cur_node in visited:
            # check if we went through this with a diff distance
            if travelled_dist < visited[cur_node][1]:
                visited[cur_node] = (prev_node, travelled_dist)
        else:
            # if we haven't been to this node, we just record that we've
            # now travelled here before
            visited[cur_node] = (prev_node, travelled_dist)
        # look through the neighbors and enqueue the nodes that we haven't
        # been to before from this current node
        for neighbor, dist in cur_node.adjacents:
            if {cur_node, neighbor} not in visited_edges:
                to_visit.append((neighbor, cur_node, travelled_dist + dist))
        to_visit = sorted(to_visit, key=lambda x: x[2], reverse=True)
    return visited
