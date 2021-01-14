# simple factorial
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 12): # testing
    print(n, factorialFun(n))

# factorial using recursion return nth term result
# this module use for store last data in series so, it take less time

from functools import lru_cache

@lru_cache(maxsize = 1000)
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)

x=50
print(factorialFun(x))
for i in range(1,x):
    print(i, ":",factorialFun(i))
