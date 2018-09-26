from copy import copy, deepcopy
import sys
MIN=sys.maxsize
N=3
visited=[]
def printBoard(board):
    print("Solution")
    for row in board:
        for ele in row:
            print(ele,end=' ')
        print()

class Board:
    """ Constructor  """ 
    def __init__(self,board,Zx,Zy,steps):
        self.board=board
        self.Zx=Zx
        self.Zy=Zy
        self.steps=steps
    
    # Get steps
    def getSteps(self):
        return self.steps
    # Get the Board
    def getBoard(self):
        return self.board
    # Get X coord of Zero 
    def getX(self):
        return self.Zx
    # Get Y coord of Zero 
    def getY(self):
        return self.Zy

""" Function to check states are equal or not  """
def check(current):
    board1=current.getBoard()
    final=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    if(board1==final):
        return 1
    else:
        return 0

""" BFS Function  """
def BFS(boardConf):
    global MIN
    """ First make stack and push initial conf  """
    stack=[]
    stack.append(boardConf)
    while stack:
        current=stack.pop()
        visited.append(current.getBoard())
        printBoard(current.getBoard())
        if check(current)==1:
            steps=current.getSteps()
            MIN=steps
            return
        """ Now push the four states to the stack """
        Zx=current.getX()
        Zy=current.getY()
        # Check if right element exist in current 
        if Zy+1<N:
            print("Done1")
        # If exist then swap with the position of zero and create newState to push it to the stack
            newBoard=deepcopy(current.getBoard())
            Rx=Zx
            Ry=Zy+1
            newBoard[Zx][Zy]=newBoard[Rx][Ry]
            newBoard[Rx][Ry]=0
            if newBoard not in stack and visited:
                stack.append(Board(newBoard,Rx,Ry,current.getSteps()+1))
        # Check if left element exist in current 
        if Zy-1>=0:
            print("Done2")
        # If exist then swap with the position of zero and create newState to push it to the stack
            newBoard=deepcopy(current.getBoard())
            Rx=Zx
            Ry=Zy-1
            newBoard[Zx][Zy]=newBoard[Rx][Ry]
            newBoard[Rx][Ry]=0
            if newBoard not in stack and visited:
                stack.append(Board(newBoard,Rx,Ry,current.getSteps()+1))
        # Check if bottom element exist in current 
        if Zx+1<N:
            print("Done3")
        # If exist then swap with the position of zero and create newState to push it to the stack
            newBoard=deepcopy(current.getBoard())
            Rx=Zx+1
            Ry=Zy
            newBoard[Zx][Zy]=newBoard[Rx][Ry]
            newBoard[Rx][Ry]=0
            if newBoard not in stack and visited:
                stack.append(Board(newBoard,Rx,Ry,current.getSteps()+1))
        # Check if upper element exist in current b
        if Zx-1>=0:
            print("Done4")
        # If exist then swap with the position of zero and create newState to push it to the stack
            newBoard=deepcopy(current.getBoard())
            Rx=Zx-1
            Ry=Zy
            newBoard[Zx][Zy]=newBoard[Rx][Ry]
            newBoard[Rx][Ry]=0
            if newBoard not in stack and visited:
                stack.append(Board(newBoard,Rx,Ry,current.getSteps()+1))


        
def main():
    """ get Initial and final configurations  """
    initial=[
        [ 1,  2,  3,  4],
        [ 0,  5, 7,  8],
        [10, 6, 11, 12],
        [9, 13, 14, 15]
    ]
    initialConfig=Board(initial,1,0,0)
    BFS(initialConfig)
    print("The minimum number of steps is : "+str(MIN))

main()    