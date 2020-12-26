import operator

class Heap:
    """Generic heap"""
    def __init__(self, max_size, compare = operator.lt):
        self.max_size = max_size
        self.array = [None]
        self.size = 0
        self.compare = compare

    def __len__(self):
        return self.size
    
    def __iadd__(self, other):
        """ allows a heap to be extended with a new list """
        if len(other) > 0:
            for n in other:
                self.insert(n)
            return self
    
    def __comp(self, parent, child):
        return self.compare(self.array[parent], self.array[child])

    def __swap(self, left, right):
        self.array[left], self.array[right] = self.array[right], self.array[left]
    
    def __bubble_up(self, idx):
        """ When a item is inserted it gets 
            inserted at the last index and then gets pushed up to its
            correct position 
        """
        while idx > 1 and not self.__comp(idx // 2, idx):
            self.__swap(idx // 2, idx)
            idx //= 2

    def __bubble_down(self, idx = 1):
        """ When a item is removed the children of it gets 
            pushed down to its correct position
        """
        while 2 * idx <= len(self): 
            nidx = self.__nidx(idx)
            if not self.__comp(idx, nidx):
                self.__swap(idx, nidx)
            idx = nidx


    def __nidx(self, idx):
        """ Heap-condition: A parent [i] has children 2 * [i] and 2 * [i] + 1.
            Returns the child with best priority
        """
        if 2 * idx + 1 > len(self): return 2 * idx
        if self.__comp(2 * idx, 2 * idx + 1): return 2 * idx
        else: return 2 * idx + 1

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
            self.size -= 1
            self.array.pop()
            self.__bubble_down()
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
    