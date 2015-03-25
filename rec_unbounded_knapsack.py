

def rec_unbounded_knapsack(w,v,c):
	@memo
	def m(r):
		if r == 0: return 0
		val = m(r-1)
		for i,wi in enumerate(w):
			if wi > r: continue
			val = max(val,v[i] + m(r-wi)
		return val
	return m(c)


def iter_unbounded_knapsack(w,v,c):
	m = [0]
	for r in range(1,c+1):
		val = m[r-1]
		for i,wi in enumerate(w):
			if wi > r:
				continue
			val = max(val , v[i] + m[r-wi])
		m.append(val)
	return m[c]
