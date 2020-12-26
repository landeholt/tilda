# Author: John Landeholt [TA]
from itertools import repeat
import random
import timeit

REPEAT = 100
NUMBER = 100

def timing(f):
    
    def avg(coll):
        return sum(coll) / len(coll)
    def best_of(coll, n = 3):
        sorted_coll = sorted(coll)
        return sorted_coll[:n]
    def wrap(*args, **kw):
        def executor():
            return f(*args)
        t = timeit.repeat(executor, repeat= REPEAT, number= NUMBER)
        avg_t = avg(t)
        best_of_t = avg(best_of(t))
        print(f'function {f.__name__} executed in: {round(avg_t / 1e-3, 3)}ms best average: {round(best_of_t / 1e-3, 3)}ms')

        return executor()
    return wrap

if __name__ == '__main__':
    @timing
    def linear_search(l, s):    
        for x in l:
           if x == s: return x
        return None
    l = list(range(100000))
    random.shuffle(l)
    n = linear_search(l,42)
    print(n)