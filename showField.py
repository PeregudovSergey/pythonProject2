n = 10
m = 10
res = [[' '] * (2 * m + 1) for i in range(2 * n + 1)]	

for i in range(1, 2 * n + 1, 2):
	for j in range(1, 2 * m + 1, 2):
		res[i][j] = '■'
'''
for i in range(2 * m): 
	res[0][i] = ''
	res[-1][i] = '-'

for i in range(2 * n): 
	res[i][0] = '|'
	res[i][-1] = '|'
'''

for x in res: 
	print(*x, sep = '')