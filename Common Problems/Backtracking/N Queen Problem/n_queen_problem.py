def initialize(n,board):
	for key in['queen','row','col','nwtose','swtone']:
		board[key] = {}
	for i in range(n):
		board['queen'][i] = -1
		board['row'][i] = 0
		board['col'][i] = 0
	
	# the diagonal from north-west to south east
	for i in range(-(n-1),n):
		board['nwtose'][i] = 0

	# the diagonal from south-west to north east
	for i in range(2*n-1):
		board['swtone'][i] = 0


def printboard(board):
	l=[[" " for i in range(7)] for j in range(7)]
	for row in sorted(board['queen'].keys()):
		#print((row,board['queen'][row]))
		l[row][board['queen'][row]] = 'Q'
	for i in range(len(board['queen'].keys())):
		print('', end='|')
		for j in range(len(board['queen'].keys())):
			print(l[i][j], end='|')
		print('')
		
		
def free(i,j,board):
	return(board['row'][i] == 0 and board['col'][j] == 0 and
		board['nwtose'][j-i] == 0 and board['swtone'][j+i] == 0)


def addqueen(i,j,board):
	board['queen'][i] = j
	board['row'][i] = 1
	board['col'][j] = 1
	board['nwtose'][j-i] = 1
	board['swtone'][j+i] = 1


def undoqueen(i,j,board):
	board['queen'][i] = -1
	board['row'][i] = 0
	board['col'][j] = 0
	board['nwtose'][j-i] = 0
	board['swtone'][j+i] = 0


def placequeen(i,board):
	n = len(board['queen'].keys())
	for j in range(n):

		# Checking if the (i,j) is free or not for queen placement
		if free(i,j,board):

			# adding if free
			addqueen(i,j,board)
			
			# if end of row is reached and we had placed all the queens
			if i == n-1:
				return(True)

			# else continue placing the queen
			else:
				extendsoln = placequeen(i+1,board)
			if extendsoln:
				return(True)
			else:
				undoqueen(i,j,board)
	# if all the rows are over and tried all the possible position but unable to place queen
	else:
		return(False)


board = {}
n = int(input())
initialize(n,board)
placequeen(0,board)
printboard(board)