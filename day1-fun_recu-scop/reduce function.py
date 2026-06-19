# reduce(func, iterable) — accumulate to single value
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product) # 40320 (8 factorial)