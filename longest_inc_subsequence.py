from itertools import combinations

def naive_lis(seq):
	for length in range(seq,0,-1):
		for sub in combinations(seq,length):
			if list(sub) == sorted(sub):	# Increasing sub sequence
				return sub 
