import numpy as np 

def f2K(f): 
    """Returns a camera intrinsic matrix, given focal length

    Args: 
    f: focal length of a camera

    Returns
    K: Camera intrinsic matrix"""
    
    K = np.eye(3)
    K[0,0] = K[1,1] = f 
    return K 