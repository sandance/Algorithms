
class Stack:
	def __init__(self):
			self.items = []
	def push(self,obj):
		self.items.append(obj)
	def pop(self):
		self.items.pop()
	def isEmpty(self):
		return self.items == []
	def size(self):	
		return len(self.items)





		
