class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data

class Queue:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.empty:
            return self.pop()
        else:
            raise StopIteration

    @property
    def empty(self):
        return len(self) == 0

    @property
    def peek(self):
        pass
    
    @staticmethod
    def build(*items):
        if len(items) > 0:
            q = Queue()
            for n in items:
                if n == "": continue
                q.push(n)
            return q

    def push(self, element):
        """ Create a node, link it up, increment size """
        pass
    
    def pop(self):
        """ check if not empty, find next node, relink, decrement size, return data """
        pass

    def remove(self):
        self.pop()
    
    def __repr__(self):
        s = ""
        p = self.head
        while p != None:
            s += p.data + ", "
            p = p.next
        s = s[:-2]
        return '[' + s + ']'
    
if __name__ == '__main__':
    q = Queue.build("John", "Landeholt")
    for n in q:
        print(n)

