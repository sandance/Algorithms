import sys
def binary_search():
	print "----------Binary Search-------"
	number=input("Enter num of elements?")
	array=[]
	for i in range(number):
		array.append(input("Enter number\t"))
	
	target =input("Enter target item?\t")
	
	low=0
	high=int(number)-1

	while low<=high:
		mid=(low+high)//2
		if array[mid]==target:
			print "Item",target,"Found at",mid
			sys.exit("Done")
		elif target < array[mid]:
			high= mid-1
		else:
			high=mid+1



binary_search()		
