#!/usr/bin/python

import sys
import os
import Queue
import time
import urllib2



#switch=list()

#def switch_list(argv):
#	print "processing " + argv



#if __name__=="__main__":
#        #basic_stuff(sys.argv[:3])
#        switch.append(sys.argv[3:])
#	for i in switch[0]:
#		switch_list(i)


hosts=["http://yahoo.com", "http://google.com", "http://amazon.com",
        "http://ibm.com", "http://apple.com"]

queue=Queue.Queue()
out_queue=Queue.Queue()

class ThreadUrl ( threading.Thread)
	def __init__(self, queue, out_queue):
		threading.Thread.__init__(self)
		self.queue = queue
		self.out_queue = out_queue
	def run(self):
		while True:
			#grab host from queue
			host = self.queue.get()

			#grabs urils of hosts and then grabs chunk of webpage
			url = urllib2.urlopen(host)
			chunk = url.read()

			#pace chunk into out queue
			self.out_queue.put(chunk)
			
			#signals to queue job is done
			self.queue.task_done()

	
class DatamineThread(threading.Thread):
		"""Threaded Url Grab"""
		def __init__(self, out_queue):
			threading.Thread.__init__(self)
			self.out_queue = out_queue
		def run(self):
			
