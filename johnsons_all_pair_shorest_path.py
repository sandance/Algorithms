from heapq import heappush,heappop

"""
	Algorithm:
		1. Let the given graph be G. Add a new vertex "s" to the graph, add edges from new vertex to all vertices of G. Let the modified Graph be G'
		2. Run Bellman ford Algorithm on G' with "s" as source. Let the distance calculated by Bellman Ford be h[0],h[1],h[2]..h[V-1]. If we find a negative weight cycle , then return
		3. Reweight the edges of Original Graph G. For each edge(u,v) assign the new weight as "original weight" + h[u] - h[v]
	
		4. Remove the added vertex "s" and run Dijkstra's Algorithm for every vertex

"""

#from heapq import heappush,heappop

inf = float('Inf')

def relax(W,u,v,D,P):
	d = D.get(u,inf) + W[u][v] # D.get(key,default=None) , if no key value , it looks with default
	
	if d < D.get(v,inf):
		D[v],P[v] = d,u
		return True

def dijkstra(G,s):
	D,P,Q,S = {s:0},{},[(0,s)],set()
	
	while Q:
		_, u = heappop(Q)	# node with lowest distance
		if u in S:
			continue
		S.add(u)
		for v in G[u]:
			relax(G,u,v,D,P)	# check if lower cost edge it possible
			heappush(Q,(D[v],v))	# add to queue with respect to priority
	return D, P




def bellman_ford(G,s):
	"""
		Input: Graph and starting vertex
		Output:	Distance from each vertex from starting vertex
	"""
	
	D,P = { s: 0 }, {}	# Zero distances to s and no parents
	# iterate over the graph with the range of number of vertices
	for rnd in G:			# n = len(G) rounds
		changed = False
		for u in G:
			for v in G[u]:
				if relax(G,u,v,D,P):
					changed = True
		# after checking all adjacent vertices of each node
		if not changed: # false remains intact
			break	# no change in this rnd 
	else:
		raise ValueError('negative cycle')
	return D,P



from copy import deepcopy

def johnson(G):
	G = deepcopy(G)			# dont want to break original
	s = object()			# 
	G[s] = { v : 0 for v in G } 	# Edges from s have zero wgt
	h, _ = bellman_ford(G,s)
	del G[s]			# delete that extra vertex
	
	for u in G:
		for v in G[u]:
			G[u][v] += h[u] - h[v] 	# weights are adjusted so they are not nonnegative
	D,P = {},{}
	for u in G:
		D[u],P[u] = dijkstra(G,u)	# shortes path from each node 
		for v in G[u]:
			D[u][v] += h[v] - h[u]	# readjust the distance
	return D, P
				
		

def test_johnson():
    """
    >>> a, b, c, d, e = range(5)
    >>> W = {
    ...     a: {c:1, d:7},
    ...     b: {a:4},
    ...     c: {b:-5, e:2},
    ...     d: {c:6},
    ...     e: {a:3, b:8, d:-4}
    ... }
    >>> D, P = johnson(W)
    >>> [D[a][v] for v in [a, b, c, d, e]]
    [0, -4, 1, -1, 3]
    >>> [D[b][v] for v in [a, b, c, d, e]]
    [4, 0, 5, 3, 7]
    >>> [D[c][v] for v in [a, b, c, d, e]]
    [-1, -5, 0, -2, 2]
    >>> [D[d][v] for v in [a, b, c, d, e]]
    [5, 1, 6, 0, 8]
    >>> [D[e][v] for v in [a, b, c, d, e]]
    [1, -3, 2, -4, 0]
    """


if __name__=='__main__':
	
	a,b,c,d,e,f,g,h = range(8)
	
	G = {
		a: {b:2, c:1, d:3, e:9, f:4},
		b: {c:4, e:3},
		c: {d:8},
		d: {e:7},
		e: {f:5},
		f: {c:2, g:2, h:2},
		g: {f:1, h:6},
		h: {f:9, g:8}
	}
#	print G
	D,P=johnson(G)
	print D,P
