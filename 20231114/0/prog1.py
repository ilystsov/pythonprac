def debug(fun):
    @wraps
    def wrapper(*args):
        print('<', *args)
        res = fun(*args)
        print('>', res)
        return res
    return wrapper

@debug
def mult(a, b):
    return a * b
