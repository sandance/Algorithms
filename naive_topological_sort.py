def naive_topsort(G,S=None):
	if S in None:
		S = set(G)			# Default: All nodes
	if len(S) ==1: return list(S)		# Base case, single node
	v=S.pop()				# Reduction,remove a node
	seq=naive_topSort(G,S)			# Recursion, assumption: (n-1)
	min_i = 0
	for i,u in enumerate(seq):
		if v in G[u]:
			min_i = i+1		# After all dependencies
	seq.insert(min_i,v)
	return seq(min_i,v)
#The problem is that it chooses an arbitrary node at each step, which means
#that it has to look where the node fits after the recursive call (which gives the linear work).
