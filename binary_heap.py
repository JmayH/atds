class BinaryHeap():

    def __init__(self):
        self.heap_list = [0]
        
    def insert(self, value):
        self.heap_list.append(value)
        self.percolate_up(self.size())

    def percolate_up(self, i):
        while i // 2 > 0:
            parent = i // 2
            if self.heap_list[i] < self.heap_list[parent]:
                self.heap_list[i], self.heap_list[parent] = self.heap_list[parent], self.heap_list[i]
            i = parent

    def del_min(self):
        if self.is_empty():
            return None
        min_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.heap_list.pop()
        if not self.is_empty():
            self.percolate_down(1)

        return min_value

    def percolate_down(self, i):
        while i * 2 <= self.size():
            min_child = self.min_child(i)

            if self.heap_list[i] > self.heap_list[min_child]:
                self.heap_list[i], self.heap_list[min_child] = \
                    self.heap_list[min_child], self.heap_list[i]

            i = min_child

    def min_child(self, i):
        left_child = i * 2
        right_child = i * 2 + 1

        if right_child > self.size():
            return left_child
        else:
            if self.heap_list[left_child] < self.heap_list[right_child]:
                return left_child
            else:
                return right_child

    def find_min(self):
        if self.is_empty():
            return None
        return self.heap_list[1]

    def is_empty(self):
        return len(self.heap_list) - 1 == 0

    def size(self):
        return len(self.heap_list) - 1

    def build_heap(self, list_of_keys):
        self.heap_list = [0] + list_of_keys[:]

        i = self.size() // 2

        while i > 0:
            self.percolate_down(i)
            i -= 1

    def __repr__(self):
        return "BinaryHeap:" + str(self.heap_list)


def main():
    print("Demonstrating minHeap binary tree")

    bh = BinaryHeap()

    bh.insert(5)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)
    bh.insert(1)
    bh.insert(50)
    bh.insert(15)

    print("Heap after insertions:")
    print(bh)

    print("Minimum value:")
    print(bh.find_min())

    print("Deleted minimum:")
    print(bh.del_min())

    print("Heap after deleting minimum:")
    print(bh)

    print("\nBuilding heap from list:")
    bh2 = BinaryHeap()
    bh2.build_heap([9, 5, 6, 2, 3])

    print(bh2)
    print("Minimum value:")
    print(bh2.find_min())

if __name__ == "__main__":
    main()