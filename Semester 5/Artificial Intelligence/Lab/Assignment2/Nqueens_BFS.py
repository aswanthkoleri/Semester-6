from copy import copy, deepcopy
N=8
sols=0
class Board:
	"""docstring for Board"""
	def __init__(self, board,col,steps):
		self.board = board
		self.col=col
		self.steps=steps
	def displayBoard(self):
		for row in self.board:
			for ele in row:
				print(ele,end=' ')	
			print()

	def getBoard(self):
		return self.board
	def getCol(self):
		return self.col
	def getSteps(self):
		return self.steps


def printBoard(board):
	for row in board:
		for ele in row:
			if ele==-1:
				print(0,end=' ')
			else:
				print(ele,end=' ')	
		print()


def markDangerous(board,row,col):
	# First right 
	i=col+1
	while i<N:
		board[row][i]=-1
		i+=1
	# lower diagonal
	i=row+1
	j=col+1
	while i<N and j<N:
		board[i][j]=-1
		i+=1
		j+=1
	# upper diagonal
	i=row-1
	j=col+1
	while i>=0 and j<N:
		board[i][j]=-1
		i-=1
		j+=1
	return board

def main():
	a=[[0]*N for i in range(N)]
	board1=Board(a,0,0)
	queue = []
	queue.append(board1);
	solution = []
	steps=0
	while queue :
		s=queue.pop(0)
		board=s.getBoard()
		Col=s.getCol()
		steps+=1
		if Col==N: 
			solution.append(board)
			print("The solution is found")
			result=solution.pop(0)
			print("The no of steps " + str(s.getSteps()))
			printBoard(result)
			print()
			exit()
		if Col<N:
			for row in range(N):
				if(board[row][Col]!=-1):
					# copy to temp 
					temp=deepcopy(board)
					# Mark the position of queen
					temp[row][Col]=1 
					# Mark the dangerous paths
					temp=markDangerous(temp,row,Col)	
					queue.append(Board(temp,Col+1,steps))
					
	# print("The solutions are : ")
	# TotalSolutions=0
	# while solution:
	# 	printBoard(solution.pop(0)) 
	# 	print()
	# 	TotalSolutions+=1
	# print("The total solutions are : "+str(TotalSolutions))

main()