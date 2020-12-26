import operator

class Heap:
    def __init__(self, max_size, compare = operator.lt):
        self.max_size = max_size
        self.array = [None]
        self.size = 0
        self.compare = compare

    def __len__(self):
        return self.size
    
    def __iadd__(self, other):
        if len(other) > 0:
            for n in other:
                self.insert(n)
            return self
    
    def __comp(self, parent, child):
        if self.array[parent] == None: return False
        return self.compare(self.array[parent], self.array[child])

    def __swap(self, left, right):
        self.array[left], self.array[right] = self.array[right], self.array[left]
    
    def __bubble_up(self, child_idx):
        while child_idx > 1:
            parent_idx = child_idx // 2
            if self.__comp(parent_idx, child_idx):
                return
            self.__swap(parent_idx, child_idx)
            child_idx = parent_idx

    def __bubble_down(self, parent_idx):
        while 2 * parent_idx <= len(self): 
            child_idx = 2 * parent_idx
            if child_idx + 1 < len(self) and self.__comp(child_idx + 1, child_idx):
                child_idx += 1
            if self.__comp(parent_idx, child_idx):
                return
            self.__swap(parent_idx, child_idx)
            parent_idx = child_idx

    @property
    def empty(self):
        return len(self) == 0
    
    @property
    def full(self):
        return len(self) == self.max_size

    def insert(self, node):
        if not self.full:
            self.size += 1
            self.array.append(node)
            self.__bubble_up(self.size)

    def pop(self):
        if not self.empty:
            data = self.array[1]
            self.array[1] = self.array[len(self)]
            self.array.pop()
            self.size -= 1
            self.__bubble_down(1)
            return data
        return None
    
    def peek(self):
        return self.array[1]
    
    def build(self, l):
        if len(l) > 0:
            for n in l:
                if not self.full:
                    self.insert(n)
        return None
class Max_heap(Heap):
    def __init__(self, max_size = 500):
        compare = operator.gt
        super().__init__(max_size = max_size, compare= compare)


class Min_heap(Heap):
    def __init__(self, max_size = 500):
        compare = operator.lt
        super().__init__(max_size = max_size, compare= compare)

if __name__ == '__main__':
    h = Min_heap()
    h.build([1,2,3,4,5,7,9])
    print(h.array)
    h += [10, 20, 100, 25]
    