

''' Topological sort based on Depth first search'''

def dfs_topsort(G):
	S,res = set(),[]
	def recurse(u):
		if u in S:
			continue
		S.add(u)
		for v in G[u]:			# Recurse through neighbours
			recurse(v)
		res.append(u)			# Finish with u? append it 
	for u in G:
		recurse(u)
	res.reverse()				#Its all backward so far
	return res				# res  , should be topological listing for that Graph G
	
	
