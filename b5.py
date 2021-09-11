import time 

def dumb():
    pass

class Stopwatch:
    def __init__(self, func=dumb, num_runs=10):
        self.func = func
        self.num_runs = num_runs

    def stopwatch(self):
        st = 0
        for i in range(self.num_runs):
            t0 = time.time()
            self.func()
            t1 = time.time()
            st += t1 - t0
        st /= self.num_runs
        print(st)

    def __call__(self, func, num_runs=10):
        self.func = func
        self.num_runs = num_runs
        self.stopwatch()

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.stopwatch()

obj = Stopwatch()

@obj
def temp():
    for i in range(1000000):
        pass

def temp1():
    for i in range(1000000):
        pass

with Stopwatch(temp1) as st:
    pass