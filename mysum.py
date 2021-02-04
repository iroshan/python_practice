def mysum(*args):
    """return the sum of the arguments supplied"""
    total = 0
    for i in args:
        total += i
    return total


assert mysum(2,3) == 5
assert mysum() == 0
assert mysum(1,2,3,4,5) == 15
