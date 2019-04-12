import pandas as pd
import numpy as np
import math

data = pd.read_excel('Absenteeism_at_work.xls')
unused_attributes = ['ID']
data = data.drop(unused_attributes, axis = 1)
points = []
print(data)
points = np.array(data)
print(points)
class k_medoids:
    def __init__(self, points, k):
        self.medoids = []
        self.k = k
        self.points = points

        for i in range(k):
            index = int((i/float(self.k)) * points.shape[0])
            self.medoids.append(points[index])

    def distance(self, a, b):
        dist = 0
        for i in range(len(a)):
            dist += abs(a[i] - b[i])
        return dist

    def find_clusters(self):
        clusters = {}
        for data_point in self.points:
            distances = []
            for medoid in self.medoids:
                distances.append(self.distance(data_point, medoid))

            minIndex = distances.index(min(distances))

            clusters.setdefault(minIndex, []).append(data_point)

        return clusters

    def find_medoids(self, cluster):
        min_distance = 100000000
        for point in cluster:
            temp = 0

            for compare_point in cluster:
                temp += self.distance(point, compare_point)

            if temp < min_distance:
                min_distance = temp
                medoid = point

        return medoid

    def fit(self):
        current_medoids = [None] * self.k
        self.k_clusters = {}
        while (np.array_equal(current_medoids, self.medoids) == False):
            self.k_clusters = self.find_clusters()

            for i in range(self.k):
                current_medoids[i] = self.medoids[i]
                medoid = self.find_medoids(self.k_clusters[i])
                self.medoids[i] = medoid

        for i in range(len(self.k_clusters)):
            print("# Cluster ",i+1)
            # print(np.array(self.k_clusters[i]).shape)
            item=np.array(self.k_clusters[i]).shape
            print("No of points : ",item[0])
            print("No of Columns : ",item[1])

model = k_medoids(points, 2)

model.fit()
