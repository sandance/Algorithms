from functools import wraps

def mydecorator(f):
	@wraps(f)
	def wrapped(*args,**kwargs):
		print "Befores decorated function"
		r = f(*args,**kwargs)
		print "After decorated function"
		return r
	return wrapped

@mydecorator
def myfunc(myarg):
	print "my function",myarg
	return "return value"

r=myfunc('asdf')
print r
