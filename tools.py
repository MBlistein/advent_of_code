import time


def time_execution(func):
    def decorated(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(f"Execution of {func.__name__} took {t2 - t1}s\n")
        return res

    return decorated
