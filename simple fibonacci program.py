# simple fibonacci series
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10): # testing
    print(n, "->", fib(n))

# fibonacci series using recursion return nth term result
# this module use for store last data in series so, it take less time
from functools import lru_cache

@lru_cache(maxsize = 1000)
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
x=50
print(fib(x))
for i in range(1,x):
    print(fib(i))
