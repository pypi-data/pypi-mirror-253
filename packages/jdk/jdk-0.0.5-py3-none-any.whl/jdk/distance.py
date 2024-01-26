import numpy as np
import pandas as pd

def Euclidean(a,b):
    a_array=a.values
    b_array=b.values
    distance = np.linalg.norm(a-b)
    
    return distance

def test():
    return 11


