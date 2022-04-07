class BaseCell: 
	x = -1
	y = -1
	neib = [] #L, R, U, D
	def __init__(self, x_, y_):
		self.x = x_
		self.y = y_
		self.neib = [0] * 4

	def unlockDirection(self, direction): 
		if (direction == 'L'): 
			self.neib[0] = 1
		if (direction == 'R'):
			self.neib[1] = 1
		if (direction == 'U'):
			self.neib[2] = 1
		if (direction == 'D'): 
			self.neib[3] = 1	