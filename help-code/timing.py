# Author: John Landeholt [TA]
from time import time
import concurrent.futures
import random

def timing(f):
    """
        Usage:  @timing
                def your_function(args):
                    return 'YOUR RETURN'
    """
    def wrap(*args, **kw):
        times = 10000
        ts = time()
        future_list = []
        with concurrent.futures.ThreadPoolExecutor(max_workers = 13) as executor:
            for _ in range(times):
                future_list.append(executor.submit(f, *args))
            for fut in future_list:
                res = fut.result()

        te = time()
        avg_time = ((te - ts) / times) / 1e-3
        return print(f'function {f.__name__} took: {round(avg_time,3)}ms')

    return wrap

@timing
def linear_search(l, s):
    for x in l:
        if x == s: return x
    return None

if __name__ == '__main__':
    l = list(range(100000))
    random.shuffle(l)
    linear_search(l,42)