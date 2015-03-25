def dfs_iterative(G,s):
	S,Q = set(),[]
	Q.append(s)			#Started on visiting s
	while Q:
		u = Q.pop()		# Get one and explore it
		if u in S:
			continue
		S.add(u)
		Q.extend(G[u]) 		# Schedule all its neighbours
		yield u 		# Report u as visited
		
