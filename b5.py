import time 

class Stopwatch:
    def __init__(self, num_runs=10):
        self.num_runs = num_runs

    def __call__(self, func, num_runs=10):
        self.func = func
        self.num_runs = num_runs
        st = 0
        for i in range(self.num_runs):
            t0 = time.time()
            self.func()
            t1 = time.time()
            st += t1 - t0
        st /= self.num_runs
        print(st)

    def __enter__(self):
        self.t0 = time.time()
        return self

    def __exit__(self, *args, **kwargs):
        self.t1 = time.time()
        print(self.t1 - self.t0)

@Stopwatch(num_runs=10)
def temp():
    for i in range(1000000):
        pass

with Stopwatch() as st:
    for i in range(1000000):
        pass
