class Dsu: 
	root = []
	siz = []
	def __init__(self, n):		
		self.root = [u for u in range(n)]
		self.siz = [1] * n

	def get(self, u): 		
		if self.root[u] == u: 
			return u
		rt = self.get(self.root[u])
		self.root[u] = rt
		return self.root[u]

	def unite(self, u, v): 		
		u = self.get(u)
		v = self.get(v)
		if u == v: 
			return False 
		if self.siz[u] < self.siz[v]:
			u, v = v, u
		self.root[v] = u
		self.siz[u] += self.siz[v]
		return True