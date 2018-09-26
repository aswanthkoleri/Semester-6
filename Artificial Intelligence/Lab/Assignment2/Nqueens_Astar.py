from copy import copy, deepcopy
N=8
sols=0
class Board:
	"""docstring for Board"""
	def __init__(self, board,col,hue,steps):
		self.board = board
		self.col=col
		self.hue=hue
		self.steps=steps
		self.g=hue+col

	def displayBoard(self):
		for row in self.board:
			for ele in row:
				print(ele,end=' ')	
			print()

	def getBoard(self):
		return self.board
	def getCol(self):
		return self.col
	def getHue(self):
		return self.hue
	def getSteps(self):
		return self.steps
	def getG(self):
		return self.g


def printBoard(board):
	for row in board:
		for ele in row:
			if ele==-1:
				print(0,end=' ')
			else:
				print(ele,end=' ')	
		print()

def printBoard1(board):
	for row in board:
		for ele in row:
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

def hueFinder(board,col):
    hue=0
    j=0
    while j<N:
    	i=col+1
    	while i<N:
    		if board[j][i]!=-1:
    			hue+=1
    		i+=1
    	j+=1
    return hue

def getBest(queue):
    best=0
    for i in range(len(queue)):
        if queue[i].getG()>queue[best].getG():
            best=i
    return best

def main():
	a=[[0]*N for i in range(N)]
	board1=Board(a,0,64,0)
	queue = []
	queue.append(board1);
	steps=0
	solution = []
	while queue :
		# s=queue.pop(0)	
		s=queue.pop(getBest(queue))
		steps+=1
		board=s.getBoard()
		Col=s.getCol()
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
					hue=hueFinder(temp,Col)
					queue.append(Board(temp,Col+1,hue,steps))
	# print("The solutions are : ")
	# TotalSolutions=0
	# while solution:
	# 	printBoard(solution.pop(0)) 
	# 	print()
	# 	TotalSolutions+=1
	# print("The total solutions are : "+str(TotalSolutions))

main()