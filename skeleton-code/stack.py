# Author: John Landeholt [TA]
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data
        

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    @property
    def empty(self):
        return self.size == 0

    @property
    def peek(self):
        return self.head.data

    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.empty:
            return self.pop()
        else:
            raise StopIteration
    
    @staticmethod
    def build(*items):
        if len(items) > 0:
            stack = Stack()
            for n in items:
                if n == "": continue
                stack.push(n)
            return stack

    def push(self, element):
        """ Create node, link it up, increment size """
        # YOUR CODE HERE
        pass

    def pop(self):
        """ Check if not empty, find next node, relink, decrement size, return data """
        # YOUR CODE HERE
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
    s = Stack.build("John", "Landeholt")
    for n in s:
        print(n)
