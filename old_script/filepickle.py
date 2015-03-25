import pickle

def savePickle(filename, object):
		#save object to a file
	file=popen(filename,'wb')
	pickle.dump(object,file) #pickle to binary file
	file.close()

def loadDbase(filename):
	file=open(filename,'rb')
	object=pickle.load(file) # unpickle from binary file
	file.close() # re-create objects in memory
	return object
