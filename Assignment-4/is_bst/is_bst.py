#!/usr/bin/python3
"""Check of a tree is a Binary Search Tree."""
import sys
import threading


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class Tree:
    """A binary tree object."""
    def read(self):
        """read input to create Tree nodes."""
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
        self.is_binary = True

    def is_BST(self):
        """Return boolean if binary search tree  or not."""
        self.result = []
        if self.n < 2:
            return True
        return self.is_binary_util(0)

    def compare_last_keys(self):
        """return the value of the last key, -inf otherwise."""
        if len(self.result) > 1:
            return self.result[-2] <= self.result[-1]
        return True

    def is_binary_util(self, root):
        """return bool using in order tree traversal."""
        if self.is_binary:
            if self.left[root] != -1:
                self.is_binary_util(self.left[root])
            self.result.append(self.key[root])
            if not self.compare_last_keys():
                self.is_binary = False
            if self.right[root] != -1:
                self.is_binary_util(self.right[root])
        return self.is_binary


def main():  # noqa
    tree = Tree()
    tree.read()
    is_BST = tree.is_BST()
    if is_BST:
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
