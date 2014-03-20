import hashlib

def create_checksum(path):
	print "Creating checksum for",path
	
	#Read in file, create checksum for file in line by line
	# Return complete checksum 
	fp = open(path)
	checksum=hashlib.md5() # bujlam nah
	while True:
		buffer=fp.read(1000);
		if not buffer: break
		checksum.update(buffer)
	fp.close()
	
	checksum=checksum.digest()
	return checksum



