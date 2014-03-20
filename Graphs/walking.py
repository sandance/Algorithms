#  Walk Function will traverse a single connected component( assuming the graph is connected)
#  To Find all the components , you need to wrap it in over the nodes
#
#


def walk(G,s,S=set()):				# Walk the Graph from node s
	P,Q = dict(), set()
	P[s] = None
	Q.add(s)
	while Q:
		u=Q.pop()				#Pick one, arbitarily
		for v in G[u].difference(P,S):	# new nodes
			Q.add(v)
			P[v]=u
	return P
	
