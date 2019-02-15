'''
    put point 1 in cluster1
    from next point compare with every cluster
        if point is in cluster then compare distance
        else
        create new cluster and insert this point


'''


import math as m
from matplotlib import pyplot as plt

cluster_list = []
Points = [
    (2, 10),
    (2, 5),
    (8, 4),
    (5, 8),
    (7, 5),
    (6, 4),
    (1, 2),
    (4, 9)
]


def euclidean_distance(p1, p2):
    return m.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)


def kNN(threshold, points):

    cluster_list.append([points[0]])

    for i in range(1, len(points)):
        clusters = []

        for j in range(len(points)):
            for c in range(len(cluster_list)):
                if points[j] in cluster_list[c]:
                    if euclidean_distance(points[i], points[j]) < threshold:
                        clusters.append(c)

        if len(clusters) == 0:
            cluster_list.append([points[i]])
        else:
            cluster_inside = cluster_list[max(clusters, key=clusters.count)]
            cluster_inside.append(points[i])
            print("cluster_inside", cluster_inside)


    pass


def plotting(plotlist):
    for i in range(len(plotlist)):
        cl = plotlist[i]
        X, Y = [], []
        for p in cl:
            X.append(p[0])
            Y.append(p[1])
        plt.scatter(X, Y)
    plt.axis([0, 12, 0, 12])
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.show()
    pass


if __name__ == '__main__':
    threshold = 4
    kNN(threshold, Points)
    plotting(cluster_list)
    print(cluster_list)

