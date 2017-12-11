import numpy as np
from scipy.io import loadmat

def f2K(f):
    """Returns a camera intrinsic matrix, given focal length
    Args:
    f: focal length of a camera

    Returns
    K: Camera intrinsic matrix"""

    K=np.eye(3)
    K[0,0]=K[1,1]=f 
    return K

def estimateFundamentalMatrixRANSAC(feats, n=1): 
    """Apply RANSAC algorithm to estimate fundamental matrix
    
    Args: 
    feats (4, K): ndarray containing K SIFT-features 
    n (int): How many times to randomly sample 8 points

    Returns: 
    F (3,3): Estimated fundamental matrix
    """
    
    for i in xrange(n): 
        #Randomly sampling 8 points
        idx = np.random.choice(feats.shape[1], (8,), replace=False)
        
        #Estimating fundamental matrix using randomly sampled points
        x1 = feats[:2,idx].T
        x2 = feats[2:, idx].T
        F = estimateFundamentalMatrix(x1, x2)

        #TO DO: Write evaluation criteria here
    return F

def estimateFundamentalMatrix(x1,x2):
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
    u,s,v = np.linalg.svd(A, full_matrices=True)
    F = v[:,-1].reshape((3,3))

    #Applying rank filtering
    u2,s2,v2 = np.linalg.svd(F, full_matrices=True)
    s2[-1] = 0 
    F = np.dot(u2, np.dot(np.diag(s2), v2.T))

    #to do: apply correct norm here
    return F 

def matFileToFeatures(filename, shape1, shape2): 
    """Reads .mat file from sfmedu and converts it into estimateFundamentalMatrix() compatible format
    (Used only for testing purposes)
    
    Args: 
    filename: path to .mat file
    shape1, shape2: dimensions of images (used for eliminating normalization effect)
    
    Returns: 
    out: ndarray (4,n) where n are total number of SIFT features"""

    #Extraction from .mat dictionary to ndarray
    matfile = loadmat(filename)
    pair = matfile['pair']
    out = pair[0,0][1]

    #Eliminating normalization
    out[0,:] = shape1[1]/2-out[0,:]
    out[1,:] = shape1[0]/2-out[1,:]

    out[2,:] = shape2[1]/2-out[2,:]
    out[3,:] = shape2[0]/2-out[3,:]

    return out 

def estimateEssentialMatrix(K, F, rank_constraint=True): 
    """Given a fundamental matrix F and camera intrinsic matrix K, computes the essential matrix E 
    by (optionally) applying rank_constaint
    
    Args: 
    K (3,3): Camera intrinstic Matrix
    F (3,3): Fundamental Matrix
    rank_constraint (True/False): If true, applies rank constraint after initial estimate, otherwise not
    
    Returns: 
    E (3,3): Essential Matrix"""
    E = K.T.dot(F.dot(K))

    if rank_constraint==False: 
        return E

    u,s,v = np.linalg.svd(E, full_matrices=True)
    s[0] = s[1] = 1 
    s[-1] = 0 
    E = u.dot(np.diag(s).dot(v.T))

    #to do: apply correct norm here 
    return E 

def get2DPointCorrespondencesFromOF(flowMat): 
    """Given a flow matrix of the images, returns the calculated corresponding 2d feature matches 
    
    Args: 
    flowMat (height, width, 2): ndarray containing the flow map of image
    
    Returns: 
    before (height x width, 2): ndarray representing the pixels' position in first image
    after (height x width, 2): ndarray representing the pixels' position in second image
    """
    #Generating all indices..
    idxx, idxy = np.meshgrid(np.arange(flowMat.shape[0]), np.arange(flowMat.shape[1]))
    idxx, idxy = idxx.T.flatten(), idxy.T.flatten()

    #Adding translation vectors to get displacements..
    before = np.concatenate((idxx[:,np.newaxis], idxy[:,np.newaxis]),axis=-1)
    after = before+flowMat.reshape((-1,2))

    return before, after