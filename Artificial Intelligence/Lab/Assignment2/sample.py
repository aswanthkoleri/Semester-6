""" The Hueristic function used will be the No of spots left for the queen  """
""" Initially there will 8*8 = 64 spots left. The more the spots the more value of huerisitic it will be having  """
from copy import copy, deepcopy
N=8
sols=0
class Board:
	"""docstring for Board"""
    def __init__(self, board,col,hue):
        self.board = board
        self.col = col
        self.hue = hue

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
# Function to find the no of spots left for the queen 
def hueFinder(board,col):
    hue=0
    j=0
    while j<N:
        i=col+1
        while i<N: 
            if board[i][j]!=-1:
                hue+=1
    return hue

def getBest(queue):
    best=queue[0]
    for i in queue:
        if i.getHue()>best.getHue():
            best=i
    return best

def main():
	a=[[0]*N for i in range(N)]
	board1=Board(a,0,64)
	queue = []
	queue.append(board1);
	solution = []
	while queue :
		# s=queue.pop(0)
        # Get the best board with max Hue value 
        s=getBest(queue)	
		board=s.getBoard()
		Col=s.getCol()
		if Col==N: 
			solution.append(board)
		if Col<N:
			for row in range(N):
				if(board[row][Col]!=-1):
					# copy to temp 
					temp=deepcopy(board)
					# Mark the position of queen
					temp[row][Col]=1
					# Mark the dangerous paths
					temp=markDangerous(temp,row,Col)
                	# Find the hue and update it to the board and then add to the queue 
                    hue=hueFinder(temp,col)
					queue.append(Board(temp,Col+1,hue))
					
	print("The solutions are : ")
	TotalSolutions=0
	while solution:
		printBoard(solution.pop(0)) 
		print()
		TotalSolutions+=1
	print("The total solutions are : "+str(TotalSolutions))

main()