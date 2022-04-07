from dsu import Dsu
from field import Field
from random import shuffle

class Builder: 	
	maze = Field(0, 0)

	def __init__(self):
		maze = Field(0, 0)

	def check(self, xx, yy): 
		return xx >= 0 and yy >= 0 and xx < self.maze.n and yy < self.maze.m

	def getIndex(self, xx, yy): 
		return xx * self.maze.m + yy

	def getIndexBack(self, index): 
		return [index // self.maze.m, index % self.maze.m]


	def buildMaze(self, mst): 		
		for i in range(len(mst)): 
			cell1 = self.getIndexBack(mst[i][0])
			cell2 = self.getIndexBack(mst[i][1])
			if cell1[0] > cell2[0]:
				mst[i][0], mst[i][1] = mst[i][1], mst[i][0]
			elif cell1[0] == cell2[0] and cell1[1] > cell2[1]:
				mst[i][0], mst[i][1] = mst[i][1], mst[i][0]
				
		self.maze.edges = mst
		for e in mst: 
			cell1 = self.getIndexBack(e[0])
			xx = cell1[0]
			yy = cell1[1]
			cell2 = self.getIndexBack(e[1])
			
			if xx == cell2[0]:
				#turn right				
				self.maze.field[xx][yy].unlockDirection('R')
				self.maze.field[xx][yy + 1].unlockDirection('L')
			else:
				#turn down
				self.maze.field[xx][yy].unlockDirection('D')
				self.maze.field[xx + 1][yy].unlockDirection('U')

		return self.maze 

	def findMstWithDsu(self):
		edges = []
		#right and down direction		
		for xx in range(n): 
			for yy in range(m):
				for direction in range(2): 
					xx1 = xx + dx[direction]
					yy1 = yy + dy[direction] 
					if self.check(xx1, yy1): 
						edges.append([self.getIndex(xx, yy), self.getIndex(xx1, yy1)])	

		shuffle(edges)
		data = Dsu(self.maze.n * self.maze.m)
		mst = [] 
		for e in edges:
			ok = data.unite(e[0], e[1])
			if ok: 
				mst.append(e)
		return mst

	def buildRandomMazeWithDsu(self, n, m): 		
		self.maze = Field(n, m)						
		
		edges = self.findMstWithDsu()		
		return self.buildMaze(edges)		


	def findMstWithDfs(self, x_cur, y_cur, used, edges): 		
		used[x_cur][y_cur] = 1
		dx = [0, 0, -1, 1]
		dy = [-1, 1, 0, 0]
		direction = [i for i in range(4)]
		shuffle(direction)
		for dr in direction: 
			x_next = x_cur + dx[dr] 
			y_next = y_cur + dy[dr]			
			if self.check(x_next, y_next) and not used[x_next][y_next]: 
				cell1 = [x_cur, y_cur]
				cell2 = [x_next, y_next]
				if cell1[0] > cell2[0]:
					cell1, cell2 = cell2, cell1
				elif cell1[0] == cell2[0] and cell1[1] > cell2[1]:
					cell1, cell2 = cell2, cell1

				edges.append([self.getIndex(cell1[0], cell1[1]), self.getIndex(cell2[0], cell2[1])])
				self.findMstWithDfs(x_next, y_next, used, edges)

	def buildRandomMazeWithDfs(self, n, m): 
		self.maze = Field(n, m)			
		
		edges = []
		used = [[0] * m for i in range(n)]

		self.findMstWithDfs(0, 0, used, edges)						

		return self.buildMaze(edges)
		
	def getField(self):
		return self.maze