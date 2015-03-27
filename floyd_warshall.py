
def memo(func):
	cache = {}
	@wraps(func)
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return wrap




def rec_floyd_warshall(G):
	@memo
	def d(u,v,k):	# u to v via 1...k
		if k == 0:
			return G[u][v]	# assume v in G[u]
		return min(d(u,v,k-1),d(u,k,k-1) + d(k,v,k-1))
	return { (u,v): d(u,v,len(G)) for u in G for v in G }



from copy import deepcopy
"""
def floyd_warshall(G):
	D = deepcopy(G)		# no intermediates yet
	for k in G:
		for u in G:
			for v in G:
				D[u][v] = min(D[u][v], D[[u,k],[k,v])
	return D

"""

inf =  float('Inf')

def floyd_warshall(G):
	D,P = deepcopy(G), {}
	for u in G:
		for v in G:
			if u ==v or G[u][v] == inf:
				P[u,v] = None
			else:	
				P[u,v] = u
	for k in G:
		for u in G:
			for v in G:
				shortcut = D[u][k] + D[k][v]
				if shortcut < D[u][v]:
					D[u][v] = shortcut
					P[u,v] = P[k,v]
	return D,P
