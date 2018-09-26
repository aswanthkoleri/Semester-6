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

def calculateManhattanDistance(board):
    sum=0
    for i in range(N):
        for j in range(N):
            if board[i][j]==1:
                sum+=abs(i-0)+abs(j-0)
            elif board[i][j]==2:
                sum+=abs(i-0)+abs(j-1)
            elif board[i][j]==3:
                sum+=abs(i-0)+abs(j-2)
            elif board[i][j]==4:
                sum+=abs(i-1)+abs(j-0)
            elif board[i][j]==5:
                sum+=abs(i-1)+abs(j-1)
            elif board[i][j]==6:
                sum+=abs(i-1)+abs(j-2)
            elif board[i][j]==7:
                sum+=abs(i-2)+abs(j-0)
            elif board[i][j]==8:
                sum+=abs(i-2)+abs(j-1)
            elif board[i][j]==0:
                sum+=0
    return sum

class Board:
    """ Constructor  """ 
    def __init__(self,board,Zx,Zy,steps,h):
        self.board=board
        self.Zx=Zx
        self.Zy=Zy
        self.steps=steps
        self.h=h    
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
    def getH(self):
        return self.h

def popBest(queue):
    min=0
    minValue=queue[min].getH()
    for i in range(len(queue)):
        hue=queue[i].getH()
        if hue < minValue:
            # If the hueristic value is less than the minValue then it means that its the most closest node to the goal node
            min=i
            minValue=queue[min].getH()
            break
            # We break here cuz this is simple hill climbing from which we will get the next node soon after we find any node bette than the current one 
    return min 
    
""" Function to check states are equal or not  """
def check(current):
    board1=current.getBoard()
    final=[[1,2,3],[4,5,6],[7,8,0]]
    if(board1==final):
        return 1
    else:
        return 0

""" BFS Function  """
def BFS(boardConf):
    global MIN
    """ First make queue and push initial conf  """
    queue=[]
    queue.append(boardConf)
    while queue :
        current=queue.pop(popBest(queue))
        visited.append(current.getBoard())
        printBoard(current.getBoard())
        
        print("Hue= "+str(current.getH()))
        print("Steps= "+str(current.getSteps()))
        if check(current)==1:
            steps=current.getSteps()
            MIN=steps
            return
        """ Now push the four states to the queue """
        Zx=current.getX()
        Zy=current.getY()
        # Check if right element exist in current 
        if Zy+1<N:
        # If exist then swap with the position of zero and create newState to push it to the queue
            newBoard=deepcopy(current.getBoard())
            Rx=Zx
            Ry=Zy+1
            newBoard[Zx][Zy]=newBoard[Rx][Ry]
            newBoard[Rx][Ry]=0
            if newBoard not in visited:
                h=calculateManhattanDistance(newBoard)
                print("Pushing board with hue= "+str(h))
                printBoard(newBoard)
                queue.append(Board(newBoard,Rx,Ry,current.getSteps()+1,h))
        # Check if left element exist in current 
        if Zy-1>=0:
        # If exist then swap with the position of zero and create newState to push it to the queue
            newBoard=deepcopy(current.getBoard())
            Rx=Zx
            Ry=Zy-1
            newBoard[Zx][Zy]=newBoard[Rx][Ry]
            newBoard[Rx][Ry]=0
            if newBoard not in visited:
                h=calculateManhattanDistance(newBoard)
                print("Pushing board with hue= "+str(h))
                printBoard(newBoard)
                queue.append(Board(newBoard,Rx,Ry,current.getSteps()+1,h))
        # Check if bottom element exist in current 
        if Zx+1<N:
            
        # If exist then swap with the position of zero and create newState to push it to the queue
            newBoard=deepcopy(current.getBoard())
            Rx=Zx+1
            Ry=Zy
            newBoard[Zx][Zy]=newBoard[Rx][Ry]
            newBoard[Rx][Ry]=0
            if newBoard not in visited:
                h=calculateManhattanDistance(newBoard)
                print("Pushing board with hue= "+str(h))
                printBoard(newBoard)
                queue.append(Board(newBoard,Rx,Ry,current.getSteps()+1,h))
        # Check if upper element exist in current b
        if Zx-1>=0: 
        # If exist then swap with the position of zero and create newState to push it to the queue
            newBoard=deepcopy(current.getBoard())
            Rx=Zx-1
            Ry=Zy
            newBoard[Zx][Zy]=newBoard[Rx][Ry]
            newBoard[Rx][Ry]=0
            if newBoard not in visited:
                h=calculateManhattanDistance(newBoard)
                print("Pushing board with hue= "+str(h))
                printBoard(newBoard)
                queue.append(Board(newBoard,Rx,Ry,current.getSteps()+1,h))


        
def main():
    """ get Initial and final configurations  """
    initial=[
        [7,3,4],
        [0,2,1],
        [5,8,6]
    ]
    h=calculateManhattanDistance(initial)
    initialConfig=Board(initial,1,0,0,h)
    BFS(initialConfig)
    print("The minimum number of steps is : "+str(MIN))

main()    