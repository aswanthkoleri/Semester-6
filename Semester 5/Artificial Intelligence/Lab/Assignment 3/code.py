import random

def findIndexIn(L,val):
    for i in range(0,10):
        if(L[i] == val):
            return i
    return -1 

# def onePoint(p1,p2,index):
#     result = [-1 for i in range(10)]
#     result[:index+1] = p1[:index+1]
#     result[index+1:] = p2[index+1:]
#     return result

def orderOne(p1,p2,lindex,rindex):
    result = [-1 for i in range(10)]
    for i in range(lindex,rindex+1):
        result[i] = p1[i]
    if(rindex == 9):
        i = 0
    else:
        i = rindex+1
    resultindex = i

    while(resultindex != lindex):
        if p2[i] not in result:
            result[resultindex] = p2[i]
            if(resultindex == 9):
                resultindex = 0
            else:
                resultindex = resultindex+1    
        if(i == 9):
            i = 0
        else:
            i = i+1
    return result

def pmx(p1,p2,lindex,rindex):
    result = [-1 for i in range(10)]
    for i in range(lindex,rindex+1):
        result[i] = p1[i]
    for i in range(lindex,rindex+1):
        if p2[i] not in result:
            resultindex = i
            while(resultindex in range(lindex,rindex+1)):
                val = p1[resultindex]
                resultindex = findIndexIn(p2,val)
            result[resultindex] = p2[i]
    for i in range(10):
        if(result[i] == -1):
            result[i] = p2[i]
    return result



def scamble(p,lindex,rindex):
    result = [-1 for i in range(10)]
    i = lindex
    while(i != rindex+1):
        randindex = random.randint(lindex,rindex)
        if p[randindex] not in result:
            result[i] = p[randindex]
            i = i+1
    result[:lindex] = p[:lindex]
    result[rindex+1:] = p[rindex+1:]
    return result

def inversion(p,lindex,rindex):
    result = [-1 for i in range(10)]
    for i in range(lindex,rindex+1):
        result[i] = p[rindex+lindex-i]
    result[:lindex] = p[:lindex]
    result[rindex+1:] = p[rindex+1:]
    return result

def onePoint(ar1,ar2,index):
    """ Create result array """
    result=[]
    for i in range(index+1):
        result.append(ar1[i])
    for i in range(index+1,len(ar2)):
        result.append(ar2[i])
    return result
def multiPoint(ar1,ar2,index1,index2):
    """ Create result array  """
    result=[]
    for i in range(index1+1):
        result.append(ar1[i])
    # print(result)
    for i in range(index1+1,index2+1):
        result.append(ar2[i])
    # print(result)
    for i in range(index2+1,len(ar1)):
        result.append(ar1[i])
    # print(result)
    return result

def uniformCrossover(ar1,ar2):
    result=[]
    for i in range(len(ar1)):
        # Produce 1 or 2 if 1 put from first array else from second array 
        no=random.randint(1,2)
        if no==1:
            result.append(ar1[i])
        else:
            result.append(ar2[i])

    return result
def swap(ar):
    index1=random.randint(0,random.randint(0,8))
    index2=random.randint(index1+1,9)
    # Now swap to create mutation
    temp = ar[index1]
    ar[index1]=ar[index2]
    ar[index2]=temp
    return ar
def inversion(ar,start,end)
def main():
    p1 = [8,4,7,3,6,2,5,1,9,0]
    p2 = [0,1,2,3,4,5,6,7,8,9]
    lindex = random.randint(0,5)
    rindex = random.randint(lindex+1,9)
    
    print(lindex)
    print(rindex)

    #Crossover
    # cOrderOne = orderOne(p1,p2,lindex,rindex)
    # cPmx = pmx(p1,p2,lindex,rindex)
    FOnePoint = onePoint(p1,p2,lindex)
    FMultiPoint = multiPoint(p1,p2,lindex,rindex)
    FuniformCrossover= uniformCrossover(p1,p2)
    
    #Mutation
    cIn = inversion(p1,lindex,rindex)
    cSc = scamble(p2,lindex,rindex)
    # cSw = swap(p2)
    FSwap = swap(p1)
    # print(FSwap)
    # print(cOnePoint)
    # print(cMultiPoint)
    # print(FuniformCrossover)


if __name__ == "__main__":
    main()