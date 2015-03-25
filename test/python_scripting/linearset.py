class Set:
	def __init__(self):
		self._theElements = List()
	# returns the number of items in the set
	def __len__(self):
		return len(self._theElements)
	#determines if an element is in the set
	def __contains__(self,element):
		return element in self._theElements
	# Add a new unique element to the set
	def add(self,element):
		if element not in self:
			self._theElements.append(element)
	
	#Removes an element from the set
	def remove(self,element):
		assert element in self, "The element must be in the set"
		self._theElements.remove(element)
	def __eq__(self,setB):
		if len(self) !=len(setB):
			return False
		else:
			return self.isSubsetOf(setB)


