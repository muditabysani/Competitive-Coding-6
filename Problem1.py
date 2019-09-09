class Solution:
	def letterCasePermutation(self, S):
		"""
		:type S: str
		:rtype: List[str]
		"""
		res = []
		if S == None or len(S) == 0:
			return res
		res.append("")
		for ch in S:
			if ch.isdigit():
				res = [i + ch for i in res]
			else:
				res = [i + j for i in res for j in [ch.upper(), ch.lower()]]
		return res