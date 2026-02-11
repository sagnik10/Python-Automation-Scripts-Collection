import time

def timer(func):
    def inner(*a, **k):
        start = time.time()
        result = func(*a, **k)
        end = time.time()
        print(round(end - start, 5))
        return result
    return inner

@timer
def slow():
    time.sleep(0.2)

slow()