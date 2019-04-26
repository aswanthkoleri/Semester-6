import pandas as pd
import numpy as np

def linkage(distance, indexes, original_distance, type = 'single'):
    indices = []
    mn = np.inf
    # To find the minimum distance in the Upper triangular matrix
    for i in range(distance.shape[0]):
        for j in range(distance.shape[1]):
            if(i >= j):
                continue
            if distance[i][j] < mn:
                mn = distance[i][j]
    # To append all the elements in the with the minimum distance value
    for i in range(distance.shape[0]):
        for j in range(distance.shape[1]):
            if(i >= j):
                continue
            if distance[i][j] == mn:
                indices.append([i, j])
    # Initialize a new distance
    new_distance = np.zeros((distance.shape[0] - len(indices), distance.shape[1] - len(indices)))
    for vals in indices:
        indexes[vals[0]] = np.append(indexes[vals[0]], indexes[vals[1]])
    for vals in indices:
        indexes.pop(vals[1])
    print(indexes)
    for i in range(len(new_distance)):
        for j in range(len(new_distance)):
            if type == 'single':
                mn = np.inf
            elif type == 'complete':
                mn = -1*np.inf
            elif type == 'average':
                mn = 0
                ct = 0
            for vals1 in indexes[i]:
                for vals2 in indexes[j]:
                    if type == 'single':
                        mn = min(mn, original_distance[vals1][vals2])
                    elif type == 'complete':
                        mn = max(mn, original_distance[vals1][vals2])
                    elif type == 'average':
                        ct += 1
                        mn += original_distance[vals1][vals2]
            if type == 'average':
                new_distance[i][j] = mn / ct
            else:
                new_distance[i][j] = mn
    print(new_distance)
    return new_distance, indexes
distance = pd.read_excel('matrixsmall.xlsx', header=None)
distance = np.array(distance)
print(distance)
original_distance = np.copy(distance)
indexes = []
for i in range(len(distance)):
    indexes.append(np.array([i]))
while len(distance) > 1:
    distance, indexes = linkage(np.copy(distance), indexes.copy(), original_distance, type = 'complete')

