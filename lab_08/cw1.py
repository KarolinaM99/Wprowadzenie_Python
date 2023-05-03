from timeit import timeit
import random
setup = """
from array import array
import random
"""
stmt1 = """
tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])
"""
stmt2 = """
list_of_floats = [random.random() for _ in range(1_000_000)]
"""
print(timeit(stmt1, setup, number=100))
print(timeit(stmt2, setup, number=100))

stmt3 = """
tab_of_ints = array('B', [random.randint(0,255) for _ in range(1_000_000)])
"""
stmt4 = """
list_of_ints = [random.randint(0,255) for _ in range(1_000_000)]
"""

print(timeit(stmt3, setup, number=100))
print(timeit(stmt4, setup, number=100))
