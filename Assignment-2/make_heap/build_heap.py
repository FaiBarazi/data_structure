# python3
import heapq

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []
        self._heap_size = 0

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        self._heap_size = n
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def get_left_node(self, parent_node):
        left_child_node = 2 * parent_node
        return left_child_node

    def get_right_node(self, parent_node):
        right_child_node = 2 * parent_node + 1
        return right_child_node

    def min_heapify(self, parent_node):
        left_node = self.get_left_node(parent_node)
        right_node = self.get_right_node(parent_node)
        if left_node <= self._heap_size and self._data[left_node - 1] < self._data[parent_node - 1]:
            smallest = left_node
        else:
            smallest = parent_node
        if right_node <= self._heap_size and self._data[right_node - 1] < self._data[smallest - 1]:
            smallest = right_node
        if smallest != parent_node:
            self._data[parent_node - 1], self._data[smallest - 1] = self._data[smallest - 1], self._data[parent_node - 1]
            self._swaps.append((parent_node - 1, smallest - 1))
            self.min_heapify(smallest)

    def GenerateSwaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        heap = self._data[:]
        heapq.heapify(heap)
        print('correct answer', heap)
        for node in range(self._heap_size // 2, 0, -1):
            self.min_heapify(node)
        print('my result', self._data)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
