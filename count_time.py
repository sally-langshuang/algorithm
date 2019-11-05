import time

class count_time:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        rst = self.func(*args, **kwargs)
        use_time = time.time() - start_time
        print(use_time, "s used in %s function." % self.func.__name__ )
        return rst

if __name__ == '__main__':
    @count_time
    def test_func():
        time.sleep(1.2)

    test_func()
    

