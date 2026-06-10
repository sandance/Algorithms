'''
Algorithm for running strongly connected components

	1. Run dfs_topsort on the graph, resulting in a sequence "seq"
	2. Reverse all edges
	3. Run a full traversal, selecting starting points (in order) from seq

'''


#kosaraju's Algorithm for Finding Strongly Connected Components


from topsort_dfs import dfs_topsort
from walking import walk



def tr(G):			# Transpose (rev edges of ) G
	GT = {}
	for u in G:
		GT[u] = set()
	for u in G:
		for v in G[u]:		# Go for all adjacent nodes in u
			GT[v].add(u)	# Add all reverse edges
	return GT


def scc(G):
	GT = tr(G)			# Get the transposed graph
	sccs,seen = list(),set()
	for u in dfs_topsort(G):	# Fixed: pass G to dfs_topsort
		if u in seen:		# Ignore nodes already covered
			continue
		C = walk(GT,u,seen)	# Walk transposed graph, not going to seen nodes
		seen.update(C)		# Fixed: mark all nodes in this SCC as seen
		sccs.append(set(C))	# Fixed: collect the SCC nodes
	return sccs			# Fixed: return sccs instead of seen



