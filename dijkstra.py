from heapq import heappush, heappop

inf = float('inf')



"""
	We look for an improvement to the currently known distance to v by trying 
	to take a shortcut throught u .

		if there is any shortcut we register new distance and parent
		if not continue
"""

def relax(W,u,v,D,P):
	d = D.get(u,inf) +  W[u][v] 
	if d < D.get(v,inf):
		D[v],P[v] = d, u
		return True



def dijkstra(G,s):
	D,P,Q,S = {s:0} , {} , [(0,s)], set()		# Estimated distance, tree, queue , visited
	
	while Q:					# Still unprocessed nodes ?
		_,u = heappop(Q)			# node with lowest estimate
		if u in S:				# already visited ? skip it
			continue			# we have visited it now
		S.add(u)				
		for v in G[u]:				#Go through all its neighbors
			relax(G,u,v,D,P)		# Relax out out-edge
			heappush(Q, (D[v],v))		# add to queue with respect to pririty
	return D, P 

if __name__=='__main__':

	a, b, c, d, e, f, g, h = range(8)
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

	print dijkstra(G,a)




