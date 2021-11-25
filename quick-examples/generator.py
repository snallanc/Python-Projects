"""
Generators:
A simple and a powerful tool to create iterators. Uses yield to return each item of the sequence.
Automatically saves the state and index of the item returned in a given iteration to continue from
the next item(__next__()) in the next iteration.
"""

"""
EXAMPLE:
Compute sum of powers of 2: 2^0 + 2^1 + 2^2 + ....
"""

def getPowersOf2(length):
    for i in range(length):
        yield 2**i

def sumOfPowersOf2(length):
    sum = 0
    for n in getPowersOf2(length):
        sum += n
    print("Sum of powers of 2 of length {0} is {1}".format(length, sum))

sumOfPowersOf2(5)