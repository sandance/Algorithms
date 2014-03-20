''' 
Algorithm for running strongly connected components

	1. Dun dfs_topsort on the graph , resulting in a sequence "seq"
	2. Reverse all edges
	3. Run a full traversal , selecting starting points (in order) from seq

'''


#kosaraju’s Algorithm for Finding Strongly Connected Components


import topsort_dfs

from topsort_dfs import dfs_topsort



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
	for u in dfs_topsort():
		if u in seen:		# Ignore , node that already covered
			continue		
		C=walk(GT,u,seen)	# Dont go backward
		seen.append(C)
	return seen


	
	
