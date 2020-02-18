'''
A utilitarian function
for defining a range of floats
that step by a float value
'''
def floatrange(start, stop, step):
    while start < stop:
        yield float(start)
        start += float(step)