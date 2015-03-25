

inf = float('inf')

def relax(W,u,v,D,P):
	d = D.get(u,inf) + W[u][v]
	if d < D.get(v,inf):
		D[v],P[v] = d,u			# update estimate and parent
		return True


	





def bellman_ford(G,s):
	"""
		Input: 	Graph and starting vertex
		Output:	Distance from each vertex from starting vertex
	"""
	D,P = {s:0} , {} 			# Zero distance to s ; and no parents
	for rnd in G:				# n = len(G) rounds
		changed = False			# No changes in round so far
		for u in G:			# For every node in G
			for v in G[u]:		# adjacent nodes
				if relax(G,u,v,D,P):
					changed = True
		if not changed:
			break			# no change in round 
	else:
		raise ValueError('negative cycle')
	return D, P 
		



if __name__=='__main__':
	a, b, c, d, e, f, g, h = range(8)
	
	G = {
		a : { b: 2 ,c:1,d:3, e:9, f:4},
		b: {c:4, e:3},
		c: {d:8},
		d: {e:7},
		e: {f:5},
		f: {c:2, g:2, h:2},
		g: {f:1, h:6},
		h: {f:9, g:8}
	}
	
	print bellman_ford(G,a)
