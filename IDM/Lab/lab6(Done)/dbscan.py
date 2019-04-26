import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
def norm(a, b):
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - b[i])**2
    return math.sqrt(sum)

data = pd.read_excel('data2.xlsx')
data = np.asarray(data)
X, y = data[:,:2], data[:,2:]
minpts = 30
eps = 2
distance = np.zeros((X.shape[0], X.shape[0]))
print(distance.shape)
for i in range(len(distance)):
    for j in range(len(distance)):
        distance[i][j] = norm(X[i], X[j])
visited = np.zeros(len(X))
clustered = np.zeros(len(X))
core_points = {}
for i in range(len(X)):
    for j in range(len(X)):
        if distance[i][j] <= eps:
            if i not in core_points:
                core_points[i] = [j]
            else:
                core_points[i].append(j)
            if j not in core_points:
                core_points[j] = [i]
            else:
                core_points[j].append(j)
to_be_delted = []
for key, val in core_points.items():
    if len(val) < minpts:
        to_be_delted.append(key)
# print(len(core_points))
for val in to_be_delted:
    core_points.__delitem__(val)
# print(len(core_points))
clusters = []
for key, val in core_points.items():
    if visited[key] == 1:
        continue
    clusters.append([])
    candidates = val
    visited[key] = 1
    while True:
        flag = 0
        for point in candidates:
            if clustered[point] == 0:
                flag = 1
                clustered[point] = 1
                clusters[len(clusters) - 1].append(point)
        if flag == 0:
            break
        new_candidate = []
        for  point in candidates:
            if visited[point] == 0 and (point in core_points):
                visited[point] = 1
                tmp_ar = core_points[point]
                for _point in tmp_ar:
                    new_candidate.append(_point)
print(len(clusters))
for i,cluster in enumerate(clusters):
    print("Cluster"+str(i),cluster)
    
