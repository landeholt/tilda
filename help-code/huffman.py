from heap import Min_heap
from collections import defaultdict
# Author John Landehol [TA]

class Pair:
    def __init__(self, char, encoding = ''):
        self.char = char
        self.encoding = encoding
    
    def __iadd__(self, code):
        self.encoding = code + self.encoding
    
    def __repr__(self):
        return f'{self.char}: {self.encoding}'

class Huffman_node:
    def __init__(self, char, probability):
        self.pairs = [Pair(char)]
        self.probability = probability
        
    @staticmethod
    def merge(self, other):
        probability = self.probability + other.probability
        pairs = self.pairs + other.pairs
        self.pairs = pairs
        self.probability = probability
        return self
        
    def __lt__(self, other):
        return self.probability < other.probability
    
    def __repr__(self):
        return f'{self.pairs}: {self.probability}'
    
    def __getitem__(self, key):
        for pair in self.pairs:
            if pair.char == key:
                return pair.encoding
        return None

def huffman_encode(text):
    freq = defaultdict(int)
    heap = Min_heap()
    
    for c in text:
        freq[c] += 1
    for k,v in freq.items():
        n = Huffman_node(k,v)
        heap.insert(n)
    while len(heap) > 1:
        left, right = heap.pop(), heap.pop()
        for p in left.pairs:
            p += '0'
        for p in right.pairs:
            p += '1'
        n = Huffman_node.merge(left, right)
        heap.insert(n)
    encoding = ''
    node = heap.pop()
    for c in text:
        code = node[c]
        if code:
            encoding += code + ' '
    return encoding[:-1]

def huffman_decode(code, freq):
    heap = Min_heap()
    for k,v in freq.items(): heap.insert(Huffman_node(k,v))
    while len(heap) > 1:
        
        left, right = heap.pop(), heap.pop()
        for p in left.pairs: p += '0'
        for p in right.pairs: p += '1'
        n = Huffman_node.merge(left, right)
        heap.insert(n)
    decoding = ''
    node = heap.pop()
    for c in code.split():
        char = node[c]
        if char:
            decoding += char
    return decoding, freq

if __name__ == '__main__':
    encoding, freq = huffman_encode('HAHA!IIIIIIH!AHRG...')
    print(encoding)
    decoding = huffman_decode(encoding, freq)
    print(decoding)