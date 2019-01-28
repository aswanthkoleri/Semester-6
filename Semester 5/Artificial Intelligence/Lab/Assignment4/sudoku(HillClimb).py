from copy import copy, deepcopy
def CheckEmptyLocations(arr,l): 
    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False

def used_in_row(arr,row,num): 
	for i in range(9): 
		if(arr[row][i] == num): 
			return True
	return False


def used_in_col(arr,col,num): 
	for i in range(9): 
		if(arr[i][col] == num): 
			return True
	return False

 
def used_in_box(arr,row,col,num): 
	for i in range(3): 
		for j in range(3): 
			if(arr[i+row][j+col] == num): 
				return True
	return False

def checkPossible(arr,row,col,num): 
	return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num)

def popFirstBest(q):
    return q.pop(0)

def solve_sudoku(grid): 
    q=[]
    q.append(grid)
    sol=[]
    l=[0,0]
    count=0
    while q :
        best=popFirstBest(q)
        # print("***** The popped ***********")
        # print(best)
        if not CheckEmptyLocations(best,l) :
            print("The solution is found and is : ")
            for i in range(9):
                for j in range(9):
                    print(str(best[i][j]),end=" ")
                print("")
            

        else : 
            row=l[0]
            col=l[1]
            # Generate all the possible nodes from the current node
            for num in range(1,10):
                if checkPossible(best,row,col,num):
                    # If possible add that node to the queue
                    best[row][col]=num
                    # print("The possible >>>>>>>>>>>>>>")
                    # print(best)
                    temp=deepcopy(best)
                    # print("The possible >>>>>>>>>>>>>>")
                    q.append(temp)
                    # print("************ queue has ")
                    # for some in q : 
                    #     print(some)
                    # print("************ queue has ")
                    best[row][col]=0
            
                            
def main():
    grid=[[0 for x in range(9)]for y in range(9)] 
    # print(grid)
    grid=[[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]]
    solve_sudoku(grid)

main()