import time
def timer(func):
    def inner():
        start = time.time()
        func()
        time.sleep(1)
        print(time.time() - start)
    return inner

@timer   #==> func1 = timer(func1)
def func1():
    print('in func1')
func1()