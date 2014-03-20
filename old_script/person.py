
class Person:
	def __init__(self,name,job,pay=0):
		self.name=name
		self.job=job
		self.pay=pay
	def tax(self):
		return self.pay * 0.25
	def info(self):
		return self.name, self.job, self.pay, self.tax()

def __get_attr__(self,attr):
	if attr=='tax':
		return self.pay * 0.30
	else:
		raise AttributeError()


