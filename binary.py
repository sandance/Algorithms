class Node():
	left=None
	right=None
	def __init__(self,key,value):
		self.key = key
		self.value = value

def insert(node,key,value):
	if node==None:
		Node(key,value)
	if node.key == key:
		node.value=value
	elif key < node.key:
		node.left = insert(node.left,key,value)
	else
		node.right = insert(node.right,key,value)

