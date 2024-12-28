# def function
#
#sequence = [a,b,c,d]
#
#Syntax: 
#   filter(function, sequence)

def is_even(x):
    return x%2 == 0

def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if not function:
        return [i for i in iterable if i]
    return [i for i in iterable if function(i)] # list comprehension


a = [1, 2, 3, 4, 5, 6]
b = ft_filter(lambda x: x % 2 == 0, a)
print(list(b))
