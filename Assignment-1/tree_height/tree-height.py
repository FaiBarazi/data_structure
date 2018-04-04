# python3

import sys, threading
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size

class TreeHeight:
    def read(self):
            self.n = int(sys.stdin.readline())
            self.parent = list(map(int, sys.stdin.readline().split()))

    def get_parents(self, parents, nodes):
        result = []
        for parent in parents:
            result += nodes[parent]
        return result

    def compute_height(self):
            # Replace this code with a faster implementation
            parents = []
            height = 0
            nodes = [[] for i in range(self.n)]
            for i, label in enumerate(self.parent):
                if label == -1:
                    parents.append(i)
                else:
                    nodes[label].append(i)
            while parents:
                parents = self.get_parents(parents, nodes)
                height += 1
            return height

def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()
