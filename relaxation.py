

inf = float('inf')

def relax(W,u,v,D,P):
	d = D.get(u,inf) + W[u][v] # possible shortcut estimate
	if d < D.get(v,inf):		# if it really a shortcut
		D[u],P[v] = d,u		# update estimate and parent
		return True		# There was a change
		
