def dec_func(func):
    def new_function(*args, **kwargs):
        print("the runing function is ", func.__name__)
        rs = func(*args, **kwargs)
        print("the result is ", rs)
        return rs

    return new_function

def dec_func1(func):
    def new_function(*args, **kwargs):
        print("11the runing function is ", func.__name__)
        rs = func(*args, **kwargs)
        print("11the result is ", rs)
        return rs

    return new_function



@dec_func
@dec_func1
def add(a, b):
    return a + b


add(6,4)
