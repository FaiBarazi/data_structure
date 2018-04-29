# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))

def getParent(table):
    """Equivalent to find set, uses path compression. """
    if table != parent[table]:
        table = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    root_destination, root_source = getParent(destination), getParent(source)
    print('I am destination', root_destination + 1)
    print('I am source', root_source + 1)
    if root_destination != root_source:
        parent[source] = destination
        rank[root_destination] += 1
        lines[root_destination] += lines[root_source]
        print('I am lines', lines)
    print('I am the parent list', parent)

    # merge two components
    # use union by rank heuristic
    # update ans with the new maximum table size

    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(max(lines))
