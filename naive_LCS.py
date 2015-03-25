from itertools import combinations

def naive_lis(seq):
	for length in range(len(seq),0,-1):
		for sub in combinations(seq,length): 
			if list(sub) == sorted(sub):
				return sub
