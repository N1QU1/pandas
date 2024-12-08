"""def trying_yield():
    yield "wow"
    yield "flipa"


itr = trying_yield()
print(next(itr))
print(next(itr))"""
def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b