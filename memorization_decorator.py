from functools import wraps


def fib(i):
	if i < 2: return 1
	return fib(i-1) + fib(i-2)




def memo(func):
	cache={}   #dictionary					#stored subproblems solutions
	@wraps(func)					# Make wrap look like func
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args) 	# Compute & cache the solution
		return cache[args]
	return wrap


fib=memo(fib)
print fib(100)
