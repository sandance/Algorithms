import walking
from walking import walk

# This code will loop through all the nodes in the Graph

'''
Walk function returns a predeccessor map for the nodes it visited, and we collect those nodes in "comp" list.
"seen" is set to make sure we dont traverse from a node in one of the earlier components. 
'''


def components(G):			# The connected components 
	comp = []	
	seen = set()			# Keep track of all nodes that you have already seen
	for u in G:
		if u in seen:
			continue	# Seen ? Ignore it
		C=walk(G,u)		# Traverse Component
		seen.update(C)		# Add keys of C to seen
		comp.append(C)		# collect the
	return comp
		
	
