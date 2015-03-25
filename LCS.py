

def rec_lis(seq):
	@memo
	def L(cur):
		res = 1
		for pre in range(cur):
			if seq[pre] <= seq[cur]:
				res = max(res, 1+ L(pre))
		return res
	return max(L(i) for i in range(len(seq)))
