# python3

import sys


n, m = map(int, sys.stdin.readline().split())

lines = list(map(int, sys.stdin.readline().split()))
ans = [max(lines)]
rank = [0] * n
parent = list(range(0, n))

def getParent(table):
    """Equivalent to find set, uses path compression. """
    if table != parent[table]:
        table = getParent(parent[table])
    return parent[table]


def merge(destination, source):
    root_destination, root_source = getParent(destination), getParent(source)
    root_value = 0

    if root_destination == root_source:
        return

    if rank[root_destination] >= rank[root_source]:
        parent[root_source] = root_destination
        if rank[root_destination] == rank[root_source]:
            rank[root_destination] += 1
        lines[root_destination] += lines[root_source]
        root_value = lines[root_destination]
        lines[root_source] = 0

    else:
        parent[root_destination] = root_source
        lines[root_source] += lines[root_destination]
        root_value = lines[root_source]
        lines[root_destination] = 0

    if root_value > ans[0]:
        ans[0] = root_value


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans[0])
