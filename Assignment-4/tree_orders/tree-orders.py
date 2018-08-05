# python3

import sys, threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
    def inOrder(self):
        self.result = []
        self.in_order_traversal(0)
        return self.result

    def in_order_traversal(self, root):
        if self.left[root] != -1:
            self.in_order_traversal(self.left[root])
        self.result.append(self.key[root])
        if self.right[root] != -1:
            self.in_order_traversal(self.right[root])

    def preOrder(self):
        self.result = []
        self.pre_order_traversal(0)
        return self.result

    def pre_order_traversal(self, root):
        self.result.append(self.key[root])
        if self.left[root] != -1:
            self.pre_order_traversal(self.left[root])
        if self.right[root] != -1:
            self.pre_order_traversal(self.right[root])

    def postOrder(self):
        self.result = []
        self.post_order_traversal(0)
        return self.result

    def post_order_traversal(self,root):
        if self.left[root] != -1:
            self.post_order_traversal(self.left[root])
        if self.right[root] != -1:
            self.post_order_traversal(self.right[root])
        self.result.append(self.key[root])

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
