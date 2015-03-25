''' This function is Depth First search's recursive implimentation'''

def dfs_recursive(G,s,S=None):
		if S is None:
			S=set()
		S.add(s)			# Visited s
		for u in G[s]:			# Explore s's neighbours
			if u in S:		# Already explored ?
				continue 
			dfs_recursive(G,u,S)	# Explore recursively
