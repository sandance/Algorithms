#!/bin/bash

	echo "Copying data...........from 10.255.0.234"
	rsync -rR  /san/vzwrawdata/{ARCHIEVE,CURRNET,QUEUEU}/./*/201306/20130616   airsage@10.255.6.201:/opt/disk1/vzwrawdata/
	
	
	echo "done ....."




