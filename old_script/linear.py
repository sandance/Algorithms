#!/usr/bin/python
import sys
num=input("Num of elements?")
print num
array=[]
for i in range(num):
	array.insert(i,input("Insert number"))
print array
target=input("Enter the search element")
for i in range(num):
	if array[i]==target:
		print "Item Found"
		sys.exit("Done")

print "Item not found"


