sum = 0
def add_binary(a,b):
    sum = a + b
    get_bin = lambda x: format(x, 'b')
    return f'{get_bin(sum)}'