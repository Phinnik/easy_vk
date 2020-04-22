import time


def delay(function):
    ''' Декоратор. Используется для задержки запросов api'''
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = function(*args, **kwargs)
        d = 1 / 3 - (time.time() - time_start)
        if d > 0:
            time.sleep(d)
        return result
    return wrapper