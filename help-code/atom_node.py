# Author John Landeholt [TA]
from enum import Enum
class Type(Enum):
    na = 0
    num = 1
    lower = 2
    upper = 3
    left_parenthesis = 4
    right_parenthesis = 5
    zero = 6

class Atom_node:
    def __init__(self, data):
        self.next = None
        self.data = data
        self.type = self.__get_type()

    def __get_type(self):
        """ In lab 8 we will check whether a node is any of theses types.
            Combined with a Queue that can check for a specific peek, 
            it will ease the code

            Usage:
            if queue.peek(Type.num):
                queue.pop()
            

            ...

            class Atom_queue(Queue):
                ...

                def peek(self, t = Type.na):
                    # confirm if head is of type t
        """
        if self.data == '0': return Type.zero
        elif self.data.isnumeric(): return Type.num
        elif self.data.islower(): return Type.lower
        elif self.data.isupper(): return Type.upper
        elif self.data == '(': return Type.left_parenthesis
        elif self.data == ')': return Type.right_parenthesis
        else: return Type.na