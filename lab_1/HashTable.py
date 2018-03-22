import BinaryTree as tree


class HashTable:
    def __init__(self, capacity=288):  # size of printable characters = 96; 96 * 3 = 288
        self.capacity = capacity
        self.size = 0
        self.table = [tree.BinaryTree() for i in range(capacity)]

    def _hash_func(self, value):
        return sum([(ord(c) - ord(' ') + 1) for c in value[:3]])

    def put(self, value):
        self.table[self._hash_func(value)].put(value)
        self.size += 1

    def find(self, value):
        node = self.table[self._hash_func(value)].find(value)
        if node is not None:
            return node.data
        else:
            return None

    def print(self):
        for i in range(self.capacity):
            print('Num of cell: ' + str(i))
            self.table[i].print_tree()
