# Fibonacci Sequence Generator
# Have the user enter a number and
# generate a fibonacci sequence
# which size is equivalent to that number.

def finacciseq(n)
    assert n>0
    series = [1]

    while len(series) < n:
