import numpy

# Read the space-separated integers that describe the shape of the array.
# Example: "3 3 3" -> shape (3, 3, 3)
shape = tuple(int(x) for x in input().split())

# numpy.zeros creates a new array of the given shape filled with 0's.
# dtype=int forces the integer type (the default would be float).
print(numpy.zeros(shape, dtype=int))

# numpy.ones creates a new array of the given shape filled with 1's.
print(numpy.ones(shape, dtype=int))
