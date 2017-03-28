#import the functions and use accordingly

#---------------------------------------------------------------------------------------------

def my_map(myFunc, myIterable):
    return list(myIterable) if myFunc is None else [myFunc(i) for i in myIterable]

#---------------------------------------------------------------------------------------------

def my_reduce(myFunc, myIterable, initializer = None):
    myIterable = iter(myIterable)
    try:
        x = myIterable.next() if initializer is None else initializer
    except StopIteration:
        raise TypeError("got error")
    for i in myIterable:
        x = myFunc(x, i)
    return x

#---------------------------------------------------------------------------------------------

def my_filter(func, iterable):
    if func is None:
        result = [i for i in iterable if i]
    else:
        result = [i for i in iterable if func(i)]

    if type(iterable) == tuple:
        return tuple(result)
    elif type(iterable) == str:
        return "".join(result)
    return result

#---------------------------------------------------------------------------------------------
