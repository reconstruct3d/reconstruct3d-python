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

def estimateFundamentalMatrix(x1, x2):
    """Given a pair, it computes the associated fundamental matrix
    using 8-point algorithm

    Args: 
    x1, x2: nd-arrays of shape (8,2); x1[i,:] and x2[i,:] should contain
    the corresponding co-ordinates of ith feature 

    Returns: 
    F: Estimated fundamental matrix"""
    
    A = np.zeros((8,9))
    #Given the points, constructing A matrix i.e matrix to solve
    for i in xrange(8):
        rowA = np.array([[x1[i,0]*x2[i,0], x1[i,0]*x2[i,1], x1[i,0]],
        [x1[i,1]*x2[i,0], x1[i,1]*x2[i,1], x1[i,1]],[x2[i,0], x2[i,1], 1]])
        
        A[i,:] = np.reshape(rowA, (9,))
    
    #Initial estimate of F
    u,s,v = np.linalg.svd(A, full_matrices=False)
    F = v[:,-1].reshape((3,3))

    #Applying rank filtering
    u2,s2,v2 = np.linalg.svd(F, full_matrices=False)
    s2[-1] = 0 
    F = np.dot(u2, np.dot(np.diag(s2), v2.T))

    #to do: apply correct norm here
    return F 