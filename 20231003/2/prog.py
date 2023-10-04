#type(1234)('23452')
def sub(obj1, obj2):
    if isinstance(obj1, list) or isinstance(obj2, tuple):
        return type(obj1)([el for el in obj1 if el not in obj2])
    return obj1 - obj2


print(sub(*eval(input())))