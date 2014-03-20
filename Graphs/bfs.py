''' Breadth first search '''

def bfs(G,s):	
	P,Q = {s:None} , deque([s])	# P is a dictionary here and Q is a Dubble ended queue
	while Q:
		u = Q.popleft()
		for v in G[u]:
			if v in P:	# Alreadu has parent
				continue
			P[v]=u		# Reached from u, so u is the parent
			Q.append(v)
	return P
