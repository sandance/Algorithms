#Topological sort of a Directed Acyclic graph

# Straigt forward adjacency set representation
#	N = [ {b,c,d,e,f}, {c,e},{d},{e},{f},{c,g,h},{f,h},{f,g} ]

# Adjacency list:  N = [ [b,c,d,e,f], [c,e],[d],[e],[f],[c,g,h],[f,h],[f,g] ]




def topsort(G):
	count = dict((u,0) for u in G) 				# The in -degree for each node
	for u in G:						# For each node in G
		for v in G[u]:					# For each adjacent node in G
			count[v] +=1 				# changing degree
	Q = [ u for u in G if count[u] == 0]			# Find a node which has degree 0 , this could be one to start with
	S = list()
	while Q:						# Start with the queue
		u = Q.pop()
		S.append(u)
		for v in G[u]:					# all adjacent node of node u 
			count[v] -=1
			if count[v] == 0:
				Q.append(v)
	return S
