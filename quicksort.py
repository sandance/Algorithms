
import sys


# A straight forward implementation of partition and select

def partition(seq):
	pi,seq = seq[0] , seq[1:] 	      # Pick and remove the pivot
	lo = [ x for x in seq if x <= pi ]    # All small elements
	hi = [ x for x in seq if x > pi  ]    # All larger elements than pivot
	return lo,pi,hi			      # Put pi (pivot) in the right place :P
	


def quicksort(seq):
	if len(seq) <=1:
		return seq				# Base case in divide and conquer problem
	lo,pi,hi = partition(seq)
	return quicksort(lo) + [pi] + quicksort(hi) 	# sort lo and hi separately




if __name__=='__main__':
	result = quicksort(sys.argv[1])
	print result
