import tarfile,os

tar=tarfile.open("test.tar","w")

for root, dir, files in os.walk(os.curdir):
	for file in files:
		fullpath=os.path.join(root,file)
		print "pathname ", fullpath
		print "filename ", file


tar.close()


