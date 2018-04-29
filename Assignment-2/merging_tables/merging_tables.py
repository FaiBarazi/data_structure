# python3

import sys
import random

n, m = map(int, sys.stdin.readline().split())

# n = random.randint(1, 100000)
# m = random.randint(1, 100000)
# lines = [random.randint(0, 10000) for i in range(n)]
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
    # print('I am destination', root_destination + 1)
    # print('I am source', root_source + 1)
    if root_destination != root_source:
        parent[source] = destination
        rank[root_destination] += 1
        lines[root_destination] += lines[root_source]
        lines[source] = 0
        lines[root_source] = 0
        #print('I am lines', lines)
    #print('I am the parent list', parent)
    #print('I am lines')

    # merge two components
    # use union by rank heuristic
    # update ans with the new maximum table size

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    # destination, source = random.randint(1, n), random.randint(1, n)
    merge(destination - 1, source - 1)
    print(max(lines))
