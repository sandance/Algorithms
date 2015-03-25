#implement the array ADT using array capabilities of the 
#ctype module
import ctypes

class Array:
	# create an array with size elements
	def __init__(self,size):
		assert size>0, " Array size must be >0"
		self._size=size
		#create array structure using the ctype
		pyArrayType=ctypes.py_object * size
		self._elements =pyArrayType()
		#Initialize each element
		self.clear(None)

	# Return the size of the Array	
	def __len__(self):
		return self._size

	#Get the contents of the index element.
	def __getitem__(self,index):
		assert index >= 0 and index < len(self) , "Array subscript outof range"
		return self._elements[index]
	
	#clears the arry by setting each element to the given value
	def clear(self,value):
		for i in range(len(self)):
			self._elements[i]=value
		
