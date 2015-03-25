from functools import wraps

def fib(n):
	if n <2: return 1
	return fib(n-1) + fib(n-2)


def memo(func):
	cache = {}
	@wraps (func)
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return wrap


fib = memo(fib)
print fib(10)
