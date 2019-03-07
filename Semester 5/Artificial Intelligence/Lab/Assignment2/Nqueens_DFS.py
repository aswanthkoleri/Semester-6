global N
N=8
sols=0
def printBoard(board):
	print("Solution :")
	for row in board:
		for ele in row:
			print(ele,end=' ')	
		print()

def isDangerous(board,row,col):
    #  row on left side
    for i in range(col):
        if board[row][i] == 1:
            return 1
 
    #  upper diagonal on left side
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return 1
 
    # lower diagonal on left side
    for i,j in zip(range(row,N,1), range(col,-1,-1)):
        if board[i][j] == 1:
            return 1
    return 0

def DFS(board,col):
	global sols
	if col >= N:
		printBoard(board)
		sols+=1
		return 

	for i in range(N):
	    if isDangerous(board, i, col)==0:
	        board[i][col] = 1
	        DFS(board, col+1)
	        board[i][col] = 0
	return 

def main(): 
	global sols
	board=[[0]*N for i in range(N)]
	DFS(board,0)
	print("Total Solutions "+str(sols))
main()