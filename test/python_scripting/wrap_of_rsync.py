import sys
from subprocess import call

source="/home/spartan/python_scripting"
target="/home/spartan/python_scripting/test"

rsync="rsync"
arguments="-a"

cmd="%s %s %s %s"%(rsync, arguments, source, target)

def sync():
	ret=call(cmd,shell=True)
	if ret !=0:
		print "rsync failed"
		sys.exit(1)

sync()

