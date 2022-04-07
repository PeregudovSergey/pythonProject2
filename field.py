from cell import BaseCell

	

class Field: 
	n = 0
	m = 0
	start = []
	finish = []

	field = []
	path = []	
	edges = []

	

	def __init__(self, n_, m_):
		self.n = n_
		self.m = m_
		self.start = [-1, -1]
		self.finish = [-1, -1]
		self.field = [[BaseCell(i, j) for i in range(n_)] for j in range(m_)]	
		
	def check(self, xx, yy): 
		return xx >= 0 and yy >= 0 and xx < self.n and yy < self.m  

	def findPathToFinish(self, xx, yy, used):
		dx = [0, 0, -1, 1]
		dy = [-1, 1, 0, 0]	
		self.path.append([xx, yy])
		used[xx][yy] = 1
		if [xx, yy] == self.finish: 
			return True

		OK = False
		for direction in range(4): 
			xx1 = xx + dx[direction]
			yy1 = yy + dy[direction]
			if self.check(xx1, yy1) and self.field[xx][yy].neib[direction] == 1 and not used[xx1][yy1]: 
				ok = self.findPathToFinish(xx1, yy1, used)
				OK |= ok
				if ok: 
					break
		if OK: 
			return True
		self.path.pop()
		return False
	
	def showField(self):		
		wall = '⬛'
		empty = '  '

		symb_end = '🏁'	
		symb_start = '⬜'	

		res = [[wall] * (2 * self.m + 1) for i in range(2 * self.n + 1)]	
		for i in range(1, 2 * self.n + 1, 2):
			for j in range(1, 2 * self.m + 1, 2):
				res[i][j] = empty

		dx = [0, 0, -1, 1]
		dy = [-1, 1, 0, 0]

		for xx in range(self.n):
			for yy in range(self.m):
				for direction in range(4):
					if self.field[xx][yy].neib[direction]:
						xx1 = 2 * xx + 1 + dx[direction]
						yy1 = 2 * yy + 1 + dy[direction] 
						res[xx1][yy1] = empty
		

		xf = self.finish[0]
		yf = self.finish[1]

		xs = self.start[0]
		ys = self.start[1]
		if xf != -1:
			res[xf * 2 + 1][yf * 2 + 1] = symb_end

		if xs != -1:
			res[xs * 2 + 1][ys * 2 + 1] = symb_start

		if len(self.path):
			last = self.path[0]			
			for i in range(1, len(self.path)):
				new_last = self.path[i]
				xx = last[0] * 2 + 1
				yy = last[1] * 2 + 1 

				xx1 = new_last[0] * 2 + 1
				yy1 = new_last[1] * 2 + 1

				if (i != len(self.path) - 1):
					res[xx1][yy1] = symb_start

				if xx1 == xx: 
					add = (yy1 - yy) // 2
					res[xx][yy + add] = symb_start
				else: 
					add = (xx1 - xx) // 2
					res[xx + add][yy] = symb_start

				last = new_last

		if (xs != -1):
			res[xs * 2 + 1][ys * 2 + 1] = '🟥'	
		return res

	def getString(self): 
		ms = self.showField()
		res = ""
		for x in ms: 
			for y in x: 
				res += y
			res += '\n'
		return res

	def setStart(self, xx, yy):
		self.start = [xx, yy]

	def setFinish(self, xx, yy): 
		self.finish = [xx, yy]

	def buildPath(self):
		used = [[0] * self.m for i in range(self.n)]
		self.findPathToFinish(self.start[0], self.start[1], used)

	