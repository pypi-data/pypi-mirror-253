import numpy as np
import pandas as pd

def Distance(a,b, ord=2):
    a_array=a.values
    b_array=b.values
    distance = np.linalg.norm(a-b, ord)
    
    return distance

def Kmeans(data, ord, k, num_iterations):
    # Initialize centroids
    centroids = data[np.random.choice(data.shape[0], k, replace=False)]

    for _ in range(num_iterations):
        # Assignment step
        clusters = {}
        for x in data:
            distances = [Distance(x, centroid, ord) for centroid in centroids]
            closest = np.argmin(distances)
            if closest not in clusters:
                clusters[closest] = []
            clusters[closest].append(x)

        # Update step
        new_centroids = []
        for i in range(k):
            new_centroids.append(np.mean(clusters[i], axis=0))
        centroids = new_centroids

    return centroids, clusters


