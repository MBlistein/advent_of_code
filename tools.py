import time


def time_execution(func):
    def decorated(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(f"Execution took {t2 - t1}s\n\n")
        return res

    return decorated
