# Author: John Landeholt [TA]
from time import time

def avg(l):
    return sum(l) / len(l)

def timing(f):
    """
        Usage:  @timing
                def your_function(args):
                    return 'YOUR RETURN'
    """
    def wrap(*args, **kw):
        times = []
        for _ in range(10000):
            ts = time()
            f(*args)
            te = time()
            times.append(te-ts)
        avg_time = avg(times) / 1e-3
        min_time = min(times) / 1e-3
        max_time = max(times) / 1e-3
        return print(f'function {f.__name__} took: {round(avg_time,3)}ms   max: {round(max_time,3)}ms, min: {round(min_time,3)}ms')

    return wrap