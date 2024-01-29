 # topsis_package/topsis_package/topsis.py

import pandas as pd
import numpy as np

def topsis(data, weights, impacts):
    normalized_matrix = data / np.sqrt((data**2).sum())

    weighted_matrix = normalized_matrix * weights

    ideal_best = weighted_matrix.max()
    ideal_worst = weighted_matrix.min()

    
    dist_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))

    topsis_score = dist_worst / (dist_best + dist_worst)

    return topsis_score