class Heap:
    def __init__(self, d):
        self.key = []
        self.size = 0
        self.d = d

    def is_empty(self):
        return 1 if self.size == 0 else 0

    def parent(self, i):
        return (i - 1) // self.d

    def kth_child(self, i, k):
        return self.d * i + k

    def insert(self, value):
        self.size += 1
        self.key.append(value)
        self.heap_up(self.size-1)

    def find_min(self):
        if (self.is_empty()):
            print("Array underflow")
            return

        return self.key[0]

    def pop(self):
        if (self.is_empty()):
            print("Array underflow")
            return

        self.size -= 1
        tmp = self.key.pop(0)
        if self.size:
            self.heap_down(0)
        return tmp

    def heap_down(self, hole):
        tmp = self.key[hole]
        while(self.kth_child(hole, 1) < self.size):
            child = self.smallest_child(hole)
            if (self.key[child] < tmp):
                self.key[hole] = self.key[child]
                hole = child
            else:
                break
        self.key[hole] = tmp

    def heap_up(self, hole):
        tmp = self.key[hole]
        while((hole > 0) and (tmp < self.key[self.parent(hole)])):
            self.key[hole] = self.key[self.parent(hole)]
            hole = self.parent(hole)
        self.key[hole] = tmp

    def smallest_child(self, hole):
        best_child_yet = self.kth_child(hole, 1)
        k = 2
        candidate_child = self.kth_child(hole, k)
        while((k <= self.d) and (candidate_child < self.size)):
            if(self.key[candidate_child] < self.key[best_child_yet]):
                best_child_yet = candidate_child
            k += 1
            candidate_child = self.kth_child(hole, k)

        return best_child_yet

    def print_heap(self):
        print("Heap = ", end='')
        for i in range(self.size):
            print(self.key[i], end="\t")
        print()
