def add_integer(a, b=98):

    if isinstance(a&b, int):
        return TypeError(a,b,"must be integer or float")
    if isinstance(a&b, float):
        return int(a) + int(b)
    return a + b

'''
this project uses txt files for testing purposes

'''