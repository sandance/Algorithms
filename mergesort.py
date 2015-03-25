
import sys

def mergesort(seq):
	mid = len(seq)//2 		# middle point for division
	left,right = seq[:mid], seq[mid:]
	if len(left) > 1:
		left = mergesort(left)
	if len(right) > 1:
		right = mergesort(right)
	result = list()
	while left and right:
		if left[-1] >= right [-1]:  	   # Left has greatest last value
			result.append(left.pop())
		else:
			result.append(right.pop()) # Right has greatest value 
	result.reverse()			   # Result is backward
	return (left or right) + result            # Also add the remainder


if __name__=='__main__':
	srtlist=mergesort(sys.argv[1])
	print srtlist
