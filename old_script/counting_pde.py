import datetime
import sys
import threading
import os,os.path
import gzip

days=list()
day_map=dict()
switch=list()


# multi- threading to speed up whole process

















# multiple thread will call this part of the code and insert the output into dictionary

def subscriber_count(sw_name):
	day=days.pop() # i want to take one day and delete that from the list
	subs=set()
	filedir='/mnt/glusterfs/hp/pde_data/'+str(sw_name)+'/'+str(day) +'/' # any file name inside that directory 
	for subdir,dirs,files in os.walk(filedir):
		for fs in files:
                	filepath=os.path.join(subdir,fs)
               		 packpath=gzip.open(filepath)
			for line in packpath:
                		line = line.strip().split(',')
                       		 #subscriber_id=token[1]
				if line[0] == "sub1":
					continue
				if len(line) < 5:
					continue
				subscriber_id = line[5]
				subs.add(subscriber_id)
				day_map(day) = len(subs) # adding day_map['20131001']=10000   	
			



def basic_stuff(argv):
	start_date=sys.argv[1]
        end_date=sys.argv[2]
        startdate=datetime.date(int(start_date[0:4]),int(start_date[4:6]),int(start_date[6:]))
        enddate=datetime.date(int(end_date[0:4]),int(end_date[4:6]),int(end_date[6:]))
	while startdate <= enddate:
		days.append((str(startdate)).replace('-',''))
		startdate += datetime.timedelta(days=1)
	

if __name__=="__main__":
	basic_stuff(sys.argv[:3])
	switch.append(sys.argv[3:])
        for i in switch[0]:
                subscriber_count(i)
	#print days
